If controversies were to arise, there would be no more need of
disputation between two philosophers than between two accountants. For
it would suffice to take their pencils in their hands…and to say to each
other: Let us calculate.

Gottfried Wilhelm Leibniz

In this chapter we start by framing reasoning as a process of
decomposition and search and explore systems with these capabilities.
Next we enumerate the model classes that are currently used as reasoning
systems, including: neuro-symbolic systems, neural iterative reasoning,
tool-augmented reasoning and search-based systems. Finally, we make a
case for neuro-symbolic program synthesis as a method that has various
desirable characteristics of reasoning systems and a clear path forward
to scaling up. We outline the full structure of the thesis and key
contributions.

# Definition

Reasoning models aim to replicate what we would typically associate with
intelligence in humans. The ability to take a difficult problem that you
do not know the answer to and work through it to get an answer (Sun et
al. 2024). Reasoning is widely applicable with applications spanning
fields, such as problem-solving, theorem proving, decision-making, and
robotics (Manning 2022).

A reasoning model is any model that executes input-conditioned iterative
computation at test time to derive conclusions not trivially stored in
its parameters.

These models spend a significant amount of resource when performing
inference as opposed to purely on training. This is a significant
problem when scaling up these models and is an active area of
research (Feng et al. 2025). A classic model that has low test-time
compute is a CNN as inference only requires a straightforward pass
through the network.

The fundamental challenge for reasoning models is building systems that
maintain structured representations and apply algorithmic
transformations to them under distribution shift.

The broad classes of models which perform reasoning are:

1.  Search-based reasoners

2.  Neural iterative reasoners

3.  Neuro-symbolic guided reasoners

4.  Tool-augmented orchestrated reasoners

# The Characteristics of Reasoning Models

The key characteristics of reasoning are the ability to represent a
problem succinctly, decompose it into sub-problems and then search for a
solution efficiently (see ).

Current models struggle with all of these aspects to varying degrees.

- **Representation**: models do not build stable, manipulable
  abstractions. LLMs encode concepts implicitly in large vector spaces,
  but they do not maintain causal or compositional structure. As a
  result, they struggle when a problem requires reusing the same
  abstraction in a modified context. This is the root of many OOD
  failures.

- **Decomposition**: models cannot reliably break complex tasks into
  correct subproblems. Most real reasoning challenges are hierarchical.
  Good decomposition is the bottleneck in program synthesis, theorem
  proving, long-horizon RL, mechanistic planning, and ARC-like tasks.
  When decomposition fails, the model appears ‘stochastic’ even if it
  has the right primitives.

- **Search**: models do not explore solution spaces systematically.
  Human reasoning relies on guided search. Current models do shallow
  hypothesis generation; they do not maintain branching, pruning, or
  uncertainty-aware search. Tool-use helps, but it is closer to patching
  than solving the underlying limitation.

<figure id="fig:reasoning">
<img src="figures/reasoning.png" />
<figcaption>The key characteristics of reasoning models: representation,
decomposition and search. Models must understand and represent problems
in a way they can process. Decomposition allows models to simplify
problems into manageable sub-problems. Search is the process through
which models dedicate resources to find solutions among many possible
explanations.</figcaption>
</figure>

In addition to these core challenges, there are several other
limitations:

- **Verification**: models cannot assess their own intermediate steps.
  Reasoning systems must detect wrong turns early. Current LLMs cannot
  reliably check their reasoning—unless external verifiers are provided
  (e.g., unit tests). This weakness makes them brittle on novel
  problems.

- **Generalisation**: current architectures lack mechanisms for
  systematic generalisation. This includes OOD generalisation, but the
  deeper issue is that fundamental operations—copy, repeat, count, bind
  variables, manage pointers—are not represented in a way that scales
  compositionally. Models interpolate; reasoning often requires
  extrapolation.

- **Grounding and task formulation**: the model cannot infer the latent
  structure of a task from minimal examples. ARC is the canonical
  illustration: identifying the “true” rule from a few demonstrations is
  hard without strong priors about the nature of structure in the world.

# Representation and Decomposition

