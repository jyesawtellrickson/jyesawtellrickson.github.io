---
layout: post
title: "Magnetic Data: Measuring the Unseen"
categories: []
---

If you've worked in data science for AI a while, you've probably seen a lot of standard business data (login, view, click, purchase, etc.), and got sick of training vision models on slightly different images, or fine-tuning an LLM to spit out just the right text.

Is that it, you ask? Far from it! There are loads of other interesting data formats and problems that are slightly outside the 'everyday' use. To become more acquainted with the different sources, I wanted to start a series on interesting data where I explore these in detail.

In this article, let's look into magnetic data.

# What Does the Data Actually Look Like?

At its core, magnetic data is typically a three-dimensional time series. Most sensors (magnetometers) provide readings for the X, Y, and Z axes, representing the magnetic flux density at a specific point in space. Because these sensors are often mobile—embedded in your smartphone, a drone, or a wearable—the data is frequently treated as spatial measurements. You aren't just measuring a signal over time; you are mapping a 3D vector field as you move through it. Using other measurement devices alongside them, you can generally map these readings back to real-world coordinates.

# The Physics: Measuring the Unseen

To model magnetic data, you have to understand the "noise" you’re swimming in. A magnetic field is defined by both its strength and direction.

*   **The Earth’s Baseline:** The Earth has a consistent but weak magnetic field (roughly **25 µT** to **65 µT**). This is your "Global Constant." The Earth's field naturally induces magnetism in ferromagnetic objects by aligning their domains.
*   **The Disturbers:** Any ferromagnetic object (like the rebar in a concrete floor or a passing car) warps this field. These objects have magnetic permeability, meaning the magnetic fields prefer to flow through them as the line of least resistance, rather than through the air.
*   **The Inverse Cube Law:** Unlike light, which drops off at $1/r^2$, the magnetic field of a dipole (like an iron bar) drops off at $1/r^3$. This means the signal disappears incredibly fast. An iron bar might be measured at twice as strong as the Earth's field at its surface, but move just a few centimeters away, and it's already lost in the background noise.

# Sensor Sensitivity: From Digital Silence to "Screaming"

The hardware you choose determines your "visibility". The environment itself is noisy; even with a great sensor, the Earth’s field isn't perfectly still. "Magnetic noise" from power lines, distant cars, and solar activity creates a background "fuzz" of about **0.05 µT**. If your signal is smaller than that fuzz, you can't see it without advanced signal processing. 

*   **Consumer MEMS (Smartphone):** Most phone magnetometers have a resolution of about **0.15 µT** to **0.6 µT**. A **0.01 µT** change is literally smaller than the "steps" the sensor can measure. It’s digital silence.
*   **Scientific Fluxgate Magnetometer:** These can detect signals down to **0.001 nT**. For these sensors, an iron bar a meter away or a steel ship a hundred meters away is screamingly loud.

### Object Detectable Distances (Standard Sensor)

So how far can we measure objects away? The table below shows some estimates I found online. While I'm not aware of any nearby pipelines or steel ships, I was able to successfuly measure cars passing me when standing on the side of the road using the phyphox app. No sound, no audio, no physical sensor, just the invisible magnetic force giving the position away - very cool!

| Object | Detectable Distance |
| :--- | :--- |
| **Iron Rebar (single)** | **20-30 cm** |
| **A Car** | **2-5 meters** |
| **Submerged Pipeline** | **5-10 meters** |
| **A Steel Ship** | **50-100 meters** |

### Typical Strengths and Impacts

For reference, the table below describes some of the expected magnetic force from objects at different magnitudes. The key thing to note is that most ferromagnetic objects and of course magnetics should be measurable with just a smartphone.

| Source | Typical Strength | Impact on Sensor |
| :--- | :--- | :--- |
| **Earth’s Field** | **50 µT** | The "Global Constant." |
| **Iron Bar (Induced)** | **10-100 µT** | A "Soft Iron" warp; changes the local shape of the field. |
| **Small Fridge Magnet** | **5,000-10,000 µT** | A "Hard Iron" source; totally overwhelms the Earth's signal. |
| **MRI Machine** | **1,500,000-3,000,000 µT** | Destroys the sensor (and anything else nearby). |

## How We Capture It: Hall Effect vs. AMR

Most modern AI applications use tiny MEMS (Micro-Electro-Mechanical Systems) built on chips. They can be smaller than a grain of rice, run for years on a single coin-cell battery, and provide high-resolution data at high speeds (up to **1 MHz**). There are two dominant ways to think about these:

