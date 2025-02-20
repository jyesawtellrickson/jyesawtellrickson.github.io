---
layout: post
title: AGI as the Best Gamer
categories: [AGI, LLM]
---

Games are fun. Humans love watching a variety of them from NFL to League of Legends to Mahjong. The competitive nature of games is enticing and the infinite strategies help keep them fresh. These factors also make them great testing grounds for AI. For example, recent work from the same group behind the ARC-AGI challenge pits LLMs against each other in games of snake to find out which is the best. In this article, let's discuss their findings along with other work towards using competitive games to evaluate AI. 

## A Quick Introduction to Games

Games come in all shapes and sizes, and this variety makes them difficult to produce one solution that fits all. The field of Reinforcement Learning (RL) has long used simple games such as Atari to showcase their methods. But single-player games can generally be solved and leads to fairly quick stagnation. We've seen very interesting results coming out of two-player games such as Chess and Go (famously AlphaGo) and those with more players such as DotA. In these competitive games, new strategies form and become dominant (the 'meta') and must be overcome by even stronger ones.

It's worth noting that there's a whole field of research dedicated to this called game theory. Game theory studies the various types of strategies that can emerge depending on player and game properties. For example, Kaggle ran an AI agent competition on the classic "Scissors, Paper, Rock" game which has interesting strategies. In this game, whatever you play, there's always a counter to it and so strategies quickly become complex as agents attempt to predict their opponents and fool them into thinking they have a certain approach. 

## LLMs and Evaluation

LLMs have taken the world by storm and shown previously unbeleivable results on countless benchmarks. This, combine with the difficulty of directly scoring natural language has made it difficult to actually evaluate modern LLMs. With this in mind, we ask: can games serve as a good benchmarking tool?

While LLMs have a wide range of functions, games can be used to target some of these, particularly:
- basic understanding capabilities: they need to process the game state text to get an internal representation.
- reasoning capabilities: given the representation they have, they need to reason about the next move.
The reasoning capabilities are of most interest here as it is something that is currently a hot topic of research. On the other hand, while the basic understanding capabilities are interesting, it's clearer how we could manually program this in if we wanted to.


## SnakeBench

[SnakeBench](https://snakebench.com/) takes this concept and pits LLMs against each other in a two-player game of snake. The approach is to convert the game state to text then ask the LLM to take one of four possible actions given the state. By running many games in a tournament style with a variety of LLMs it's possible to get a score for each LLM.

Unsurprisingly, the current results of SnakeBench show the strongest reasoning models on top. o3-mini is the current leader, followed by DeepSeek-R1 and gemini-2.0-flash. The good news is that this correlates fairly well with various other standard benchmarks. It suggests that games can be an effective way to evaluate agents.

But it's also clear that these LLMs have a long way to go. For example, in [this game](https://snakebench.com/match/b3af747e-9f95-40bd-8bab-a5db6dfab220) there is a very quick draw because neither LLM properly predicts the opponent will move into their path causing a collision.

## Beyond Snake: A World of Games

Now that we've seen how a specific game can be used to evaluate LLMs, how far can we take this? Some other interesting games considered in the research:
- [LMArena](https://lmarena.ai/?leaderboard): a simple choose the best response. Not quite a game in the traditional sense, but it can be considered a competitive game that resets each round.
- [Outsmart](https://edwarddonner.com/2024/08/06/outsmart/): a four-player game of coin collecting which requires actors to form alliances through private messages.
- [Repeated Games](https://arxiv.org/abs/2305.16867): game theory has a canonical list of games which including the Prisoner's Dilemma and the Battle of the Sexes which were tested in this paper.

Apart from the competitive games discussed above, the usage of LLMs as agents in a variety of single player games is explored.


## An Argument Againts Games

While we argued that games are great for LLMs to compete because they cannot stagnate like a benchmark, this isn't entirely true. In many cases optimal strategies for games can exist, or even if they don't, the improvements can be diminishing as the strategies become close to optimal. For now, there's a lot more room here compared to existing benchmarks and this can be maintained by leveraging games requiring more complex strategies.

We've also seen the lack of intelligence that LLMs can exhibit in these games. While the jury is still out, it's not clear that LLMs can craft world models which help them to actually understand the state of a game and make optimal decisions. This leaves room for other intelligence frameworks to compete and could provide interesting comparison points for this specifically.

One can also argue that a lot of useful things can't be framed as games, e.g. detecting cancer cells in a scan. While intelligence is a great goal to strive for and games can be good at testing this, there are still many useful tasks that do not necessarily correlate and we should continue to drive towards with separate benchmarking.

# Games in the Future

At the end of the day, developing games is relatively cheap, observing the outcomes is entertaining and they're relatively easy to scale up to multiple LLMs and in complexity which makes them a great benchmark. I hope to see more evaluation frameworks like SnakeBench in the future.


For:
Games are good when there's no right or wrong, can decide who is better. Could also do a score, but often hard. E.g. LLM answers to questions 


Notes
Any benchmark could be framed as a game, it's a competition to see who gets most right or gives best answer
A game is something with direct competition 
Not all games are suitable, eg those with Nash equilibria 
- [Zork](https://www.pcjs.org/software/pcx86/game/infocom/zork1/): in [this paper](https://arxiv.org/abs/2304.02868) the authors play the text-based game Zork with LLMs.
As we continue to improve AI, games will no doubt evolve too ([here I discuss the future of sports](https://medium.com/swlh/future-sports-ais-next-step-e94e32819bde)). 