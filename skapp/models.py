from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Goal(models.Model):
    DURATION_CHOICES = [
        (7, '7 Days'),
        (14, '14 Days'),
        (21, '21 Days'),
        (28, '28 Days'),
        (35, '35 Days'),
        (49, '49 Days'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField(default=timezone.now)
    duration = models.IntegerField(choices=DURATION_CHOICES)

    total_points = models.IntegerField(default=0)
    bonus_points = models.IntegerField(default=0)
    penalty_points = models.IntegerField(default=0)

    progress_days = models.IntegerField(default=0)
    missed_days = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.total_points = self.duration * 20
        self.bonus_points = self.duration * 10
        super().save(*args, **kwargs)

    def current_Score(self):
        score = self.total_points - (self.missed_days * self.penalty_points)
        if self.is_completed:
            score += self.bonus_points
            return score

class DailyCheckedIn(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    success = models.BooleanField(default=True)                