Early Transformers provide a good example of poor representation. The
“strawberry” problem is a famous failure of early Transformer models to
correctly count the three “r”s in the word “strawberry” which showed the
limitations of tokenization and representation. Because transformers
process text as sub-word tokens (see ) rather than individual
characters, their internal representation of the word often lacks the
granular orthographic detail necessary for symbolic tasks. This issue is
deeply tied to decomposition in reasoning: for a model to reason
accurately about a whole, it must be able to effectively decompose that
representation into its constituent parts. When the model’s view of the
data is compressed incorrectly, it cannot fail to perform sub-tasks,
leading to a breakdown in the full solution.

<figure id="fig:tokenisation">
<img src="figures/tokenisation.png" style="width:20.0%" />
<figcaption>An example of tokenisation in the o3 pro transformer. This
type of representation makes them ill-suited to tasks such as character
counting. From gpt-tokenizer.dev.</figcaption>
</figure>

The capacity for human intelligence to solve complex problems hinges on
hierarchical decomposition: breaking down grand objectives into
manageable, temporally extended sub-goals (see ). Modern artificial
intelligence models adopt this principle to overcome limitations in
scalability, data efficiency, and interpretability. The core benefit of
a hierarchical design stems from the separation of concerns, allowing
different levels of the architecture to specialize in distinct time
scales and levels of abstraction. This specialization drastically
improves learning efficiency, particularly in sequential decision-making
environments.

<figure id="fig:goal-subdivision">
<img src="figures/goal_subdivision.png" />
<figcaption>Goals can be continually subdivided into smaller and smaller
goals which can be more manageable.</figcaption>
</figure>

In Hierarchical Reinforcement Learning (HRL), this principle is manifest
through the definition of options or meta-actions that span multiple
time steps. A high-level policy selects an abstract option (e.g., “open
the door”), while a low-level policy executes the primitive actions
necessary to achieve that sub-goal (e.g., reaching, grasping,
twisting) (Kulkarni et al. 2016). Similarly, advanced neural
architectures like Hierarchical Reasoning Machines (HRMs) leverage two
recurrent networks operating at different time scales: a slow,
high-level module manages abstract planning and context, and a fast,
low-level module handles detailed execution (Wang et al. 2025). By
creating a nested structure of computation, these models gain enhanced
effective depth, allowing them to perform deliberate, algorithmic
reasoning that is typically intractable for traditional, flat neural
networks.

This concept extends beyond planning and control into data
representation and pattern recognition. The success of Convolutional
Neural Networks (CNNs) is predicated on their hierarchical nature, where
early layers extract simple features (edges, textures), middle layers
combine these into parts (eyes, wheels), and final layers integrate
these parts for high-level object recognition (LeCun et al. 2015). In
multi-modal settings, such as Vision-Language Models (VLMs), the
hierarchical approach involves separate deep networks processing the raw
modalities (e.g., tokens for text, pixels for images) before integrating
their high-level representations in a specialized, shared embedding
space. Furthermore, in unsupervised learning, Hierarchical Clustering
algorithms naturally organize data into a nested tree-like structure,
revealing relationships and patterns at multiple granularities
simultaneously, which is crucial for complex data analysis and taxonomy
creation. In all these cases, hierarchical decomposition provides a
modular framework for both construction and analysis, ultimately leading
to more robust, data-efficient, and structurally understandable AI
systems.

## Object Detection Systems

There also exist dedicated object-based systems which explicitly
decompose the world into discrete entities. These systems often use
attention mechanisms or explicit object proposals to isolate individual
objects from raw sensory data. By representing the environment as a
collection of objects with their own properties and relations, these
models can reason about interactions, dynamics, and causal structure
more effectively. Object-centric representations facilitate transfer
learning, as knowledge about one object can be generalized to others of
the same type. They also enable compositional reasoning, where complex
scenes are understood as arrangements of simpler components. Examples
include models like MONet (Burgess et al. 2019) and Slot
Attention (Locatello et al. 2020), which learn to segment scenes into
objects without supervision, allowing for more interpretable and modular
representations that align closely with human cognitive processes
(see ).

<figure id="fig:monet">
<img src="figures/monet.png" style="width:50.0%" />
<figcaption>An example of MONeT performing object segmentation. The top
row shows the original images, the second row shows object segmentations
for each slot and the bottom row shows the output from one of the slots.
Figure from <span class="citation"
data-cites="burgess2019monet">(Burgess et al. 2019)</span>
(edited).</figcaption>
</figure>

