---
layout: post
title: Fine-tuning on Tasks
categories: [LLMs]
---

Foundational models are great. Through self-supervised training alone they're able to learn powerful representations of the underlying data (basically the entire internet) and be useful out of the box. Of course, they're not useful in all cases, so we utilise fine-tuning to make them better in our specific domain. I might be a medical professional, so I collect a bunch of medical documents, or question and answer pairs from doctor-patient conversations and then I show the model these pairs and continue to optimise it. In the end, I have hopefully improved the foundational to be much better at my specific task.

But can we do better?

## It's fine-tuning all the way down

In comes test-time training. The Surprising Effectiveness of Test-Time Training for Abstract Reasoning ([Akyürek et al, 2024](https://arxiv.org/html/2411.07279v1)) describes a method which is able to use more test-time compute to drastically improve the capabilities of LLMs.

Put simply, test-time training can be described as fine-tuning your model further based on the specific example. In contrast to fine-tuning where you would typically fine-tune on a collection of samples, in test-time training you fine-tune on only the example that you're trying to predict in that exact moment.

In order to fine-tune on the task at hand, you need some objective. This can be a standard self-supervised objective, but better is if it can be a supervised one, directly generated from the test case.

## An ARC solution

The original paper applies the method to the Abstracting Reasing Corpus, a complex reasoning challenge crafted by Francois Chollet (see my [overview](https://towardsdatascience.com/ais-next-step-abstraction-reasoning-db2d90e82799)).

In addition, with the ARC Prize (a related competition) coming to a conclusion in December, methods were shared. A great [write-up](https://www.kaggle.com/competitions/arc-prize-2024/discussion/545671) by Guillermo Barbadillo describes how he was able to use test-time training to significantly improve his performance on the ARC challenge.

In the case of ARC, you can generate multiple training samples from the test cases which makes the method particularly effective. The paper's results show a drastic +30% improvement in accuracy (6% -> 36%).

## Inference-time compute

Test-time training is an example of inference-time compute which is quickly becoming the next hot thing following OpenAI's 'reasoning tokens'. It's likely we'll see more innovative inference-time improvements coming in the next couple of years.
