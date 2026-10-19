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
    print("✓ Initialized 4-Node Sovereign Fabric (N=4, f=1 tolerance)")

    # 2. Propose a transaction
    tx_action = "SET_CAPABILITY_STATE"
    tx_target = "LOCAL_MODEL_ROUTER"
    tx_payload = "mode=sovereign_mesh&status=verified"

    print(f"\n🗳️ Proposing Transaction: [{tx_action}] on {tx_target}")
    result = fabric.verify_and_execute(tx_action, tx_target, tx_payload)

    print("\nConsensus Outcome:")
    print(f"  • Consensus Reached: {result['consensus_reached']}")
    print(f"  • Commit Votes:      {result['commit_votes']} / 4")
    print(f"  • Byzantine Faults:  {result.get('byzantine_faults', 0)}")
    print(f"  • Execution Block:   {result.get('block_hash', 'N/A')[:16]}...")

    print("\n✓ Simulation completed successfully in pure Python standard library.")

if __name__ == "__main__":
    main()
