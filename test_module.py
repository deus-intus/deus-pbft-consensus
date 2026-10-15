import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from module import DeusSovereignFabric

class TestSovereignFabric(unittest.TestCase):
    def test_healthy_consensus(self):
        fabric = DeusSovereignFabric(total_nodes=4)
        res = fabric.verify_and_execute("TRANSFER_FUNDS", "LOCAL_ESCROW", "amount=5000")
        self.assertTrue(res["consensus_reached"])
        self.assertEqual(res["status"], "EXECUTED_SOVEREIGN")
        self.assertGreaterEqual(res["votes_collected"], 3)

    def test_fault_tolerance_with_byzantine_node(self):
        fabric = DeusSovereignFabric(total_nodes=4)
        fabric.nodes[0].is_faulty = True  # 1 faulty node within f=1 budget
        res = fabric.verify_and_execute("EXECUTE_SHELL", "LOCAL_DAEMON", "command=deploy")
        self.assertTrue(res["consensus_reached"])
        self.assertEqual(res["votes_collected"], 3)

if __name__ == "__main__":
    unittest.main()
