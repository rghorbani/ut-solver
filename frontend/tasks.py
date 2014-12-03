"""
Celery Tasks
"""

from celery import task
# from lex.lexer import p_statement_assign


@task
def solve_problem(problem):
    # a, b, c = p_statement_assign(problem.problem_text)
    return problem.problem_text