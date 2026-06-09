---
layout: post
title: An Introduction to AI Generation
categories: [Personal]
---

Recently I lost my Spotify subscription, and stubborn as I am, I decided to try surviving without it. My default response is to just find playlists on YouTube and listen to those. After vibing to some music for a while I realised that it might be AI generated. Sure enough, looking closer I found that all the music from the channel I liked was AI-generated, along with the video background. Quite impressive. Given I had access to some compute I thought it might be fun to experiment with creating something similar myself. The remainder of this post entails my experiment in creating a study music video.

# The Plan

To create a study music video we need music and we need a video. After a bit of research I turned to ComfyUI as a powerful tool for AI generation and came up with a plan:

1. Acquire the hardware.
2. Generate a 5m audio clip using ACE-Step, a SOTA model for audio generation.
3. Create an image using a persona as the basis for the video using Z Image Turbo.
4. Turn the image into a video with Flux.

# Production

The first step was to prepare the hardware. I have access to a 24GB VRAM system which allows me to use some of the best video generation models, however I quickly found out that wasn't enough. With just 32GB System RAM I later ran into issues with model offloading, so I had to increase my total RAM to 64GB before being able to generate everything.

To get started with the audio, I needed to create a prompt. From my experience with LLMs, I know that getting the right prompt is one of the crucial parts for getting good output. As a beginner, I turned to Gemini for a good quality prompt. Below is the prompt when I asked for chill study music - looks good to me. I fed this into an audio generation template and inspected the results. The first attempt was pretty bad. There was no progression and the second half of the song was sort of just empty. Not to be deterred I tried again and the 2m clip it generated was decent. I decided to scale up to my target length of 5m and the results were not bad. On to the next step.

```text
75 bpm, 4/4 time signature, key of D minor, lo-fi hip hop, study music, chillhop, soft fender rhodes piano, background rain sounds, mellow vinyl crackle, relaxed jazz chords, cozy rainy day atmosphere, instrumental, no vocals
```

For image generation, I again requested a prompt (below) and plugged it into the image generation template. Image generation is relatively quick, so I asked for 8 and chose the best result. Very straightforward.

```text
(masterpiece, top quality, best quality), (digital illustration, clean art style, cozy lo-fi anime aesthetic:1.1), smooth coloring, atmospheric perspective.

(Subject: young adult woman, relatable, cozy demeanor, focused expression), (Appearance: unique platinum blonde bob hairstyle with straight bangs, wearing large round gold-rimmed eyeglasses), (Attire: oversized knitted cream sweater, subtle silver locket necklace).

(Setting: cluttered cozy bedroom desk, deep rain outside a large window, blurry city lights, dim indoor lighting, warm lamplight illuminating the desk).

(Mood: deep focus, nostalgic, peaceful, study atmosphere).
```

Video is where things get tougher. Video generation is expensive. I found that most recommendations are for ~5s clips, but I needed 5m of video. The natural solution is to create looping video and repeat it, but current AI systems do not handle that well. A classic strategy is to reverse the video, but I made the early mistake of wanting rain in the video which, unless I want it to rain upwards, rules out that trick. Instead, I need a properly looping video. Again I asked for a prompt and the recommendation was to use terms like "cinemagraphs" and "living photos".  I also decided to try generating a longer video in the hope that I could trim it down to parts which roughly align. It somewhat worked.

# The Result

The final result can be seen below. If the embed doesn't load, you can open the video on YouTube: [YouTube — study music video](https://www.youtube.com/watch?v=FUR0kjld16w).

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
	<iframe src="https://www.youtube.com/embed/FUR0kjld16w" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>
</div>

It's not amazing, but I was pretty happy with the result for just a day's work. The music is particularly good given it was from one of my first few attempts. I've been listening to it on repeat and happily vibing. All together the generation time was around one hour for five minutes of video.

Some takeaways:
- Video is the slowest part: image generation took around 15s per image, audio generation was around one second per second of audio, while video generation took around 15m for a 30s clip, or 5m for a 5s clip. Because the video models are so large and the data size it takes a very long time to load and offload the models as well as process the files.
- Video is also the toughest part: getting the video to loop well and not have any abnormalities was definitely the most time-consuming. You need to watch the entire video and generate many costly samples. I'm guessing this is not the most important part of the user experience for study music, so this could be optimised. Some solutions include using dedicated tools for image to still photos that add very basic effects, or stitching together many shorter clips to fill out the entire video. 
- Creativity is required (sort of): to generate a character I simply used the first prompt from Gemini, but I wasn't super excited by the result. I tried prompting the image generation a few times, but it didn't vary much from the original image, and as I tried to edit the prompt myself I realised creativity is still fairly important in defining the vision. That said, I do think you could prompt an LLM to come up with these creative ideas and again act as more of a reviewer.
- It's scalable! I found the videos on YouTube are typically an hour long. So I would need to run the generation process 12 times to get the full one-hour clip. This would be around half a day of run time. So theoretically you could output one clip per day with just some consumer hardware. This might not be the best content strategy, but it's nice to know it's achievable.

# Conclusion

While I don't think I'll be launching my content empire just yet (the market seems way too saturated), it was a fun project to see what's possible with the current tools. If you haven't tried before and have access to the required compute, I definitely recommend giving it a go.