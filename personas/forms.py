# -*- coding: utf-8 -*-
from personas.models import Persona
from django.forms import ModelForm


class PersonaForm(ModelForm):

    class Meta:
        model = Persona
        exclude = ['pk']
