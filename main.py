from model import get_abstract_model
from solver import Solver


def solve_rooks_problem():
    abstract_model = get_abstract_model()
    concrete_model = abstract_model.create_instance()

    # Dump connfigurations (for debugging)
    with open('./concrete_model_dump.txt', 'wt') as f:
        concrete_model.pprint(f)

    solver = Solver(concrete_model=concrete_model)
    solver.solve()
    solver.print_solution()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve_rooks_problem()
