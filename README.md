# Hello, CQRS!

A simple Python implementation of the CQRS (Command Query Responsibility
Segregation) pattern using SQLAlchemy and SQLite. It uses a shared database for
both reads and writes, with a clean structure that makes it easy to split into
separate databases in the future. Includes Pytest tests with an in-memory
database for isolation and speed.

## Getting Started

```bash
make sync 
```

## Running App

```bash
make run
```

## Running Tests

```bash
make test
```
