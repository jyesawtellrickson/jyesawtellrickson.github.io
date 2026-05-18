---
layout: post
title: An Introduction to Loss Functions
categories: [Knowledge]
---

In machine learning, a loss function is a measure of how well a given algorithm approximates the desired output given a certain set of inputs. Loss functions are an important part of the machine learning process as they not only indicate how well the algorithm works, but also provide insights into the model's performance and allow for optimization of the model's parameters. 

Imagine a sheep herder. The sheep are parameters and you need to coral them into the right pen/configuration. The loss function is the approach you use to get them there. e.g. you could stand behind shouting at them and they might run towards the pen, but they’ll overshoot and you’ll then have to chase them from the other side. You could stand in the pen and try to call them, but the signal would be too weak to reach the furthest ones. You could build your pen in a valley so they tend to approach, but if it’s in a really messy landscape it will be difficult. There are many methods to choose from, each with their own benefits.

Let's start by exploring the properties that make a good loss function.

## The Properties of a Loss Function

Given you could choose from any which function, how do you choose a specific one? Well, you need it to satisfy some properties.

- Ultimately it will be used for **gradient descent**: So it must be cheaply differentiable, and smooth (e.g. MAE is bad example because it has a discontinuity at 0). This removes a lot of possibilities as many functions don't have derivatives that are easy to calculate or approximate.
- **Robustness** to outliers: Real world data is messy, so it shouldn’t let these cause massive gradients and break the network. (e.g. MSE is bad for this, MAE less so)
- **Pseudo-convexity**: Ideally any update to your network would lead you towards the optimal configuration. While this may be too much to ask for, we can aim for locally well-behaved regions, that will make updates tend towards the goal.
- Non-vanishing, **informative gradients**: e.g. MSE with sigmoid activation leads to flat gradients when a network is very wrong. This means that the network will struggle to make meaningful updates.
- Non-negative, zero minimum: these basic properties allow for better convergence.

This still leaves us with many possibilities, so how exactly should you select a loss function given your problem?

## Selecting a Loss Function

Your loss function choice will depend on which task you’re trying to solve. The most common tasks include:
- **Regression**: predicting a number, or set of numbers directly. Most mathematically straightforward with clear direction for wrong predictions.
- **Classification**: predicting the class of an input among competing options. It's not about learning just from the correct class, but also, how can you utilise the fact that you know it shouldn't be other classes?
- **Generation**: no longer are you optimising towards a single prediction, generation often involves a large set of outputs and loss functions must balance diversity with realistic outputs.
- **Representation Learning**: shaping an imaginary space to have desirable properties.

Each of these tasks has unique loss functions specifically designed for them. You can trial different ones depending on your goals and model. 

It’s also possible to have more than one loss function. For example, if a model has multiple outputs, you could have a loss function for each output. Additional losses can also further help training or shape the outputs in a way you like, regularisation losses are a great example of this.

## Failure Modes 

But what is there to look out for when using a loss function? 

- **Shortcut learning**: A network is fundamentally lazy. If your loss function only evaluates the final output, the network will find the path of least computational resistance to minimize that number, even if it completely misses the actual underlying logic.
- **Easy negative dominance**: e.g. predicting the empty pixels, instead of the ones that actually matter. Loss can be driven down while the model is not actually getting good at the task. Focal loss is a good example of a function that stops this by scaling down gradients of examples it’s already highly confident about.
- **Gradient starvation** (dead neurons): The Trap: If a loss function creates a landscape with massive, flat plateaus (often caused by pushing values too deep into the tails of a Sigmoid or Tanh function), the derivative approaches zero. The network stops updating entirely. In Reinforcement Learning, this manifests as a "loss of plasticity"—after training for a while, the network just loses the ability to learn anything new because the weights have been pushed into regions where the gradients are dead.
- **Over-confident miscalibration**: Standard Categorical Cross-Entropy actively encourages the model to push its confidence to 100% (1.0 probability) for the target class and 0% for everything else, even if the data is inherently ambiguous. This results in highly "miscalibrated" models that are frequently wrong but never in doubt.

## Key Loss Functions

### Regression

In regression tasks we (largely) predict continuous values. Most functions are basically how far is your number from the correct number. 'Farness' can be measured by various distance functions such as linear (MAE), quadratic distance (MSE), relative distance (MSLE) or percentage difference (MAPE). 

MSE (L2 loss)
- Mean Square Error or Root Mean Square ERror
- The standard deviation of the residuals
- Heavily penalises large errors.
- https://www.statisticshowto.datasciencecentral.com/rmse/

MAE (L1 loss)
- Mean Absolute Error
- The average of the absolute value of the residuals    

Huber Loss:
- Combination of MSE and MAE

Quantile loss:
- Used for predicting intervals rather than point estimates. It penalizes overestimations and underestimations differently based on a chosen quantile (useful for predicting confidence intervals).

Mean Absolute Percentage Error (MAPE): 
- Measures error as a percentage of the true value. Highly interpretable for business metrics but struggles if true values are near zero.

Mean Squared Logarithmic Error (MSLE):
- Penalizes relative differences rather than absolute differences. Useful when predicting values that span several orders of magnitude (like population or housing prices).

### Classification

Compared to regression, the signal is often weaker, only telling you which class among many is correct (rather than how much it looks like this class vs. that class). Classification loss functions model the targets and network outputs as probability distributions (though neither truly are) and compares them to calculate a score. Cross entropy is the standard with variants that account for the label’s entropy (KL divergence), handle class imbalance (focal loss) or address over-confidence (hinge loss).

