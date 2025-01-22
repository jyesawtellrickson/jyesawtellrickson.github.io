---
layout: post
title: Explicit Reasoning Threads
categories: [AGI]
---

When discussing about how an AGI should be designed, its helpful to fall back on the human thought process. Much of modern work was inspired by the human brain. Follows are my thought processes for various problems to use as a reference.

## Abstract Reasoning Corpus Problems
See https://arcprize.org/

Summary:
- start by looking at input of one example and notice anything interesting based on my priors (e.g. objects, colours, gaps)
- compare the input to the output and check for persistence (e.g. object), compare to all my known transformations priors (e.g. shift, colour change, extend, etc.) on what is likely transformation and then make a hypothesis that is valid for the one case.
- validate and/or extend the hypothesis with further examples
- in none of these examples were the further examples really necessary, it was possible to get a good guess from just one example pair, but in other tasks you really need to see multiple pairs, in that case the reasoning chain would be more complex.


Puzzle ID: 3aa6fb7a
1. Look at Ex.1 Input: there's an interesting shape repeated with a missing part.
2. Look at Ex.1 Output: Oh, indeed, it looks like the shape remains but it has been filled in with a darker colour. Now I have a hypothesis, let me check other examples.
3. Look at Ex.2 Input and Output: yes, there are more bases, but approach is the same.

Puzzle ID: 0ca9ddb6
1. Look at Ex.1 Input: there's just two dots, not much to go off.
2. Look at Ex.1 Output: oh, looks like there are more dots added around the initial ones to make some pattern, probably the pattern and colour corresponds to the initial dot colour. I have a reasonable hypothesis.
3. Look at Ex.2 Input and Output: that's correct, but there are also some pixels that don't have patterns. I need to extend my hypothesis as it was not complete. 
4. Look at Ex.3 Input and Output: another colour added that doesn't have any pattern. Should be safe to assume that all non-defined colours also have no pattern. Hypothesis updated and now valid on all examples.

Puzzle ID: 1e0a9b12
1. Look at Ex.1 Input: some dots the same colour.
2. Look at Ex.1 Output: oh, looks like the dots have persisted, but just dropped downwards, like gravity.
3. Look at Ex.2 Input and Output: yes, it's valid.
4. Look at Ex.3 Input and Output: still valid.

Puzzle ID: 0d3d703e
1. Look at Ex.1 Input: lines of colour, classic RGB but out of order.
2. Look at Ex.1 Output: seems the shape is preserved but the colour changes. Could be a direct mapping between colours, will need to check if it's valid or there are other colour mappings.
3. Look at Ex.2 Input and Output: yes, it's valid and we need to add another colour mapping.
4. Look at Ex.3 Input and Output: need to add some more. It's also likely that colours share the mapping regardless of the direction, so it's bidirectional mapping, pairs of colours.


## Lunar Lander
https://gymnasium.farama.org/environments/box2d/lunar_lander/
(assuming observation space is actually pixels and number of actions are known)

1. There is an object descending that looks like a spacecraft. It's approaching what looks to be the ground with some flags. Probably we want the spacecraft to go between the flags since it's a game. I guess we can control the spacecraft.
2. It's off-course so I'll have to move it, let's press buttons. Pressing buttons spits out pixels, something like a thruster and makes it move in that direction. I can use the thrusters to control it's movement. Getting the correct force is a bit hard though.
3. I still failed even though I landed between the flags. Maybe I came in too fast? I can try again with this approach.
4. Success.


## Deepmind Mathematics
https://github.com/google-deepmind/mathematics_dataset
Summary:
- The first step is typically to work out what type of problem it is, then remember the relevant formula or checks. 
- Next we must do some calculations step-by-step to arrive at our answer. The wider part of the search is at the start when we must think of the method. Afterwards, it's typically more straightforward.


Question: Calculate -841880142.544 + 411127.
1. Seems like a straightforward addition. Use a calculator or manually calculate.


Question: Let e(l) = l - 6. Is 2 a factor of both e(9) and 2?
1. To check if two is a factor of both, we need to check if it is not a factor for any of them.
2. 2 is a factor of 2.
3. To check e(9) we'll need to make it a number first. e(9) = 9 - 6 = 3. 2 is not a factor of 3 and thus not a factor of e(9). 
4. Since 2 is not a factor of e(9) it is not a factor of both, the answer is False.


Question: Three letters picked without replacement from qqqkkklkqkkk. Give prob of sequence qql.
1. We will want to calculate some probabilities. Picked without replacement makes it a bit trickier as probabilities will change over time. We can calculate total probability by modelling it as a chain of events, p(q) * p(q) * p(l).
2. Calculate probabilities: count each letter and divide by total number of letters. Total letters is 12. q: 4/12=1/3, k: 7/12, l: 1/12. Double check all probabilities sum to 1; they do.
4. So first part is 1/3. Now calculate next parts with same procedure, with 1 less total and 1 less q.
5. p(q) = 3/11, and p(l) = 1/10.
6. Putting it together we get 1/110.









