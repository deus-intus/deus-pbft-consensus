# AI Agent Swarm Integration Guide — Deus PBFT Consensus

This guide explains how autonomous multi-agent squads can use **Deus PBFT Consensus** to agree on shared system state, escrow releases, or capability updates before committing changes.

---

## 1. Why Swarm Consensus Matters
In multi-agent architectures (e.g. Creator Agent, Code Agent, Verifier Agent), no single agent should unilaterally mutate production state. Deus PBFT enforces that at least **$2f + 1$** agents verify and sign a proposed payload before execution.

---

## 2. Universal Tool Definition (JSON Schema)

```json
{
  "name": "propose_consensus_transaction",
  "description": "Propose an action to the PBFT swarm consensus state machine.",
  "parameters": {
    "type": "object",
    "properties": {
      "action": {
        "type": "string",
        "description": "Action type (e.g. RELEASE_ESCROW, COMMIT_MODEL_WEIGHTS, UPDATE_REGISTRY)"
      },
      "target": {
        "type": "string",
        "description": "Target entity or contract identifier"
      },
      "payload": {
        "type": "string",
        "description": "Serialized parameters or cryptographic hash of the proposal"
      }
    },
    "required": ["action", "target", "payload"]
  }
}
```

---

## 3. Python Integration Pattern
```python
from module import DeusSovereignFabric

# Initialize 4-node cluster (allows 1 faulty or hallucinating node)
fabric = DeusSovereignFabric(total_nodes=4)

def execute_agent_proposal(action: str, target: str, payload: str) -> dict:
    decision = fabric.verify_and_execute(action, target, payload)
    if decision["consensus_reached"]:
        return {"status": "COMMITTED", "block": decision["block_hash"]}
    return {"status": "REJECTED", "reason": "Insufficient Byzantine agreement"}
```
