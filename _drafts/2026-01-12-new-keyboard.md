---
layout: post
title: A New Keyboard
categories: []
---

We had a big family gathering for Christmas which meant we decided to do a Secret Santa for gifts. I made the bold choice of a new keyboard. I wanted to share my experience so far for two reasons: I'm a big fan of custom setups, 2. it requires a decent amount of work.

The specific keyboard I decided on was a 36-key from YMDK. 36 keys are great because your hands don't need to travel more than one key meaning you can reduce wrist movement and theoretically increase your typing speed. On the other hand, you only have 36 keys. Standard keyboards have roughly 100 keys including a keypad, function and control keys. The difference must be made up somehow and this typically comes through layers.

Layers are commonly implemented in keyboards with fewer keys to increase the number of available keys for the typist. In short, when you hold the activator, typically a key, the result of pressing the other keys changes. For example, upon triggering the numpad activation key, the left side of the keyboard could turn into a numpad.

There are many different layouts available with different layers and key options. The one I decided on was [Miryoku](https://github.com/manna-harbour/miryoku) as it contains a lot of functionality and seemed relatively simple. Things I like about it so far:
- Mouse emulation: one layer allows for mouse control, basically moving the cursor in each direction and clicking functionality. This is quite useful if there are simple actions to take that aren't easy without a mouse and allows you to keep your hands in the same position. 

Of course there are things that I don't like too:
- Tap-Hold: To pack more actions into one keyboard keys can be programmed to have different actions depending on if they are tapped or held. This also introduces delay when you want to use those keys. One example that often gets me is the Shift modifier which sits over "n" for me. I often mistakenly capitalise letters when just trying to enter "n".
- Tenting: my previous keyboard was tented, meaning it had an angle to it. This gives comfort when typing. The new keyboard is completely flat and I can definitely feel the difference. I'd like to put something underneath to get the same effect but I haven't figured out what yet.

# My Woes Begin

While I loved the keyboard I received, there was an issus with the LEDs. When I pressed certain keys, others would light up, and lighting effects that moved by position were not matching up with reality. I asked their customer support, and while the representative tried to be helpful it was clear that the technical team behind them didn't want to spend much time on it. It was up to me to fix it.

I'll start by specifying that I have almost no experience programming keyboards - this was going to be rough. But we have AI assistants now..! With Gemini by my side and the original firmware from the manufacturer I began. My first goal was just to put the existing firmware onto the device. I soon discovered that the keyboard came with the plum bootloader, a feature intended to make it easier to update. However this means that any firmware generated has to account for the space on the chip taken up by the custom bootloader, as well as be in the right format. 

I tried generating the firmware with QMK but the keyboard refused to accept it, likely because the firmware being generated didn't properly account for the unique bootloader. At a loss, I turned to an AI agent to help me fix it. The agent was confident that there was an issue with where the firmware was trying to write onto the keyboard which sounded reasonable. It even went as far as to write a custom script which would make the firmware install it the correct place, confidently asserting it would work. This was a big mistake.

After a few back and forths of the keyboard not responding to the firmware it finally excepted it - hurrah! Except, not. The keyboard stopped responding. Plugging it in? Nothing. It looked like I had bricked it, and indeed consulting with my AI agent didn't make me feel any better with it declaring I'd need some expensive equipment to have a hope at recovering it.

memory allocation groups, wish I knew more about this.
broken bootloader, bricked, not vial

still issues