Building on these foundations, the scope of object-centric reasoning
extends beyond purely unsupervised vision tasks. Architectures like DETR
(DEtection TRansformer) (Carion et al. 2020) have further refined this
approach by framing object detection as a direct set prediction problem,
utilizing the global context of Transformers to eliminate the need for
hand-crafted components like non-maximum suppression. This object-first
philosophy is equally prevalent in Natural Language Processing, where
Named Entity Recognition (NER) serves as a primary mechanism for
decomposing unstructured text into discrete semantic entities. By
isolating specific objects of interest—such as people, locations, or
organizations—NLP systems can build structured representations of
complex narratives, mirroring the way vision models segment a physical
scene.

Furthermore, the principles of decomposition and representation are
increasingly applied to non-visual signals and abstract data
structures (Baevski et al. 2022). In signal processing, complex acoustic
environments are often converted into spectrograms and then decomposed
using computer vision techniques to isolate specific audio objects, such
as individual bird calls or mechanical signatures. A similar logic
governs anomaly detection in finance; for instance, in fraud detection,
a series of isolated, seemingly benign transactions are combined into a
single fraud object based on their relational properties. This motif
discovery is critical in clinical data analysis, where models analyze
time-sequence data like EEG or ECG to identify specific physiological
patterns or motifs. By treating these temporal segments as discrete
objects with causal relationships, researchers can move toward more
interpretable and modular diagnostic systems that align closely with
human cognitive processes.

## Human Cognition and Resource-Rational Planning

The inspiration for these architectures is deeply rooted in cognitive
neuroscience, where mounting evidence suggests the brain itself employs
a hierarchical control system to manage the combinatorial explosion
inherent in complex problem-solving. Research indicates that humans
utilize hierarchical representations for efficient planning and flexible
behavior, a strategy often referred to as resource-rational
decomposition (Botvinick 2012; <span class="nocase">Solway et al.</span>
2014). This cognitive mechanism allows individuals to simplify complex
tasks (such as navigating a maze or solving a multi-step arithmetic
problem) by first choosing a sequence of sub-goals at an abstract level
(e.g., going from office → cafe → post office) and only later executing
the concrete, low-level actions required for each sub-goal. This
two-tiered system minimizes the computational burden by reducing the
overall search space, enabling humans to operate effectively despite
biological constraints on memory and processing speed. The neural
dynamics observed in the prefrontal cortex during decision-making
further support this top-down, hierarchically organized representational
structure, where higher-level contextual information influences
subordinate task representations before an action is selected (Cellier
et al. 2022). This biologically inspired framework provides compelling
validation for adopting hierarchical models in artificial general
intelligence research.

Further research explores different human approaches to reasoning
problems, noting large diversity in approaches which often converge to
the same solution (Ahn et al. 2026). This strongly reflects the nature
of reasoning problems with many possible paths to finding a solution for
a given problem. Researchers also noted an increase in response time as
people become familiar with a class of problems which also lead to a
decrease in accuracy.

# Search

Search is one of the earliest areas of AI research, with roots in
symbolic AI and heuristic problem solving. The fundamental idea is to
explore a structured space of possible solutions—programs, proofs,
plans, configurations—using systematic methods that balance breadth and
depth. Search-based reasoning models leverage this principle to navigate
combinatorial solution spaces efficiently, often guided by learned
heuristics or domain knowledge. This paradigm is crucial for domains
where outcomes are governed by strict, symbolic rules, and where a
direct, feed-forward calculation is insufficient to guarantee
correctness or optimality.

In logic and mathematics, search is used to establish the truth of
statements. SAT (Satisfiability) and SMT (Satisfiability Modulo
Theories) solvers are foundational tools that rely on efficient search
algorithms to determine if a formula can be satisfied. Modern solvers
typically employ variants of the DPLL (Davis-Putnam-Logemann-Loveland)
algorithm, often enhanced with Conflict-Driven Clause Learning (CDCL).
This process systematically explores the space of variable assignments,
pruning branches through powerful heuristics and learning from past
failed attempts, enabling them to verify complex software and hardware
designs (Moskewicz et al. 2001). Similarly, interactive and automated
theorem provers like Lean and Coq use search to navigate the vast space
of potential proofs. While the user may guide the process with tactics,
the underlying machinery performs an exhaustive, back-chaining search to
validate each logical step, ensuring the final theorem is mathematically
sound (Avigad et al. 2018).

