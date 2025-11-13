# Networking & Docker: Key Concepts

This document summarizes the core topics we've discussed, from low-level network packets to high-level application protocols and containerization.

## 1. Network Diagnostics

`ping`: A tool that sends an ICMP "Echo Request" to a host. Used to check if a host is reachable and to measure latency.

`ping 127.0.0.1`: Pings your own computer (the "loopback" address).

`ping -f` (Flood Ping): Sends packets as fast as possible. A form of DoS attack.

Request timeout: Means the host did not reply.

DUP!: Duplicate packets, often a sign of an IP address conflict on the network.

`traceroute`: Maps the "hops" (routers) a packet takes to reach a destination.

How it works: Sends packets with an incrementally increasing TTL (Time To Live). Each router that "expires" the packet sends back a message.

`traceroute -n -q 1`: A faster trace that disables DNS lookups (-n) and sends only one query (-q 1) per hop.

Pinging "Cool" Things: You can't ping the ISS (it's not on the public internet), but you can ping anycast addresses like 8.8.8.8 (Google DNS), which routes you to the geographically closest server.

## 2. The TCP/IP Protocol Stack

This model explains how data is packaged and sent. The key is encapsulation: each layer wraps the data from the layer above it.

### Layer 5: Application

Protocols: HTTP, SMTP (Email), DNS.

Data Unit: Data/Message.

### Layer 4: Transport

Protocols: TCP & UDP.

Data Unit: Segment (TCP) or Datagram (UDP).

### Layer 3: Network

Protocol: IP (Internet Protocol).

Data Unit: Packet. Responsible for routing with IP addresses.

### Layer 2: Data Link

Protocol: Ethernet, Wi-Fi.

Data Unit: Frame. Responsible for local delivery with MAC addresses.

### Layer 1: Physical

Protocol: Cables, radio waves.

Data Unit: Bits.

## 3. Core Protocols: TCP vs. UDP

Feature

TCP (Transmission Control Protocol)

UDP (User Datagram Protocol)

Analogy

A phone call

A postcard

Connection

Connection-oriented. A 3-way handshake (SYN, SYN-ACK, ACK) is required to start.

Connectionless. Just sends data.

Reliability

Reliable. Guarantees packets arrive in order and re-sends lost packets (using ACKs and sequence numbers).

Unreliable. "Fire and forget." No guarantee of delivery or order.

Use Cases

Web (HTTP), Email (SMTP), File Transfer (FTP)

Video Streaming, Online Gaming, DNS, VoIP

Collisions

On Wi-Fi, if two packets are sent at once, they collide and are lost. Wi-Fi uses CSMA/CA (Collision Avoidance) to "listen" before speaking.

## 4. Application Protocols & Security

HTTP (Hypertext Transfer Protocol)

1.0: One request per connection. Very slow.

1.1: Introduced "Keep-Alive" (persistent connections), but suffered from "Head-of-Line Blocking."

2.0: Introduced multiplexing, allowing multiple requests/responses at the same time over one connection.

`BGP` (Border Gateway Protocol): The "GPS of the internet." It manages routing between large, independent networks (Autonomous Systems).

`DNS` (Domain Name System): The "phone book" of the internet.

`A`: Maps a name to an IPv4 address.

`AAAA`: Maps a name to an IPv6 address (solves IPv4 exhaustion).

`CNAME`: An alias. Points one name to another (e.g., www.blog.com -> blog.github.io).

`MX`: Mail Exchanger. Directs a domain's email to a specific mail server.

`TXT`: Arbitrary text. Used for domain verification (SPF, DMARC) to prevent email spoofing.

`dig` / nslookup: Tools that generate UDP packets (on port 53) to send DNS queries.

Encrypted DNS: DoH (DNS over HTTPS) and DoT (DNS over TLS) encrypt your DNS queries so your ISP cannot see what sites you are visiting.

`TLS` (Transport Layer Security): The 'S' in HTTPS. It encrypts your HTTP traffic.

Man-in-the-Middle (MITM) Attack: An attacker intercepts your connection and sends a fake certificate. Your browser stops this by checking the Certificate Authority (CA). If the cert isn't signed by a trusted CA (like Let's Encrypt), you get a security warning.

__Private Key: NEVER be shared. It's your ultimate digital secret.__

## 5. `SSH` (Secure Shell)

What it is: `SSH` is not just a shell. It's a secure, multiplexing transport protocol.

How it works: It authenticates a user and then runs a single forced command, securely piping stdin, stdout, and stderr.

The "shell" you get is just the default command: /bin/bash.

The server can be configured to force any command, like git-receive-pack (for git push) or interactive apps like ssh-chat.com or ssh starwarstel.net.

Port Forwarding:

-R (Remote): Exposes a localhost port to a remote server (e.g., to demo a local website).

-D (Dynamic): Creates a SOCKS proxy, effectively a personal VPN.

Learning More: OverTheWire: Bandit is a wargame played entirely over SSH that teaches you how to master the Linux command line.

## 6. Docker (Containers)

Why use it?: Solves the "it works on my machine" problem by packaging an application with all its dependencies (libraries, OS, etc.).

`docker run -d`: Runs a container in detached (background) mode.

`docker stop [id]`: Stops a running container.

Persistence: A container's filesystem is ephemeral (temporary).

Volumes: The correct way to save data (like a database). The volume is managed by Docker and can be attached to new containers.

Bind Mounts (-v ...): Maps a host folder directly into a container (good for dev).

Dev Containers: A VS Code feature that uses a Docker container as your full, consistent, and shareable development environment.