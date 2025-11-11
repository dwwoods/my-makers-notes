---
title: The Keys to the Kingdom
sub_title: A Journey through SSH
author: David Woods
---

<!-- end_slide -->

# There is no Cloud.

<!-- pause -->

<!-- end_slide -->

<!-- column_layout: [1, 1] -->

<!-- column: 0 -->

# TELNET: The Open Window

```
> login: admin
> password: hunter2

[EVERYTHING IS VISIBLE]
```

<!-- column: 1 -->

## The Danger

* Plain text transmission
* Passwords visible to anyone
* Wireshark can read everything
* Like sending postcards with secrets

<!-- pause -->

**We needed a tunnel.**

<!-- end_slide -->

# SSH: The Secure Shell

```
[YOUR COMPUTER] ════╗
                    ║ 🔐 ENCRYPTED
     🔐 TUNNEL 🔐   ║ 🔐 SECURE
                    ║ 🔐 PRIVATE
[REMOTE SERVER] ════╝
```

<!-- pause -->

**The backbone of the modern internet**

<!-- end_slide -->

<!-- column_layout: [1, 1] -->

<!-- column: 0 -->

# The Magic: Star Wars

```ascii
    .    .
      *     .      *
  .      _-====-_      .
       .-'  *  '-.
      /    * *    \
     |   *     *   |
      \  EPISODE  /
       '-.  IV  .-'
          '-=-'
```

<!-- column: 1 -->

## Pure Text, Pure Magic

Press `Ctrl+E` to run:

```bash +exec
open -a Terminal "ssh://starwarstel.net"
```

<!-- pause -->

* Not a video file
* Pure text stream
* From someone-elses computer to you
* Character by character
* **The terminal is a canvas**

<!-- end_slide -->


<!-- column_layout: [1, 1] -->

<!-- column: 0 -->

# SSHTron: Multiplayer Combat

```
┌─────────────────────┐
│ ╔═══                │
│ ║                ╗  │
│ ║                ║  │
│ ║    ╔═══╗       ║  │
│ ╚════╝   ╚═══════╝  │
└─────────────────────┘
```



Press `Ctrl+E` to run:


```bash +exec
open -a Terminal "ssh://sshtron.zachlatta.com"
```
<!-- column: 1 -->
```bash
#to play along at home
ssh sshtron.zachlatta.com
```
<!-- pause -->
**What's happening?**
1. Keystroke → Encrypted tunnel → Server
2. Server processes move
3. Server sends new map → Your terminal draws it
4. **All in milliseconds.**

<!-- end_slide -->



<!-- jump_to_middle -->

# Would you like to know more?

```
     .--.      .--.
    /  " /      \ "  \
   |   /'.--./'.\   |
   |  | ( '.' ) |  |
   |  \  '---'  /  |
    \  '._____.'  /
     '-._______.-'
    FEDERAL NETWORK
```



<!-- end_slide -->

<!-- column_layout: [1, 1] -->

<!-- column: 0 -->

# The Challenge

```
    ___
   /   \
  | O_O |   BANDIT
  |  >  |   Level 0 → ???
   \___/
  /|   |\
 / |   | \
```

<!-- column: 1 -->

## Take the Keys

**overthewire.org/wargames/bandit**

<!-- pause -->

* Start at Level 0
* Use SSH to log in
* Find files, decode strings
* Learn other peoples computers, security, and the real internet

<!-- pause -->

**Don't just be a user of the cloud.**

**Take the keys. Open the shell. Control the machine.**

<!-- end_slide -->


# Quick Reference

```bash
# Star Wars in ASCII
ssh starwarstel.net

# Multiplayer Tron
ssh sshtron.zachlatta.com

# Bandit Level 0
ssh bandit0@bandit.labs.overthewire.org -p 2220
# Password: bandit0
```

<!-- pause -->

## Thank you.

**Questions?**

<!-- end_slide -->

<!-- jump_to_middle -->

# Speaker Notes

*Use arrow keys to navigate*