In sequential decision-making environments, search is the primary
mechanism for look-ahead planning. Classical game AI, exemplified by the
chess engine Stockfish, uses the Alpha-Beta Pruning algorithm to
traverse the game tree. This minimax search efficiently explores
millions of potential moves per second, pruning branches that are
provably inferior, thus allowing the engine to evaluate moves deep into
the future and select the optimal strategy (Campbell et al. 2002).

More generally, Monte Carlo Tree Search (MCTS) provides a sampling-based
approach that combines the selectivity of tree search with the
generality of random sampling. MCTS comprises four steps (Selection,
Expansion, Simulation, and Backpropagation) and efficiently focuses
computational effort on the most promising moves (Browne et al. 2012).
This breakthrough was central to the success of advanced AI agents like
AlphaGo and MuZero. These agents demonstrated the power of deep learning
to extract features (perception) and generate value/policy predictions
(guidance) that effectively channel the MCTS component. By integrating
model-based reinforcement learning with tree search, agents can evaluate
future states not just based on learned values, but by simulating them
directly, leading to human-superhuman planning capabilities.

The cost of search is typically measured in the number of nodes that
must be expanded. Key parameters to model the cost include the depth of
the solution *d* and the breadth of the search space, or the branching
factor *b*. It is clear that the expansion as depth increases is the
main problem to solve (see ). In the case of breadth-first search the
worst-case cost can be calculated by summing the cost to get to each
level of depth of the search as seen in .

$$\begin{equation}
    Cost = 1 + b + b^2 + b^3 + \dots + b^d = \sum\_{i=0}^{d} b^i
    \label{eq:bfs}
\end{equation}$$

More generally, we can think of the cost as *O*(*b*<sup>*d*</sup>) by
taking the most significant factor as *b* is typically large. Search
methods can then be evaluated by how they can reduce this cost either by
decreasing the depth of solutions or the branching factor.

<figure id="fig:search-expansion">
<img src="figures/search_expansion.png" />
<figcaption>The number of nodes expanded grows exponentially with depth
according to the branching factor of the search space.</figcaption>
</figure>

# Model Classes

## Neuro-Symbolic Guided Reasoning

These systems blend neural perceptual modules with symbolic constraints,
rules, or program structures. The symbolic component narrows the
solution space or enforces correctness, while the neural component
supplies generalization and robustness. They offer a principled
compromise between expressivity and rigor, though their integration
pipelines can be brittle.

Symbolic reasoning is essential for intelligent systems because it
enables explicit manipulation of structured knowledge, supporting tasks
that require compositionality, abstraction, and verifiable
generalisation beyond the statistical patterns captured by purely neural
models. It provides mechanisms for rule-based inference, causal
explanation, and systematic extrapolation—capabilities closely
associated with human-level reasoning.

Traditional symbolic reasoning systems focus heavily on manipulating
Domain Specific Languages and rapid exploration of a vast search tree.
While efficient for small programs these methods clearly breakdown as
the depth of search increases and the search space grows exponentially.

A computer language specialized to a particular application domain or
task, offering expressive power and efficiency tailored to that specific
context rather than general-purpose programming.

Neuro-symbolic methods combine neural networks with symbolic search to
improve the search efficiency. Given a DSL of size *B* and a maximum
program length of *D*, the size of the search space is
𝒪(*B*<sup>*D*</sup>). This combinatorial explosion makes explicit
enumeration intractable for even modest values of *B* and *D*. To
improve upon search efficiency systems decrease either *B* or *D*.

- *B*: The size of the DSL is generally fixed but can be addressed in a
  few ways. Firstly, through careful design, the size of the DSL can be
  minimised. This usually requires a domain expert and does not
  significantly change the value. Another straightforward way to
  decrease the DSL size is type-based pruning where only functions which
  are valid for the current inputs are applied. Depending on the number
  of types, this can significantly reduce the number of available DSL
  functions. Finally, the DSL size can be reduced through the use of
  different search techniques such as beam search. By only expanding the
  most likely functions within the DSL the effective size of the DSL can
  be reduced to a constant at the cost of guaranteedness.

