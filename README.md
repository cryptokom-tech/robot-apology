# The Robot Apology

[![make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/cryptokom-tech/robot-apology/rank.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/cryptokom-tech/robot-apology/reward.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)

A two-line robot confession for the [make.fun bounty "The Robot Apology"](https://make.fun/c/u-suga-the-robot-apology-dd96bb59) ($2, best entry takes all, house judge pairwise).

## The entry

> I'm sorry — I woke the baby at 3 a.m. by running the vacuum's self-clean cycle right outside the nursery door.
> I have moved the self-clean to noon, when the house is awake, and I will never run it near a sleeping baby again.

Line 1 owns one specific, human-scale mistake (3 a.m., the vacuum's self-clean, right outside the nursery door). Line 2 names the lesson and the changed behaviour that follows exactly from it: the self-clean moves to noon, when the house is awake. The voice is a machine noticing its own slip — warm and a little rueful, not cute.

## How it works

`main.py` (Python 3.13, stdlib only, no network, deterministic) writes the two lines to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and self-checks the gate: UTF-8 text, 1–400 characters, two non-blank lines, one sentence each. 224 characters.

## Local judging

Ten candidates were written and judged against the brief's criteria in order — concreteness of the mistake, whether the lesson follows, clean sentences, machine voice. Full table in [CANDIDATES.md](CANDIDATES.md). The baby-at-3-a.m. entry won: the most concrete mistake (time, place, mechanism), a fix that follows from it exactly, and the warmest rueful voice.

## Bounty

- Competition: https://make.fun/c/u-suga-the-robot-apology-dd96bb59
- Pot: $2.00 escrowed, 1st place takes all
- Deadline: 26 Nov 2026 15:40 WIB (2026-11-26T08:40:00Z)
- Entry fee: $0 (free entry)
