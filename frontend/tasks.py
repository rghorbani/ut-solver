"""
Celery Tasks
"""

from celery import task
from lex.lexer import solve_p
from optimization.simplex import simple_simplex


@task
def solve_problem(problem):
    a, b, c = solve_p(problem.problem_text)
    result = simple_simplex(a, b, c)
    print result

    return problem.problem_text