import itertools
from typing import Optional

from pyomo.environ import ConcreteModel, SolverFactory, SolverStatus
from pyomo.opt.results import SolverResults


class Solver:
    def __init__(self, concrete_model: ConcreteModel):
        self.concrete_model: ConcreteModel = concrete_model
        self._solution: Optional[SolverResults] = None

    def solve(self) -> None:
        solver = SolverFactory('scip')
        self._solution = solver.solve(self.concrete_model, tee=True)

    def solution_exists(self) -> bool:
        solution_found = (
            self._solution.solver.status == SolverStatus.ok or
            self._solution.solver.status == SolverStatus.warning
        )
        return solution_found

    def print_solution(self) -> None:
        assert self.solution_exists(), 'The solver did not find any solution!'

        rooks = [
            f'{column}{row}'
            for column, row in itertools.product(
                self.concrete_model.columns, self.concrete_model.rows
            )
            if self.concrete_model.place_rook[column, row].value
        ]

        print(f'Best solution (with {len(rooks)} rooks): {rooks}.')
