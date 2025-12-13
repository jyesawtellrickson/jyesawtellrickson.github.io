
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

import torch
import torch.nn as nn
import torch.optim as optim
import argparse

# Command line arguments
parser = argparse.ArgumentParser(description='Train a deep CNN on MNIST')
parser.add_argument('--num_layers', type=int, default=100, 
                    help='Number of convolutional layers (default: 100)')
parser.add_argument('--epochs', type=int, default=3,
                    help='Number of training epochs (default: 3)')
parser.add_argument('--lr', type=float, default=1e-3,
                    help='Learning rate (default: 1e-3)')
args = parser.parse_args()

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
print(f"Training with {args.num_layers} layers for {args.epochs} epochs (lr={args.lr})")

# Data
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])
train_ds = datasets.MNIST(root="./data", train=True, download=True, transform=transform)
test_ds = datasets.MNIST(root="./data", train=False, download=True, transform=transform)
train_loader = DataLoader(train_ds, batch_size=64, shuffle=True, num_workers=0, pin_memory=True)
test_loader = DataLoader(test_ds, batch_size=1000, shuffle=False, num_workers=0, pin_memory=True)

# Model: simple stacked convs -> pool -> fc
class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10, num_layers=2):
        super().__init__()

        layers = []
        in_channels = 1
        out_channels = 16
        kernel_size = 3
        projection_layer_size = 16
        # param count: 3x3x16x16 = 2K per layer
        # fc: 16x14x14x128 = 401K
        # flops: 2 x 3x3x16x16 x 28x28 per layer = 3.6M per layer
        # fc flops: 2 x 16x14x14 x 128 = 57K
        # vs. 40TFLOPS on my gpu

        for i in range(num_layers):
            conv = nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size, padding=1)
            nn.init.xavier_uniform_(conv.weight)
            nn.init.zeros_(conv.bias)
            layers.append(conv)
            layers.append(nn.ReLU(inplace=True))
            in_channels = out_channels

        layers.append(nn.MaxPool2d(2))  # Downsample by 2

        self.features = nn.Sequential(*layers)

        # Initialize classifier layers
        fc1 = nn.Linear(in_channels * 14 * 14, projection_layer_size)
        fc2 = nn.Linear(projection_layer_size, num_classes)
        nn.init.xavier_uniform_(fc1.weight)
        nn.init.xavier_uniform_(fc2.weight)
        nn.init.zeros_(fc1.bias)
        nn.init.zeros_(fc2.bias)

        self.classifier = nn.Sequential(
            nn.Flatten(),
            fc1,
            nn.ReLU(inplace=True),
            fc2
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x

model = SimpleCNN(num_layers=args.num_layers).to(device)

# Model analysis functions
def count_parameters(model):
    """Count total and trainable parameters"""
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return total_params, trainable_params

def get_model_memory(model):
    """Calculate model memory usage in MB"""
    param_size = 0
    buffer_size = 0
    
    for param in model.parameters():
        param_size += param.nelement() * param.element_size()
    
    for buffer in model.buffers():
        buffer_size += buffer.nelement() * buffer.element_size()
    
    size_all_mb = (param_size + buffer_size) / 1024**2
    return size_all_mb

def count_flops(model, input_size=(1, 1, 28, 28)):
    """Estimate FLOPs for a forward pass (simplified calculation)"""
    flops = 0
    
    # Count Conv2d FLOPs
    for module in model.modules():
        if isinstance(module, nn.Conv2d):
            # FLOPs = 2 * kernel_h * kernel_w * in_channels * out_channels * output_h * output_w
            # For our case with padding=1, output size stays the same
            kernel_ops = module.kernel_size[0] * module.kernel_size[1] * module.in_channels
            output_size = 28 * 28  # Stays same with padding=1
            flops += 2 * kernel_ops * module.out_channels * output_size
        elif isinstance(module, nn.Linear):
            # FLOPs = 2 * in_features * out_features
            flops += 2 * module.in_features * module.out_features
    
    return flops

# Print model statistics
total_params, trainable_params = count_parameters(model)
model_memory = get_model_memory(model)
flops = count_flops(model)

print("\n" + "="*60)
print("MODEL STATISTICS")
print("="*60)
print(f"Total parameters:      {total_params:,}")
print(f"Trainable parameters:  {trainable_params:,}")
print(f"Model memory:          {model_memory:.2f} MB")
print(f"FLOPs per forward pass: {flops:,} ({flops/1e9:.3f} GFLOPs)")
print("="*60 + "\n")

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=args.lr)

