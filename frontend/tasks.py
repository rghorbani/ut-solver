"""
Celery Tasks
"""

from celery import task
from lex.lexer import parse_problem
from optimization.simplex import simple_simplex


@task
def solve_problem(problem):
    parse_result = parse_problem(problem.problem_text)
    print parse_result
    if parse_result is not None:
        a, b, c, x = parse_result
        if a and b and c and x:
            result = simple_simplex(a, b, c)
    print result

    return problem.problem_text