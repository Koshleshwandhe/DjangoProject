# expenses/models.py

from django.db import models

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Expense(models.Model):
    expenseId = models.AutoField(primary_key=True)
    payerId = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    EXPENSE_TYPE_CHOICES = [
        ('EQUAL', 'Equal'),
        ('EXACT', 'Exact'),
        ('PERCENT', 'Percent'),
    ]
    type = models.CharField(max_length=10, choices=EXPENSE_TYPE_CHOICES)
    expenseName = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return self.expenseName

class Participant(models.Model):
    expenseId = models.ForeignKey(Expense, on_delete=models.CASCADE)
    participantId = models.ForeignKey(User, on_delete=models.CASCADE)
    shareAmount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Expense: {self.expenseId} - Participant: {self.participantId}'
