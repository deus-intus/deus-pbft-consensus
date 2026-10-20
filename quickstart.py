#!/usr/bin/env python3
"""Deus PBFT Consensus — 30-Second Standalone Quickstart
Runs in pure Python 3 standard library with zero external dependencies.
"""

from module import DeusSovereignFabric

def main():
    print("=" * 60)
    print("🛡️ Deus PBFT Consensus — Byzantine Fault Tolerance State Machine")
    print("=" * 60)

    # 1. Initialize a 4-node consensus fabric (tolerates f=1 Byzantine fault)
    fabric = DeusSovereignFabric(total_nodes=4)
    total_nodes = len(fabric.nodes)
    print(f"✓ Initialized {total_nodes}-Node Sovereign Fabric "
          f"(N={total_nodes}, f={fabric.f} tolerance, quorum={fabric.quorum_threshold})")

    tx_action = "SET_CAPABILITY_STATE"
    tx_target = "LOCAL_MODEL_ROUTER"
    tx_payload = "mode=sovereign_mesh&status=verified"

    # 2. Healthy round — all nodes honest, consensus should be reached.
    print(f"\n🗳️  Scenario A — Healthy fabric: [{tx_action}] on {tx_target}")
    result = fabric.verify_and_execute(tx_action, tx_target, tx_payload)
    print(f"  • Votes Collected:   {result['votes_collected']} / {total_nodes}")
    print(f"  • Quorum Required:   {result['quorum_required']}")
    print(f"  • Consensus Reached: {result['consensus_reached']}")
    print(f"  • Status:            {result['status']}")
    print(f"  • Execution Block:   {result['digest'][:16]}...")

    # 3. Byzantine round — inject f=1 faulty node; quorum (2f+1) must still hold.
    fabric.nodes[0].is_faulty = True
    print(f"\n🗳️  Scenario B — 1 Byzantine node faulty (f={fabric.f}): [{tx_action}] on {tx_target}")
    result = fabric.verify_and_execute(tx_action, tx_target, tx_payload)
    print(f"  • Votes Collected:   {result['votes_collected']} / {total_nodes}")
    print(f"  • Quorum Required:   {result['quorum_required']}")
    print(f"  • Consensus Reached: {result['consensus_reached']}")
    print(f"  • Status:            {result['status']}")

    print("\n✓ Simulation completed successfully in pure Python standard library.")

if __name__ == "__main__":
    main()
