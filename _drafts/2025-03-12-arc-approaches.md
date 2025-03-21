---
layout: post
title: Approaches to Solving ARC Prize
categories: [AGI]
---

The ARC Prize has ....

We can look at the top techniques that have been applied to solve ARC so far:
1. Brute-force program search: The most traditional approach. [Icecuber](https://github.com/top-quarks/ARC-solution) used this approach during the inaugaral ARC challenge, scoring 129/419.
2. Neural-guided program search: DreamCoder 
3. Direct program induction: Variational Autoencoders are example of a program that can be learned directly on the data to output solutions. 
4. LLM program search: LLMs. Note that LLMs can also be asked to directly output answers, but this has shown to be ineffective. 
5. Latent program search: 


## Latent Program Search

The core algorithm of latent program search is as follows:
1. For each input/output pair, get the corresponding latent vector which represents a first estimate at the program that can solve it. This encoder maps from specification (I+O) to program (P) IO->P.
2. Define the best-guess program as the average of the latents across each input/output pair.
3. Run a gradient descent optimisation for K steps with the n problems as your batch and perturbations in the latent space for your gradients. Loss is log loss. This is across the decoder which is f(i, P) -> O
4. Choose the z from the K steps which gave the least loss.
5. Apply to the true input.