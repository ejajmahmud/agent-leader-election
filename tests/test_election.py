"""Unit tests for BullyElection."""
import unittest
from agent_leader_election.election import BullyElection

class TestElection(unittest.TestCase):
    def test_election(self):
        e = BullyElection()
        e.add_node("low", 1)
        e.add_node("high", 100)
        self.assertEqual(e.elect(), "high")
        e.remove_node("high")
        self.assertEqual(e.elect(), "low")

if __name__ == "__main__":
    unittest.main()
