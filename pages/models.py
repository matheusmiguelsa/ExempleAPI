from django.db import models
from django.core.validators import MinLengthValidator


class Client(models.Model):
    payment_id = models.IntegerField()
    start_date = models.DateField(max_length=8)
    end_date = models.DateField(max_length=8)
    original_value = models.FloatField()
    collaborator_owner = models.CharField(max_length=30)
    social_bussiness_name = models.CharField(max_length=40)
    CNPJ = models.CharField( max_length=14, validators=[MinLengthValidator(14)])

    def __int__(self):
        return self.payment_id