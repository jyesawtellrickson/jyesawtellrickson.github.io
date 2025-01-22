---
layout: post
title: What is reasoning?
categories: [AGI]
---

There's a lot of talk about whether LLM's can reason or not. With the release of OpenAI's o1 and now the upcoming release of o3 which are touted to be strong reasoners, it seems we're getting close to 'reasoning capabilities', but what does that mean? Let's try to debug what reasoning is.

One basic definition we can start with: "reasoning refers to the ability of an intelligent system to logically process information, draw inferences, solve problems, and make decisions in a manner that is flexible, robust, and generalizable across domains." 

Let's get more detailed.

## Two Broad Categories of Reasoning 
Reasoning is not something that's new to AI. It has been studied throughout history as a way to understand how our own minds work. Leveraging this work, we can take a step back and look at the kinds of reasoning that exist:

We can start with two generic categories of reasoning:
1. **Certainty from rules or axioms**: given general statements, we can reason about what else must be true. A classic example of this is mathematics theorem proofs where one starts with a set of axioms and continues to combine them to reach a more interesting statement.
2. **Probabilistic generalisation**: given some observations, what useful information can we probably conclude from it? Scientists apply this every day when they take experiment results and extrapolate to new theories.

These two different reasoning categories must be approached quite differently.

## Certainty from Rules

In the case of certainty, we're largely dealing with deductive reasoning where we continue to derive truths based on a starting set of axioms. While this may seem very limited, there are plenty of applications.

Approaches to solving these problems generally include symbolic manipulation with formal systems. For example, you might have to verify if a system satisfies a certain set of constraints. This can be verified by following rigid calculations and logic. Through simplifying assumptions it's possible to express many systems in more rigid structures to which we can apply this type of reasoning.

Also, there's _a lot_ in mathematics.

## Probabilistic Generalisation

Probabilistic generalisation is a very broad category in which observations are combined to reach new findings. Inductive reasoning is a standard application of these principles in which given a set of observations some truth is predicted. 

> The last time I went hiking it was raining, the time before it was also raining. Therefore, it's likely that the next time I go hiking it will be raining too.

Machine learning techniques are classic applications of this type of reasoning. They are fed many examples and expected to output functions that describe some relationship. For example, people might train a linear classifier to predict house prices based on various properties of the house. Or one could train a CNN to recognise various patterns in images to label them as a cat or dog.

More generally, the scientific method follows this approach. A hypothesis is made and then reviewed with new data to make new conclusions.


## Other Reasoning Types

We've touched on just two broad categories of reasoning, but there are many tangential and sub-fields of reasoning. This different reasoning types are generally some form of previously discussed reasoning applied to a specific problem.

We mention many of these with a description for completeness:
- Causal reasoning: identifies cause-and-effect relationships between events.
- Temporal reasoning: considers time-related relationships and sequences.
- Probabilistic reasoning: evaluates likelihoods and uncertainties to draw conclusions.
- Analogical reasoning: draws conclusions based on the similarities between two situations or concepts.
- Spatial reasoning: understands and manipulates spatial relationships and configurations.
- Moral reasoning: determines right or wrong actions based on ethical principles or societal norms.
- Critical reasoning: evaluates arguments for validity, consistency, and logical soundness.


## Next Steps

But how can you measure the quality of your reasoning? How do current AI systems perform?

In future work, we'll cover classic tests for evaluating reasoning as well as the current state of reasoning in AI models.


