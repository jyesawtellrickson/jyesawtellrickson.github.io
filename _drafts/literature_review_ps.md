Proofs and functional programs are one and the same thing…simplifying a
proof corresponds to executing a program.

Philip Wadler

This chapter introduces the problem of program synthesis and motivates
its importance. We define what program synthesis is and review the
various domains and benchmarks that have been used to evaluate synthesis
systems. We then explore the landscape of neuro-symbolic program
synthesis, categorizing recent work by learning paradigm, model
architecture, search strategy, application domains, and computational
cost. Finally, we discuss the efficiency and scalability of these
systems, highlighting the trade-offs between neural guidance and search
complexity.

# Definition

The automated creation of executable programs from high-level
specifications, which may take the form of examples, logical
constraints, or natural language descriptions (Gulwani 2017).

The objective is to reduce human effort in programming, improve
correctness by construction, and enable automation of complex tasks
without requiring detailed procedural instructions. Program synthesis is
increasingly important as software complexity grows, as it allows both
expert and non-expert users to leverage computation effectively, while
also serving as a testbed for research in artificial intelligence,
formal methods, and human-computer interaction.

Despite its utility, program synthesis presents significant challenges.
The search space of possible programs grows combinatorially with program
size and complexity, making exhaustive search infeasible. Ambiguity in
specifications is another major difficulty: many programs may satisfy
the same set of examples or constraints, and choosing the most
appropriate or generalizable program requires careful reasoning.
Ensuring correctness, efficiency, and interpretability simultaneously is
non-trivial, particularly when specifications are incomplete or noisy.
Furthermore, integrating human intent effectively into the synthesis
process remains an open problem, especially when non-expert users
provide examples that are partially inconsistent or under-specified.

Overall, program synthesis represents a convergence of formal reasoning,
search-based problem-solving, and AI-driven automation. Its significance
lies not only in reducing manual programming effort but also in
providing a framework for building intelligent systems that can reason,
generalize, and generate complex behaviours autonomously. As
computational systems become increasingly embedded in all aspects of
human activity, program synthesis continues to emerge as a critical tool
for scalable, reliable, and accessible automation.

# Domains and Benchmarks

The importance of program synthesis is reflected in its broad range of
applications. These include string transformations, grid/agent tasks,
abstract reasoning tasks, graphics and code generation.

In general, benchmarking is significantly more difficult in program
synthesis compared to other tasks. This is for a few reasons:

- Program synthesis is not a single task; it is a meta-problem whose
  concrete difficulties depend entirely on the domain being
  instantiated. Different tasks are often fundamentally different
  regimes. This includes the program semantics, complexity class,
  acceptable failure modes and evaluation granuality.

- The DSL is both the interface and the inductive bias. Designing a DSL
  is itself half the research. Two key consequences: A richer DSL makes
  tasks “easier” because more solutions are expressible directly. A
  poorly structured DSL forces the synthesizer to rediscover low-level
  patterns, exaggerating difficulty and distorting comparisons. Even
  subtle DSL design changes—commutativity rules, higher-order
  constructs, canonical forms—shift the search landscape by orders of
  magnitude. So benchmarking two synthesizers with different DSLs is
  only fair if they share the same specification language, which rarely
  holds.

- In real synthesis settings, specifications are incomplete, noisy, or
  ambiguous (e.g., ARC, programming-by-example, robot task planning).
  Constructing ground-truth labels is itself a research problem. This
  makes benchmark design slow and subjective.

Integer, list and string-based tasks collectively make up the early
applications of program synthesis. The original DeepCoder DSL involves
integer registers and list manipulation functions (sort, tail,
etc.) (Balog et al. 2017). Many follow-up works also use this DSL or
similar integer domains (Zohar and Wolf 2019). These tasks are often
synthetic but challenge the model to chain arithmetic and list
operations correctly. String tasks as popularised by Microsoft Excel’s
Flash Fill (extracting substrings, reformatting names, see ) are a major
testbed (Cambronero et al. 2023). These tasks have some practical usage
in data cleaning, integration, and transformation. Systems like Flash
Fill showed how inductive synthesis can learn string or table
transformations from a few examples. This is a practical, high-impact
case where synthesis directly reduces human labour in data wrangling,
Extract, Transform, Load (ETL) pipelines, and enterprise software.

