# Universal Computer

Universal Turing machine simulator in Python. Reads a JSON machine description and executes it step-by-step on an unbounded tape.

## Usage

```bash
python3 utm.py machines/incrementer.json --tape "1101"
```

Increments binary `1101` (13) to `1110` (14).

Add `--trace` to see each step:

```bash
python3 utm.py machines/incrementer.json --tape "1101" --trace
```

## Machine Description Format

JSON files with: states, input alphabet, blank symbol, transition function, start state, and halt state. Each transition maps `(state, symbol)` to `(next_state, write_symbol, direction)` where direction is `L`, `R`, or `S` (stay).

## Sample Machines

| Machine | Description |
|---------|-------------|
| `incrementer.json` | Increments a binary number |
| `even_odd.json` | Decides if a unary number is even or odd |

## Implementation

- **Tape:** Python dict mapping positions to symbols (default: `_` blank)
- **Execution:** Runs until halt state or configurable step limit
- **Output:** Final tape contents and step count

## Project Structure

```
utm.py       # Universal Turing machine simulator
machines/    # JSON machine descriptions
```

## License

Copyright 2026 BlackRoad OS, Inc. All rights reserved.
