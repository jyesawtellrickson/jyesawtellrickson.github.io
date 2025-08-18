---
layout: post
title: Understanding Recurrence in Modern Models
categories: []
---

- we've all heard of recurrent neural networks (RNN)
- but there are many ways to 'recur' in a model
- autoregressive models, e.g. transformers, as an example of recurrence
- taxonomy of recurrence: sequence length, depth, spatial dimensions (e.g. GNN), others
- All of these can be seen as: hk+1=fθ(hk,x) where the k is over something different (e.g. time, layer, spatial)
- some of the key models
- why recurrence is important
- key issues with recurrence
- next steps for recurrence

# Understanding Recurrence in Modern Models

We’ve all heard of recurrent neural networks (RNNs), the workhorse of sequence modeling for decades. RNNs explicitly model sequences by maintaining a hidden state that evolves over time, allowing the network to 'remember' information from previous inputs. But recurrence isn’t limited to RNNs. In fact, there are many ways that modern models implement some form of recurrence, often in unexpected ways.

# Beyond Traditional RNNs: Different Forms of Recurrence

At its core, recurrence refers to the repeated application of a function where the input depends on the previous output. This idea can manifest in multiple dimensions: over time, over layers, over space, or even over latent representations.

For instance, autoregressive models like transformers exhibit a form of recurrence over their outputs: each token prediction depends on previously generated tokens. Though transformers are often celebrated for parallel computation and attention mechanisms, autoregressive generation is fundamentally a sequential, recurrent process.

# A Taxonomy of Recurrence

Recurrence can be classified along several axes:
- Sequence length / temporal recurrence – the classic case in RNNs or LSTMs, where a hidden state evolves as new time steps are processed.
- Depth recurrence – in deep equilibrium models, a single layer is applied iteratively until convergence, essentially making depth an unrolled recurrence.
- Spatial recurrence – seen in graph neural networks (GNNs), where node embeddings are updated iteratively based on neighbors, propagating information across the graph.
- Other forms – iterative refinement in diffusion models or iterative inference in energy-based models can also be framed as recurrence.

All of these can be described by a general form:

$$ h_{k+1} = f_\theta(h_k, x) $$

Where k indexes the type of recurrence: time, layer, spatial iteration, or another dimension. The function f defines how information is transformed at each step.

# Key Models Leveraging Recurrence

Several important models illustrate the diversity of recurrence:
- RNNs, LSTMs, GRUs – temporal recurrence.
- Transformers (autoregressive) – sequential output recurrence.
- Deep Equilibrium Models (DEQs) – recurrent depth.
- Graph Neural Networks – spatial recurrence.
- Diffusion models – iterative latent refinement.

Each of these models exploits recurrence to capture dependencies that a single, feedforward pass would struggle to model.

# Why Recurrence Matters

Recurrence allows models to process variable-length sequences, perform iterative refinement, and share parameters across steps or layers. It brings flexibility and efficiency: rather than learning separate parameters for each step, recurrence lets models generalize across time, depth, or space.

# Challenges with Recurrence

Despite its power, recurrence introduces difficulties:
- Gradient instability – vanishing or exploding gradients in deep or long recurrences.
- Computational complexity – sequential dependence can hinder parallelization.
- Convergence issues – in iterative models like DEQs or diffusion models, convergence can be slow or unstable.

# Recurrence and the Human Brain

Interestingly, recurrence is not just a computational abstraction, it has clear parallels in the human brain. Neurons in the cortex are highly recurrent: signals are not processed strictly in a feedforward manner. Instead, feedback loops allow the brain to integrate information over time, refine perceptions, and propagate context across layers of processing.

For example, the visual cortex uses recurrent circuits to refine object recognition, especially under ambiguity or partial occlusion. Similarly, working memory relies on recurrent activity in prefrontal circuits to maintain and manipulate information over short periods. In essence, recurrence enables the brain to iteratively update its internal state based on new inputs and prior context, a principle mirrored in RNNs, DEQs, and GNNs.

Understanding recurrence in artificial models can therefore shed light on how the brain balances memory, prediction, and computation, while neuroscience inspires more robust architectures for iterative reasoning in AI.

# The Future of Recurrence

Modern research explores hybrid approaches that combine recurrence with parallel computation, attention mechanisms, and learned iterative solvers. Examples include universal transformers (depth recurrence with attention) and equilibrium graph models (iterative message passing with convergence guarantees). The goal is to retain the benefits of recurrence—flexibility and expressivity—while mitigating its drawbacks.

Recurrence is not just a feature of old-school RNNs—it’s a unifying principle across many modern models, whether over time, depth, or space. Understanding it helps us design models that better capture complex dependencies and iterative processes in data.