# FizzBuzz TDD Kata

A Python implementation of the classic FizzBuzz problem, built using Test-Driven Development (TDD) with the Red-Green-Refactor cycle.

## The FizzBuzz rules

- Multiple of 3 → "Fizz"
- Multiple of 5 → "Buzz"
- Multiple of both 3 and 5 → "FizzBuzz"
- Otherwise → the number itself

## Tools

- uv — Python project and dependency manager
- pytest — testing framework
- marimo — interactive notebook
- ruff — linter

## How to run

    uv run pytest notebook.py
    uv run marimo edit notebook.py

## TDD workflow

The notebook grows the contract of the fizzbuzz function one test at a time, following the Red → Green → Refactor cycle.

## Author

Hala Dagher
