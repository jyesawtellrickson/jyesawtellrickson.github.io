---
layout: post
title: Deep Equilibrium Models and the Implicit Function Theorem
categories: [AGI, Review]
---

Deep Equilibrium Models (DEQs) are a class of models which represent 'infinite depth' neural networks through the use of recursion. Think Recurrent Neural Networks, but instead of recurring in time, they recur in depth. DEQs are interesting because with this depth they're able to represent complex reasoning approaches which require many steps, compared to something like a 16 layer transformer. DEQs have demonstrated competitive performance in language modeling and vision tasks—often improving accuracy while reducing memory by up to 88%.

# Architecture

DEQs consist of a single layer which is continually stacked on itself. If we define our layer as $$f(z, \theta)$$, then we have $$f(f(f(f(z, \theta), \theta), \theta), \theta)...$ as we continually apply that layer. Since it would be impractical to infinitely apply the transformation, there must be a stopping point. The stopping point is called the fixed point equilibrium and is defined by $$z* = f(z*, \theta)$$ where $$z*$$ is the equilibrium value. We can point out that this formulation provides infinite-depth modeling, while having only a constant memory cast (a single layer). This is a great property, especially as we see modern models exploding in memory size, sometimes taking 10 GPUs just to do inference.

So how do we find $$z*$$? One method would be to continually apply the layer and check for when you have converged to a certain point within some error term. This is fine, but could be inefficient in cases where large depth is required. On the other hand, you can apply root-finding methods (e.g., Broyden’s method, Newton's method) which allow you to jump straight to an answer.


# Replacing Backpropogation with a Linear Solver 

If we apply some black-box root finding method, then we can no longer rely on backpropogation through the computation graph to calculate gradients and train the network. Even if we could backprop through the various iterations of the method, it would likely be inefficient, so we need a more efficient method.

The Implicit Function Theorem (IFT) is leveraged to compute gradients efficiently. Instead, by calculating the inverse Jacobian of the parameters in the equilibrium state it's possible to get gradient data from only one 'layer' in the model. This means we can efficiently train the model by looking only at the gradient at the fixed-point equilibrium.

In this case, we need to solve a linear system rather than backpropagating through the entire forward pass.

This interplay—using IFT to compute gradients without the memory overhead typical of conventional backpropagation—is the core efficiency advantage of DEQs. So let's pause on this. With just one single gradient approximation step, you're getting many layers of effort. This was unintuitive for me - how can you understand how the state has evolved from the starting point by looking at the changes happening right at the end when the value has already converged?

The best analogy that I came up with was that it's like finding the sum of a geometric series. You don't need to calculate the sum of each individual value as you step through the sequence, you can calculate the sum directly with a derived formula. Similarly with HRMs, we can analyse the sequence and the convergence to come up with a formula which will tell us all the information we need to know, based on the converged value.

# An Example Model

To better get a feel for this, let's consider a simple unary linear model: $$f(x, t) = x*t + 1$$ where $$t$$ is our parameter to learn. Let's take our dataset to simply be the point (1, 3). We can see that $$t$$ should be 2/3 in this case since the equilibrium will be 3 * (2/3) + 1 = 3.

We can then apply the implicit function theorem. We define some function F(x, t) =  x - f(x) = 0 based on our convergence criterion and then take the derivative wrt. t to get our gradient. In our simple case, this yields a gradient of (left to the reader to derive!):

$$\frac{\partial x}{\partial t} = \frac{x}{1-t}$$

In terms of loss, we can apply the standard MSE loss, giving the full update as:

$$t \rightarrow t - (y - x')\frac{x'}{1-t}$$

Where x' is the output of our network after convergence and y is the target value.

Note that this gradient update rule depends on only three variables: the current parameter value, the target output and the output of our network. This was achieved without relying on any intermediate calculations and without any backpropogation through the network (which is defined to be 'infinitely deep'). This is amazing !

If we run this process with a starting value of 0.5 a learning rate of 0.02 (note it's quite sensitive to learning rate) and iterate the model 10 times (this was roughly sufficient to get convergence), we get the results below (code can be seen [here](https://colab.research.google.com/drive/1rJKB60J4hn9pDCuP3t3dUlKuA4Znep-F#scrollTo=uY8NacXkbONx)). While the system is initially converging to ~2, after just a few updates the network converges to the correct value of 3. This is a very simple linear stack which is equivalent to just a single linear layer, so is not at all useful, but it gives a good proof of concept for how the gradient flows in the DEQ setup.

```text
Step 0: 1.50
Step 1: 1.75
Step 2: 1.88
Step 3: 1.94
Step 4: 1.97
Step 5: 1.98
Step 6: 1.99
Step 7: 2.00
Step 8: 2.00
Step 9: 2.00
Loss: 0.50, Gradient: -4.00, New t: 0.58

Step 0: 1.58
Step 1: 1.92
Step 2: 2.11
Step 3: 2.22
Step 4: 2.29
Step 5: 2.33
Step 6: 2.35
Step 7: 2.36
Step 8: 2.37
Step 9: 2.38
Loss: 0.20, Gradient: -3.53, New t: 0.65

Step 0: 1.65
Step 1: 2.07
Step 2: 2.35
Step 3: 2.53
Step 4: 2.65
Step 5: 2.72
Step 6: 2.77
Step 7: 2.80
Step 8: 2.82
Step 9: 2.84
Loss: 0.01, Gradient: -1.32, New t: 0.68

Step 0: 1.68
Step 1: 2.14
Step 2: 2.45
Step 3: 2.66
Step 4: 2.80
Step 5: 2.89
Step 6: 2.96
Step 7: 3.00
Step 8: 3.03
Step 9: 3.05
Loss: 0.00, Gradient: 0.51, New t: 0.67

Step 0: 1.67
Step 1: 2.11
Step 2: 2.41
Step 3: 2.61
Step 4: 2.74
Step 5: 2.83
Step 6: 2.88
Step 7: 2.92
Step 8: 2.95
Step 9: 2.97
Loss: 0.00, Gradient: -0.30, New t: 0.67
```

# DEQ Applications

In the original paper, the authors apply the model to a relatively simple task, the "copy memory task". This task tests a model's ability to exactly memorise elements across a long period of time. They also test it on a basic language modelling task. More recently, authors have extended DEQs work, one example of which is Hierarchical Reasoning Models (HRM). HRM's have been used to model complex reasoning tasks such as maze solving, Sudoko and even the Abstract Reasoning Corpus (ARC).


# Conclusion

DEQs model infinitely deep networks by solving for equilibrium states. Training hinges on the Implicit Function Theorem to compute gradients with constant memory overhead. This combination of depth, efficiency, and mathematical rigor makes DEQs both elegant and practical—a compelling direction for rational, memory-constrained model design. I like these models a lot because they combine a variety of different techniques and step away from the standard backpropogation techniques that are pervasive in machine learning.