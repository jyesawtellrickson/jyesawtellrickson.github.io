---
layout: post
title: Self-Supervised Learning Methods
categories: [Knowledge]
---

Self-supervised learning is a popular method for training models across many fields of AI. It represents a paradigm that does away with one of the toughest challenges of machine learning applications - labelling a dataset. Self-supervised learning leverages massive unlabelled databases by creating its own labels to learn useful representations of data which can later be used for downstream tasks, often leveraging some unrelated training objective. In this article, we'll discuss the key self-supervised learning methods and how they relate to each other.

# Three Overarching Categories

Self-supervised learning methods can be broadly separated into three categories:
1. **Classical**: this category includes very custom tasks such as 'jigsaw puzzles' and heavily geometry-based methods.
2. **Contrastive**: approaches that compare samples to each other to create spaces that well describe the underlying distribution.
3. **Generative**: methods that train models to generate samples that follow the training distribution.

As we'll see, in each of these methods we'll learn some model while utilising a massive unlabelled dataset which can then be augmented for downstream tasks.

# Classical Self-Supervised Learning

As self-supervised learning was being developed many interesting methods were proposed. These methods, referred to as pretext task methods, created unique tasks depending on the problem that was being tackled. Examples include:
- Image colourisation: colour is removed from a sample and the model is tasked with predicting the colours from the black and white image.
- Jigsaw puzzles: samples are cut into smaller pieces (like a jigsaw) and shuffled and the model is tasked with rearranging them as in the original image.
- Rotation prediction: random rotations are applied to samples and the model must predict what rotation was applied.

These tasks aren't necessarily useful but the thing that relates them all is that for a model to perform well on the task it must learn about how images are represented. This 'background' learning is typical of self-supervised learning methods.

Another group of classical techniques is the class of geometric methods, or manifold learning, many of which are still in use today. These methods explicitly model distances, angles and neighbourhoods to learn useful lower-dimensional spaces. One prime example is t-SNE (t-Distributed Stochastic Neighbor Embedding), a nonlinear dimensionality reduction technique which is mostly used for visualisation of high dimensional data. t-SNE uses gradient-based optimisation to minimise the divergence between the probabilities of points being neighbours in the original high dimensional vs. the target low dimensional space.

# Contrastive Self-Supervised Learning

In contrastive learning, samples are directly compared to something to help form a well-structured space. There are two main categories of approaches here:
- Pure contrastive: use similar, positive samples and dissimilar negative samples to both minimise and maximise distances at the same time. 
- Consistency regularisation: utilises only similar samples to try to pull together.

While contrastive methods use both push and pull forces to form their space, consistency regularisation focuses only on pulling similar samples closer together.

One example of constistency regularisation is the 'mean teacher' model, or student-teacher self-distillation. For this approach, a student model is trained to match the outputs of a teacher model when given similar inputs. The teacher is itself an exponential moving average (EMA) of the student. The key idea is that the student is fed crops of an image which contain less information than the full one fed to the teacher and to be able to match the results it must understand something about what's actually represented in the image. Meta's DINO is a great example of this which is still in development today with DINOv3.

# Generative Self-Supervised Learning

Generative self-supervised learning captures the most popular techniques you've likely heard of and is the basis of the 'generative revolution' which has taken AI by storm in the last few years. The key defining characteristic behind generative methods is that they directly train a model which can produce samples from the training distribution, while often training an auxiliary model for other tasks. Similar to the other categories, generative methods capture a wide array of techniques:
- Adversarial methods: like GANs
- Reconstructive methods: like VAEs
- Token masking: the method behind LLMs.

# Conclusion

Self-supervised methods are so powerful because they leverage massive datasets without having to rely on expensive human labelling. Classical techniques were the basis for exploration into the area and are still in use today, while contrastive methods hove proven useful many image-based tasks. Generative self-supervised learning has become the number one technique through the huge growth in LLMs. These techniques will continue to develop and grow and remain a mainstay for any AI practitioners.
