# Rooks problem

The rooks problem in chess involves determining the number of ways to place N rooks on an 
N x N chessboard such that no two rooks threaten each other. This means each rook must be 
placed in a unique row and a unique column.

This project solves this problem using a 8 x 8 chessboard. To do so, a solver called
SCIP, one of the most powerful non-commercial solvers, is used. The Pyomo library is
also used to interact with such model.

## Installation

- Base enviornment: You should have installed Python and pip.
- Miniconda (or Conda): It provides the most straightforward installation of the solver, already compiled. Check out [this](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#term-Miniconda) page.


## Development tools

- Type checking with flake8:
```bash
$ flake8 --max-line-length=89
```

## Running
```bash
$ python main.py
```

## Code structure
- `main.py`: Main execution file. It orchestrates the execution.
- `model.py`: Model definition and construction.
- `solver.py`: Defines the solver and its functions.
- `concrete_model_dump.txt`: Internal structure of the model (for debugging)
- `conda-env.yml`: Environment for Conda/Miniconda.
- `requirements.txt`: Requirements of the project.

## Attributions
- Base of the code and ideas extracted from _Josep's blog_ [here](https://johomo.hashnode.dev/solve-your-first-problem-with-mathematical-programming).
- Definition of the rooks problem extracted from [here](https://mathworld.wolfram.com/RooksProblem.html).
