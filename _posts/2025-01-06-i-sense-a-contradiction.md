---
layout: post
title: I Sense a Contradiction
categories: [LLMs]
---

When playing around with ChatGPT in the non-obvious space of prompts, you can find some interesting behaviours. 

"Bayesian prompts"

The task was to forecast the number of animals in an ecosystem where we have data points at finite time steps. The data points look exponential, but a quadratic equation is suggested. Once the model works out the initial estimates, a new data point is added, introducing a contradiction.

https://chatgpt.com/share/677b2972-a058-8000-9408-f5bf50d56a71

While performing the calculations, the model observed an error in its output and wrote:

> "--> I sense a contradiction"

Which was followed by:

> "Thank you for catching that! Let us carefully recompute..."

This looks a lot like a multi-agent system. Two major possibilities:
1. Two agents at inference: an evaluation agent is checking the output of the main agent and stepping in when it predicts the output is erroneous.
2. (more likely) Two agents at training: when training the model, it's possible to include examples where the output is initially incorrect, this is observed with the interjection and then a correct output follows. In this way, the trained model can 'correct itself' as statistically it learns the sort of patterns that lead to the "contradiction" message, and then in some way reset itself. This data could be hand-crafted but is likely synthetic.

On top of the error detection above, as it was getting deeper into the calculations, output was stopped and replaced with

> "Analyzing" 

It's unclear to me why the output was hidden, but it may have been that it was pausing to use the tools. After the output there were links to python usage to do key calculations.