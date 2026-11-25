---
layout: post
title: "Automating a YouTube Study Music Channel: One Month, 23 Videos, and 11 Subscribers"
categories: [AI, Project]
---

A few months ago, I ran a one-month experiment to see if I could build and automate a YouTube study music channel from scratch. The result is [Silver Sounds](https://www.youtube.com/@SilverSoundsStudio). If you want to see what the early output looked like, here is one of the first uploads: [1 Hour of Lofi for Late-Night Coding](https://www.youtube.com/watch?v=v6D3EkctOZs).

{% include youtubePlayer.html id="v6D3EkctOZs" %}

The short version of how it went: I built a fully UI-based, end-to-end content generation platform, published 23 long-form videos, and walked away with 11 subscribers and a few hundred total views. As a growth experiment, it flopped. As an engineering exercise in trying to remove the human from a creative pipeline, it surfaced some genuinely interesting bottlenecks.

## The Strategy and the Numbers

The plan was simple: commit to a one-month trial, publish a few videos per week, and rotate through alternating themes to see what resonated. From a data perspective, the goal was to treat the channel like an optimization problem: test different aesthetics, titles, and musical moods, then double down on whatever pulled in watch time.

The reality hit pretty quickly:

* **23 videos published** over the month
* **11 subscribers** gained
* **Hundreds of views** across the entire catalogue

Study music on YouTube is an absurdly saturated space. You aren't just competing with established 24/7 streams; you are competing with thousands of other people running similar automated pipelines. More importantly for my original plan, the traffic volume was way too small to do any meaningful A/B testing. When a video gets 40 views, you have zero statistical power to tell whether a title, thumbnail, or theme performed better, it's all noise.

## The End-to-End Architecture

Rather than stitching scripts together by hand every few days, I built a fully UI-based end-to-end platform to manage the whole workflow from concept to final render.

One of the more surprising parts of the build was how little boilerplate I actually had to write myself. An AI model was able to implement the entire pipeline end-to-end. My role shifted from writing glue code to reviewing outputs and providing aesthetic feedback, tweaking layouts, rejecting off-vibe themes, and adjusting pacing.

Under the hood, the stack broke down like this:

* **OpenAI API:** Handled ideation such as generating the alternating video themes, mood descriptions, individual song names as well as their bpm, key and scale and the specific instruments.
* **ComfyUI (via API):** Served as the local generation engine for both the music tracks and the background visuals, triggered programmatically via API requests rather than clicking around in the node graph.
* **librosa & NumPy:** Analyzed the generated audio tracks programmatically to flag quality issues before they made it into a final compilation.
* **Pillow:** Generated the visual overlays (tracklists, titles, and framing elements) dynamically for each video.
* **FFmpeg:** Handled the heavy lifting of assembling the final long-form video—concatenating audio tracks, looping the background footage, and compositing the Pillow overlays.

## The Hardest Bottleneck: Local Looping Video

If I had to point to the single most painful technical constraint, it wasn't the audio or the orchestration, it was generating video locally, specifically **looping video**.

Study music videos rely on subtle, seamless background loops (rain on a window, a glowing monitor, drifting clouds). Running local video generation models to produce clean loops requires a massive amount of VRAM and brutal generation times: **10+ minutes just to render a 5-second clip**.

That latency completely changes how you iterate. If a 5-second generation has a weird temporal artifact, a morphing object, or a jarring seam where the loop resets, you just burned 10 minutes of GPU time for a throwaway clip. Scaling that up to multiple alternating themes per week quickly turns your local GPU into a space heater.

On top of this, most AI video generation models create short clips with text to guide them towards some end but the end doesn't have to match a specific frame, or if it does it's a unique frame. If your first frame and last frame are identical then the models can reduce error (e.g. weird artefacts) by just having the video be a static image. This is offset by the model's penalty for matching the text prompt, but in practice I found that most of the time the video generated has only subtle movements or fails altogether. Again leading to wasted compute.


## Trying to Remove the Human from the Loop

The core engineering question I kept coming back to was: *how far can you actually automate audio and video generation before you need a human to step in?*

Current generative audio models are impressive, right up until they aren't. Even when a track starts strong, it can suddenly introduce weird spectral artifacts, metallic distortion, or degenerate into a stuck groove, repeating the exact same bar over and over. If you're stitching dozens of tracks into a 90-minute study mix, listening to every minute manually defeats the point of automation.

Using `librosa` and `NumPy` gets you part of the way there. You can write heuristic checks to catch the obvious failure modes automatically:

* **Repetition detection:** Computing self-similarity matrices or checking autocorrelation to catch tracks that get stuck looping a single phrase.
* **Harmonic hallucination:** Measuring how much the balance between the 12 musical notes (chroma) shifts over time, averaged across all notes to avoid wandering off key.
* **Signal anomalies:** Flagging sudden silence, clipping, harsh high-frequency artifacts, or abrupt energy drops.
* **Loudness normalization:** Ensuring transitions between tracks don't jolt someone out of focus.

That filters out the broken files, but it doesn't solve *taste*. A track can pass every signal-processing check and still sound subtly off or emotionally flat. The same applies to the visuals—an automated pipeline can tell you a video rendered cleanly, not whether the lighting and motion actually feel relaxing.

## Where the Experiment Landed

Looking back at the month, the project ran into two completely separate walls. On the product side, the music still carried enough subtle AI artifacts to make it hard to stand out against human-curated lofi. On the distribution side, the niche is so crowded that without an existing audience or a strong hook, you never even reach the minimum traffic threshold needed to learn from the data.

The irony of the whole experiment is that the exact reason it was so easy to build (AI models can now write the orchestration code and drive ComfyUI pipelines end-to-end) is the exact same reason the market is flooded. Automating the factory is mostly a solved problem; solving for taste and distribution is still the hard part.

All-in-all I was happy with the results and still listen to my music today, there are some real bangers in there.