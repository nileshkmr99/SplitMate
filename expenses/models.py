from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    EXPENSE_TYPE_CHOICES = [
        ("EQUAL", "Equal"),
        ("EXACT", "Exact"),
        ("PERCENT", "Percentage"),
    ]

    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses_paid")
    created_at = models.DateTimeField(auto_now_add=True)
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPE_CHOICES)

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"

class Split(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name="splits")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="splits_owed")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} owes ₹{self.amount} for {self.expense.title}"