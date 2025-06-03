
# Test-Time Compute Problems


Applied in domains where generalization, flexibility, or adaptation outweigh the need for low-latency inference.
* Hard-to-generalize tasks
* test time adaptation tasks



Guided search:
* heuristic
* learned or dynamic model (e.g. NN value model, self-judge LLM)

Goal states (can check status and retry/adjust):
* Known e.g. figure out the path to the end of the maze (A*)
* unknown, e.g. find the most optimal solution, you want to decrease the cost (AlphaEvolve), you want to win (AlphaGo)
* between: output = expected output for subproblems (ARC)

Transition function:
* Learned: dreamer
* known: AlphaGo


Types of problems:

Components:
* Data: state (e.g. TSP, maze, question), multiple examples (e.g. learn and apply), self-created (e.g. build new problems based on input/output - can be done without verifier? e.g. one-way functions like encryption, matrices that can't be inverted)
* Output: multi-step (e.g. actions in maze, MPC), step (e.g. ARC output)
* Verifier: external, internal, internal+(e.g. LLM judge), world model, none
* Model: ensemble, iterative
* Search: raw, latent, average, none

Few-shot learning:
* Practice on examples until you're confident in your guess
* e.g. search possible transformations
* e.g. ARC, program synthesis, AlphaCode, Dreamcoder

Optimisation across multiple actions:
* known minimisation function, e.g. total distance travelled; known goal state
* simulating trajectories with word model
* e.g. travelling salesman, maze navigation, AlphaZero
* frame image classification as a search for the transformations that transform a base state (class) to the predicted one.

Generation / iterative refinement:
* training samples suggesting what good looks like
* can take many small steps to reach the desired outcome
* can iterate on a solution eternally
* has some version of an internal oracle
* e.g. image generation diffusion models, LLMs

Symbolic domain:
* the data can be directly manipulated according to structured rules / functions
* e.g mathematics, ARC+DSL, coding



Characteristics:
* Search: tree, beam, in latent space, 
* Scratchpad 
* Learned priors
* don't predict the output directly, predict a function which creates the output, have an internal measure of output quality


Using an oracle:
* oracle that will tell you if you're right or wrong
* discriminative: just go down from top to bottom
* good: adjust your predictions based on info (it's not class A, so maybe not class B??)



How do world models compare?


How does ML take gradient steps when it doesn't know the solutions? (is it posthoc?)
Aren't all NNs probabilistic models? What makes it unique?



If I learn with data augmentations, does it produce better outcomes?




# Notes

Program synthesis and symbolic AI (symbolic search); known goal states so can check status and retry / adjust