More specifically, programming by example or specification is now
commonly used to generate code for a variety of applications. Models
such as OpenAI Codex show applicability to real programming problems
(e.g. Python functions) by treating them as NLP tasks (Chen et al.
2021).

<figure id="fig:text_synthesis_examples">
<blockquote>
<p><span class="math display">$$\begin{align*}
\text{BobThomas} &amp;\rightarrow \text{Bob} \\
\text{MaryJones} &amp;\rightarrow \text{Mary} \\
\text{JohnThomasMiles} &amp;\rightarrow \text{John}\\
\text{FredSmith} &amp;\rightarrow \text{???}
\end{align*}$$</span></p>
</blockquote>
<figcaption>Example of a program synthesis task in the string domain. In
this example, the first name must be extracted. One method to do this is
split the text based on capitalised words and take the first indexed
one.</figcaption>
</figure>

In robotics and embedded systems, synthesizers can produce controllers
from temporal logic specifications (Wongpiromsarn et al. 2012). This
eliminates entire classes of runtime errors because the controller
provably satisfies liveness and safety constraints. The synthesis step
forms a bridge between symbolic reasoning and continuous control. Karel
is a common toy example where a robot navigates a 2D grid, requiring
loops and conditionals (Carmon and Wolf 2023).

Program synthesis can also be applied to graphical tasks. Systems have
been evaluated on inverse graphics (2D/3D shape modelling)
problems (Ellis et al. 2019, 2021). The Abstraction and Reasoning Corpus
(ARC) is a suite of visual puzzles requiring abstract
reasoning (Chaudhuri 2025). Several recent works apply program synthesis
to ARC (Alford et al. 2022; Witt et al. 2023).

In education, program synthesis can be used to enhance the learning
process. Synthesis tools can generate small programs or puzzles given
pedagogical constraints, providing interactive learning experiences for
students in programming and logic (<span class="nocase">Solar-Lezama et
al.</span> 2016). They can also be used to provide direct feedback by
analysing a student’s code, synthesising a fix and providing minimal
hints.

## Abstract Reasoning Corpus

Designed as a psychometric intelligence test for AI, the Abstract
Reasoning Corpus (ARC) measures a model’s capacity for few-shot learning
and abstract reasoning in unseen environments (Chollet 2019). Tasks are
framed as visual grid-based logic puzzles, where a solver must observe a
small set of demonstration pairs, abduce the latent transformation rule,
and apply it to a test input mapping
*G* : {1, …, *H*} × {1, …, *W*} → *C*. Because the evaluation set
features entirely novel transformations grounded in priors (Spelke and
Kinzler 2007), ARC effectively neutralizes the advantage of pure
statistical pattern matching, making it a rigorous testbed for
neuro-symbolic architectures and directed data generation strategies.
The original ARC dataset is divided into 400 training tasks and 400
evaluation tasks, as well as a private test set. An example is shown in
. It is available at <https://github.com/arcprize/ARC-AGI>.

The distinct spatial and conceptual challenges of ARC have driven the
development of targeted derivative benchmarks to isolate specific
failure modes in modern architectures. To decouple raw algorithmic
induction from the complexities of 2D spatial parsing, a known
vulnerability for sequence-based models, 1D-ARC (Xu et al. 2024)
flattens the reasoning tasks into single-dimensional arrays. Conversely,
to address the risk of models employing rather than acquiring true
conceptual abstraction, ConceptARC (Moskvichev et al. 2023)
systematically groups tasks by underlying semantic rules (e.g.,
symmetry, inside/outside). This allows for a more granular evaluation of
whether a system generalizes robustly across different spatial
instantiations of the exact same logical concept.

