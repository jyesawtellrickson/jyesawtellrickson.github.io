---
layout: post
title: Why we can't talk to dogs, yet
categories: [LLMs, Project]
---

Wouldn't it be great if you could communicate directly with your dog? If you could ask him why he bit your furniture, or just understand what he's barking about? While research has tried address this in the past, the problem is still far from solved, and potentially unsolvable. Let's see why.

## Canine Communication

Canine communication is complex. Dogs do not use vocalizations in the same structured way humans use language. Their communication is multimodal, involving body posture, facial expressions, scent, and environmental context. A bark or whine may carry different meanings depending on the situation, making it hard to map vocalizations directly to specific semantic content without additional cues.

Studies have also shown that dogs vocalize differently based on who or what they are responding to—for example, showing distinct vocal behaviors when interacting with owners versus food. This suggests that while vocalizations are meaningful, interpreting them accurately would require integrating visual and situational context, such as video input, alongside audio.

## Datasets

One of the main obstacles to further progress is the lack of publicly available, large-scale, and well-annotated datasets of dog vocalizations with corresponding behavioral or contextual video data. While some datasets exist (e.g., bark recordings in various contexts), they are often small, limited in scope, or not annotated with enough detail to train highly accurate models.

One of the best datasets, [Barkopedia](https://huggingface.co/datasets/ArlingtonCL2/Barkopedia-Dog-Vocal-Detection) contains 4.5 hours of labelled data and an additional 24 hours of unlabelled data. 

It shocks me that this is a limitation though. Looking at the [Youtube 8M dataset](https://research.google.com/youtube8m/explore.html), we can quickly see that there are 26K videos under the category of dog. While much of the data is likely not usable, if we assume 50% of the videos are, and an average length of 1 minute, with 10s of vocalisations, then we land at 26K * 0.5 * 10s = 36 hours of usable vocalisation footage. Vocalisations can be extracted via a trained model (there are a few) and labelled via a combination of existing tags, transcripts and VLMS. 

## Technology

Self-supervised speech representation models, such as Wav2Vec2—originally designed for human speech—are being explored for their potential to decode dog barks by identifying patterns in tone, pitch, and context. Additionally, AI models have shown promise in distinguishing nuances in dog vocalizations and even identifying attributes like age, breed, and sex from audio data alone. In general, transformers provide a great methodology to convert the audio through mel spectograms to understandable outputs. 

I can imagine a world where the audio plus contextual information along with a little artistic flair allows us to convert repeated "woof"s at dinner time into "I'm hungry", "Seriously, I want to eat", "I'm soooo hungry". With 1B pet owners globally, it seems like a potential market opportunity.