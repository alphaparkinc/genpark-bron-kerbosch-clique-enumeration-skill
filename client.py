class BronKerboschCliqueFinder:
    """Bron-Kerbosch maximal clique enumerator with pivoting."""
    def find_maximal_cliques(self, graph: dict[int, list[int]]) -> dict:
        adj = {int(k): set(v) for k, v in graph.items()}
        cliques = []

        def bron_kerbosch(R: set, P: set, X: set):
            if not P and not X:
                cliques.append(sorted(list(R)))
                return
            # Pivot selection (vertex with maximum degree in P union X)
            u = max(P | X, key=lambda node: len(adj.get(node, set())))
            for v in list(P - adj.get(u, set())):
                neighbors = adj.get(v, set())
                bron_kerbosch(R | {v}, P & neighbors, X & neighbors)
                P.remove(v)
                X.add(v)

        all_nodes = set(adj.keys())
        bron_kerbosch(set(), all_nodes, set())

        cliques.sort(key=lambda c: (-len(c), c))
        return {
            "total_maximal_cliques": len(cliques),
            "maximum_clique_size": len(cliques[0]) if cliques else 0,
            "cliques": cliques
        }
