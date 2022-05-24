from django.forms import DateField, ModelForm, DateInput
from .models import Client
from project import settings
import requests
import json
from django.core.exceptions import ValidationError



class DateInput(DateInput):
    input_type = 'date'


class ClientForm(ModelForm):
    start_date = DateField(widget=DateInput, input_formats=settings.DATE_INPUT_FORMATS)
    end_date = DateField(widget=DateInput, input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        widgets = {'my_date_field': DateInput()}
        model = Client
        fields = [
            "payment_id",
            "start_date",
            "end_date",
            "original_value",
            "collaborator_owner",
            "social_bussiness_name",
            "CNPJ",
            ]


    

