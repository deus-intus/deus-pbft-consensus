<div align="center">

```
  ____  _____ _   _ ____    ___ _   _ _____ _   _ ____  
 |  _ \| ____| | | / ___|  |_ _| \ | |_   _| | | / ___| 
 | | | |  _| | | | \___ \   | ||  \| | | | | | | \___ \ 
 | |_| | |___| |_| |___) |  | || |\  | | | | |_| |___) |
 |____/|_____|\___/|____/  |___|_| \_| |_|  \___/|____/ 
```

### **TECHNOLOGY · PEOPLE · A HIGHER TOMORROW**
**DEUS INTUS // DEVELOPER ARM** — *Brand System v1.0*  
*Digital systems, products, and infrastructure.*

---
</div>

> **Elevator Line:** *"We build intelligent systems, products, and infrastructure that help ideas become operational reality."*

# 🛡️ Deus PBFT Consensus (`deus-pbft-consensus`)

> **Zero-dependency Practical Byzantine Fault Tolerance consensus state machine for local AI agent workforces.**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-0A57D6.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-33CFFF.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20(pure%20stdlib)-33CFFF.svg)](#)
[![Model Agnostic](https://img.shields.io/badge/AI-Model%20Agnostic-031B4E.svg)](./AGENT_SETUP.md)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Walkthrough%20Notebook-EAF4FF.svg)](./walkthrough.ipynb)

---

## 1. What This Is
Deus PBFT Consensus is a sovereign multi-agent coordination protocol written in pure standard-library Python. It provides mathematical fault tolerance ($N \ge 3f + 1$) for autonomous agent swarms, ensuring no single malfunctioning or hallucinating agent can unilaterally mutate production state.

## 2. Who It Is For
- **Multi-Agent Architects:** Coordinating agent swarms (Coders, Creators, Verifiers) that require cryptographic consensus before committing changes.
- **Autonomous Financial Systems:** Enforcing quorum approval on fund transfers, escrow releases, and smart contracts.
- **Enterprise DevOps:** Multi-node consensus verification without heavyweight blockchain or distributed database overhead.

## 3. Current Status
**Production / Standalone Sovereign Package.** Verified state machine supporting Pre-Prepare, Prepare, and Commit three-phase voting cycles.

## 4. What Works Now vs Planned
### What Works Now:
- Full Practical Byzantine Fault Tolerance state machine ($N=4$, tolerates $f=1$ faulty node).
- Multi-phase quorum voting with cryptographic block hashing.
- 1-Click quickstart execution via `python3 quickstart.py`.
- Interactive Jupyter Notebook walkthrough in [`walkthrough.ipynb`](./walkthrough.ipynb).
- Model-agnostic swarm coordination schemas in [`AGENT_SETUP.md`](./AGENT_SETUP.md).

### Planned:
- Dynamic node cluster discovery over Tailscale/local network sockets.

## 5. How to View or Use It (30-Second Quickstart)
No installation required! Zero external pip dependencies:

```bash
# 1. Clone the repository
git clone https://github.com/deus-intus/deus-pbft-consensus.git
cd deus-pbft-consensus

# 2. Run the 1-click simulation
python3 quickstart.py

# 3. Run the unit test suite
python3 -m unittest test_module.py
```

## 6. What Is in the Repository
- `module.py` — `DeusSovereignFabric` consensus state machine and node cluster logic.
- `quickstart.py` — 30-second runnable demo simulating 4 nodes and 1 Byzantine fault.
- `walkthrough.ipynb` — Visual Jupyter Notebook execution trace.
- `AGENT_SETUP.md` — Swarm consensus schemas for Gemini, Claude, OpenAI, and Ollama agents.
- `test_module.py` — Full unit test suite.

## 7. Model-Agnostic Swarm Coordination
Any agent persona can submit proposals or participate in voting rounds via standard JSON tool calls. Full schemas are provided in [`AGENT_SETUP.md`](./AGENT_SETUP.md).

## 8. Connections and Requirements
- Python 3.9 or higher (pure standard library).
- Zero external runtime packages.

## 9. License and Contribution Information
Licensed under the permissive [MIT License](./LICENSE). Copyright © Deus Intus Ltd.

---

## 🛡️ Intellectual Property & Statutory UK Trade Mark Notice

- **Registered UK Trade Mark:** `DEUS INTUS®` is a registered trade mark of **Deus Intus Ltd** in the United Kingdom under **UK Trade Mark No. UK00004416539**. All rights reserved.
- **Corporate Registration:** Deus Intus Ltd is a company registered in England and Wales (Company No. `17209569`), Registered Office: `66 Paul Street, London, EC2A 4NA, United Kingdom`.
- **Statutory IP Architecture:** Software primitives synthesized by Deus Intus combine 20-year statutory public-domain algorithmic cores with modern permissive runtimes into zero-dependency, model-agnostic, sovereign software modules.
- **Support & Inquiries:** Official support at [`support@deusintus.com`](mailto:support@deusintus.com).
