from pyomo.environ import (
    AbstractModel,
    Binary,
    Constraint,
    maximize,
    Objective,
    Set,
    Var,
)
from pyomo.core.expr.numeric_expr import LinearExpression
from pyomo.core.expr.relational_expr import EqualityExpression, InequalityExpression


def get_abstract_model() -> AbstractModel:
    model = AbstractModel(name='rooks-problem')

    # Sets: Indexes for parameters, variables and other sets.
    model.columns = Set(
        name='columns',
        doc='Set of columns of the chest board.',
        initialize=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    )

    model.rows = Set(
        name='rows',
        doc='Set of rows of the chest board.',
        initialize=[1, 2, 3, 4, 5, 6, 7, 8],
    )

    # Parameters: Values that you know prior to solving the problem, and will not change
    # during the execution.
    #   There are no parameters in this problem.

    # Variables: Values defined while solving the problem to get the best solution.
    # The following variable is indexed by columns and rows, therefore,
    # one variable for each combination of columns and rows is defined.
    model.place_rook = Var(
        model.columns,
        model.rows,
        name='place_rook',
        doc='Binary variable: 1 if rook is placed, 0 otherwise.',
        domain=Binary,
    )

    # Constraints: Requirements and forbidden actions to achieve a correct solution.
    model.constraint_at_most_one_rook_per_column = Constraint(
        model.columns,
        name='at_most_one_rook_per_column',
        doc=constraint_at_most_one_rook_per_column.__doc__,
        rule=constraint_at_most_one_rook_per_column,
    )

    model.constraint_at_most_one_rook_per_row = Constraint(
        model.rows,
        name='at_most_one_rook_per_row',
        doc=constraint_at_most_one_rook_per_row.__doc__,
        rule=constraint_at_most_one_rook_per_row,
    )

    model.constraint_no_rook_on_a1 = Constraint(
        name='no_rook_on_a1',
        doc=constraint_no_rook_on_a1.__doc__,
        rule=constraint_no_rook_on_a1,
    )

    # Objective: Function of variables that returns a value to be maximized or minimized.
    # In this case: to have the maximum number of rooks in the board.
    model.objective_function = Objective(
        rule=number_of_rooks_in_the_board,
        sense=maximize,
    )

    return model


# Constraints definition
def constraint_at_most_one_rook_per_column(
        model: AbstractModel,
        column: str,
) -> InequalityExpression:
    """Limit the number of rooks per column to at most one."""
    rooks_per_column = sum(model.place_rook[column, row] for row in model.rows)
    return rooks_per_column <= 1


def constraint_at_most_one_rook_per_row(
        model: AbstractModel,
        row: int,
) -> InequalityExpression:
    """Limit the number of rooks per row to at most one."""
    rooks_per_row = sum(model.place_rook[column, row] for column in model.columns)
    return rooks_per_row <= 1


def constraint_no_rook_on_a1(
        model: AbstractModel,
) -> EqualityExpression:
    """No rook in position a1."""
    rook_on_a1 = model.place_rook['a', 1]
    return rook_on_a1 == 0


# Objective function definition
def number_of_rooks_in_the_board(
        model: AbstractModel,
) -> LinearExpression:
    """Count number of rooks in the board."""
    rooks = sum(
        model.place_rook[column, row]
        for column in model.columns
        for row in model.rows
    )
    return rooks
