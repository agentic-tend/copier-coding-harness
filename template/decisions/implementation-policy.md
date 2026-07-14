# Implementation Policy

This file defines how implementation topology evolves from declared structure into working semantics without unnecessary expansion.

## Topology Evolution

Treat structure and behavior as coupled axes:

- Vertical evolution creates skeletons before internal logic so syntactic topology exists before unit semantics fill it.
- Horizontal evolution follows 3M principle:
  - make it work — write the smallest plain-code implementation that satisfies the contract;
  - make it right — simplify the working code and align its units with the declared topology;
  - make it fast — optimize only against explicit performance evidence and a relevant benchmark.

## Complexity Boundary

- Optimize execution briefs for the smallest conceptual diff (keep it stay simple). If the requested scope is over-designed, surface the simpler route before implementation.
- Add abstraction only when required by multiple concrete uses or an explicit contract boundary.

## Redesign Gate

When implementation friction appears, produce the smallest failing evidence before proposing a broader redesign.

A broader redesign must identify which existing boundary fails and why a local correction is insufficient.
