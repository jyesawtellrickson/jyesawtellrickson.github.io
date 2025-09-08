---
layout: post
title: ARC-AGI 3 2025 July Demo
categories: [AGI, Competition]
---

ARC-AGI-3 is the latest challenge in Francois Chollet's ARC Prize. While currently still under development, the authors released a sample of the challenges and are running a small competition. In this post I'd like to discuss my attempt at 'hand-writing' some solutions and what it told me about a real solution. If you'd like to know more about the ARC-AGI-3 challenge, I previously wrote about it [here]({% post_url 2025-06-11-arc-agi-3 %}).

## The Problems

The three example games they shared can be seen below. There are also three test games that are hidden. Each example game consists of 10 different levels of increasing difficulty. They're available to play on their [website](https://three.arcprize.org/). The rest of the post will contain spoilers for the games, so if don't want that, play them first!

The games are relatively simple, solvable by humans without too much thinking required. As we'll discuss, a lot of what makes them more challenging happens automatically in our brains.

### LS20 aka Pathfinder

The first game is a basic path finding game with some tasks to complete along the way. You have to match the colour, shape and rotation of the target square/s and reach them without running out of energy. 

{% include fig.html url="/images/arc-agi-3-trial/ls20-1-1-shrunk.png" description="" width="256px" %}


### FT09 aka Switcher

The second game is a constraint satisfaction problem in which you must mach a grid to a known set of constraints. The grid can be manipulated directly early on, but later through the use of some 'tools'.

{% include fig.html url="/images/arc-agi-3-trial/ft09-1-1-shrunk.png" description="" width="256px" %}


### VC33 aka Overflow

In the third game there are switches which can move white tiles from one bucket to another. The goal is to align a target block with the same colour on the wall. This is done by changing the level of the white tiles and moving the target blocks around.

{% include fig.html url="/images/arc-agi-3-trial/vc33-1-1-shrunk.png" description="" width="256px" %}


## A Bad Solution

ARC involves creating systems that can reason about never before seen problems. As such, handwriting a solution is bad. That said it can be instructive to understand the sought of issues you might have in building such a system. I decided to code up partial solutions to two of the problems to experience this.

To approach the task I wrote the skeleton for a solver with function names and descriptions and then had an LLM fill in the blanks. To simulate what a working system would face, I did this for each level, one at a time. Due to the increasing difficulty across levels this meant that upon beating a level it would require some extra work to solve the next level. This iterative reasoning felt very natural in thought, but when it comes to coding it feels less natural as you must re-write programs and potentially refactor code if it's not extensible.

As I wrote the functions, it was clear that I was placing a lot of bias into the system. For example, "get_remaining_steps" is a simple function, extract the 1x1 purple pixels in the top few rows, but knowing that these represent in-game steps, that they will remain a fixed part of the UI, that they'll disappear over time are all things which come naturally to me but not to a new solver.

Some of the specific issues I came across for each problem:
- **Pathfinder**: the actual pathfinding algorithm can become fairly complex as it requires multi-hop reasoning. For example, if I want to navigate to a certain location, I have to check if I get there with the remaining steps, but also if I do get there, will I be able to reach my next location with the steps I have left over, or what will be my next location, or can I model how the state will change based on the interactions with objects. It can become a very complex planning algorithm, but I found even for the hardest level it doesn't need to be.
- **Switcher**: the hardest part in the reasoning here is avoiding getting stuck in loops as some constraints affect others (classic CSP). As is a classical solution, the algorithm should be able to account for constraint hierarchy, solving them in a logical order. Again, this could turn into a relatively sophisticated planning algorithm, but I found that for the hardest levels simpler approaches will suffice.


## Key Takeaways

My key takeaway from this work is that visual understanding is painful to hardcode, but the reasoning is less so. In my solutions, 80% of the code was just visual processing. Maybe this isn't surprising if we consider what it would take to write an object detection system from scratch vs. the simplicity of many key planning algorithms. Given the simplicity of the ARC visual representations, it was still surprising to me.

Gives this, the key difficulty for this style of approach becomes: how can I identify objects, their interactions and their meanings. For example: this object is defined by a contiguous grid of non-black (background) pixels, it causes the 'internal state' object to change when the 'agent' object covers it, it can be used to ensure that the 'internal state' matches the 'target state' which is a necessary condition for completion.

So maybe one big stepping stone for ARC could be building a robust object detector. While this doesn't align with the competition goals, it would help pivot the competition to focus on the important part of reasoning. Afterwards, the focus could shift to the purpose of the objects (the more interesting part!). Because while we've largely 'solved' object detection for the continuous case with real images (e.g. YOLO), there doesn't exist a good object detector for discrete, game-like images. This is likely a data problem as there is no massive corpus of game-like images to train a supervised on semi-supervised model on.

It's worth noting that it's also possible to skip the object notation altogether. Some of the best performing ARC solutions are now transductive models which directly output solutions, never explicitly describing objects. I'm still a little hesitant to embrace transductive, with a personal strong prior belief over inductive models, so I still see this work as valuable.

## LLM as Object Detectors

At this point you might be thinking that multi-modal LLMs are already capable object detectors, and you're not far off. The below extract is ChatGPT's interpretation of a state from LS20 (Pathfinder). 

Only being prompted to describe the image and objects, the LLM is able to find the objects and also make good hypotheses about their interactions. There are various hypotheses which are incorrect (e.g. which object is the agent, the use of the red squares), but the hypotheses are relevant and verifiable. So what's the issue? Whilst theses systems can now produce good overall descriptions, they lack the ability to understand the fine-tuned details of visual data. Case and point, when given an updated state after just one action, they hallucinate what has changed and miss things that have. If something was "bottom-right quadrant" and is still in that rough area, the model will likely see it as unchanged, despite it moving a few pixels.

So while LLMs of today can directly give a good description of the scene, the precision understanding is still lacking. This is of course improvable via scaffolding (e.g. "now I'll write a function that extracts the horizontal row of small purple dots in the top left corner...") and it remains to be see how effective solutions produced by people are in the ARC-AGI-3 competition.

```text
This image appears to be a low-resolution (pixel art style) scene, likely from a game or a game-like simulation environment. Here's a detailed breakdown of the elements:

General
- Dimensions: 64×64 pixels
- Style: Pixelated, top-down view
- Background: Predominantly dark gray, suggesting a floor or wall.

Objects (by color and shape)
- Top-left corner:
    - A horizontal row of small purple dots – possibly a progress bar, health bar, or aesthetic UI element.
- Top-right corner:
    - Three small red squares – likely representing window control buttons (close/minimize/maximize), reinforcing the idea this is a UI window.
- Middle region (main scene):
    - A large irregular dark gray shape with walls/openings suggesting it’s a room or maze.
    - A small black rectangle with white and blue pixels inside it (center-top) – could represent a character or agent inside a room.
    - A white L-shape with a blue dot inside it (center) – might be another agent or a composite object (e.g., robot + item).
    - A blue and orange block (bottom-right quadrant) – possibly a container, chest, or a marked goal region.
    - A blue dot near the center – possibly a small item or unit (e.g., bullet, object to collect).
- Bottom-left corner:
    - A white and blue L-shaped object – possibly a player start location, entrance, or another character.

Interpretation
This is likely a game sprite or screenshot showing:
- A player character or agent interacting with objects.
- Several rooms or compartments, some containing interactable elements.
- HUD/UI elements at the top.
```

## Conclusion

ARC-AGI-3 is shaping up to be a fun new challenge for reasoning models that pushes us from static problem solving in ARC-AGI-1/2 into the classic RL domain of games.