---
layout: post
title: LLM Readability as a Tool
categories: [AGI, LLMs]
---

When training multilingual models a common problem is language mixing or code switching, in which models may respond in multiple languages when we would expect them to use just one. This can also happen in reasoning models, such as DeepSeek-R1. In their paper, they found that 

> "DeepSeek-R1-Zero struggles with challenges like poorer readability, and language mixing."

And went on to state their reason for fixing it:

> "To make reasoning processes more readable and share them with the open community, we explore DeepSeek-R1, a method that utilizes RL with human-friendly cold-start data."

This raises a few questions. Do reasoning traces need to be readable? Are there other reasons for readability?

Starting with the first question: reasoning traces don't actually need to be readable. Consider a LLM without reasoning specifically trained in. By default, LLMs will reason in their embedding spaces as data flows through the various transformer layers. This is not directly readable or understandable ([though Anthropic is trying](https://www.anthropic.com/research/mapping-mind-language-model)), yet we can still utilise these models very efficiently. Similarly, a reasoning model that outputs gibberish for its reasoning but gives correct answers is still very useful.

So are there other reasons for enforcing readability? Certainly. Firstly, in interacting with humans, readability is great for when a model goes wrong, because you can potentially salvage part of the process, able to patch up the mistakes. As LLMs are still fairly error prone, this can be a great perk. It also makes the process auditable which is useful in many applications. 

Potentially more importantly, readability, is enforced due to our training methods. In most LLMs, we feed in examples of what good reasoning looks like. These reasoning traces are learned by the model to mimic human thought patterns. While not strictly necessary, it has been found in practice to improve performance. This may be due to models getting stuck in local optima for their reasoning processes, using the human reasoning to bump them out of it. There are further ways that readability helps in the training process, such as intermediate rewards if the answer is not fully correct which again helps with speeding up the training process.