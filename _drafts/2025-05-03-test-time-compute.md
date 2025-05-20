---
layout: post
title: Test-Time Compute
categories: [AGI]
---

Test-time compute has recently been popularised with LLMs (e.g. o1/o3, DeepSeek-R1 and other reasoning models) as its application has allowed LLMs to perform significantly better on complex reasoning problems (e.g. mathematics, reasoning). But why does test-time compute work? Is it a new idea? Let's explore these questions.

# Why Test-Time Compute

Firstly we should consider why test-time compute works in the case of LLMs. A common example of this is chain-of-thought reasoning in which an LLM is prompted to first think about its answer, thus investing more in test-time computation.

We can describe three key reasons why this improves results:
- **Decomposability**: complex problems can be decomposed into simpler ones. The model can then solve the simpler problems and stitch them together. This constrains the model to walk through a causal chain rather than just 'guessing'.
- **Increased depth**: token space is the model's inference time working memory. It can explore deeper than it's trained (e.g. 96 layers) by offloading some of the depth to the token sequence.
- **Sampling**: generating multiple tokens, then feeding those as inputs to generate the answer is somewhat like sampling and can reduce hallucination and surface the correct reasoning path, similar to ensembling methods.

These three methods are generally applicable outside of LLMs and have been used before. Now let's have a look at test-time compute outside of LLMs.

# Test-Time Compute Outside of LLMs

There is an entire field of AI research called **search**, you might have heard of it. In search, a program is tasked with finding the correct actions which will yield a goal state, given the starting state.

$$P=(S,A,T,s_0,G)$$

Many intro to AI courses feature A* search as a classic example where a model 'learns' the space at inference time. However A* doesn't learn anything prior to that, there's no learned bias enabling the model. Instead, more complex models like AlphaZero form good examples where a model is trained to have strong priors on what good actions look like (policy and value networks). Once trained AlphaZero uses Monte Carlo Tree Search (MCTS) rollouts to determine the best move which allows it to explore many potential plays instead of just guessing the best action based on the first output of the policy network.


**Probabilistic models** define distributions which are designed to be sampled upon at inference time. Specifically, they define a distribution over latent variables z, observed data x, and outputs y and use inference to compute beliefs.

$$p(y,z|x) = p(y|z, x) * p(z|x)$$

At test time, the posterior p(z|x) must be computed or approximated. They often rely on Markov Chain Monte Carlo (MCMC) or Variational Inference which are computationally expensive. A prime example is Variational Autoencoders which consist of an encoder and decoder to model the mapping to and from a latent distribution.


Test-time optimisation is a subset of test-time compute in which the model continues to improve after training (e.g. Meta Learning). During training the model is setup to be adaptable with specific training regimes, which means they can take a few gradient steps at test time. 


Energy-based models (EBMs) learn useful landscapes which are then traversed at test-time to generate useful samples. Examples of this include diffusion models (e.g. Stable Diffusion) which iteratively refine the output, stepping through the landscape until they find a low energy state.


Data augmentation has historically been applied in computer vision to improve predictions by investing more compute at test-time. Inputs are augmented in various ways (e.g. rotation, shift) and the results are combined to produce the final predictions. This can be retroactively applied to any model, but can also be trained from the start.


# The Test of Time

Across these domains, test-time compute often compensates for limitations in model capacity or data efficiency. It reflects a broader principle: if the model can't learn everything offline, we can use online compute to search, adapt, or verify.

applied in domains where generalization, flexibility, or adaptation outweigh the need for low-latency inference.
* Hard-to-generalize tasks
* test time adaptation tasks

# Notes


Program synthesis and symbolic AI (symbolic search); known goal states so can check status and retry / adjust
Iterative refinement
Self-judge: proposing different paths and scoring them (e.g. LLM judge) to choose which one
Ensembling: just have more models (e.g. different seeds) to increase the cost at test


Types of problems:

Components:
* Data: state (e.g. TSP, maze, question), multiple examples (e.g. learn and apply), self-created (e.g. build new problems based on input/output - can be done without verifier? e.g. one-way functions like encryption, matrices that can't be inverted)
* Output: multi-step (e.g. actions in maze, MPC), step (e.g. ARC output)
* Verifier: external, internal, internal+(e.g. LLM judge), world model, none
* Model: ensemble, iterative
* Search: raw, latent, average, none

Few-shot learning:
* Practice on examples until you're confident in your guess
* e.g. search possible transformations
* e.g. ARC, program synthesis, AlphaCode, Dreamcoder

Optimisation across multiple actions:
* known minimisation function, e.g. total distance travelled; known goal state
* simulating trajectories with word model
* e.g. travelling salesman, maze navigation, AlphaZero
* frame image classification as a search for the transformations that transform a base state (class) to the predicted one.

Generation / iterative refinement:
* training samples suggesting what good looks like
* can take many small steps to reach the desired outcome
* can iterate on a solution eternally
* has some version of an internal oracle
* e.g. image generation diffusion models, LLMs

General prediction:
* e.g. data augmentation for image generation

Symbolic domain:
* the data can be directly manipulated according to structured rules / functions
* e.g mathematics, ARC+DSL, coding



Characteristics:
* Search: tree, beam, in latent space, 
* Scratchpad 
* Learned priors
* don't predict the output directly, predict a function which creates the output, have an internal measure of output quality

Meta learning


Using an oracle:
* oracle that will tell you if you're right or wrong
* discriminative: just go down from top to bottom
* good: adjust your predictions based on info (it's not class A, so maybe not class B??)



Self as the verifier? (e.g. LLMs)
How do world models compare?


How does ML take gradient steps when it doesn't know the solutions? (is it posthoc?)
Aren't all NNs probabilistic models? What makes it unique?



If I learn with data augmentations, does it produce better outcomes?

Dreamcoder