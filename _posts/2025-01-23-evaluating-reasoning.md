---
layout: post
title: How to Evaluate Reasoning Capabilities
categories: [AGI]
---

Reasoning is a trait that has long been lauded among humanity. Among many other capabilities, it allows us to take seemingly disparate ideas and combine them together in interesting ways to form new ideas. It's something that is often sort out for in the workplace, ideal among friends, and now a trait that we wish to see in our programs. But how can you evaluate reasoning?

When we talk about intelligence and reasoning, most people immediately think of standardized tests. IQ exams, SATs, chess puzzles, and logic challenges have long been our go-to methods for assessing cognitive capabilities. But as artificial intelligence continues to evolve, these traditional metrics are starting to look limited.

## The Classic Reasoning Toolbox
Humans have developed numerous ways to test reasoning skills. The most obvious is the intelligence quotient (IQ) test which comes in many forms. This includes the Wechsler Adult Intelligence Scale and Raven's Progressive Matrices. As a society, we also rely heavily on standard academic tests such as the SATs which have reasoning components. 

Reasoning can also be tested through play, and problems like the Tower of Hanoi or chess puzzles are good examples of this. 

## Why Traditional Tests Fall Short for AI
Despite the multitude of tests, many of them have inherent limitations when applied to artificial intelligence:
- **Visual components often trip up AI systems**: While humans navigate visual puzzles with ease, most AI models struggle with puzzle-specific imagery, having been trained primarily on realistic imagery instead of the style typically used in intelligence tests.
- **Test length matters**: Traditional assessments typically include fewer than a hundred questions, but AI can potentially process far more inputs to provide a comprehensive evaluation. When evaluating models it's best to use tests with thousands of examples.
- **Capability mismatch**: AI and human intelligence are fundamentally different. An AI might excel at lightning-fast deductive reasoning but stumble on nuanced abductive reasoning that comes naturally to humans. For this reason, some tests may give interesting results for humans but either be fully saturated or too difficult for AI.

## AI Reasoning Assessments
In light of this, researchers have developed specialized tests to probe AI reasoning more effectively:
- **Mathematical reasoning tests**: there are a variety of mathematics based tests which are a go-to for testing reasoning in LLMS, including GSM and FrontierMath.
- **Coding problem-solving benchmarks**: coding requires problem solving and many systems are specialised for this task, making it a great test. The most popular tests are SWE-Bench and Codeforces.
- **Generalised reasoning**: testing more every day types of questions across a wide variety, examples are BIG-Bench and CommonSenseQA.
- **Visual puzzles**: As mentioned earlier, humans have been solving visual puzzles for a long time, and while not possible for many systems, those with vision capabilities can take advantage of them, or the visual puzzle can be converted to text. The Abstraction and Reasoning Corpus (ARC) ([link](https://arcprize.org/)) is the an infamous challenge in reasoning for the last few years. Other problems include: Bongard Problems, Raven's Progressive Matrices and Blockworld challenges.

## The Current State of AI Reasoning
Let's be real: today's AI systems are not great reasoners. Until very recently, there was a near-consensus that AI models fundamentally could not reason. Now, with models like o3 just around the corner, the conversation is more nuanced. But it's still clear that these systems don't quite reason in the same way that humans do (for better or worse).

Significant investment is flowing into developing more sophisticated reasoning approaches. Techniques like Chain of Thought (CoT) and Tree of Thought (ToT) are pushing the boundaries of how LLMs processes and generates complex logical sequences. It will be interesting to see how far these take us.
