---
layout: post
title: LLMs as a Repository of Vector Programs
categories: [LLMs]
---

I recently came across Chollet's mental model for LLMs and it really helped me (quoted from [his blog](https://arcprize.org/blog/oai-o3-pub-breakthrough)):

> My mental model for LLMs is that they work as a repository of vector programs. When prompted, they will fetch the program that your prompt maps to and "execute" it on the input at hand. LLMs are a way to store and operationalize millions of useful mini-programs via passive exposure to human-generated content.

He has a full-write up on the details [here](https://fchollet.substack.com/p/how-i-think-about-llm-prompt-engineering). 

One part I'll pull out: "You can see a LLM as analogous to a database: it stores information, which you can retrieve via prompting."

He goes on to say there are two main differences:
1. *LLMs are continuous, interpolative databases*: Instead of being stored as entries, data is stored in a continuous vector space. This means you can choose any point on the curve and get something interesting (since LLMs are semantically continuous).
2. *LLMs contain data AND programs*: on top of potentially the world's single densest, large repository of knowledge, LLMs contain programs. The programs are highly non-linear functions which work within the latent embedding space, magically(?).

Read the [full article](https://fchollet.substack.com/p/how-i-think-about-llm-prompt-engineering) for a deeper discussion.



