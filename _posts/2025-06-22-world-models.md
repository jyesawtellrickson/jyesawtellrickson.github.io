---
layout: post
title: Coding World Models with LLMs
categories: [AGI, Tutorial]
---

Recently I ran an experiment in which I tried to get LLMs to output explicit world models in the form of Python code which could be used as the core of a MCTS policy for control in basic gymnasium environments. This is different to typical world model learning which would be something like a parameterised neural network. The reason why we would care about something like this is for on-the-fly reasoning, such as in ARC-AGI-3 where agents must act in a completely new environment.

# Coded World Models with LLMs

The idea behind the approach is that given an LLM's pre-trained knowledge it should be able to accurately model the physics of various simulations, and even better so when fed in example transitions. Overall, the project wasn't very successful, with small models failing to produce reasonable code when it became a little tricky (e.g. calculating angular velocity changes based on translation forces). For example, this is code output by Gemma3:4b (with constants tuned). It introduces the concept of friction which may be unnecessary for a good enough model, but overall has the right idea, utilising trigonometry to calculate changes the velocity, adjusting speed differently based on actions.

```python
def get_next_state(observation: list, action: int) -> list:
    """Returns the next observation given the current observation and action."""
    cart_position, cart_velocity, pole_angle, pole_angular_velocity = observation

    # Constants (tuned for the specific game)
    dt = -3.72e-05 # Time step
    pole_length = 885.53
    gravity = -217921501.39
    friction = 1.60

    # Calculate new cart position and velocity
    new_cart_position = cart_position + cart_velocity * dt

    # Calculate new cart velocity - more robust damping
    new_cart_velocity = cart_velocity + (gravity * math.sin(pole_angle) / pole_length) * dt
    new_cart_velocity = new_cart_velocity * friction

    # Apply action
    if action == 0:  # Push left
        new_cart_velocity -= 0.5
    elif action == 1:  # Push right
        new_cart_velocity += 0.5

    # Calculate new pole angle and angular velocity - improved damping
    new_pole_angle = pole_angle + pole_angular_velocity * dt
    new_pole_angular_velocity = pole_angular_velocity * friction * (1 - abs(new_cart_velocity) / 1.0) # Damp angular velocity

    return [new_cart_position, new_cart_velocity, new_pole_angle, new_pole_angular_velocity]
```

# Graphical Models

It did get me thinking though, as humans, we don't typically come up with detailed world models (at least I couldn't repeat it back) when solving these sorts of tasks. I couldn't tell you what the equation is for the angular velocity of the pole, but I can succeed after just one or two trials at the game. So do I have a model? What is it?

I believe I do have a structured model, and it's something like this:
- Pushing left makes the cart go a little bit left and the pole drifts a bit to the right; and same for the other side.

```python
def get_next_state(observation: list, action: int) -> list:
    """Returns the next observation given the current observation and action."""
    cart_position, cart_velocity, pole_angle, pole_angular_velocity = observation

    dt = 1
    a_bit = 0.1
    a_bit_less = 0.05
    new_cart_velocity = cart_velocity 
    new_pole_angular_velocity = pole_angular_velocity

    if action == 0:
        new_cart_velocity += a_bit
        new_carte_angle -= a_bit_less
    else:
        new_cart_velocity -= a_bit 
        new_carte_angle += a_bit_less

    new_cart_position = cart_position + new_cart_velocity * dt
    new_cart_angle = cart_angle + new_cart_velocity * dt

    return [new_cart_position, new_cart_velocity, new_pole_angle, new_pole_angular_velocity]
```

This leads me to a control policy:
- If pole is falling left, push cart left to counteract; and same for the other side.
- If cart is drifting too far left, let the pole hang to the right for a bit before resuming 1; and same for the other side.

With this model, I'm able to tackle the problem fairly well. It's a simple model, and could be represented by some small control chart. It could be made even simpler if you just want to perform well in the short term: right if angle > 0 else left.

So how can we get an LLM to produce this simplified world model, instead of the more complex world model we saw before? Maybe just through better prompting...I'll be playing around with it, wish me luck!
