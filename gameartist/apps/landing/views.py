from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import ContactForm, FormularioForm

from ..blog import models

# def index(request):
#     return render(request, 'landing/index.html')


def formulario(request):
    template = loader.get_template('landing/formulario.html')

    if request.method == 'GET':
        form = FormularioForm()
    else:
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()

            subject = 'Kradleco nueva solicitud recibida'
            from_email = form.cleaned_data['email']
            nombre = form.cleaned_data['nombre']
            enlace = 'https://www.kradleco.es/admin/landing/solicitud/'
            message = 'Solicitud recibida de: ' + nombre + '\nCon email: ' + from_email +\
                      '\n\nPara ver dicha solicitud, visita: ' + enlace

            enviar_email(subject, message)

            form = FormularioForm()

            return redirect('solicitud-recibida')
        else:
            print('Error en el formulario')

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def index(request):
    template = loader.get_template('landing/index.html')

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Kradleco formulario de contacto'
            from_email = form.cleaned_data['from_email']
            message = 'Email recibido de: ' + from_email + '\n\n' + form.cleaned_data['message']

            enviar_email(subject, message)

            form = ContactForm()
            return redirect('mensaje-enviado')
        else:
            print('Error en el formulario')

    post_list = models.Post.objects.filter(
        fecha_de_publicacion__lte=timezone.now()
    ).order_by('-fecha_de_publicacion')[:6]

    context = {
        'form': form,
        'post_list': post_list,
    }

    return HttpResponse(template.render(context, request))


def mensaje_enviado(request):
    return render(request, 'landing/mensaje-enviado.html')


def solicitud_recibida(request):
    return render(request, 'landing/solicitud-recibida.html')


def enviar_email(subject, message):
    try:
        send_mail(subject, message, 'contact@kradleco.es', ['info@kradleco.es', 'rafa@quitiweb.com'])
        # send_mail(subject, message, 'contact@kradleco.es', ['rafa@quitiweb.com'])
    except BadHeaderError:
        return HttpResponse('Invalid header found')
