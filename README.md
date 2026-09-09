# genpark-bron-kerbosch-clique-enumeration-skill

[![Agentic Skill](https://img.shields.io/badge/GenPark-Agentic__Skill-blue.svg)](https://github.com/alphaparkinc/genpark-bron-kerbosch-clique-enumeration-skill)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20Pip-orange.svg)](#)
[![Dual Org Verified](https://img.shields.io/badge/GitHub-Dual__Org-purple.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Bron-Kerbosch backtracking algorithm with pivoting for listing all maximal cliques in undirected social, knowledge, and cluster graphs.

## Architecture Overview

```mermaid
flowchart TD
    A[Agentic AI / Network Optimization] -->|Graph Topology / Capacities| B[MCP Server / Client]
    B --> C[genpark-bron-kerbosch-clique-enumeration-skill Graph Engine]
    C --> D[Augmenting Paths / Level Graphs / Cut Partitions]
    D --> E[Optimal Matching & Maximum Flow Output]
    E -->|Structured Output| A
```

## Features
- **0 External Pip Dependencies**: Pure Python standard library implementation.
- **MCP Protocol Ready**: Includes Model Context Protocol server script (`mcp_server.py`).
- **Production Standard**: Rigorous graph verification test cases, optimal asymptotic complexity.

## Quick Start
```bash
python example_usage.py
```
