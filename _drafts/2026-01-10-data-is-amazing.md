---
layout: post
title: The Hidden Power of Magnetic Data
categories: [Data]
---

If you've worked in data science for AI a while, you've probably seen a lot of standard business data (login, view, click, purchase, etc.), and got sick of training vision models on slightly different images, fine-tuning a LLM to spit out just the right text.

Is that it, you ask? Far from it! There are loads of other interesting data formats and problems that are slightly outside the 'everyday' use. To become more acquainted with the different sources I wanted to start a series on interesting data where I explore these in detail.

In this article let's look into magnetic data.

# What Does the Data Actually Look Like?

At its core, magnetic data is typically a three-dimensional time series. Most sensors (magnetometers) provide readings for the $X, Y,$ and $Z$ axes, representing the magnetic flux density at a specific point in space. These can also be considered as a 3d vector. These sensors are often mobile: embedded in a smartphone, a drone, or a wearable so the data is frequently treated as spatial measurements. From a physics standpoint, we can consider this as mapping out a dynamic 3D vector field. Note that due to the direction of the signal affecting measurement, the orientation of the sensor also impacts the measurement, the same location with the same magnetic field would yield different results depending on the orientation.

# The Physics: Measuring the Unseen

To model magnetic data, you have to understand the "noise" you’re swimming in.
- The Earth’s Baseline: The Earth has a consistent but weak magnetic field (roughly $25$ to $65\,\mu\text{T}$). This is acts as a "Global Constant" that you can measure wherever you go - it's what powers compasses and similar navigation systems.
- The Disturbers: Any ferromagnetic object (like the rebar in a concrete floor or a passing car) warps this field. These objects have magnetic permeability, meaning the field prefers to flow through them rather than the air. There are also many magnetic sources in the urban environment. The small magnet in a phone is around 1000 times stronger than the Earth's magnetic field.
- The Inverse Cube Law: Unlike light, which drops off at $1/r^2$, the magnetic field of a dipole (like an iron bar) drops off at $1/r^3$. This means the signal disappears fast. An iron bar might be twice as strong as the Earth's field at its surface, but move just a few centimeters away, and it's already lost in the background noise.

This is one of the key dificulties: how can you map the environment when there are so many noisy signals which also vary significantly. 

# Sensor Sensitivity: From Digital Silence to "Screaming"

The hardware you choose determines your "visibility":
- Consumer MEMS (Smartphone): Resolution of $\approx 0.15\,\mu\text{T}$. If a signal is smaller than that, it’s "digital silence."
- Scientific Fluxgate Magnetometer: Can detect signals down to $0.001\,\text{nT}$. At this level, a steel ship a hundred meters away is "screamingly loud."

ObjectDetectable Distance (Standard Sensor)Iron Rebar$\approx 20\text{--}30\,\text{cm}$A Car$\approx 2\text{--}5\,\text{meters}$A Steel Ship$\approx 50\text{--}100\,\text{meters}$Submerged Pipeline$\approx 5\text{--}10\,\text{meters}$How We Capture It: Hall Effect vs. AMRMost modern AI applications use tiny MEMS (Micro-Electro-Mechanical Systems). 

There are two dominant ways to think about these:
1. The Hall Effect (The "Pushed Water" Analog): Imagine a river (electrical current) flowing through a channel. When a wind (magnetic field) blows perpendicular to the river, it pushes the water up against one bank. By measuring the "pushed water" (the Hall Voltage), we can calculate the strength of the wind. Hall sensors are generally non-magnetic themselves.
2. Anisotropic Magnetoresistive (AMR) (The "Hiker" Analog): Imagine hikers traveling along a trail with a specific grain. An external magnetic field is like a force that twists the entire landscape, rotating that grain. The hikers now have to change their gait to walk against the new pattern, which changes the difficulty of the journey (the resistance).

# Why is this an AI Problem?

Magnetic data is notoriously difficult for "vanilla" models. A CNN might struggle because features appear and disappear abruptly based on tiny changes in distance. Furthermore, the same location can have completely different readings depending on the sensor's orientation.

The "Synthetic Aperture" Solution:
A single stationary sensor is almost useless for mapping. However, by moving the sensor, you create a synthetic aperture. As you move a known distance (tracked via an accelerometer), the AI can fit the curve of the signal's decay. If the signal doubles when you move $10\,\text{cm}$, the $1/r^3$ math allows the model to solve for the exact distance to the source.

