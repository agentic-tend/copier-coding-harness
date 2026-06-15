# Testing Policy

This file defines how tests express public boundaries before implementation details.

Tests should specify:

- accepted inputs;
- observable outputs;
- invariants;
- error behavior;
- minimal integration paths.

Tests should not specify:

- private helper layout;
- incidental intermediate state;
- implementation ordering;
- formatting-only behavior.