- *D*: Synthesising more complex functions and adding them to the DSL
  can reduce the total required steps as in (Ellis et al. 2021).
  DreamCoder is an example of DSL evolution where the system runs search
  procedures and then evaluates its history to look for common
  combinations of the DSL or constants to create new DSL entries.
  Decomposition of problems into subproblems can decrease the overall
  length at the cost of introducing an increase in the number of
  problems to be solved.

A key issue in neuro-symbolic guided reasoning is that the symbolic
space is separate from the reasoning vector space, requiring some way to
communicate between them. Vector Symbolic Architectures (VSAs), or
Hyperdimensional Computing, represent symbolic information using
high-dimensional, identically distributed random vectors (typically
*D* &gt; 10, 000) (Kanerva 2009). They rely on a set of algebraic
operations that allow for the composition of complex, nested structures
within a fixed-dimensional space. In neuro-symbolic systems, VSAs bridge
the gap between connectionist pattern matching and symbolic reasoning by
providing a mathematically rigorous way to perform transparent,
rule-based manipulation of data directly within vector spaces.
Researchers have explored using VSAs to encode transformations and
properties to solve tasks requiring both perception and abstract
logic (Joffe and Eliasmith 2025).

## Neural Iterative Reasoning

Neural iterative reasoning models compute incrementally. Instead of
producing an answer in a single forward pass, they refine an internal
state or hypothesis over multiple steps. This refinement may occur
through recurrence, message-passing, latent-space updates, or repeated
prompting. The common motif is learned iteration: the model is not given
an explicit symbolic search procedure but instead learns to improve its
representation or partial solution in a self-consistent manner. These
approaches offer flexibility and powerful inductive biases, yet they
often sacrifice interpretability, step-level control, and guarantees of
convergence.

Latent-state refinement models systems maintain a hidden state
representing the model’s current “understanding” of the world or the
input, and they iteratively update this state to make it more coherent.

Joint Embedding Predictive Architectures (JEPA) refine a latent
representation by enforcing predictability across views of the same
underlying scene or state. They do not simulate the world
token-by-token; rather, they iteratively sculpt an abstract state
intended to capture stable, predictable structure. Their reasoning
emerges from repeated updates that reduce prediction error or increase
latent consistency. World models more broadly (e.g., recurrent latent
dynamics models) also fall here: they maintain a compact state of the
environment that is improved through iterative dynamics rather than
explicit symbolic rollouts.

Deep Equilibrium Models (DEQ) define a network as the fixed point of an
iterative update rule (Bai et al. 2019). Rather than stacking layers,
they repeatedly apply the same transformation until convergence, and
then differentiate through the equilibrium. The reasoning is implicit:
the equilibrium computation effectively performs many refinement steps,
even if only the fixed point is exposed. DEQs are attractive because
they offer unbounded depth with a small parameter budget, but
controlling convergence and failure modes is difficult. Many papers have
built upon this foundation, by removing the reliance on ’infinite
expansions’ (Wang et al. 2025) and reducing the
complexity (Jolicoeur-Martineau 2025).

LLMs are firstly models that operate over continuous statistical
representations through language tokens. In modern agentic LLM systems,
they are augmented with tools which allow them to interface with
symbolic systems. These systems range from simple tools such as a
calculator (see ) through to APIs with other systems all the way through
to full internet access. Research shows when trained properly they are
able to master over ten thousand different tools (Qin et al. 2023). In
this way, LLMs become pseudo-symbolic systems which can get symbolic
results fed into their reasoning streams. Despite this, the symbols are
not first-class citizens as is the case with traditional neuro-symbolic
architectures.

## Tool-augmented Orchestrated Reasoning

These models coordinate external tools—planners, solvers, search
engines, code execution, or specialized modules—under the direction of a
central controller, often a large language model. Reasoning emerges
through delegation: the orchestrator decomposes tasks, invokes tools,
and aggregates results. This approach is highly capable and scalable,
but depends on reliable tool interfaces and strong planning competence
in the orchestrator.

