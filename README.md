<!-- BlackRoad SEO Enhanced -->

# universal computer

> Part of **[BlackRoad OS](https://blackroad.io)** — Sovereign Computing for Everyone

[![BlackRoad OS](https://img.shields.io/badge/BlackRoad-OS-ff1d6c?style=for-the-badge)](https://blackroad.io)
[![BlackRoad Forge](https://img.shields.io/badge/Org-BlackRoad-Forge-2979ff?style=for-the-badge)](https://github.com/BlackRoad-Forge)
[![License](https://img.shields.io/badge/License-Proprietary-f5a623?style=for-the-badge)](LICENSE)

**universal computer** is part of the **BlackRoad OS** ecosystem — a sovereign, distributed operating system built on edge computing, local AI, and mesh networking by **BlackRoad OS, Inc.**

## About BlackRoad OS

BlackRoad OS is a sovereign computing platform that runs AI locally on your own hardware. No cloud dependencies. No API keys. No surveillance. Built by [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc), a Delaware C-Corp founded in 2025.

### Key Features
- **Local AI** — Run LLMs on Raspberry Pi, Hailo-8, and commodity hardware
- **Mesh Networking** — WireGuard VPN, NATS pub/sub, peer-to-peer communication
- **Edge Computing** — 52 TOPS of AI acceleration across a Pi fleet
- **Self-Hosted Everything** — Git, DNS, storage, CI/CD, chat — all sovereign
- **Zero Cloud Dependencies** — Your data stays on your hardware

### The BlackRoad Ecosystem
| Organization | Focus |
|---|---|
| [BlackRoad OS](https://github.com/BlackRoad-OS) | Core platform and applications |
| [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc) | Corporate and enterprise |
| [BlackRoad AI](https://github.com/BlackRoad-AI) | Artificial intelligence and ML |
| [BlackRoad Hardware](https://github.com/BlackRoad-Hardware) | Edge hardware and IoT |
| [BlackRoad Security](https://github.com/BlackRoad-Security) | Cybersecurity and auditing |
| [BlackRoad Quantum](https://github.com/BlackRoad-Quantum) | Quantum computing research |
| [BlackRoad Agents](https://github.com/BlackRoad-Agents) | Autonomous AI agents |
| [BlackRoad Network](https://github.com/BlackRoad-Network) | Mesh and distributed networking |
| [BlackRoad Education](https://github.com/BlackRoad-Education) | Learning and tutoring platforms |
| [BlackRoad Labs](https://github.com/BlackRoad-Labs) | Research and experiments |
| [BlackRoad Cloud](https://github.com/BlackRoad-Cloud) | Self-hosted cloud infrastructure |
| [BlackRoad Forge](https://github.com/BlackRoad-Forge) | Developer tools and utilities |

### Links
- **Website**: [blackroad.io](https://blackroad.io)
- **Documentation**: [docs.blackroad.io](https://docs.blackroad.io)
- **Chat**: [chat.blackroad.io](https://chat.blackroad.io)
- **Search**: [search.blackroad.io](https://search.blackroad.io)

---

> ⚗️ **Research Repository**
>
> This is an experimental/research repository. Code here is exploratory and not production-ready.
> For production systems, see [BlackRoad-OS](https://github.com/BlackRoad-OS).

---

# Universal Computer

This repository contains an implementation of a **universal Turing machine** in Python.  A universal Turing machine is a theoretical device capable of simulating any other Turing machine.  In other words, it can compute anything that is computable.  The implementation here is simple and educational; it demonstrates the principles of universality and emulation in a compact form.

## Overview

The core of the project is a Turing machine simulator that reads a description of another machine and an input tape, then executes that machine's transition function step by step.  The simulator supports tapes of unbounded length in both directions and maintains a set of states, including a halting state.  The universal machine itself accepts programs encoded as tables of transitions.

### Features

- **Tape representation:** The tape is implemented as a Python dictionary mapping integer positions to symbols.  Positions not present in the dictionary are assumed to hold a blank symbol (`'_'`).
- **Transition function:** Each transition is a mapping from `(current_state, current_symbol)` to `(next_state, write_symbol, move_direction)`, where `move_direction` is `'L'`, `'R'`, or `'S'` (stay).
- **Machine description format:** Machine descriptions are loaded from JSON files.  A description includes the set of states, the input alphabet, the blank symbol, the transition function, the start state, and the halting state.
- **Simulation:** The simulator runs the machine until it reaches the halting state or exceeds a configurable step limit.  It yields the final tape contents and the number of steps executed.

### Running the simulator

To use the universal Turing machine, first prepare a JSON file describing the machine you want to simulate (see `machines/` for examples), then run:

```
python3 utm.py machines/your_machine.json --tape "your input tape here"
```

For example, to run a binary incrementer:

```
python3 utm.py machines/incrementer.json --tape "1101"
```

This will increment the binary number `1101` (13) to `1110` (14).

## Directory structure

- `utm.py` – the universal Turing machine simulator.
- `machines/` – sample machine descriptions in JSON format.
- `README.md` – this file.

## Sample machines

The repository includes a few sample machine descriptions:

- `incrementer.json` – a machine that increments a binary number.
- `even_odd.json` – a machine that decides whether a unary number has an even or odd number of symbols.

Feel free to add more machines to the `machines/` directory to explore the power of Turing machines!

## License

This project is released under the MIT License.  See `LICENSE` for details.

---

## 📜 License & Copyright

**Copyright © 2026 BlackRoad OS, Inc. All Rights Reserved.**

**CEO:** Alexa Amundson | **PROPRIETARY AND CONFIDENTIAL**

This software is NOT for commercial resale. Testing purposes only.

### 🏢 Enterprise Scale:
- 30,000 AI Agents
- 30,000 Human Employees
- CEO: Alexa Amundson

**Contact:** blackroad.systems@gmail.com

See [LICENSE](LICENSE) for complete terms.
