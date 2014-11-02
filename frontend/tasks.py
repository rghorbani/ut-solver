"""
Celery Tasks
"""

from celery import task


@task
def solve_problem(problem):
    return problem.problem_text