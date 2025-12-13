---
layout: post
title: "Paper Review: AlphaEvolve"
categories: [Review]
---
AlphaEvolve paper review


Feels like neural-guided program synthesis / sketch.

Actually a very simple approach. The overall idea is simple, but they alone have the compute to make it even possible. The magic in this work is likely all the small things they had to do (e.g. MAP elites algorithm in the DB), scheduling across so many GPUs.

Similar to DeepSeek-R1 model. Create some complex scaffolding, collect valuable traces, improve base models with those traces, repeat.

Currently it's costly because you have to restart the whole training procedure at each loop. Why? LLMs can be fine-tuned, but (a) hardware/software scales up, so better to re-train with new architecture, (b) local minima.

How to solve? Faster training of models = faster convergence. Remove RLHF step.

Run the fine-tuning part many times before re-training full base model. Can eek out some gains. (Deepseek did one iteration of this when they distilled onto Qwen)

Is using evolution by applying small changes. What about other search methods? e.g. genetic modification with cross-over meiosis 

No tuning of the model. What about adding into the ensemble models which are continuously fine-tuned (input: prompt, output: good solution; negative case is the the bad solutions).
