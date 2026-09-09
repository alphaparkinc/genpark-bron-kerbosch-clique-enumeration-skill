import sys
import json
from client import BronKerboschCliqueFinder

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "find_cliques":
        finder = BronKerboschCliqueFinder()
        return finder.find_maximal_cliques(params.get("graph", {}))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
