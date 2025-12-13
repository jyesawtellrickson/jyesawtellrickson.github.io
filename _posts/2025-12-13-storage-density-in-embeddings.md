---
layout: post
title: "Embeddings: a Tool for Compression and Expansion"
categories: [Knowledge]
---

Embeddings are at the heart of machine learning. Embeddings allow us to represent any imaginable object as a list of numbers which can be processed by models. This idea is shockingly powerful. Literally anything, a picture of a car, a poem you wrote in fifth grade, the sound of your favourite song or something as abstract as a stream of vibrations in the Earth's crust. By formulating all these different inputs into a consistent form we can leverage similar techniques to do useful work such as description, prediction and prescription.

Embeddings come in different forms. Some embeddings perform compression, taking a 'large' object and extracting the key information that represent it's core, while others take a 'small' object and attempt to capture all it's meaning. In this article we'll explore these two sides of embeddings.

While there are many lenses with which to analyse embeddings, let's consider the raw data compression rate, which effectively measures the "density" of an embedding in terms of storage size. While this doesn't capture the subtle complexity of semantic information content (which is what truly matters in embeddings), it is interesting to compare the efficiency of models across different data types.

## A Tool for Compression

A picture is worth a thousand words, and probably more. Images (and video) are the most popular way for social communication, with platforms like IG and Tiktok garnering billions of active users worldwide. Users flock to see engaging content packed to the brim with detail. However, for many useful tasks, images contain a lot of useless information. For example, the background colour of the wall may not be important when trying to classify household objects. Image models trained for tasks such as classification can learn representations of images which condense an image representation of objects or scenes down to small embeddings. Let's see exactly how much compression is happening.

We can compare a raw image, compressed image and typical embedding of an image. 

Raw Image: A 256x256 pixel image with 3 color channels (RGB) where each channel is an 8-bit integer (0-255) is typically stored as 24 bits per pixel (8 bits 1$\times$ 3 channels).2

$$\text{Input Size (Bits)} = 256 \times 256 \times 3 \times 8 \text{ bits/channel} = 1,572,864 \text{ bits}$$

Compressed Image: Images can be compressed with various algorithms including the wellknown JPEG and WEBP formats. These formats can provide up to 90% compression without losing too much visual detail.

Output Data Size (Embedding): A 64-dimension embedding vector typically uses 32-bit floating-point numbers (float32) for each dimension, as this is the standard for modern deep learning.

$$\text{Output Size (Bits)} = 64 \text{ dimensions} \times 32 \text{ bits/dimension} = 2,048 \text{ bits}$$

Armed with the bit size of the images and embedding we can now analyse the compression ratio. In the case of a raw image to embedding, we have:

$$\text{Compression Ratio} = \frac{\text{Input Size (Bits)}}{\text{Output Size (Bits)}} = \frac{1,572,864}{2,048} \approx 768$$

This means the 64-dimension embedding is about 768 times smaller than the raw input image data. Images aren't typically stored in the uncompressed format, but rather as compressed types such as JPEG, account for a generouse 10x compression, we still have a large compression factor of 77x.


## A Tool for Expansion

While images contain massive amounts of information, much of which is not useful, language transmits a lot of meaning in just a few letters. Let's calculate the 'compression ratio' for language.

Calculating the raw bit size for a language input is more complex because language models operate on tokens rather than individual characters, and the input length is variable. Let's use a typical sentence and a standard transformer model as an example:

Input Sentence: "The quick brown fox jumps over the lazy dog."

Encoding: Modern text is usually encoded using UTF-8, where most common English characters take 8 bits (1 byte).

$$\text{Text Size (Bits)} = 44 \text{ characters} \times 8 \text{ bits/character} = 352 \text{ bits}$$


Similar to images, text can also be compressed by replacing common patterns with condensed representations. This can lead to up to 90% compression too, giving a size of just 35 bits.


However, the model processes tokens, which are typically represented by an integer ID. Since a transformer's vocabulary size is often $\approx 50,000$ tokens, the token ID requires $\log_2(50,000) \approx 15.6$ bits. We'll use 16 bits (2 bytes) per token ID for the input size in the model's first layer.

Tokenisation varies from model to model, but this sentence tokenises to 10 tokens across various GPT models ([GPT Tokenizer](https://gpt-tokenizer.dev/)).

$$\text{Transformer Embedding Size (Bits)} = 10 \text{ tokens} \times 16 \text{ bits/token ID} = 160 \text{ bits}$$

Output Data Size (Sentence Embedding): A popular, high-quality sentence transformer (like all-MiniLM-L6-v2) often produces an embedding of 384 dimensions. Again, these are typically 32-bit floating-point numbers.

$$\text{Output Size (Bits)} = 384 \text{ dimensions} \times 32 \text{ bits/dimension} = 12,288 \text{ bits}$$

Compression Ratio (Raw Bits)

$$\text{Compression Ratio} = \frac{\text{Text Size (Bits)}}{\text{Output Size (Bits)}} = \frac{352}{12,288} \approx 0.029$$

In contrast to what we saw with images, text embeddings are uncompressed versions of their sources.


## But What Are Embeddings, Really?

For the image example, the ratio was much greater than one, indicating massive compression. For the language example, the ratio is much less than one, indicating the model is performing expansion in terms of raw storage size, not compression. Why is the language ratio $<1$? This result highlights a critical difference:
- Image: The input is raw pixel data (mostly redundant/local information), and the model's job is to compress it into its abstract semantic features.
- Language: The input is already highly compressed symbolic data (token IDs). The embedding model's job is to expand this sparse, discrete ID into a dense, high-dimensional space that captures the rich, continuous semantic relationships between words and concepts. The value of a language embedding isn't in saving space, but in making the abstract meaning of the text mathematically comparable.

While we've looked at storage density, the true measure of a "super dense" model is its Information Density:

$$\text{Information Density} \propto \frac{\text{Semantic Information Contained}}{\text{Vector Size (Bits)}}$$

A "super dense" embedding is one that retains a high amount of the original input's semantic meaning while having a minimal size. For instance, a 768D image embedding might score slightly better on downstream tasks than a 1024D one, meaning the 768D vector has a higher information density. The key is how well the model filters out noise and redundancy while preserving meaning.

## Human's Embeddings

It's also interesting to consider how humans store information. The word "car" conjures up a lot of information in the human mind. While language models store the information in the token embeddings and network parameters, humans store it in their brain with neuron connections. Similarly with the visual and auditory cortex, humans can translate from raw sensory information to embedded meanings within the brain.

## Conclusion

Our simple model of storage density revealed the difference in how embeddings are used in language and vision models. Storage density is one way to think about embedding density, but there are others such as information density which provide insight into the model's ability to preserve meaning. Human's also have some form of embeddings stored within our brains which acts to translate from low-level sensory information to deeper meanings.