1.  **The Hall Effect (The "Pushed Water" Analog):** A constant electrical current is forced to flow through a conductive slab. When an external magnetic field is introduced perpendicular to the plane of the flow, the Lorentz Force ($F = q\mathbf{v} \times \mathbf{B}$) acts on the moving charge carriers. 
    > Imagine a river (electrical current) flowing through a channel. When a wind (magnetic field) blows perpendicular to the river, it physically pushes the water up against one bank. By measuring the "pushed water" (the Hall Voltage), we can calculate the strength of the wind. Hall sensors are generally non-magnetic themselves.
2.  **Anisotropic Magnetoresistive (AMR) (The "Hiker" Analog):** Uses magnetic materials like Permalloy. 
    > Imagine a group of hikers (the current) traveling along a trail with a defined grain. An external magnetic field is like a massive force that twists the entire landscape, rotating that grain. The hikers now have to change their gait to walk against the new rotated pattern, which changes the difficulty of their journey (the resistance).

# Why is this an AI Problem?

Magnetic data is notoriously difficult for "vanilla" models. A CNN might struggle because features appear and disappear abruptly based on tiny changes in distance. Furthermore, the exact same location can have completely different readings depending on the sensor's orientation, and dynamic environments (like a car driving past in the distance) constantly shift the baseline. 

So how do we apply AI?

*   **The "Synthetic Aperture" Solution:** A single stationary sensor is almost useless for mapping. However, by moving the sensor, you create a synthetic aperture. As you move, the magnetic field doesn't just change intensity; it changes gradient. By tracking movement via an accelerometer, an AI model can fit the curve of the signal's decay. Since we know dipoles decay at $1/r^3$, if the signal doubles when you move **10 cm**, the math allows the model to solve for the exact distance to the source, turning a 1D data point into a 4D trajectory.
*   **Magnetic Gradient Tensor (MGT) Sensing:** Instead of one Hall Effect sensor, modern solutions use a Tensor Array—four or more micro-sensors spaced millimeters apart. This instantly measures the Spatial Gradient ($\nabla B$). While intensity might be ambiguous, the gradient across the chip is vastly higher for a nearby object, effectively giving the AI "depth perception."
*   **Physics-Informed Neural Networks (PINNs):** Since magnets follow strict physical laws, PINNs shine here. We incorporate physical constraints (like the Magnetic Dipole Model or Steinmetz Equation) directly into the loss function, ensuring the model never predicts a physically impossible magnetic flux.
*   **Standard Architectures:** For spatial mapping and anomaly detection, CNNs can process spatial grids. Since the data is fundamentally a time-series, LSTMs, RNNs, and Transformers are perfectly suited for tracking and telemetry.

# The Frontiers: Research & Startup Ideas

Where can we actually use this? The greatest strength of magnetic fields is that they see where others are blind. They operate perfectly indoors, without light, without line of sight, and even without air (unlike ultrasonic sensors). 

*   **GPS-Denied Navigation:** The Earth’s crust has a unique, consistent magnetic fingerprint. AI can use these sequences to navigate indoors or underwater where GPS can't reach. Excellent research like *Accurate Indoor Localization Using Magnetic Sequence Fingerprints with Deep Learning* is already paving the way here.
*   **Wearable Interaction & IoT:** Imagine a smart glove or magnetic clothing that tracks your finger movements relative to a tiny magnetic puck on your wrist—allowing you to type in the air as if on a keyboard. Precise sensors can even be used for heartbeat fingerprinting or detecting human speech.
*   **Automotive & Autonomous Driving:** It's the ultimate tool for near-distance sensing and vehicle crash detection. It can help driverless cars deal with occlusion, like detecting a hidden car on the other side of a neighboring truck.
*   **Detection in Harsh Environments:** Finding hidden objects, buried explosives, or submerged pipelines in environments where cameras and Lidar instantly fail.
*   **Food Spoilage Detection:** Emerging research is looking into chemical markers that react with "bad gas" from spoiling food, producing a measurable new magnetic field that a sensor can pick up.

# Final Thoughts

Magnetic data takes us out of the clean, digital world and back into the "fuzz" of reality. It requires a heavy blend of signal processing, spatial reasoning, and deep learning. But for those of us willing to deal with the $1/r^3$ drop-off, the dynamic environments, and the noise of solar storms, it offers a fascinating way to see what every other sensor is blind to.