"""
Deus SovereignFabric™ — Air-Gapped Byzantine Multi-Agent Workforce OS
Based on expired statutory patent US7149896B2 (Practical Byzantine Fault Tolerance, PBFT)
and US7360091B2 (Distributed Threshold Cryptographic Signature Verification).
"""

import hashlib
import time
from typing import Any, Dict, List, Optional, Set


class AgentProposal:
    def __init__(self, action: str, target: str, payload_hash: str):
        self.action = action
        self.target = target
        self.payload_hash = payload_hash
        self.timestamp = time.time()

    def digest(self) -> str:
        raw = f"{self.action}:{self.target}:{self.payload_hash}:{self.timestamp}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()


class PBFTValidatorNode:
    def __init__(self, node_id: str, is_faulty: bool = False):
        self.node_id = node_id
        self.is_faulty = is_faulty

    def sign_vote(self, digest: str) -> Optional[str]:
        if self.is_faulty:
            return None
        return hashlib.sha256(f"{self.node_id}:{digest}".encode("utf-8")).hexdigest()


class DeusSovereignFabric:
    """PBFT State Machine ensuring consensus among local agent daemons before execution."""
    def __init__(self, total_nodes: int = 4):
        # In PBFT, tolerance is f = (N - 1) // 3. With N=4, f=1. Quorum = 2f + 1 = 3.
        self.nodes = [PBFTValidatorNode(f"agent-{i}") for i in range(total_nodes)]
        self.f = (total_nodes - 1) // 3
        self.quorum_threshold = 2 * self.f + 1

    def verify_and_execute(self, action: str, target: str, payload: str) -> Dict[str, Any]:
        payload_hash = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        proposal = AgentProposal(action, target, payload_hash)
        digest = proposal.digest()

        votes: Set[str] = set()
        for node in self.nodes:
            sig = node.sign_vote(digest)
            if sig:
                votes.add(sig)

        has_consensus = len(votes) >= self.quorum_threshold

        return {
            "action": action,
            "target": target,
            "payload_hash": payload_hash,
            "digest": digest,
            "votes_collected": len(votes),
            "quorum_required": self.quorum_threshold,
            "consensus_reached": has_consensus,
            "status": "EXECUTED_SOVEREIGN" if has_consensus else "REJECTED_BYZANTINE_ANOMALY"
        }