Furthermore, to ground these evaluations in developmental psychology,
benchmarks like KidsARC (Opiełka et al. 2024) adapt ARC’s complexity to
mirror the visual analogy tests administered to young children. By
utilizing single input-output analogies, KidsARC facilitates direct
performance comparisons between human cognitive baselines and artificial
systems. Together, these benchmarks provide a comprehensive framework
for validating the generalisability and robustness of program synthesis
solvers.

<figure id="fig:arc_example">
<img src="figures/arc_example_1e32b0e9.png" />
<figcaption>Example of a task (1e32b0e9) from the Abstract Reasoning
Corpus (ARC). The model must learn the transformation from the input to
the output and apply it to the test input. In this example, the
transformation is to take the shape from the top left part of the grid
and apply it to each other part of the grid as the other colour and
behind the existing shapes.</figcaption>
</figure>

## ILP String Transformation Corpus

The ‘ILP String Transformation Corpus’ is a collection of tasks that
require transforming input strings into output strings based on
underlying patterns or rules. One example is shown in . These tasks are
commonly used to evaluate the capabilities of program synthesis systems.
The corpus includes a variety of transformations such as substring
extraction, character replacement, formatting changes, and pattern-based
modifications. Each task consists of a set of input-output pairs that
exemplify the desired transformation, and the goal is to synthesize a
program that can generalize this transformation to new, unseen inputs.
It consists of 327 input-output tasks that are common problems in tasks
like business spreadsheet processing.

This corpus serves as a benchmark for assessing the generalization and
reasoning abilities of synthesis models in handling string-based tasks.
These tasks are prevalent in real-world applications like data cleaning,
text processing, and user interface automation. The dataset was
introduced by (Cropper and Dumančić 2020) and is publicly available at
<https://github.com/logic-and-learning-lab/ilp-experiments/tree/main/ilpexp/problem/strings/examples>.

Similar datasets include the Flash Fill dataset, which was introduced by
Microsoft Research as part of their Flash Fill system for string
transformation tasks in Excel (Cambronero et al. 2023) though it is not
available publicly.

<figure id="fig:string_dataset_examples">
<blockquote>
<p><span class="math display">$$\begin{align*}
\text{Bob Thomas} &amp;\rightarrow \text{Dr.\ Thomas} \\
\text{Mary Jones} &amp;\rightarrow \text{Dr.\ Jones}
\end{align*}$$</span></p>
</blockquote>
<figcaption>Example of a program synthesis task in the string
domain.</figcaption>
</figure>

# Neuro-symbolic Program Synthesis

Neuro-symbolic program synthesis combines neural networks with symbolic
search to learn programs from data. In these systems, the target
function is a program in a DSL or a fragment of code; neural components
guide or generate the program while symbolic methods (search, execution,
pruning) ensure correctness. Over the last decade researchers have
explored many variants of this idea (Chaudhuri 2025). We organize recent
work by learning paradigm, model architecture, search strategy,
application domains, and computational cost/efficiency.

## Learning Paradigms

Various learning paradigms can be applied to synthesis systems including
supervised learning, pre-training LLMs, iterative or bootstrapped
learning and reinforcement learning.

Supervised learning on synthetic data is the standard learning paradigm.
Most neural synthesizers train on large automatically generated datasets
of (input-output, program) examples. For instance, RobustFill (Devlin et
al. 2017) generates many string-transformation examples from its DSL to
train an attention-based RNN that encodes an unordered set of I/O
examples and decodes the DSL program. Write-Execute-Assess (Ellis et al.
2019) similarly samples random programs from its grammar to produce
training data. This synthetic training helps models generalize to new
tasks with few real examples. In all these cases the learning is
essentially offline supervised learning (often by maximum likelihood on
ground-truth programs) rather than reinforcement learning. Indeed, when
evaluated, reinforcement learning (RL) approaches often do not
significantly improve over maximum-likelihood training in
program-generation tasks (Chen et al. 2019; Zohar and Wolf 2019).

