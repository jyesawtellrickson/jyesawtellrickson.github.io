---
layout: post
title: Enumerating Embedding Mechanisms
categories: [LLMs, AGI]
---

LLMs 'see the world' through tokens. Sentences are chunked up into tokens which are then embedded into vectors to work with.

What makes them powerful is that they're embedding ideas, or concepts, or meanings, not just literal text. By abstracting a token to an embedding and then learning those embeddings by fitting to human knowledge, they're making that token represent something much more nebulous. Worth noting: this isn't a new methodology, e.g. word2vec, which does much the same, came out in 2013.

What's really important is the idea behind the token, and language is just one way we as humans evolved to communicate ideas. But, is it the only way? Is it the most efficient way?

Let's see how else we can embed ideas, with the running example of the concept of gravity:

- words: "gravity is the phenomenon that is responsible for bringing objects towards the ground" (also sign language); 
- using a formula: G=m1m2/s^2; 
- via code: force = mass * acceleration; 
- via graphs: object1 --force-- object2; 
- datastreams: e.g. 100011101011010
- images (2D, 3D representations of reality): apple falling from a tree with faint trajectory 
- via data / graph: data points from pencil drop experiments
- dance: this can be considered a multi-dimensional object (e.g. hand, leg, etc.) moving in a 3D space  
- music: words=bars, tokens=notets; 12notes per octave, 5ish octaves = 60 characters, unlike language, multiple tokens can be enabled at once, it's what makes music great (sound effects are objects of music)

Compression
(a man standing by a tree is 8tokens*128embd = 2^10 floats vs. 32x32px = 2^10 floats) - if you want to be descriptive, image seems a lot more information-dense than language - because it's grounded in the physical world? e.g. counter-example "electricity", but with language transformers we can accumulate all the meaning into one token, can't do that with images (ViT)? [if i take a cat image and a dog image, can I create an image with one of each?]


(also, multi-modal, images + text + raw readings from sensors)
 b

Features of a good language:
* Universality: can express anything
* Efficiency: can express with fewer bits
* Data: has pre-existing data that can be leveraged



What is an embedding on a graph?

Problems with language:
• Lack of Direct Grounding: Language can describe concepts abstractly, but without grounding in sensory data or experience, it may not fully capture the nuances of the physical or social world. Example: A robot needs spatial or tactile representations to navigate, which language alone may not provide.
• Sequential Nature: Language is inherently linear (words, sentences), which can make it less suited for parallel or multi-dimensional reasoning, such as in vision or spatial tasks.

In the real world, you don't get language inputs, you get sensor readings. These sensor readings could be agg'd, but you'd have to learn those / build those.

Why are LLMs scary though? Because despite the lack of sensory handling, we have already built sufficient tools to collect and process sensory data and enable high-level actions. Why? Because we also suck at handling raw sensory data! They can also write programs/create tools that can process the data for them. 
=> you should work either on LLMs (the most efficient reasoners), or on efficient sensor-based controllers.
==> but LLMs could just discover the new controllers themselves (i.e. most big breakthroughs can be written as code)


Project: Learning the concept of gravity in computer vis