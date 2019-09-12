from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse_lazy

from gameartist.apps.blog.models import Post
from gameartist.apps.landing.models import Categoria, Imagen
from .forms import ContactForm, FormularioForm



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

    categorias = Categoria.objects.filter().all()

    imagen = Imagen.objects.get(nombre="aa")

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

    post_list = Post.objects.filter(
        fecha_de_publicacion__lte=timezone.now()
    ).order_by('-fecha_de_publicacion')[:2]

    context = {
        'form': form,
        'post_list': post_list,
        'categorias': categorias,
        'imagen': imagen
    }

    return HttpResponse(template.render(context, request))


def mensaje_enviado(request):
    return render(request, 'landing/mensaje-enviado.html')


def solicitud_recibida(request):
    return render(request, 'landing/solicitud-recibida.html')


def enviar_email(subject, message):
    try:
        send_mail(subject, message, 'jlramos97@gmail.com', ['jlramos97@gmail.com', 'joseluis@quitiweb.com'])
        # send_mail(subject, message, 'contact@kradleco.es', ['rafa@quitiweb.com'])
    except BadHeaderError:
        return HttpResponse('Invalid header found')


def categoria(request, cat):
    template = loader.get_template('landing/categoria.html')

    categoria = Categoria.objects.filter(nombre=cat).first()

    imagenes = Imagen.objects.filter(categoria=categoria)

    context = {
        'categoria': categoria,
        'imagenes': imagenes
    }

    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('landing/about.html')
    context = {}

    return HttpResponse(template.render(context, request))