More recently, large language models (LLMs) pretrained on code (e.g.
GPT-based models) have been applied to program synthesis. For example,
OpenAI Codex is a GPT transformer fine-tuned on GitHub code; on the
HumanEval benchmark (docstring-to-code), it solves 29% of problems with
a single sample (and 70% with repeated sampling) (Chen et al. 2021).
These models leverage massive unsupervised pre-training on code before
any task-specific training (or minimal finetuning). This “pre-trained on
code” paradigm has become a powerful approach: code LMs encode rich
statistical knowledge of programming and require only modest extra
training for specific synthesis tasks.

Some systems interleave learning and synthesis. DreamCoder (Ellis et al.
2021) uses a wake-sleep procedure: it alternates between (1)
synthesizing programs for a batch of tasks (the “wake” phase) using its
current library of components, and (2) refactoring those programs to
extract common sub-expressions into new library primitives (the “sleep”
phase). This bootstraps an increasingly powerful DSL and a neural search
policy. DreamCoder learns its own structure hypothesis (the library)
from data, rather than relying on a fixed DSL. The process is
unsupervised in the sense that it uses only the given input-output
examples, but it ultimately improves itself by augmenting its DSL. The
wake-sleep cycle resembles curriculum learning, as the system tackles
simpler programs first and gradually builds up complexity. In
benchmarks, this approach solves more tasks (and faster) than a fixed
DSL with the same neural policy.

A few works apply reinforcement learning (RL) to program synthesis. For
example, DeepMind’s AlphaDev uses an AlphaZero-like agent (policy + MCTS
search) to discover new algorithms in assembly code (DeepMind 2023).
However, in more traditional program synthesis benchmarks, simple RL
often yields marginal gains. (Carmon and Wolf 2023) note that treating
synthesis as a Markov Decision Process (MDP) and training with policy
gradients yielded little improvement over supervised learning. Thus,
while RL has proven effective in some domains (e.g. game-like code
search in AlphaDev), most neural synthesizers rely on supervised or
hybrid learning.

## Neural Models and Representations

Neural program synthesizers use a variety of architectures to encode
inputs and decode programs.

Early works often used RNNs. For instance, RobustFill employs an
attentional RNN encoder (a variant of (Bahdanau et al. 2016)) that takes
as input an unordered set of example input-output strings (Devlin et al.
2017). In contrast, Code LMs (GPT) are Transformer-based: they take a
textual specification (docstring or prompt) and autoregressively
generate code tokens (Chen et al. 2021). Both RNNs and Transformers
output text (code) token-by-token. Larger-scale code models (GPT-3,
Codex, etc.) have effectively become state-of-the-art for many synthesis
tasks by “textually” generating the program.

Some approaches use simple feedforward networks (MLPs). DeepCoder used
an MLP that takes hand-crafted features of input-output pairs and
predicts a probability distribution over DSL functions (Balog et al.
2017). Those probabilities then guide a symbolic search. Similar neural
predictors (usually MLPs or lightweight networks) have been used to
estimate which functions or grammar rules are likely given the I/O.

A few systems use more structured models. In Write-Execute-Assess, the
policy network is a CNN+pointer network: it “attends” over the set of
partial programs currently in scope (as stored variables) and decodes
the next program line (Ellis et al. 2019). Graph neural networks
(GNNs) (Corso et al. 2024) have also been applied in some synthesis
contexts such as encoding data structures or program Abstract Syntax
Trees (ASTs), though they are less common in I/O-driven synthesis than
RNNs/Transformers.

