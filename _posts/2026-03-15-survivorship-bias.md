---
layout: post
title: The Math of Survivorship Bias
categories: []
---

Among all the cognitive biases out there, survivorship bias has got to be one of my favorites. It feels so unnatural at first glance, yet it totally makes sense once it's explained to you. It's horribly pervasive in our daily lives and creates a remarkably bad feedback loop. For that reason, I wanted to talk a bit about it today and look at the underlying math that defines it.

## The Everyday Trap

We see survivorship bias everywhere, particularly when we look at health gurus, finance gurus, or any social media gurus for that matter. We look at the handful of people who achieved massive success and try to reverse-engineer their routines, entirely forgetting to account for the thousands of people who woke up at 4:00 AM, took ice baths, and invested in the exact same crypto, only to fail. We are only measuring the "survivors."

It happens in business, too. Imagine a business owner looking at their support metrics and saying: *"We barely get any complaints about our website, so it must be working great."* 

What they fail to realize is that the most frustrated customers didn't bother to complain—they just left. The owner is only surveying the customers who "survived" the user experience enough to successfully submit a ticket.

## Abraham Wald and the Missing Bullet Holes

To truly understand how to calculate and correct for this bias, we have to look at its most famous historical example. During WWII, military commanders wanted to add armor to their planes to minimize the probability of them being shot down. 

They looked at the planes returning to base and counted the bullet holes. They saw lots of holes in the fuselage and wings, and almost none in the engines. Naturally, their first instinct was to put armor where they saw the most hits. 

But a mathematician named Abraham Wald saw the flaw in their logic. Let's map out exactly what he realized using probability.

### Setting Up the Probabilities

Let’s define our events for a given plane:
*   $S$: The plane Survives and returns to base.
*   $C$: The plane Crashes (where $P(C) = 1 - P(S)$).
*   $H_i$: The plane is Hit in a specific area $i$ (e.g., $H_{\text{wing}}$ or $H_{\text{engine}}$).

As you might expect, the military's goal was to minimize the overall probability of a crash. We can define that probability as the sum of the crash probabilities given a hit to a specific area, multiplied by the probability of that area getting hit:

$$P(C) = \sum P(C \vert H_i) P(H_i)$$

Our goal is to figure out which area has the highest $P(C \vert H_i)$ — meaning a hit there guarantees a crash — so we can add armor and lower that specific conditional probability.

### The Flaw in the Military's Logic

The military commanders were counting the bullet holes on the runway and assuming they were measuring $P(H_i)$ — the raw probability of an area being hit. 

Because they only looked at the planes on the runway, they were *actually* measuring $P(H_i \vert S)$ — the probability that a plane was hit in area $i$, given that it survived.

### The Math (Bayes' Theorem)

We can connect what the military actually observed to what they needed to know using Bayes' Theorem:

$$P(H_i \vert S) = \frac{P(S \vert H_i) P(H_i)}{P(S)}$$

Now, let's plug in a crucial assumption: $P(H_i)$ is fairly evenly spread. Because anti-aircraft fire is somewhat random, the probability of a bullet hitting the wing is roughly equal to hitting the engine. Since $P(H_i)$ is constant across all areas, and $P(S)$ is the overall survival rate (also a constant), we get a direct proportional relationship:

$$P(H_i \vert S) \propto P(S \vert H_i)$$

This equation is the mathematical heart of survivorship bias. It tells us that the number of bullet holes you observe on a surviving plane is directly proportional to the survivability of that area.

### Solving for the Crash Probability

Let's look at the engines ($H_{\text{engine}}$). The military observed almost zero bullet holes there on returning planes:

$$P(H_{\text{engine}} \vert S) \approx 0$$

Because of our proportional relationship, this directly implies that the probability of surviving an engine hit is also near zero:

$$P(S \vert H_{\text{engine}}) \approx 0$$

If the probability of surviving a hit to the engine is zero, then the probability of crashing from a hit to the engine is one:

$$P(C \vert H_{\text{engine}}) = 1 - P(S \vert H_{\text{engine}}) \approx 1$$

## The Takeaway

By formally mapping this out, Abraham Wald proved that you don't put armor where $P(H_i \vert S)$ is high (the wings). You put the armor where $P(H_i \vert S)$ is artificially low (the engines), because the lack of observed holes is mathematical proof that $P(C \vert H_i)$ is near 100%.

It’s an incredibly elegant solution to a problem that routinely fools human intuition. The next time you are analyzing data to make a decision, make sure you ask yourself: *Where are my missing bullet holes?*