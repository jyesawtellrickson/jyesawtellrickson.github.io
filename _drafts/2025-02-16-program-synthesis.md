---
layout: post
title: 
categories: []
---

Overview of program synthesis
 - why program synthesis
    - llms are a vector database that store string programs
    - building reusable knowledge for a system that can expand
    - interpretability. Yes, and no, they'll learn sufficiently complex functions that we won't be able to understand. While they're theoretically understandable, it's not a tractable problem. If you tried to understand how Meta's codebase worked from scratch, how far would you get? What's the difference of having a clear composition of functions vs. a list of I/Os as a result of running a non-transparent function (no lying for one).
    - generalisable beyond training set
 - tl;dr on methods
    - basic bottom-up enumerative search, simple but not scalable
    - lots of complex methods proposed to improve on specific types of problems
 - program by example PBE as an interesting class (& ARC)
 - neural-guided program synthesis
 - problem of building data in (e.g. DSL, scoring functions) vs. having model learn from data (e.g. neural network)
 - ultimately need SOME grounding to learn, else the model is just living in a different universe. Whether it's data or higher-level rules, we must give the system something to guide it


 - are there things that LLMs can't do because they haven't seen training data, and we don't have available, that program synthesis could do without having that data? What about RL?