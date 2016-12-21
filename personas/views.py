from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views import View

from personas.forms import PersonaForm
from personas.models import Persona


class HomeView(View):

    def get(self, request):

        """
        Renderiza el home con un formulario de acceso
        :param request:
        :return: objeto HttpResponse con los datos de la respuesta
        """

        return render(request, 'home.html')


class PersonaQueryset(object):

    @staticmethod
    def get_personas():
        possible_personas = Persona.objects.all().select_related("owner")
        return possible_personas


class PersonaDetailView(View):
    def get(self, request, pk):
        """
        Renderiza el detalle de una imagen
        :param request: objeto HttpRequest con los datos de la petición
        :param pk: clave primaria de la foto a recuperar
        :return: objeto HttpResponse con los datos de la respuesta
        """
        possible_photos = PersonaQueryset.get_personas().filter(pk=pk)
        if len(possible_photos) == 0:
            return HttpResponseNotFound("La imagen que buscas no existe")
        elif len(possible_photos) > 1:
            return HttpResponse("Múltiples opciones", status=300)

        photo = possible_photos[0]
        context = {'photo': photo}
        return render(request, 'personas/detalle_persona.html', context)


class PersonaCreationView(View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Presenta el formulario para dar de alta a una persona
        :param request: objeto HttpRequest con los datos de la respuesta
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        persona_form = PersonaForm()
        context = {'form': persona_form, 'message': message}
        return render(request, 'personas/alta_persona.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Presenta el formulario para dar de alta una persona y, en caso de que la petición sea POST la valida
        y la crea en caso de que sea válida
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        persona_form = PersonaForm(request.POST)
        if persona_form.is_valid():
            new_persona = persona_form.save()
            persona_form = PersonaForm()
            message = 'Foto creada satisfactoriamente. <a href="{0}">Ver foto</a>'.format(
                reverse('detalles_persona', args=[new_persona.pk])
            )

        context = {'form': persona_form, 'message': message}
        return render(request, 'personas/alta_persona.html', context)