Most neural synthesizers condition on I/O examples (input-output pairs)
that specify the task. These examples may be fed as raw values, strings,
images, etc., depending on domain. Notably, some models also ingest
intermediate execution states. The Read-Eval-Print Loop (REPL) approach
explicitly executes partial programs: it feeds the set of current
programs in scope into a “REPL” (which produces, e.g., rendered images
or strings) and then the network uses that semantic state as input along
with the specification (Ellis et al. 2019). This gives the model a
direct view of what each candidate program does so far.

In all cases the model ultimately outputs a program (as text or
structured AST). For example, RobustFill’s neural decoder emits a string
of DSL tokens representing the string transformation program (Devlin et
al. 2017). The Write-Execute-Assess model decodes one production rule at
a time (Ellis et al. 2019). Alternatively, “neural induction” models (as
opposed to synthesis) skip program output and directly emit the output
string, but these do not meet our criterion of producing a
program (Macfarlane and Bonnet 2025).

## Search and Expansion Strategies

Even with a neural model, most systems include a search or decoding
strategy to handle the combinatorial space of programs.

In many end-to-end models, decoding is simply done by beam search over
token sequences (treating it like any seq2seq task). Beam search
explores a breadth of top candidate sequences and is akin to best-first
search in the program tree. A notable variant is Complete Anytime Beam
(CAB), which progressively widens the beam under a time budget (Zohar
and Wolf 2019).

Some works use MCTS or related stochastic search. (Carmon and Wolf 2023)
propose an MCTS variant for program synthesis: they modify the visit
counts and encode the executed prefix of the program. On DSLs like
DeepCoder and Karel, this improved on beam and standard MCTS baselines.
In REPL-based synthesis, the authors actually use Sequential Monte Carlo
sampling (a form of MCTS) combined with a learned value function: at
each step they sample next actions from the policy, execute them, and
weight candidates by a learned value (Ellis et al. 2019). This SMC
sampler outperforms beam search and pure sampling, solving more tasks
with far fewer expansions. Similarly, AlphaDev treats algorithm
discovery as a game: it uses AlphaZero-style RL to guide an MCTS search
that discovers new assembly routines (DeepMind 2023).

DeepCoder and related methods combine a neural predictor with a
traditional enumerative search (like a Satisfiability Modulo Theorise
solver) (Balog et al. 2017). The network estimates which functions (or
next statements) are likely given the I/O (e.g. an MLP outputting
probabilities for each DSL function). These probabilities are used to
prioritize the search order. (Zohar and Wolf 2019) predicted the next
line of code given the current execution state and used a learned
garbage collector to drop unneeded variables during search. This yields
an informed breadth-first search that is much faster than brute force.

For some structured problems, it makes sense to search forwards from
inputs and backwards from outputs simultaneously. (Alford et al. 2022)
design a bidirectional neural search for ARC (visual reasoning) tasks.
They extend execution-guided synthesis by adding “inverse semantics”
deductions, effectively searching the program space from both ends. This
neural-guided bidirectional search was shown to solve ARC tasks (and
other puzzles) that brute-force methods could not, leveraging human-like
reasoning strategies.

Another approach is to decompose the I/O examples into subtasks. (Witt
et al. 2023) propose a Divide-Align-Conquer strategy: they segment each
I/O example into parts (using structure-mapping analogies) and solve for
smaller programs whose outputs compose to the target. This compositional
strategy can reduce search complexity from exponential to near linear in
the number of components for highly structured domains. They demonstrate
significant gains on string transformation problems and even apply it to
ARC, where flat search is intractable.

In summary, neural program synthesis often uses neural-guided search: a
network suggests or ranks candidates, and a symbolic search
(beam/MCTS/enumeration) completes the synthesis. Pure “generate once”
decoding (no search) is uncommon except for strong LLMs with sampling.
Most systems find a balance: the network makes the search focused and
feasible, while execution-testing (the DSL interpreter) guarantees
correctness.

## Efficiency, Resources, and Scalability