Multi-agent systems use multiple specialized agents that communicate and
collaborate to solve complex tasks. Each agent may have distinct
capabilities (e.g., reasoning, perception, action), and the system
orchestrates their interactions to achieve goals that no single agent
could handle alone (Jiang and Karniadakis 2025; Piao et al. 2025).

LLMs have been integrated into environment loops where they can
perceive, plan, and act through tool use. Examples include embodied
agents that navigate virtual worlds, robotic systems that manipulate
physical objects, and interactive assistants that perform multi-step
tasks by invoking APIs or external services (Wang et al. 2023; Yao et
al. 2023).

<figure id="fig:llm-calculator">
<blockquote>
<p><strong>User:</strong> What is 482 <span class="math inline">×</span>
37?<br />
<strong>LLM:</strong> I will compute the product using the
calculator.<br />
<strong>LLM</strong> <span class="math inline">→</span>
<strong>Calculator:</strong> <code>compute(482 * 37)</code><br />
<strong>Calculator</strong> <span class="math inline">→</span>
<strong>LLM:</strong> <code>17834</code><br />
<strong>LLM:</strong> The result is 17 834.</p>
</blockquote>
<figcaption>Example of an LLM delegating arithmetic to an external
calculator.</figcaption>
</figure>

## Search-Based Reasoning

These systems cast reasoning as an explicit search over a structured
state space—such as programs, proofs, plans, or symbolic configurations.
They rely on heuristics, pruning rules, or optimization objectives to
navigate combinatorial possibilities. Their strength lies in
transparency and exactness, but they are limited by the exponential
growth of the search domain.

# Conclusion

Following the current research outlined above it is the author’s belief
that an intelligent reasoning system can be considered as a strongly
guided search process that leverages decomposition to recursively
simplify problems. In humans this search process is heavily guided by a
neural network with few expansions, but in silicon-based systems the
expansions are far more, and the neural network is weaker. Decomposition
is critical to see problems as more than just a collection of values and
imbue meaning.

Ahn, Caroline, Quan Do, Leah Bakst, et al. 2026. *Exploring Human
Behavior During Abstract Rule Inference and Problem Solving with the
Cognitive Abstraction and Reasoning Corpus*.
<https://arxiv.org/abs/2602.22408>.

Avigad, Jeremy, Leonardo de Moura, and Soonho Kong. 2018. “The
Mechanization of Mathematics with the Lean Proof Assistant.” *Journal of
Automated Reasoning* 62 (1): 233–69.
<https://doi.org/10.1007/s10817-017-9430-6>.

Baevski, Alexei, Wei-Ning Hsu, Xu Qiantong, Arun Babu, Jiatao Gu, and
Michael Auli. 2022. “Data2vec: A General Framework for Self-Supervised
Learning in Speech, Vision and Text.” *arXiv Preprint arXiv:2202.03555*.

Bai, Shaojie, J. Zico Kolter, and Vladlen Koltun. 2019. *Deep
Equilibrium Models*. <https://arxiv.org/abs/1909.01377>.

Botvinick, M. M. 2012. “Hierarchical Reinforcement Learning and the
Human Frontal Lobe.” *Cognitive Sciences* 16 (2): 110–17.

Browne, Christopher B., Edward Powley, Daniel Whitehouse, et al. 2012.
“A Survey of Monte Carlo Tree Search Methods.” *IEEE Transactions on
Computational Intelligence and AI in Games* 4 (1): 1–43.
<https://doi.org/10.1109/TCIAIG.2010.2101358>.

Burgess, Christopher P., Loic Matthey, Nicholas Watters, et al. 2019.
*MONet: Unsupervised Scene Decomposition and Representation*.
<https://arxiv.org/abs/1901.11390>.

Campbell, Murray, A. Joseph Hoane, and Feng-hsiung Hsu. 2002. “Deep
Blue.” *Artificial Intelligence* 134 (1–2): 57–83.
<https://doi.org/10.1016/S0004-3702(01)00122-8>.

Carion, Nicolas, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier,
Alexander Kirillov, and Sergey Zagoruyko. 2020. “End-to-End Object
Detection with Transformers.” *European Conference on Computer Vision*,
213–29.

