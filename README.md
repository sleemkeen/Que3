# DBS Admission Application System

## CA_ONE – Part II: Programming in Python (Question 3)

A TCP-based client-server application for managing student admission applications at DBS.

---


### Protocol
- **Connection-Oriented Protocol (TCP)** - Ensures reliable data transmission between client and server
- Host: `127.0.0.1` (localhost)
- Port: `5200`

### Database
- **SQLite** - A disk-persistent relational database
- Database file: `applications.db`
- Stores all application records with unique registration IDs

### Data Format
- JSON serialization for data transmission between client and server

---

## Project Structure

```
Que3/
├── server.py      # TCP server that handles incoming applications
├── client.py      # Console-based client for applicant input
├── database.py    # SQLite database operations
├── applications.db # Database file (auto-generated)
└── README.md      # This file
```
