# Cowrie-Honeypot-Log-Analyser


A Python-based tool to parse and analyze Cowrie honeypot logs, designed to extract SSH brute-force attempts, attacker credentials, source IPs, and commands used — aiding blue teamers in understanding and responding to malicious behavior.

---

##  Features

- Parses Cowrie's structured JSON logs (`cowrie.json`)
- Detects:
  - Successful and failed login attempts
  - Brute-force attack patterns
  - Source IPs and credentials used
  - Attacker-issued commands
- Generates readable summaries for incident analysis
- Optional integration with IP reputation services (e.g., AbuseIPDB, IPInfo)

---

##  Tech Stack

- Python 3
- Libraries: `json`, `datetime`, `collections`, `requests` *(optional)*

---