Physics-Informed Neural Networks (PINNs):
This is where magnetic AI shines. Instead of letting a model guess wildly, we incorporate physical constraints (like the Magnetic Dipole Model) directly into the loss function. This ensures the model never predicts a "physically impossible" magnetic flux.

# The Frontiers: Research & Startup Ideas
Where can we actually use this?
- GPS-Denied Navigation: The Earth’s crust has a unique "magnetic fingerprint." AI can use these sequences to navigate indoors or underwater where GPS can't reach.
- Wearable Interaction: Imagine a smart glove that tracks your finger movements relative to a tiny magnetic puck on your wrist—allowing you to "type" on any surface or even in the air.
- Food Spoilage Detection: Research is looking into chemical markers that react with "bad gas" from spoiling food, which in turn produces a measurable change in a magnetic field.
- The "Blind" Spotter: Unlike Lidar or Cameras, magnetic fields don't care about smoke, darkness, or physical walls. It's the ultimate tool for detecting "hidden" objects, from buried explosives to a car hidden behind a truck in an autonomous driving "occlusion" scenario.

# Final Thoughts
Magnetic data takes us out of the clean, digital world and back into the "fuzz" of reality. It requires a blend of signal processing, spatial reasoning, and deep learning. But for those willing to deal with the $1/r^3$ drop-off and the noise of solar storms, it offers a way to see where every other sensor is blind.







- what is the physics behind the data generation
ferromagents- the earth's magnetic field induces magnetism in ferromagnetic objects by aligning their domains (dipoles?)
magnetic permeability - magnetic feilds want to pass through line of least resistance and will flow towards oferromagnetic objects
iron bar measured at 2 to 1 times stronger than the earths field at the surface but drops off at r^3 (magnetic feed of a dipole) so at just a few cm it would be less than the earths field
Consumer MEMS (Smartphone): Most phone magnetometers have a resolution of about $0.15\,\mu\text{T}$ to $0.6\,\mu\text{T}$. A $0.01\,\mu\text{T}$ change is literally smaller than the "steps" the sensor can measure. It’s "digital silence."Scientific Fluxgate Magnetometer: These can detect signals down to $0.001\,\text{nT}$. For these sensors, an iron bar a meter away is "screamingly loud."
The Environment: Even with a great sensor, the Earth’s field isn't perfectly still. "Magnetic noise" from power lines, distant cars, and even solar activity creates a background "fuzz" of about $0.05\,\mu\text{T}$. If your iron bar's signal is smaller than that fuzz, you can't see it without advanced signal processing.
ObjectDetectable Distance (Standard Sensor)Iron Rebar (single)$\approx 20\text{--}30\,\text{cm}$A Car$\approx 2\text{--}5\,\text{meters}$A Steel Ship$\approx 50\text{--}100\,\text{meters}$Submerged Pipeline$\approx 5\text{--}10\,\text{meters}$


SourceTypical StrengthImpact on SensorEarth’s Field$50\,\mu\text{T}$The "Global Constant."Iron Bar (Induced)$10\text{--}100\,\mu\text{T}$ (Disturbance)A "Soft Iron" warp; changes the local shape of the field.Small Fridge Magnet$5,000\text{--}10,000\,\mu\text{T}$A "Hard Iron" source; totally overwhelms the Earth's signal.MRI Machine$1,500,000\text{--}3,000,000\,\mu\text{T}$Destroys the sensor (and anything else nearby).

- what tools to collect the data
Most modern devices (like your smartphone or a drone) use Hall Effect sensors or Magnetoresistive sensors. These are tiny MEMS (Micro-Electro-Mechanical Systems) that detect how a magnetic field affects the flow of electricity through a conductor.
Anisotropic Magnetoresistive
hall sensor
Current Flow: A constant electrical current ($I$) is forced to flow through a thin slab of conductive or semiconductive material (the "Hall element").Magnetic Interaction: An external magnetic field ($B$) is introduced. Critically, this $B$ field must be perpendicular to the plane of the current flow.Charge Deflection: The Lorentz Force ($F = q\mathbf{v} \times \mathbf{B}$) acts on the moving charge carriers (electrons or holes). It pushes them to one side of the slab.Voltage Generation: This creates an accumulation of charge on one edge and a depletion on the other. This separation of charge generates a tiny, measurable electric field and potential difference: the Hall Voltage ($V_H$).
The Lorentz force acts on a conductor, moving electrons to one side of a conductor creating a voltage which is directly proportional to the magnetic field in the direction of the sensor
hall is nonmagnetic, AM is magnetic
Permalloy
Hall Analog (Force): A river is flowing (current). A constant wind starts blowing perpendicular to the river (external magnetic field). The wind physically pushes the water up onto one bank. We measure that "pushed water" (the Hall voltage).

