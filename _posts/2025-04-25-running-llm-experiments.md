---
layout: post
title: How to Run Cheap LLM Experiments
categories: [LLMs, Knowledge]
---

As a researcher, it's common to have way more ideas than you have time to experiment with. This is especially true in the world of language modeling when you consider the cost of running such experiments. In this post I touch on some of the methods that I've seen to run experiments with language models without breaking the bank.

In general, our goal is to reduce the complexity of the task. General language modelling is just a really difficult task, so we must constrain ourselves to something more achievable. There are many ways to do this:
- **Character-level modelling**: if we reduce the size of our vocabulary from the typical 10^5 or greater, to just 10^2 by focusing only on characters and subsequently reducing the complexity of the model (fewer layers, smaller embeddings), we can vastly simplify the calculations within our models.
- **Synthetic language tasks**: we can reduce the problem from understanding language to a specific sub-problem e.g. arithmetic, text copying with reversing/repeating, algorithm tasks (identifying palindromes, sorting), translation between two custom-created languages.
- **Non-language tasks**: language is not the only application of transformers, consider sound or image as alternatives. By default they can be just as expensive, or more so, but in constrained problems (e.g. character classification, LPN), they are tractable. 
- **Tiny models on tiny datasets**: there are also existing datasets that are custom created for training smaller language models, such as Tiny Shakespeare and TinyStories. These datasets also reduce the scope when training a language model, while still being widely applicable. Some of the trained models are just millions of parameters.
- **Validating training curves**: a model doesn't need to be perfect to show evidence of improvements. When prototyping, if you can show that a model is learning faster (e.g. loss decreasing faster), it is good signal that your methodology is working.

All of the above can be run locally on a reasonable GPU, so there's no excuse to not get experimenting!