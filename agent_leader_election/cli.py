"""Command line interface for agent-leader-election."""
from .election import BullyElection

def main():
    e = BullyElection()
    e.add_node("node_1", 10)
    e.add_node("node_2", 50)
    e.add_node("node_3", 30)
    print("Elected Leader:", e.elect())

if __name__ == "__main__":
    main()
