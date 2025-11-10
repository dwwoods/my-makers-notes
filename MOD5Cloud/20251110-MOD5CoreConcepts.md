# Networking

Date: *10 Nov 2025* 

## Mental Model

[You, the User]
  ↓
Ask the directory → DNS Lookup
  ↓
Get the building's street address → IP Address
  ↓
Pick the correct door on that building → Port (usually 443 for secure web)
  ↓
Agree how deliveries will work → TCP Handshake
  ↓
Switch to sealed, private boxes → TLS Handshake (now it’s HTTPS)
  ↓
Send a note asking for a page → HTTP Request ("GET /")
  ↓
Receive a box of content → HTTP Response (HTML, CSS, JS, etc.)
  ↓
Your browser lays it out nicely → You read the page like a book

## Nomenclature
Core Concepts Recap

| Concept | Internet Meaning | City / Building Analogy | Example |
|---|---|---|---|
| DNS | Converts a domain name into an IP address | Asking the city directory “Where is whatever.co.uk?” | `whatever.co.uk` → `99.83.154.118` |
| IP Address | Numeric address of a server | The building’s street address | `99.83.154.118` |
| Port | Entry point for a particular service on that server | Which door you’re allowed to use (Front door = 443 for secure web) | Port 443 (HTTPS), Port 80 (HTTP) |
| TCP | Guarantees reliable, ordered delivery of data between two machines | The agreed delivery process: “I’ll send numbered boxes, you confirm each, I’ll resend any missing ones” | Makes sure your messages arrive in the right order |
| TLS | Proves identity and encrypts the data in transit | Locked, tamper-proof boxes + ID badge check so you know it’s the real building | Stops attackers reading or altering what you send |
| HTTP | The actual request/response format for web content | The note in the box that says “Please send me /index.html” and the box of documents you get back | `GET /`, `POST /login`, responses like `200 OK` or `404 Not Found` |

## The Journey of a Web Request

Here is a simplified step-by-step journey of what happens when you access a secure website.

```
[You]
  ↓
Ask the directory (DNS)
  ↓
Get the building’s address (IP)
  ↓
Go to a specific door (Port 443)
  ↓
Agree how to send data (TCP)
  ↓
Lock it down and verify identity (TLS)
  ↓
Send your request note (HTTP Request)
  ↓
Get the response box (HTTP Response)
  ↓
[Read the page]
```
