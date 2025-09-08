---
layout: post
title: Think it Faster in AI
categories: [Productivity]
---

Ever since reading ["How could I have thought that faster?"](https://www.lesswrong.com/posts/rYq6joCrZ8m62m7ej/how-could-i-have-thought-that-faster) this year, I have been trying to put it into practice. Working with AI models, I found there are plenty of opportunities. One can spend hours on some buggy code just to find the bug they fixed wasn't the real problem after all, or that someone had already solved it five years ago on Stack Overflow. One can invests hours into modelling to realise that there was a far simpler approach if you just thought about it from another angle...

Following are two examples I've come across recently which are simple (1) and annoying (2).

Reading through CS231n's course notes, I stumbled upon what I believe is Andrej Karpathy's(https://karpathy.ai/) advice when training any DL model.

1. Check your initial loss is accurate (e.g. for cross-entropy classification loss log(1/C)) - this saves you straight away by making sure you're optimising the right thing.
2. Train on a very small collection of training samples and optimise to 100% accuracy - checks your whole training loop is working as you expect it to, can catch a variety of bugs.
3. Begin full training, but just try a few learning rates which gets you to start dropping loss after 100 iterations or so - this starts to give you a feel for how your model is responding and can save you from wasting time launching runs with unreasonable metrics.
4. (do various paramater sweeps, full training, etc.)

At each step of the process, we're stopping and thinking, are we going in the right direction? Is there something amiss? I think these are all great, simple examples of how we can 'think things faster' by investing a bit of time early on. I wonder how many times whoever wrote these rules made those mistakes and thought back to themselves, "how could I have done that faster?"

In my own work, I was setting up a transformer training flow to deploy on our network. I assumed that it was going to run just fine because we have decent GPUs to leverage, I even did some back of the hand calculations to confirm it. I set it up locally, got it running and went to deploy, but...it crawled. Really slowly. I overestimated the GPU and underestimated the pace of inference for the model. My calculations weren't horribly wrong, but they were wrong enough. So how could I have thought it faster? 

Making a quick calculation to estimate the viability was a great start, 10 points for that. However, there was a much easier way. I could have actually just run a test on the system first. Sure, there would have been some setup cost but a quick test would have shown me where my estimates were wrong. I could have thought it faster. -20 points.


All that to say, there are plenty of opportunities to get introspective. I'm slowly getting better at noticing them, and I do find it is making me more efficient (slowly). I just wish I had read that article faster! 
