
- Based on Logical Approach
- Based on the Nature of Evidence
    - Statistical Reasoning: Relies on data and probabilities.
    - Bayesian Reasoning: Combines prior beliefs with new evidence.
    - Causal Reasoning: Relies on cause-effect relationships.
- Based on Contextual or Practical Focus
    - Pragmatic Reasoning: Centers on practicality and outcomes.
    - Temporal Reasoning: Involves timing and sequences of events.
    - Moral/Ethical Reasoning: Evaluates decisions based on ethics.
- Based on Analogies or Comparisons
    - Analogical Reasoning: Infers similarities between cases.

Critical Thinking
Creative Reasoning
Counterfactual Reasoning: imagining alternative scenarios and their outcomes
Reasoning under uncertaintity: making decisions when information is incomplete or noisy.




> Giving a proper definition for reasoning is hard and the term is used in many different ways.

## An Example Application

ARC approaches with certainty vs. probabilistic

Another way to think about the difference here is the two sides of general to specific vs. specific to general. 

These two types of reasoning require different approaches to handle. Consider (1): when dealing with absolutes, transitions between knowledge are 100% calculable and deterministic. If A -> B and B -> C, then we know A -> C, there's no question. In this way, the problem is like a massive search where there are clear transitions between places of interest.

On the other hand, in (2), the possible scenarios are far greater as is the complexity of the calculations.


Solving MATH: deductive reasoning. You search over possible theorems that are applicable, directly apply them and see if you come to a valid conclusion. You a-priori know that there is a definite solution and can get to that result without having to make strong assumptions.

Solving ARC: (primarily) inductive reasoning. In ARC you have a set of examples which you have to combine together to come up with a general rule, this is hallmark inductive reasoning. It is probabilistic and data-driven since you're given just a few examples. Following a solution that is found, deductive reasoning is applied to go from a generic rule and test case to a test solution.


It's raining outside, and I know that when it rains the ground gets wet, therefore, I deduce that the ground is wet!
Deduction is straightforward and computation. The interesting part is the choice of which axioms to start from and combine. There are X billion possible facts to choose from and combinatorially large combinations of them. 
So if we say someone has great skills of deduction, what we're really praising is their observation (finding axioms others can't), or there choice of which axioms to combine (actually abduction as you're making hypotheses)


Deduction is solved by computers. If something can be expressed in symbolic form, than a computer can deduce all possible outcomes eventually. 

What's not solved is the abduction part of choosing the right hypotheses to test, finding the right information with which to perform induction.


ARC solution: 
- analyse comminalities between input pairs, output pairs, I/O pairs; identify properties, objects => perform inductive reasoning
- given the identified properties, create hypotheses for what the transformations could be => perform inductive reasoning
- evaluate the transformation on examples => perform deductive reasoning

A good reasoner highlights the most important observations, this makes it a lot easier to make the generalisations.


DreamCoder uses step-by-step abductive + deductive reasoning. It says: given this current state, what is the most likely next transformation I should make P(a|s). It then applies deductive reasoning to work out the next state P(s'|a,s) where we're given a model and the transition is deterministic. It then repeats this process with the next state until a terminal state is reached. A RNN?


But how does one train the function P(a|s) - you need to know what is relevant and important. Self-play without grounding is not useful. So you must ground yourself in a bunch of problems. Where do those problems come from? Dreaming?



- Deductive Reasoning: From general to specific.
- Inductive Reasoning: From specific to general.
- Abductive Reasoning: Inference to the best explanation.




## Where are we today?

A comprehensive review paper on reasoning is "Reasoning with Large Language Models, a Review" by Plaat et. al, 2024. Within, they discuss three approaches to improving LLM's reasoning abilities that are prevalent in the literatutre:
1. Generate
2. Evaluate
3. Control 
