from django.db import models
from django.contrib.auth.models import User


class Problem(models.Model):
    user_id = models.ForeignKey(User)
    problem_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)