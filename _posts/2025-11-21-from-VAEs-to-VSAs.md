---
layout: post
title: "Embedding Dimensions: from VAEs to VSAs"
categories: [Knowledge]
---

Vectors are at the heart of modern machine learning techniques. LLMs are powered by the transformer which operates on language tokens which are mapped to embeddings that have around 1000 dimensions. Similarly, vision models represent images as pixels of colour which are translated to vectors (or tensors), audio models represent sound as frequencies and amplitudes which are again translated to vectors. Vectors are a core computational input and processing component throughout machine learning. 

In this article, I want to discuss two extremes: Variational Autoencoders (VAEs) and Vector Symbolic Architectures (VSAs). VAEs often create very dense embeddings, packing a lot of information from whatever high-dimensional data source they're trained on into embeddings of just 10s of dimensions. On the other hand, VSAs leverage hyperdimensional embeddings on the order of 10,000 dimensions or more as a basis for computation, leveraging their statistical properties.

## Variational Autoencoders

If you’ve ever tried to pack for a holiday in a carry-on bag, you understand the core philosophy of a Variational Autoencoder (VAE): compression is understanding. Europe's Ryanair has taught me this lesson all too well.

The "Autoencoder" part is simple enough. It’s a neural network shaped like an hourglass. You feed data (like an image) into the wide top, it gets crunched down through progressively smaller layers into a tiny "bottleneck," and then the network tries to reconstruct the original image from that bottleneck on the other side. If the output looks like the input, you know that the tiny bottleneck contains all the essential information required to describe the data.

But a standard Autoencoder is a bit of a cheat—it memorizes specific points. The "Variational" part is where the magic (and the math) happens. Instead of mapping an input to a single fixed point in that bottleneck, a VAE maps it to a probability distribution (usually a Gaussian blob). It says, "This image is somewhere in this cloud of possibilities."

This forces the model to learn a latent space—a smooth, continuous manifold where similar concepts live near each other. If you train a VAE on faces, you don't just get a database of JPEGs. You get a coordinate system for "faceness." You might find that moving along one dimension changes the angle of the head, while another changes the skin tone.

We are talking about aggressive compression here. We might take an image with thousands of pixels (dimensions) and squash it down to a latent vector of just 10 or 20 dimensions. It turns out that the world is actually quite simple if you can just find the right manifold to view it from.

# Vector Symbolic Architectures

Now, let’s do the exact opposite. If VAEs are about finding the absolute minimum number of variables to describe the world, Vector Symbolic Architectures (VSAs), also known as Hyperdimensional Computing—are about exploding that information into a space so massive that we can rely on the law of large numbers to do our thinking for us.

In a VSA, we don't use 10 dimensions. We don't even use the 1,000 dimensions typical of an LLM embedding. We use something on the order of 10,000 dimensions or more. Some systems use as many as 10 million dimensions.

Why on earth would we want to make our data larger? It comes down to orthogonality. In a 10,000-dimensional space, if you pick two vectors at random, they are almost guaranteed to be orthogonal (uncorrelated) to each other. This geometric quirk allows us to do something incredible: we can superimpose information without it getting muddied.

VSAs define an algebra for these hypervectors. There are various different formulations (e.g. MAP, BSC, HRR) but they do similar things. You can combine vectors using operations like "binding" and "bundling":
- Bundling (Superposition): You can add two vectors together ($A + B$) to create a vector that is similar to both. It’s like a memory that stores multiple items at once.
- Binding (Association): You can multiply vectors ($A * B$) to create a new vector that is dissimilar to both constituents. This is great for assigning values to variables, like binding "Name" to "Jye."

Because the space is so vast, these operations are incredibly robust. You can corrupt 40% of the bits in a hypervector and still retrieve the original information perfectly. It’s distributed representation in its purest form—holographic, noise-resistant, and strangely similar to how we suspect the biological brain might actually work.

VSAs have been applied to complex reasoning tasks such as Raven's Matrices where they modelled the possible transformations between objects and ARC Prize where they were combined with neural models.

# Conclusion

We are currently living through a "dense vector" revolution. Transformers and Diffusion models—the current kings of AI—rely heavily on the continuous, compressed representations that technologies like VAEs helped popularize. We want to squeeze as much semantic meaning as possible into a 1024-dimensional float array so our GPUs can crunch it efficiently.

But there is a beauty in the brute-force statistics of VSAs that is hard to ignore. VAEs try to learn the perfect, delicate structure of the data. VSAs simply construct a space so large that structure can be built algebraically, on the fly, without needing an optimization algorithm to fine-tune every weight.

As we push for AI systems that can reason symbolically rather than just predict the next token, we might find ourselves looking less at how small we can make our vectors, and more at how wide we can stretch them.