Binary/Categorical Cross Entropy
- Measures the overlap between two probability distributions (e.g. logits).
- Can be weighted if there is a large class imbalance.
- Cross entropy is defined as below. Most labels have only p=1 for one class so it’s simply -log(q).
- From the maximum likelihood perspective we want to maximise the probability of the correct class, q, but q is a probability which has bad properties for loss functions, so we take the negative logarithm to bound it from 0 to inf.

KL Divergence:
- Measures how one probability distribution differs from a reference distribution. Widely used in reinforcement learning and variational autoencoders.
- Removes the entropy of the label distribution P. If the P distribution is one hot encoded then it’s the same as cross entropy since the entropy is 0.

Focal loss:
- A modification of the standard cross entropy to better handle class imbalance.
- Introduces two parameters:
    - Focusing parameter $\gamma > 0$ that down-weights easy examples.
    - A class weighting factor (1-p) that reduces the effect of contributing classes which are already accurately predicted (close to 1).
- Defined as $FL(p_t) = -\alpha_t(1-p_t)^\gamma\log(p_t)$, where pt = p if y=1, else 1-p.

Hinge loss (can be squared):
- Used in SVM.
- Enforces correct classification and a margin - the classifier should output the correct label with some buffer, not just barely.
- In the binary case (-1, 1): $L(y, f(x)) = \max\{0, 1-yf(x)\}$
- As above, f(x) must be greater than 1 for the loss to hit 0, so even if it’s maxing the correct prediction with 0.00001, it will continue to be pushed to classify more correctly.
- Not smooth like cross-entropy, but has a flat region.


### Computer Vision

Computer vision has a wide range of tasks, some of which regression or classification loss functions are suitable for, but many for which custom functions have been found to be more effective. These functions address problems such as detection (IOU), segmentation (DICE) and leverage image priors such as structural differences (SSIM) or feature map differences (perceptual).

DICE Loss
- Derived from the Sørensen–Dice coefficient, it measures the overlap between two samples. Highly effective for medical image segmentation where the background dominates the image.

IOU
- Measures overlap between regions.
- Generalised version provides gradients even when there is no overlap.

Structural Similarity Index (SSIM) Loss: 
- Rather than pixel-by-pixel differences, SSIM evaluates changes in luminance, contrast, and structure. Used in image reconstruction to ensure the output "looks" human-perceptible.

Perceptual Loss (VGG Loss): 
- Instead of comparing raw pixels, this runs both the generated image and the target image through a pre-trained network (like VGG) and compares their high-level feature maps. Crucial for style transfer and super-resolution.


### Generative

Minimax GAN Loss: 
- The original loss function for Generative Adversarial Networks. The Generator tries to minimize it (fool the discriminator), while the Discriminator tries to maximize it (distinguish real from fake).

Wasserstein Loss: 
- Used in WGANs. Instead of classifying "real vs. fake," it measures the Earth Mover's Distance—essentially the cost of transforming the generated distribution into the real distribution. It solves many training instability issues in GANs.

Evidence Lower Bound (ELBO) Loss: 
- The core loss for Variational Autoencoders (VAEs). It balances two things: how well the model reconstructs the input data, and how closely the latent space matches a normal distribution (measured via KL divergence).

### Representation Learning

When pre-training models, often the goal is to create a good representation before working on the true task so a supplementary one must be created. This leads to a variety of custom loss functions. Contrastive loss is a classic example that minimises the distance between examples from the same class while maximising distance from other classes. Other loss functions utilise triplets of examples (triplet margin) or focus on minimising angles instead of distances (cosine embedding).

Contrastive Loss: 
- Takes a pair of inputs and trains the model to minimize the distance between them if they are from the same class, and maximize the distance if they are from different classes.

Triplet Margin Loss: 
- Takes an "anchor" image, a "positive" (same class), and a "negative" (different class). It forces the anchor to be closer to the positive than to the negative by a defined margin.

Cosine Embedding Loss: 
- Measures the cosine of the angle between two vectors. Useful when the magnitude of the vectors doesn't matter as much as their directional alignment.


### Auxiliary Losses

There are many ways to enhance a model's learning. Auxiliary losses modify properties of a network in addition to whatever task they’re being trained on. Weight regularisation is a classic example of this in which the sum of the absolute weights (lasso) or the sum of the square of the weights (ridge) are added to the loss. Other auxiliary losses penalise similarities in latent representations (orthogonality), force same-class examples to have similar representations (centre), encourage latent distributions to map to statistical functions (ELBO), enforce sparsity in activations (sparsity) encourage higher entropy in outputs (entropy regularisation).


### Other Losses

In addition to all the losses mentioned above we have many more for very specific applications. Some ones that I find particularly interesting:
- **Mixture of Experts (MoE) Load Balancing Loss**: In massive sparse models (like GPT-4), a "router" decides which sub-networks (experts) process which tokens. Left alone, the router will get lazy and send all data to just one or two experts. The load balancing loss artificially penalizes the model if the distribution of tokens across experts is uneven, forcing the entire network to participate.
- **Physics-Informed Neural Network (PINN) Loss / Logic-Constraint Loss**: Used when the output must obey strict real-world rules (like thermodynamic equations or rigid logical syntax). The loss function is defined as standard error plus the mathematical residual of the underlying differential equation or logical constraint. If the model predicts an outcome that violates the laws of physics or the rules of a logic puzzle, it incurs a massive loss penalty.
- **Temporal Difference (TD) Error**: The backbone of Q-learning, not quite a loss function, but worth mentioning. It measures the difference between the model's current estimate of a state's value and the actual reward received plus the estimated value of the next state. It allows the model to learn dynamically step-by-step without waiting for the end of the sequence.

## Conclusion

So as we've seen, there are many loss functions to choose from. It's useful to be aware of the options so that you can always be training your models to success. 