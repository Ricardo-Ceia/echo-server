# Simple Multi-threaded Echo Server

## Overview

This project implements a simple multi-threaded echo server based on the functionality described in **[RFC 862 - Echo Protocol](https://datatracker.ietf.org/doc/html/rfc862)**. The server listens for incoming client connections, receives messages, and echoes them back to the clients. Each connection is handled in a separate thread, allowing the server to support multiple clients simultaneously.

### About RFC 862 - Echo Protocol

The Echo Protocol, as defined in RFC 862, is a simple standard for testing and debugging network connections. Clients send data to the server, which then returns the exact same data to the client. This project adheres to the fundamental behavior of the Echo Protocol while adding modern features like multi-threading for concurrent client handling.

---

## Features

- **Multi-threaded**: Handles multiple clients concurrently using threads.
- **Echo Functionality**: Implements the behavior defined in RFC 862 by sending back the same message received from the client.
- **Graceful Connection Management**: Detects and handles client disconnections.
- **Optimized Socket Reuse**: Configured to prevent issues related to the TCP `TIME_WAIT` state.

---

## How It Works

1. The server binds to a specified host (`127.0.0.1`) and port (`65432`).
2. It listens for incoming client connections.
3. For each client:
   - A new thread is created to handle communication.
   - Messages sent by the client are echoed back.
   - Connections are closed when the client sends an empty message.
4. The main server loop continuously accepts and manages new client connections.