# Gradient tracking helper
def track_gradients(model):
    """Track gradient statistics for each layer"""
    grad_stats = []
    for name, param in model.named_parameters():
        if param.grad is not None:
            grad_norm = param.grad.norm().item()
            grad_mean = param.grad.mean().item()
            grad_max = param.grad.max().item()
            grad_min = param.grad.min().item()
            grad_stats.append({
                'name': name,
                'norm': grad_norm,
                'mean': grad_mean,
                'max': grad_max,
                'min': grad_min
            })
    return grad_stats

# Training and evaluation loops
def train_one_epoch(model, loader, optimizer, criterion, device, track_grads=False):
    import time
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    grad_stats_list = []
    start_time = time.time()
    
    for batch_idx, (images, targets) in enumerate(loader):
        images, targets = images.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, targets)
        loss.backward()
        
        # Track gradients on first batch
        if track_grads and batch_idx == 0:
            grad_stats_list = track_gradients(model)
        
        optimizer.step()

        running_loss += loss.item() * images.size(0)
        _, preds = outputs.max(1)
        correct += preds.eq(targets).sum().item()
        total += images.size(0)
    
    elapsed_time = time.time() - start_time
    throughput = total / elapsed_time  # images per second
    
    return running_loss / total, correct / total, grad_stats_list, throughput

def evaluate(model, loader, criterion, device):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for images, targets in loader:
            images, targets = images.to(device), targets.to(device)
            outputs = model(images)
            loss = criterion(outputs, targets)
            running_loss += loss.item() * images.size(0)
            _, preds = outputs.max(1)
            correct += preds.eq(targets).sum().item()
            total += images.size(0)
    return running_loss / total, correct / total

# Run training
for epoch in range(1, args.epochs + 1):
    # Track gradients on first epoch
    train_loss, train_acc, grad_stats, throughput = train_one_epoch(
        model, train_loader, optimizer, criterion, device, track_grads=(epoch == 1)
    )
    test_loss, test_acc = evaluate(model, test_loader, criterion, device)
    print(f"Epoch {epoch}: Train loss {train_loss:.4f}, Train acc {train_acc:.4f} | Test loss {test_loss:.4f}, Test acc {test_acc:.4f} | Throughput: {throughput:.1f} images/s")
    
    # Print gradient statistics for first epoch
    if epoch == 1 and grad_stats:
        print("\n=== Gradient Statistics (First Batch) ===")
        print(f"{'Layer':<50} {'Grad Norm':<12} {'Mean':<12} {'Max':<12} {'Min':<12}")
        print("-" * 100)
        for stat in grad_stats:
            print(f"{stat['name']:<50} {stat['norm']:<12.6f} {stat['mean']:<12.6f} {stat['max']:<12.6f} {stat['min']:<12.6f}")
        
        # Check for vanishing/exploding gradients
        norms = [s['norm'] for s in grad_stats]
        avg_norm = sum(norms) / len(norms)
        print(f"\nAverage gradient norm: {avg_norm:.6f}")
        if avg_norm < 1e-5:
            print("⚠️  WARNING: Gradients may be vanishing (very small norms)")
        elif avg_norm > 1e3:
            print("⚠️  WARNING: Gradients may be exploding (very large norms)")
        else:
            print("✓ Gradients appear to be in a reasonable range")
        print("=" * 100 + "\n")