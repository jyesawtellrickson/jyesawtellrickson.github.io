---
layout: post
title: Another Framework for General Intelligence
categories: [AGI]
---

The following describes the framework that I use when thinking about general intelligence. There are already many out there, but none that resonated strongly with me, or were expressed succinctly enough. That led me to create my own for reasoning through the problems that we're tackling. Following is the framework itself and a quick view on our current status.

Before that, we quickly clarify what we mean by an AGI by starting with the definition of intelligence. I'm partial to Chollet's definition of which equates roughly to 'skill acquisition efficiency' (read his paper [On the Measure of Intelligence](https://arxiv.org/abs/1911.01547) for much more detail). In short, we want an entity that can learn new behaviours (or skills) relatively quickly when exposed to new tasks or environments, something that many modern AI systems fail to achieve. The environment in question here is ours, the physical world. Now let's explore what we need to achieve this.

At a high-level I split capabilities into two categories, core and agency. 
- Core
    - Knowledge-base
    - Reasoning
    - Prediction
    - Learning
- Agency
    - Goal-driven
    - Always on
    - Actuation

Let's discuss these in detail.

## Core

At it's core, an AGI should have capabilities. These are largely based off what we have observed from intelligence as we know it. It might not be the list for all intelligences, but is likely the one for what humans will create.

Firstly: **knowledge**. Everything mankind has achieved has been built on the shoulders of others. Science is a wonderful discipline that pushes people to share the results to advance society's knowledge as a whole. This knowledge in turn leads to greater discoveries and so the loop continues. Any AGI will need to have access to knowledge (e.g. APIs) as well as its own dense, searchable representation of the world's knowledge. That knowledge must then be leveraged.

**Reasoning** (often referencing Kahneman's System II) is the ability to go beyond knowledge. By combining, expanding upon and integrating knowledge, reasoning allows a system to push outside its boundaries for new discoveries. It requires multiple steps of consistent action and is one of the biggest challenges currently being tackled in AI research. One specific type of reasoning that is particularly useful is reasoning into the future.

**Prediction** is a method for looking ahead into the future. This is critically important for any system that wants to exist in our world where time is one of the key physical dimensions. Ultimately, systems optimise for some future value, and so they must be able to correctly predict what is that future value of today's actions.

Lastly, an AGI must be amazing at **learning**. With all the three previously mentioned capabilities, you'd have a formidable system, however, it would be limited. Learning allows a system to evolve and grow beyond itself. Learning is what AI has always had at its core. We want systems that are not only capable at some task, but can continue to grow as they collect more data. Reinforcement Learning is a classic topic in AI literature which studies this in depth.

## Agency

Given it's the [already crowned buzzword of 2025](https://www.digitimes.com/news/a20241230PD208/ai-agent-genai-ai-openai-2025.html), it's probably not surprising to see it pulled out here. Having strong core capabilities is one thing, but an AGI must exist in the physical world as we know it. This requires certain other capabilities which are less well understood.

An AGI must be **goal-driven**. This is maybe obvious, but how to design and move towards those goals is hardly so. There is a growing community of researchers investing into this problem of goal design. What do we want AGI to achieve? Is it possible to guide AGI? How do we stop AGI going rogue? Apart from the technical questions of building loss functions, running optimisers etc., there are a lot of details that we must get right.

An AGI must be **always on**. Almost all AI systems that you see today are designed to solve a task and then be done with it. Even something like ChatGPT which is technically always on and serving requests doesn't constantly act towards a single goal. The fact that we have limited time to work with and must plan accordingly is often one of the crippling challenges for humans and AGIs must be able to balance their time, do continuous learning, deal with infinite contexts and process errors.

Finally, and most importantly, an AGI must have **actuation**. It must be able to act upon the world to drive the outcomes it strives towards. This includes ideas like multi-modality and embodied AI but also raises various ethical questions of where we want AI to plug into society. Is it possible to have an AGI acting as chief economist, what tools would it have to do so? Actuation allows systems to influence their surroundings.

## Where are we now?

I like to think of each of these areas in terms of the amount of investment and the current progress against the capability. In this way we can construct the quadrant shown below.

![AGI Framework Progress Chart]({{ site.url }}/images/AIPC.png)

Notably:
- We've made great progress with LLMs as a storage of facts and at another level, functions for common text manipulations (e.g. writing poetry). Massive amounts of money have been thrown at the problem and it paid off.
- Reasoning is the next big thing, and models like o3 show how much money can be spent here ($2K to solve a single ARC task). While these models show improved reasoning against the baselines, it's still clear from the failure modes that they're not truly generalising when they make simple off-by-one errors. Still plenty of progress to be made.
- The more agentic capabilities (always on, goald-driven) still require more investment and more progress. When the core capabilities aren't yet there, it's less exciting to work on this, but given how fast the core capabilities have increased, investment is well overdue.

## Next steps

Given the framework and our current progress towards AGI, I'm very excited to continue tracking this and contribute. Areas of low investment and progress seem like good areas to add value while areas of high investment and limited progress also present great (albeit crowded) opportunities for those few great ideas.
