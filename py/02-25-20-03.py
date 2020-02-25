"""
Count number of edges in a graph

f(n, seen) -> edges

Criterion for edge: <=1 link
"""

class Node:
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def __repr__(self):
        return str(hash(self))

# Expected number of edges: 4
deepest_node = Node()
graph = Node([
    Node(),
    Node([
        Node([deepest_node]),
        Node([deepest_node])
    ]),
    Node()
])


def count_edges(node: Node, seen: set=set()) -> int:
    for n in node.nodes:
        seen.add(frozenset([node, n]))
        count_edges(n, seen)
    return len(seen)


if __name__ == '__main__':
    print(f'Edge count for graph: {count_edges(graph)}')

    print(f'Edge count for deepest_node: {count_edges(deepest_node)}')
