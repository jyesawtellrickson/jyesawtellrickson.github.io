---
layout: post
title: Test-Time Compute Matters: From LLMs to Search
categories: [AGI]
---


Test-time compute has recently been popularised with LLMs (e.g. o1/o3, DeepSeek-R1 and other reasoning models) as its application has allowed LLMs to perform significantly better on complex reasoning problems (e.g. mathematics, reasoning). This article explores why it works, why it's not new, and how it's been employed across different AI paradigms.

## Why Test-Time Compute?
Firstly though, why should we care about test-time compute? It gives good results. In the world of LLMs, training costs have sky-rocketed and the training process has been optimised many times over. If there was a low hanging fruit, it would be good to take. In this setting, test-time compute is just that and showed significant performance improvement across a wide variety of problems. 

More generally we can think of an analogy with human thinking: if you're working on a tough problem, your goal is generally not to solve it as fast as possible, it's to solve it well. We dedicate much thought process to the most gnarly (e.g. best movie of all time) or most important (e.g. cure for cancer) of problems, but in the regular AI inference paradigm we simply pass it through one network all the same. 

There are also a subset of interesting problems where the information given at test-time is very unique, or very large. In this case, models which are able to learn and adapt the most from that high signal information can perform better than those that do simple inference.

So how is test-time compute leverage in LLMs?


## Test-Time Compute in LLMs
Firstly we should consider why test-time compute works in the case of LLMs. A common example of this is chain-of-thought reasoning in which an LLM is prompted to first think about its answer, thus investing more in test-time computation.

We can describe three key reasons why this improves results:
- **Decomposability**: complex problems can be decomposed into simpler ones. The model can then solve the simpler problems and stitch them together. This constrains the model to walk through a causal chain rather than just 'guessing'.
- **Increased depth**: token space is the model's inference time working memory. It can explore deeper than it's trained (e.g. 96 layers) by unrolling computation in token space.
- **Sampling**: LLMs can generate multiple candidate reasoning chains and aggregate their outputs, which resembles marginalisation over latent reasoning paths.

These three methods are generally applicable outside of LLMs and have been used before. LLMs are also used for in-context learning: giving them an example of what you want them to do in the prompt then giving them a new, related query. The model has learned how to interpret a wide variety of problems during training which allows it to generalise at test time. 

Now that we've seen various methods that allow LLMs to utilise test-time compute, let's explore other applications in AI.

## Search 

There is an entire field of AI research called **search**, you might have heard of it. In search, a program P is tasked with finding the correct actions A which will yield a goal state G, given the starting state $s_0$, guided by some transition function T between states S and a value model.

$$P=(S,A,T,s_0,G)$$

Many intro to AI courses feature A* search as a classic example where a model 'learns' the space at inference time. However A* doesn't learn anything prior to that, there's no learned bias enabling the model. Instead, more complex models like AlphaZero form good examples where a model is trained to have strong priors on what good actions look like (policy and value networks). Once trained AlphaZero uses Monte Carlo Tree Search (MCTS) rollouts to determine the best move which allows it to explore many potential plays instead of just guessing the best action based on the first output of the policy network. Another example is search across programs which is embodied by AlphaCode, or Dreamcoder.

In the above cases, the search is carried out with the assistance of a tool which can continually tell you information about the problem (e.g. what's the transition to the next state in the game, code executes correctly to yield answer). However, models can learn what's called a **world model** which can be used to understand the expected transitions in between states. This enables the search to be more free. A great example of this is [Dreamer V3](https://www.nature.com/articles/s41586-025-08744-2) which is able to learn a world model across diverse control domains including Breakout, Ms Pacman and Minecraft.


## Probabilistic Models

**Probabilistic models** define distributions which are designed to be sampled upon at inference time. Specifically, they define a distribution over latent variables z, observed data x, and outputs y and use inference to compute beliefs.

$$p(y,z|x) = p(y|z, x) * p(z|x)$$

At test time, the posterior p(z|x) must be computed or approximated. They often rely on Markov Chain Monte Carlo (MCMC) or Variational Inference which are computationally expensive. A prime example is Variational Autoencoders which consist of an encoder and decoder to model the mapping to and from a latent distribution.


**Energy-based models** (EBMs) are a subset of probabilistic models which learn unnormalised probabilistic models. They learn useful landscapes which are then traversed at test-time to generate useful samples. While not traditional EBMs, diffusion models (e.g. Stable Diffusion) are score-based models and their training process has been shown to be equivalent to EBMs. Diffusion models iteratively refine the output, stepping through the score-based landscape until they find a good state.

## Versatile Compute Extension Methods

**Test-time optimisation** is a subset of test-time compute in which the model continues to improve after its initial training. Meta Learning is a classic example of this in which the model is trained with an objective that includes test-time optimisation. During training the model is set up to be adaptable, which means they can take good quality updates at test time. One modern example of this is the Latent Program Network (LPN) which shapes a latent space such that it can be traversed at test time.

Data augmentation has historically been applied in computer vision to improve predictions by investing more compute at test-time. Inputs are augmented in various ways (e.g. rotation, shift) and the results are combined to produce the final predictions. This can be retroactively applied to any model, but can also be trained from the start. This is similar in nature to the **sampling** that we saw for probabilistic models and even LLMs in that you're trying to squeeze as much information out of your architecture to increase robustness when doing predictions.

While data augmentation runs the same model multiple times, it's also possible to just have more models. Ensembling has been applied successfully across many fields and problems. It can be as simple as training the same model on different splits of the data, or as complex as training a variety of unique models with expected differences in biases. Ensembling generally works by allowing models to pool their good estimates and marginalise the poor ones. 



## The Test of Time

Test-time compute, far from being a new concept, is a recurring solution across AI paradigms for injecting problem-specific computation at inference time. It often compensates for limitations in model capacity, or data efficiency. Whether through search, sampling, or test-time optimisation, it serves a critical role in boosting generalisation beyond what static models can achieve. As models scale, we expect even more of the 'intelligence' to shift from training to test-time reasoning.

It reflects a broader principle: if the model can't learn everything offline, we can use online compute to search, adapt, or verify.

