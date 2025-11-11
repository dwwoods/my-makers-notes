# Common Networking Commands

Date: *10 Nov 2025*

Here are some brief notes on common command-line tools for exploring the networking concepts we've covered.

## `dig` (Domain Information Groper)

Your go-to tool for asking DNS servers questions. It's powerful and provides detailed information.

* **Common Use:** Find the IP address (the `A` record) for a domain.

    ```bash
    # Ask the default DNS server for the IP of example.com
    dig example.com
    ```

## `nslookup`

Another tool for DNS queries. It's simpler than `dig` and is widely available, though sometimes considered less powerful.

* **Common Use:** Quickly find the IP address for a domain.

    ```bash
    nslookup example.com
    ```

## `ping`

A fundamental utility for testing network connectivity. It sends a small packet (an ICMP "echo request") to a target host and waits for a reply, measuring the round-trip time.

* **Common Use:** Check if a remote server is online and measure the latency (delay) to it.

    ```bash
    # Send 4 packets to example.com to see if it's reachable.
    # The -c 4 flag is useful as ping can otherwise run indefinitely on some systems.
    ping -c 4 example.com
    ```

## `curl` (Client for URL)

A versatile tool to transfer data from or to a server using various protocols, most commonly HTTP/HTTPS. It's like a web browser without the graphical interface.

* **Common Use:** Fetch the HTML content of a web page or test an API endpoint.

```bash
    # Get the full HTML of the example.com homepage
    curl https://example.com
    
    # Only get the HTTP headers (useful for checking status codes)
    curl -I https://example.com
```

## `mkcert`

A simple, zero-config tool for making locally-trusted development certificates. This is essential for running a local development server over HTTPS without getting browser privacy warnings.

* **Common Use:** Create a certificate/key pair for a local domain like `localhost`.

```bash
    # 1. Install a local Certificate Authority (CA) in your system's trust stores.
    #    You only need to do this once.
    mkcert -install

    # 2. Generate a certificate for your local server.
    #    This creates two files: localhost-key.pem (private key) and localhost.pem (certificate).
    mkcert localhost
```

## `telnet`

A simple, text-based tool to "talk" to another computer over a network. While old, it's excellent for one specific modern task: checking if a port is open on a server.

* **Common Use:** Test if a web server is listening on the standard HTTPS port (443).

```bash
    # If it connects, the port is open. If it fails, it's closed or firewalled.
    telnet example.com 443
```

## `termshark`

A terminal-based user interface for `tshark` (the command-line version of Wireshark). It's fantastic for inspecting live network traffic directly in your terminal, letting you see the concepts from your notes in action.

* **Common Use:** Watch the TCP/TLS handshake and HTTP requests happen in real-time. This is invaluable for debugging network-level issues.

    ```bash
    # Monitor traffic on a network interface (e.g., en0 on macOS, eth0 on Linux)
    # This usually requires administrator privileges.
    sudo termshark -i en0
    ```

## `route`

This command is used to view and manipulate the IP routing table. The routing table tells your computer which network path to take to send data to a specific destination.

* **Common Use (Viewing):** Display the current routing table to see where traffic is being sent. The command can differ between operating systems.
  * On macOS: `netstat -r`
  * On Linux: `route -n` or `ip route`

* **Common Use (Finding a path):** On macOS and some other systems, you can ask how to get to a specific IP or domain.

```bash
    # Shows which interface and gateway will be used to reach the IP for example.com
    route get example.com
```
