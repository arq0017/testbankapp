from django.db import models


# model for storing bank names
class Bank(models.Model):
    # custom primary key
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)


class BankBranch(models.Model):
    ifsc = models.CharField(max_length=50, primary_key=True)
    # bank_id expects Bank model object
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.ifsc
