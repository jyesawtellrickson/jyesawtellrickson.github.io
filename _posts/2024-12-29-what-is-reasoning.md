---
layout: post
title: What is reasoning?
categories: [AGI]
---

There's a lot of talk about whether LLM's can reason or not. With the release of OpenAI's o1 and now the upcoming release of o3 which are touted to be strong reasoners, it seems we're getting close to 'reasoning capabilities', but what does that mean? Let's try to debug what reasoning is.

One basic definition we can start with: "reasoning refers to the ability of an intelligent system to logically process information, draw inferences, solve problems, and make decisions in a manner that is flexible, robust, and generalizable across domains." 

Let's get more detailed.

## Types of reasoning 
Reasoning is not something that's new to AI. It has been studied throughout history as a way to understand how our own minds work. Leveraging this work, we can take a step back and look at the kinds of reasoning that exist:

- Based on Logical Approach
    - Deductive Reasoning: From general to specific.
    - Inductive Reasoning: From specific to general.
    - Abductive Reasoning: Inference to the best explanation.
- Based on the Nature of Evidence
    - Statistical Reasoning: Relies on data and probabilities.
    - Bayesian Reasoning: Combines prior beliefs with new evidence.
    - Causal Reasoning: Relies on cause-effect relationships.
- Based on Contextual or Practical Focus
    - Pragmatic Reasoning: Centers on practicality and outcomes.
    - Temporal Reasoning: Involves timing and sequences of events.
    - Moral/Ethical Reasoning: Evaluates decisions based on ethics.
- Based on Analogies or Comparisons
    - Analogical Reasoning: Infers similarities between cases.

Critical Thinking
Creative Reasoning
Counterfactual Reasoning: imagining alternative scenarios and their outcomes
Reasoning under uncertaintity: making decisions when information is incomplete or noisy.

## Where are we today?

A comprehensive review paper on reasoning is "Reasoning with Large Language Models, a Review" by Plaat et. al, 2024. Within, they discuss three approaches to improving LLM's reasoning abilities that are prevalent in the literatutre:
1. Generate
2. Evaluate
3. Control 
