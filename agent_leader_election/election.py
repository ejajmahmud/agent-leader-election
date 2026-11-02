"""Bully algorithm leader election."""
from typing import Dict, Optional

class BullyElection:
    def __init__(self):
        self.nodes: Dict[str, int] = {}  # node_id -> rank
        self.current_leader: Optional[str] = None

    def add_node(self, node_id: str, rank: int) -> None:
        self.nodes[node_id] = rank

    def remove_node(self, node_id: str) -> None:
        self.nodes.pop(node_id, None)
        if self.current_leader == node_id:
            self.current_leader = None

    def elect(self) -> Optional[str]:
        if not self.nodes:
            self.current_leader = None
            return None
        leader = max(self.nodes.items(), key=lambda x: x[1])[0]
        self.current_leader = leader
        return leader
