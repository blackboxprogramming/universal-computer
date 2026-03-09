# Universal Computer

[![CI](https://github.com/blackboxprogramming/universal-computer/actions/workflows/ci.yml/badge.svg)](https://github.com/blackboxprogramming/universal-computer/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776AB.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-Proprietary-9c27b0)](LICENSE)

A universal Turing machine simulator in Python. Demonstrates the foundational concept of computability: a single machine that can simulate any other Turing machine.

## How It Works

A Turing machine has a tape (infinite in both directions), a read/write head, a set of states, and a transition function. Given a state and the symbol under the head, the machine writes a new symbol, moves left/right/stay, and transitions to a new state. It halts when it reaches the halt state.

This implementation uses:
- **Dictionary-based tape** -- positions map to symbols, missing positions are blank
- **JSON machine descriptions** -- portable, human-readable definitions
- **Configurable step limit** -- prevents infinite loops

## Usage

```bash
# Increment binary number: 1101 (13) -> 1110 (14)
python3 utm.py machines/incrementer.json --tape "1101"

# Check parity
python3 utm.py machines/even_odd.json --tape "1111"
```

## Included Machines

| Machine | File | Description |
|---------|------|-------------|
| Binary Incrementer | `incrementer.json` | Adds 1 to a binary number |
| Even/Odd | `even_odd.json` | Determines parity of a unary number |

## Creating Your Own Machine

```json
{
  "states": ["q0", "q1", "halt"],
  "alphabet": ["0", "1"],
  "blank": "_",
  "transitions": {
    "q0:0": ["q0", "0", "R"],
    "q0:1": ["q1", "1", "R"],
    "q0:_": ["halt", "_", "S"]
  },
  "start": "q0",
  "halt": "halt"
}
```

Each transition key is `"state:symbol"` mapping to `[next_state, write_symbol, direction]` where direction is `L` (left), `R` (right), or `S` (stay).

## Development

```bash
pip install pytest
pytest tests/ -v
```

## Theory

Alan Turing proved in 1936 that a universal Turing machine can compute anything that any Turing machine can compute. Every computer is a physical realization of this idea.

## License

Proprietary -- BlackRoad OS, Inc.
