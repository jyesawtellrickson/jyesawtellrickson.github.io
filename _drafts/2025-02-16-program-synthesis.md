---
layout: post
title: 
categories: []
---

The most complex actions we take, the most difficult problems we solve, they're only possible through the combination of many small puzzle pieces, fitting together beautifully. These pieces fit into different hierarchies from low level actions like twitching a finger to high level concepts such as drinking a glass of water. Program synthesis is a field of research which studies the creation of such complex programs.

## Why Program Synthesis

Given the success of LLMs as general problem solvers, why do we care about program synthesis? 


As it stands, there is no one solution that solves the majority of program synthesis problems (as LLMs can be to NLP), rather a diverse collection of methods. Bottom-up enumerative search is the most basic method which works simply by going step-by-step and building up a program. If your program was composed of various letters, you could think of it as just choosing the next letter in a sequence. You'll eventually stumble upon some words, but maybe it's not the most efficient method.

To improve on enumerative search, many more complex methods have been proposed for specific problems. These include XXXX






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