Cellier, D., I. T. Petersen, and K. Hwang. 2022. “Dynamics of
Hierarchical Task Representations.” *Journal of Neuroscience* 42 (38):
7276–84.

Ellis, Kevin, Daniel Ritchie, Armando Solar-Lezama, and Joshua
Tenenbaum. 2021. “DreamCoder: Growing Generalizable, Interpretable
Knowledge with Wake-Sleep Bayesian Program Learning.” *Science* 374
(6565): 1041–48.

Feng, Sicheng, Gongfan Fang, Xinyin Ma, and Xinchao Wang. 2025.
*Efficient Reasoning Models: A Survey*.
<https://arxiv.org/abs/2504.10903>.

Jiang, Qile, and George Karniadakis. 2025. *AgenticSciML: Collaborative
Multi-Agent Systems for Emergent Discovery in Scientific Machine
Learning*. <https://arxiv.org/abs/2511.07262>.

Joffe, Isaac, and Chris Eliasmith. 2025. *Vector Symbolic Algebras for
the Abstraction and Reasoning Corpus*.
<https://arxiv.org/abs/2511.08747>.

Jolicoeur-Martineau, Alexia. 2025. *Less Is More: Recursive Reasoning
with Tiny Networks*. <https://arxiv.org/abs/2510.04871>.

Kanerva, Pentti. 2009. “Hyperdimensional Computing: An Introduction to
Computing in Distributed Representation with High-Dimensional Random
Vectors.” *Cognitive Computation* 1 (2): 139–59.
<https://doi.org/10.1007/s12559-009-9009-8>.

Kulkarni, Tejas D., Karthik R. Narasimhan, Ardavan Saeedi, and Joshua B.
Tenenbaum. 2016. *Hierarchical Deep Reinforcement Learning: Integrating
Temporal Abstraction and Intrinsic Motivation*.
<https://arxiv.org/abs/1604.06057>.

LeCun, Yann, Yoshua Bengio, and Geoffrey Hinton. 2015. “Deep Learning.”
*Nature* 521 (7553): 436–44. <https://doi.org/10.1038/nature14539>.

Locatello, Francesco, Dirk Weissenborn, Thomas Unterthiner, et al. 2020.
*Object-Centric Learning with Slot Attention*.
<https://arxiv.org/abs/2006.15055>.

Manning, Christopher D. 2022. “Human Language Understanding &Amp;
Reasoning.” *Daedalus* 151 (2): 127–38.
<https://doi.org/10.1162/daed_a_01905>.

Moskewicz, Matthew W., Conner F. Madigan, Yi Zhao, Lintao Zhang, and
Sharad Malik. 2001. “Chaff: Engineering an Efficient SAT Solver.”
*Proceedings of the 38th Design Automation Conference (DAC)* (Las Vegas,
NV), June, 530–35.

Piao, Jinghua, Yuwei Yan, Jun Zhang, et al. 2025. *AgentSociety:
Large-Scale Simulation of LLM-Driven Generative Agents Advances
Understanding of Human Behaviors and Society*.
<https://arxiv.org/abs/2502.08691>.

Qin, Yujia, Shihao Liang, Yining Ye, et al. 2023. *ToolLLM: Facilitating
Large Language Models to Master 16000+ Real-World APIs*.
<https://arxiv.org/abs/2307.16789>.

<span class="nocase">Solway, A. et al.</span> 2014. “Optimal Behavioral
Hierarchy.” *PLoS Computational Biology* 10 (8).

Sun, Jiankai, Chuanyang Zheng, Enze Xie, et al. 2024. *A Survey of
Reasoning with Foundation Models*. <https://arxiv.org/abs/2312.11562>.

Wang, Guan, Jin Li, Yuhao Sun, et al. 2025. *Hierarchical Reasoning
Model*. <https://arxiv.org/abs/2506.21734>.

Wang, Guanzhi, Yuqi Xie, Yunfan Jiang, et al. 2023. *Voyager: An
Open-Ended Embodied Agent with Large Language Models*.
<https://arxiv.org/abs/2305.16291>.

Yao, Shunyu, Jeffrey Zhao, Dian Yu, et al. 2023. *ReAct: Synergizing
Reasoning and Acting in Language Models*.
<https://arxiv.org/abs/2210.03629>.