The computational cost of neural synthesis varies widely. Modern deep
models (especially large Transformers) can be very expensive to train:
for example, training GPT-like models on code uses thousands of
GPU/TPU-hours (the Codex paper hints at training huge models) (Chen et
al. 2021). Inference cost depends on search: straightforward decoding
(sampling from a pre-trained model) incurs GPU/TPU inference but no
extra search. By contrast, neural-guided search involves many program
“node expansions.” A single beam search or MCTS can expand thousands of
partial programs; execution of each candidate may also be costly.

However, learning can dramatically reduce search effort. For instance,
the SMC sampler in Write-Execute-Assess solves more tasks with an
order-of-magnitude fewer node expansions than prior methods (Ellis et
al. 2019). In their string domain, the value-guided sampler solved 100%
of tasks using 10x fewer expansions compared to unguided search.
Similarly, DreamCoder’s learned library allows it to solve problems with
far less search than using the base grammar alone (Ellis et al. 2021).

In summary, earlier neural synthesizers (small RNNs) required only
modest GPUs for training, whereas recent systems (Transformers, LLMs)
need massive clusters. On the other hand, neural guidance can
drastically cut the effective search space. We characterize a method’s
search efficiency roughly by how many expansions it needs: end-to-end
generation methods (no search) have “low” expansions, neural-guided
beam/MCTS “medium”, and brute-force or generic search “high”. For
example, a pure neural model like Codex uses no search expansions (it
directly outputs code with beam/sample), whereas bootstrapped symbolic
methods without strong heuristics might expand exponentially many
programs.

Alford, Zachary, Armando Solar-Lezama, and Kevin Ellis. 2022.
“Neural-Guided, Bidirectional Program Search for Abstraction and
Reasoning.” *Proceedings of the 44th Annual Meeting of the Cognitive
Science Society (CogSci)*.
<https://sites.dartmouth.edu/lisplab/alford-neural-2022/>.

Bahdanau, Dzmitry, Kyunghyun Cho, and Yoshua Bengio. 2016. *Neural
Machine Translation by Jointly Learning to Align and Translate*.
<https://arxiv.org/abs/1409.0473>.

Balog, Matej, Alexander L. Gaunt, Marc Brockschmidt, Sebastian Nowozin,
and Daniel Tarlow. 2017. *DeepCoder: Learning to Write Programs*.
<https://arxiv.org/abs/1611.01989>.

Cambronero, José, Sumit Gulwani, Vu Le, et al. 2023. “FlashFill++:
Scaling Programming by Example by Cutting to the Chase.” *Proceedings of
the ACM on Programming Languages* 7 (January): 952–81.
<https://doi.org/10.1145/3571226>.

Carmon, Nadav, and Lior Wolf. 2023. “Improved Tree Search for Automatic
Program Synthesis.” *arXiv Preprint arXiv:2303.07166*.
<https://ar5iv.labs.arxiv.org/html/2303.07166>.

Chaudhuri, Swarat. 2025. *Neural Program Synthesis: A Literature
Review*. <https://proceedings.mlr.press/v70/devlin17a/devlin17a.pdf>.

Chen, Mark, Kevin Tworek, Heewon Jun, et al. 2021. “Evaluating Large
Language Models Trained on Code.” *arXiv Preprint arXiv:2107.03374*.
<https://arxiv.org/abs/2107.03374>.

Chen, Xinyun, Chang Liu, and Dawn Song. 2019. “Execution-Guided Neural
Program Synthesis.” *ICLR*. <https://openreview.net/pdf?id=H1gfOiAqYm>.

Chollet, François. 2019. *On the Measure of Intelligence*.
<https://arxiv.org/abs/1911.01547>.

Corso, Gabriele, Hannes Stark, Stefanie Jegelka, Tommi Jaakkola, and
Regina Barzilay. 2024. “Graph Neural Networks.” *Nature Reviews Methods
Primers* 4 (1). <https://doi.org/10.1038/s43586-024-00294-7>.

