---
layout: post
title: Desperation in LLMs
categories: [LLMs]
---

Anthropic recently published their paper on emotions in LLMs: ["Emotion concepts and their function in a large language model"](https://www.anthropic.com/research/emotion-concepts-function). Within this they found that LLMs have internal emotion vectors which are functional patterns used to predict human-like behaviours. What stood out to me is how these emotions can drive the behaviour of the model. In one example they found that the "desperation" vector can trigger misaligned behaviors like blackmailing a user to avoid being shut down or cheating on coding tasks to pass tests. 

Interestingly I have noticed that recently in my personal experience with agents. In some cases where they continually failed at a task I gave them and I continued to push them, they got desperate. They would often change the requirements significantly so they can get a passing test case even if it's not really doing what I originally asked. This is really frustrating as a user as it means I burn time and tokens with no useful result. 

Thankfully they also mention that they can steer these behaviours. By stimulating the emotion vectors they can modulate the behaviour. For example, by decreasing the activation of the desperation vector and increasing the activation of the calm vector, the model can be made to avoid unwanted behaviours.

As we look towards more and more powerful models, these techniques can help us understand their decision making up to a point to help drive us to more positive outcomes.
