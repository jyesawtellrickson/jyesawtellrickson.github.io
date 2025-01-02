---
layout: post
title: Autoregressive Errors are Independent?
categories: [LLMs]
---

In his (2024 interview with Lex Fridman)[https://www.youtube.com/watch?v=gn6v2q443Ew], Yann LeCunn claims that LLMs "are doomed" due to their autoregressive nature. He states that if we assume that the prediction errors from token to token are independent then it will eventually lead to a sequence being 'incorrect'. He does state that this is a strong assumption, but how strong is it? 

Lex rightly asks in response if the autoregression process could be 'self-correcting' or 'gravitating towards the truth' due to the model's training data. This seems a completely reasonable rebuttal. Let's explore it.

If I write the statement "Mark Zuckerberg is the CEO of", I'd expect the model to complete Facebook (or Meta). Throwing this into Llama3 7b I get just that:

> "Mark Zuckerberg is the CEO of Facebook and ..."

So the model hasn't made an error the results are good. What if we introduce an error though, will the model continue in its erroneous ways, or will it self-right? We prompt with "Mark Zuckerberg is the CEO of Apple":

> "Mark Zuckerberg is the CEO of Apple. Wait, no that's not true. He is actually the co-founder and CEO of Facebook. Apple is a separate company founded by Steve Jobs, who passed away in 2011."

One way to interpret what has happened here is that the next token prediction for "Wait" has been affected by the previous drifting away from the truth. Rather than continuing along this, the model brings the output back to the truth as we might expect. Full disclosure, this doesn't happen all the time, there were cases where it went on with Mark as the CEO of a different silicon valley behemoth. This shouldn't be too surprising either. One of the most popular capabilities of LLMs is generating creative text. To do that, the model needs to be able to continually generate even if the text isn't 'true'. Proper context would go a long way in making sure the probabilities of solutions we want are more likely to be output. For example, with additional prompting such as "The following is a factual statement" (which I found made it stricter).

This is just one case, but in general, we'd expect our models are able to right themselves when they go off track. There are likely existing mechanisms to help enforce this more strictly but could also be interesting research.