<!-- end_slide -->

## Slide 1: The Hook (0:00-0:45)

**Opening:**
"I want to let you in on a secret that marketing departments hate."

**The Reveal:** [Pause] "There is no 'Cloud.'"

**The Truth:** "There is only... other people's computers."

**Context:** When you connect to the internet, you aren't floating in the ether. You are physically connecting a wire from your machine to a server in a basement in Virginia, or a warehouse in Dublin.

**Core idea:** The internet, at its core, is just a conversation.

**Transition:** But for a long time, that conversation was dangerous.

<!-- end_slide -->


## Slide 2: The Danger (0:45-1:30)

**History:** In the beginning, we had Telnet.

**Simplicity:** Telnet was simple. It allowed me to type commands here, and have them run over there.

**The catch:** But there was a catch. Telnet is polite. Too polite. It shouts everything across the room.

**Vulnerability:** If I typed my password, Telnet sent it as plain text.

**The threat:** If a hacker was sitting between us using a tool like Wireshark (or "Telshark" for the veterans), they could see everything.

**Consequences:** They could read my emails, steal my passwords, and take my server. It was like sending your bank details on the back of a postcard.

**Transition:** We needed a tunnel. We needed privacy.

<!-- end_slide -->


## Slide 3: The Solution (1:30-2:15)

**Introduction:** Enter SSH. Secure Shell.

**Importance:** This is the backbone of the modern internet.

**Mechanism:** SSH takes that open conversation and wraps it in impenetrable math. It uses Encryption.

**Key concept:** I have a key (a private key), and the server has a lock (a public key).

**Handshake:** When they meet, they shake hands, verify each other, and build a tunnel.

**Capability:** Inside that tunnel? I can do anything.

**Examples:** I can fix a database crash in Tokyo while sitting in my pajamas in London. I can move files. I can run updates.

**Transition:** But... I can also do things that are infinitely cooler.

<!-- end_slide -->

## Slide 4: The Magic (2:15-3:00)

**Creative use:** Because SSH is just a stream of text, we can manipulate that text to create art.

**History lesson:** If you open your terminal right now and type: `ssh towel.blinkenlights.nl`

**Surprise:** You don't get a command prompt. You get A New Hope.

**[Gesture to screen]** where ASCII Star Wars is playing

**Technical detail:** This isn't a video file. This is pure text, streamed securely from a server in the Netherlands to your machine, character by character.

**Philosophy:** It proves that the terminal isn't just for work. 

<!-- end_slide -->


## Slide 5: The Demo (3:00-4:00)

**Interaction:** But watching a movie is passive. SSH is interactive. So, let's play a game.

**[Live demo]** Type: `ssh sshtron.zachlatta.com`

**Introduction:** This is SSHTron.

**Explanation:** I am running a multiplayer game on someone else's computer, rendering the graphics locally on mine using nothing but text colors.

**[Play for 10 seconds]** - ideally crash into a wall

**Technical breakdown:** What is happening here?
- My computer sends a keystroke (Turn Left)
- It travels encrypted through the internet tunnel
- The server processes the move
- The server sends back the new map
- My terminal draws it

**Performance:** All in milliseconds. No graphics card required. Just pure connection.

<!-- end_slide -->


## Slide 6: The Challenge (4:00-5:00)

**Recap:** So, you know the history. You've seen the fun.

**The question:** Now, how do you get the power? How do you learn to control these "other people's computers" securely?

**The challenge:** I want to leave you with a challenge. It's called Bandit.

**Description:** It is a wargame hosted by OverTheWire.

**Mechanism:** You start at Level 0. You use SSH to log in.

**Progression:**
- To get the password for Level 1, you have to find a specific file
- To get to Level 2, you have to decode a string

**Learning:** It teaches you Linux. It teaches you security. It teaches you how the internet actually works.

**Closing:** Don't just be a user of the cloud. Take the keys. Open the shell. And control the machine.

**Finale:** Thank you.

<!-- end_slide -->