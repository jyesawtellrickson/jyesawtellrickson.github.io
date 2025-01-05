---
layout: post
title: GPUs are Awesome
categories: [AGI]
---

I'm definitely late to the party, but I think I just grok'ed how awesome GPUs are. 

I'm using [Ollama](https://ollama.com/) to run LLM's locally and I just downloaded a new model. The model is around 9GB on disk, so with my reasonable 30MB/s connection, it took around 5m. I then went on to do inference.

With a basic test like "why is the sky blue?" the model quickly returned a reasonable response. Wait. It needs to use all those parameters I just downloaded, and it needs to do that for EACH token. So for the 5 minutes it took me to download the file, my GPU has processed that many times over in less than a second. That's crazy.

I do have some understanding of GPUs (e.g. x-much VRAM to fit your model) and realise that you have to use all the parameters to run inference, but it never really grok'ed until now. It's amazing the speed at which the GPU can process data.

I didn't run a test, but according to [this](https://www.hardware-corner.net/guides/hardware-for-mistral-llm/) summary, inference for Mistral 7b is around 60 tokens/s on my GPU. Considering each token utilises the 9GB, that's 0.5TB parameters processed each second (and math done on top of that!). Mind boggling.

An unrelated, informative video on CUDA I watched recently to end this post: [How CUDA Programming Works | GTC 2022](https://www.youtube.com/watch?v=n6M8R8-PlnE&list=PLdmLRmaL6vCjaR9u79Dc0gjGXV_DvdUHe&index=5&ab_channel=DantheMan).