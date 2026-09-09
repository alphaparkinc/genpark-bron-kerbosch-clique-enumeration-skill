from client import BronKerboschCliqueFinder

def main():
    print("=== Bron-Kerbosch Maximal Clique Enumerator ===")
    finder = BronKerboschCliqueFinder()
    g = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }

    res = finder.find_maximal_cliques(g)
    print("Cliques Found:", res)
    assert [0, 1, 2] in res["cliques"]
    assert res["maximum_clique_size"] == 3

    print("Bron-Kerbosch Finder verified successfully!")

if __name__ == "__main__":
    main()