Cropper, Andrew, and Sebastijan Dumančić. 2020. *Learning Large Logic
Programs by Going Beyond Entailment*.
<https://arxiv.org/abs/2004.09855>.

DeepMind. 2023. *AlphaDev Discovers Faster Sorting Algorithms*. Google
DeepMind Blog.
<https://deepmind.google/blog/alphadev-discovers-faster-sorting-algorithms/>.

Devlin, Jacob, Jonathan Uesato, Alexander Polosukhin, Rishabh Singh, Sam
Lee, and Wojciech Zaremba. 2017. “RobustFill: Neural Program Learning
Under Noisy i/o.” *Proceedings of the 34th International Conference on
Machine Learning (ICML)*, 990–99.
<https://proceedings.mlr.press/v70/devlin17a/devlin17a.pdf>.

Ellis, Kevin, Daniel Ritchie, Armando Solar-Lezama, and Joshua
Tenenbaum. 2021. “DreamCoder: Growing Generalizable, Interpretable
Knowledge with Wake-Sleep Bayesian Program Learning.” *Science* 374
(6565): 1041–48.

Ellis, Kevin, Matt Welling, Armando Solar-Lezama, and Regina Barzilay.
2019. “Write, Execute, Assess: Program Synthesis with a REPL.”
*Proceedings of the 36th International Conference on Machine Learning
(ICML)*. <http://www.mit.edu/~fsosa/papers/repl_icml.pdf>.

Gulwani, Sumit. 2017. “Program Synthesis.” *Foundations and Trends in
Programming Languages* 4 (1-2): 1–119.

Macfarlane, Matthew V, and Clément Bonnet. 2025. *Searching Latent
Program Spaces*. <https://arxiv.org/abs/2411.08706>.

Moskvichev, Arseny, Victor Vikram Odouard, and Melanie Mitchell. 2023.
*The ConceptARC Benchmark: Evaluating Understanding and Generalization
in the ARC Domain*. <https://arxiv.org/abs/2305.07141>.

Opiełka, Gustaw, Hannes Rosenbusch, Veerle Vijverberg, and Claire E.
Stevenson. 2024. *Do Large Language Models Solve ARC Visual Analogies
Like People Do?* <https://arxiv.org/abs/2403.09734>.

<span class="nocase">Solar-Lezama, Armando et al.</span> 2016. “Learning
a Neural Semantic Parser from User Feedback.” *Proceedings of the 54th
Annual Meeting of the Association for Computational Linguistics*, 1–12.

Spelke, Elizabeth S., and Katherine D. Kinzler. 2007. “Core Knowledge.”
*Developmental Science* 10 (1): 89–96.
https://doi.org/<https://doi.org/10.1111/j.1467-7687.2007.00569.x>.

Witt, Jonas, Sebartijan Dumančić, Tias Guns, and Claus-Christian Carbon.
2023. “A Divide-Align-Conquer Strategy for Program Synthesis.” *arXiv
Preprint arXiv:2301.03094*. <https://arxiv.org/abs/2301.03094>.

Wongpiromsarn, Tichakorn, Ufuk Topcu, and Richard M. Murray. 2012.
“Receding Horizon Temporal Logic Planning.” *IEEE Transactions on
Automatic Control* 57 (11): 2817–30.
<https://doi.org/10.1109/TAC.2012.2195811>.

Xu, Yudong, Wenhao Li, Pashootan Vaezipoor, Scott Sanner, and Elias B.
Khalil. 2024. *LLMs and the Abstraction and Reasoning Corpus: Successes,
Failures, and the Importance of Object-Based Representations*.
<https://arxiv.org/abs/2305.18354>.

Zohar, Amit, and Lior Wolf. 2019. *Automatic Program Synthesis of Long
Programs with a Learned Garbage Collector*.
<https://arxiv.org/abs/1809.04682>.
