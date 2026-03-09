"""Tests for the Universal Turing Machine simulator."""

import json
import os
import pytest

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utm import TuringMachine, parse_tape, tape_to_string

MACHINES_DIR = os.path.join(os.path.dirname(__file__), '..', 'machines')


def load_machine(name: str) -> TuringMachine:
    path = os.path.join(MACHINES_DIR, name)
    with open(path, 'r') as f:
        return TuringMachine(json.load(f))


# ── Tape representation ────────────────────────────────────────────────────

class TestTape:
    def test_parse_tape_basic(self):
        tape = parse_tape("1101", "_")
        assert tape == {0: "1", 1: "1", 2: "0", 3: "1"}

    def test_parse_tape_empty(self):
        tape = parse_tape("", "_")
        assert tape == {}

    def test_parse_tape_with_blanks(self):
        tape = parse_tape("1_0", "_")
        assert tape == {0: "1", 2: "0"}

    def test_tape_to_string(self):
        tape = {0: "1", 1: "1", 2: "1", 3: "0"}
        assert tape_to_string(tape, "_") == "1110"

    def test_tape_to_string_empty(self):
        assert tape_to_string({}, "_") == ""

    def test_tape_to_string_with_gaps(self):
        tape = {0: "1", 2: "1"}
        result = tape_to_string(tape, "_")
        assert result == "1_1"


# ── Incrementer machine ────────────────────────────────────────────────────

class TestIncrementer:
    def test_increment_unary_3(self):
        """111 (unary 3) should become 1111 (unary 4)."""
        tm = load_machine("incrementer.json")
        tape = parse_tape("111", tm.blank)
        final_tape, steps, state = tm.run(tape)
        result = tape_to_string(final_tape, tm.blank)
        assert result == "1111"
        assert state == tm.halt

    def test_increment_unary_1(self):
        """1 (unary 1) should become 11 (unary 2)."""
        tm = load_machine("incrementer.json")
        tape = parse_tape("1", tm.blank)
        final_tape, steps, state = tm.run(tape)
        result = tape_to_string(final_tape, tm.blank)
        assert result == "11"

    def test_increment_empty(self):
        """Empty tape should become 1 (unary 1)."""
        tm = load_machine("incrementer.json")
        tape = parse_tape("", tm.blank)
        final_tape, steps, state = tm.run(tape)
        result = tape_to_string(final_tape, tm.blank)
        assert result == "1"


# ── Even/odd machine ──────────────────────────────────────────────────────

class TestEvenOdd:
    def test_even_length(self):
        tm = load_machine("even_odd.json")
        tape = parse_tape("1111", tm.blank)
        final_tape, steps, state = tm.run(tape)
        assert state == tm.halt

    def test_odd_length(self):
        tm = load_machine("even_odd.json")
        tape = parse_tape("111", tm.blank)
        final_tape, steps, state = tm.run(tape)
        assert state == tm.halt


# ── Machine behavior ──────────────────────────────────────────────────────

class TestMachineBehavior:
    def test_halts_within_step_limit(self):
        tm = load_machine("incrementer.json")
        tape = parse_tape("1", tm.blank)
        _, steps, _ = tm.run(tape, max_steps=100)
        assert steps < 100

    def test_step_limit_prevents_infinite_loop(self):
        """A machine that never halts should stop at max_steps."""
        desc = {
            "states": ["q0"],
            "alphabet": ["0", "1"],
            "blank": "_",
            "transitions": {"q0:0": ["q0", "1", "R"], "q0:1": ["q0", "0", "R"], "q0:_": ["q0", "0", "R"]},
            "start": "q0",
            "halt": "halt"
        }
        tm = TuringMachine(desc)
        tape = parse_tape("0", tm.blank)
        _, steps, state = tm.run(tape, max_steps=50)
        assert steps == 50
        assert state != tm.halt

    def test_missing_transition_stops(self):
        """Machine should stop when no transition exists."""
        desc = {
            "states": ["q0", "halt"],
            "alphabet": ["a"],
            "blank": "_",
            "transitions": {},
            "start": "q0",
            "halt": "halt"
        }
        tm = TuringMachine(desc)
        tape = parse_tape("a", tm.blank)
        _, steps, state = tm.run(tape)
        assert steps == 0
        assert state == "q0"

    def test_stay_direction(self):
        """S direction should not move the head."""
        desc = {
            "states": ["q0", "halt"],
            "alphabet": ["a"],
            "blank": "_",
            "transitions": {"q0:a": ["halt", "b", "S"]},
            "start": "q0",
            "halt": "halt"
        }
        tm = TuringMachine(desc)
        tape = parse_tape("a", "_")
        final_tape, steps, state = tm.run(tape)
        assert state == "halt"
        assert final_tape[0] == "b"
        assert steps == 1
