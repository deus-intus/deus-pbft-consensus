# 🛡️ Deus PBFT Consensus (`deus-pbft-consensus`)
**Zero-dependency Practical Byzantine Fault Tolerance consensus state machine for local AI agent workforces.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Statutory Status: Public Domain](https://img.shields.io/badge/Statutory%20IP-Expired%20Public%20Domain-brightgreen.svg)](https://patents.google.com/patent/US7149896B2/en)

---

## 🏛️ The Algorithmic Origin: 2004 Math Meets 2026 Agent Governance

Autonomous AI agents executing shell scripts, transferring funds, or writing production code cannot rely on ungrounded single-model outputs. They require **mathematical consensus**.

`deus-pbft-consensus` implements the core state machine from **US Patent 7,149,896 B2** (*"Byzantine fault-tolerant state-machine replication in distributed asynchronous networks"*, filed Oct 27, 2004, expired Oct 27, 2024 by IBM).

It guarantees that high-stakes autonomous actions cannot execute unless a quorum of independent local agent validator nodes ($2f + 1$ out of $3f + 1$) cryptographically verify and sign the proposed action digest.

---

## 🚀 Quickstart

### 1. Installation
Pure standard-library Python. Zero external dependencies.
```bash
pip install -e .
```

### 2. Python Usage
```python
from module import DeusSovereignFabric

# Initialize a 4-node Byzantine consensus fabric (tolerates 1 rogue/hallucinating node)
fabric = DeusSovereignFabric(total_nodes=4)

# Simulate a high-stakes agent proposal
action = "DATABASE_MIGRATION"
target = "PRODUCTION_POSTGRES"
payload = "ALTER TABLE users ADD COLUMN verified_at TIMESTAMP;"

result = fabric.verify_and_execute(action, target, payload)

print(f"Status: {result['status']}")
print(f"Consensus Reached: {result['consensus_reached']}")
print(f"Votes: {result['votes_collected']} / Quorum Required: {result['quorum_required']}")
```

Output:
```
Status: EXECUTED_SOVEREIGN
Consensus Reached: True
Votes: 4 / Quorum Required: 3
```

---

## 💼 Need Enterprise Air-Gapped Multi-Agent Governance?

While `deus-pbft-consensus` is an open-source primitive for multi-agent validation, **Deus Intus Ltd** provides the **Deus SovereignFabric™ Enterprise Edition**:

| Feature | Open-Source (`deus-pbft-consensus`) | SovereignFabric™ Enterprise |
|---|:---:|:---:|
| **Quorum** | In-Memory Simulation | Networked Cross-Device Daemon Quorum |
| **Signing** | SHA-256 Mock Signatures | Hardware Enclave & Ed25519 Threshold Keys |
| **Audit Trail** | Return Dictionary | Immutable Local Merkle Audit Ledger |
| **Model Guard** | Generic Payload String | Real-Time Local Neural Evaluation (Qwen 2.5 / Llama) |
| **Pricing** | **Free / MIT Open Source** | **£25,000 One-Time Perpetual Buyout** |
| **Displacement** | Replaces custom try-except loops | **Eliminates £50,000/yr Copilot Studio + LangSmith** |

👉 **[Explore Sovereign Enterprise Licensing & Case Studies](https://deusintus.co.uk/solutions/sovereign-fabric)**

---

## 📜 License
MIT License. Copyright (c) 2026 Deus Intus Ltd (UK Company No. 17209569).