AMR Analog (Interaction): A group of hikers (the current) is traveling along a trail. The trail has a defined "grain" or "pattern" (the initial magnetization of the Permalloy). An external magnetic field is like a massive force that comes along and twists the entire landscape, rotating that grain. The hikers now have to change how they step to walk with or against the new rotated pattern, which changes the difficulty of their journey (the resistance).


- challenges
same location can have different readings depending on irientation
solar storms
signal to noise ratios
AI models (especially CNNs) struggle with features that appear and disappear so abruptly based on tiny changes in distance.
dynamic environments ega a car driving past in the distance

- what are the applications / interesting papers
gps deficient environments navigation, earth has a consistent crustal mpa that can be used for nav
indoor fingerprinting
detection: find buried items (explosvies), submarines
space weather forecasting
wearable magnometers to detect human speech
heartbeat fingerrinting with recise sensors
control interfaces with magentic pucks
smart magnetic clothing that measures changes in magnetic fields as singals for eg device control
food spoilage: chemical reacts with bad gas which produces a new magnetic field that can be measured

strengths:
- see where others are blind; e.g indoors vs gps, without light vs cameras, without line of sight vs Lidar, no air vs ultrasonic
- eg hidden in objects to see surrounding objects
- also good in harsh / messy environments
- microscopic sensors, built on chips, smaller than a grain of rice, track position inside a robot finger or in medical instruments
- low power sensing: can stay online for years from a single coin-cell battery
- high speed - high resolution data up to 1MHz, e.g. a motor spinning at high rpm in inudstrial machinery




ideas:
gloves for typing in air. type like im on my keyboard
vehicle crash detection e.g when reversing
driverless cars dealing with occlusion - a car on the other side of the neighbouring truck
auto bike helmet
iot
near-distance sensing




- what models can be applied
spatial (mapping/detection)
- time frequency data, spatial grids (anomaly detection, velocity prediction)
temporal (tracking/telemetry)
physical (material properties/core loss)
physics based models PINNs since magnets follow strict laws
- How they work: Unlike standard NNs, PINNs incorporate physical constraints (like the Magnetic Dipole Model or the Steinmetz Equation) directly into the loss function. This ensures the model doesn't predict "physically impossible" magnetic flux.

cnn for spatial data
LSTMs, RNNs, transformers for sequence data since its a timeseries

1. The "Synthetic Aperture" (Movement as a Sensor)A single stationary sensor is almost useless for mapping. However, a single moving sensor creates a "synthetic aperture."The Logic: As you move, the magnetic field doesn't just change intensity; it changes gradient.The Math: Magnetic fields from dipoles (like most magnets) decay at a rate of $1/r^3$.AI Application: By moving the device a known distance (using an accelerometer/IMU for scale), an AI model can fit the curve of the signal's decay. If the signal doubles when you move 10cm, the math only allows for one specific distance-to-source solution. This resolves the ambiguity by turning a 1D data point into a 4D trajectory.2. Magnetic Gradient Tensor (MGT) SensingInstead of one single Hall Effect sensor, modern "single-device" solutions often use a Tensor Array—four or more micro-sensors (like TMRs) spaced just millimeters apart on a single PCB.The Innovation: This allows the device to measure the Spatial Gradient ($\nabla B$) instantly.Why it works: The intensity might be the same for a far/strong source and a near/weak source, but the gradient (how fast the field changes from the left side of the chip to the right) is vastly higher for a nearby object.Research Goal: High-resolution tensor sensing allows an AI to determine the "vector direction" and "proximity" simultaneously, effectively giving the sensor "depth perception."3. Using "Priors" (Th


Accurate Indoor Localization Using Magnetic Sequence Fingerprints with Deep Learning
https://link.springer.com/content/pdf/10.1007/978-3-030-95384-3_5.pdf



