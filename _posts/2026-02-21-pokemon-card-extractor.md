---
layout: post
title: A Quick Pokemon Card Extractor
categories: [AI, Project]
---

Recently I was chatting with a friend who got into Pokemon card collecting and we were discussing the problem of grading cards (cf. evaluating the quality) and how one could use AI to firstly crop the card out of an image. My friend was confident that you'd need some fancy deep learning system to do any good but I disagreed, believing that given the relative standardisation of the card traditional CV techniques would do the job. Below I outline the approach that I used. 

Before we get into it, I want to highlight one key takeaway for me. LLMs has somewhat reversed the need for deep learning over traditional AI systems. Hear me out. Traditional AI systems, circa 1970, were mostly handwritten rules, but these just didn't scale as you needed many professionals and a lot of back and forth. Deep learning changed that by introducing high capacity models that could learn directly from data, all you needed to do was collect a lot of it and then the model could learn. Collecting data was a cheap, scalable exercise compared to the expertise required for rule writing, and so it took off. Fast forward to today and data collection has become an industry making it even cheaper but at the same time everyone now has an expert in their pocket via an LLM. The key insight is that with a cheap scalable expert the relationship has somewhat flipped back, making it possible to 'handcraft' expert systems with a similar amount of effort to collect data for a deep learning system.

Now there's an obvious caveat here that this isn't true for truly complex systems where deep learning provides a real edge, but for many projects it's amazing what can now be achieved through direct programming with an AI assistant. Let's look at one such project.

Here's an example of a Pokemon card. It has a standard shape with an image at the top, some text and a clear yellow border. While this one is fairly clear, there are many variants of this standard such as full arts which drop the border and have art covering the entire card, potentially including holographic elements adding many reflections. Let's not get too worried by that and see what's possible.

{% include fig.html url="/images/pokemon/pika.jpg" description="" width="128px" %}


With a quick prompt to Claude, it created a crop function that used Canny edge detection to find the sharp card edges and a contour function to build a shape from those edges. It worked OK, but there are many improvement points. Some examples: depending on the background there may be a lot of high frequency noise leading to many extra edges; there may be many contours that are not the card, e.g. the central artwork. To fix these, we could modify the code manually, but instead we can turn to our expert and just feed the problems in directly. 

With the help of Claude we can introduce various fixes to the pipeline:
 - Gaussian Blur: to remove high frequency noise before processing.
 - Morphological closing: to connect broken edges in the outline.
 - Card prior requirements: the card should be close to a certain aspect ratio, make up a large part of the image, be shaped like a rectangle 

These fixes give us a much more robust system with very little effort and no training required.

{% include fig.html url="/images/pokemon/card_crop.png" description="" width="512px" %}


Going one extra step, we can also transform the final cropped card to get a top-down view of the card with a perspective transform. 

The final results are shown below. Notably on some of the difficult cases it doesn't get a prefect crop along the edges, but it's pretty close and I'm confident with a little more hacking you could keep improving the quality.

{% include fig.html url="/images/pokemon/together.png" description="" width="512px" %}

So with just an hour of effort it was possible to string together a decent system for extracting Pokemon cards. It shows how far LLMs have come and the power of handcrafted solutions.