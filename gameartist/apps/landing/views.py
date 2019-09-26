from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from gameartist.apps.blog.models import Post
from .models import Categoria, Imagen, About, Header, Empresa
from .forms import ContactForm


def index(request):
    template = loader.get_template('landing/index.html')

    categorias = Categoria.objects.all()
    header = Header.objects.all().first()
    empresas = Empresa.objects.all()

    post_list = Post.objects.filter(
        fecha_de_publicacion__lte=timezone.now()
    ).order_by('-fecha_de_publicacion')[:2]

    context = {
        'post_list': post_list,
        'categorias': categorias,
        'header': header,
        'empresas': empresas,
    }

    return HttpResponse(template.render(context, request))


def mensaje_enviado(request):
    return render(request, 'landing/mensaje-enviado.html')


def enviar_email(subject, message):
    try:
        # send_mail(subject, message, 'jlramos97@gmail.com', ['jlramos97@gmail.com', 'joseluis@quitiweb.com'])
        send_mail(subject, message, 'contact@gameartist.es', ['rafa@quitiweb.com'])
    except BadHeaderError:
        return HttpResponse('Invalid header found')


def categoria(request, cat):
    template = loader.get_template('landing/categoria.html')

    categoria = Categoria.objects.filter(id=cat).first()

    imagenes = Imagen.objects.filter(categoria=categoria)

    context = {
        'categoria': categoria,
        'imagenes': imagenes
    }

    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('landing/about.html')

    about_info = About.objects.filter(activo=True).first()

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'GameArtist formulario de contacto'
            from_email = form.cleaned_data['from_email']
            message = 'Email recibido de: ' + from_email + '\n\n' + form.cleaned_data['message']

            enviar_email(subject, message)

            form = ContactForm()
            return redirect('mensaje-enviado')
        else:
            print('Error en el formulario')

    context = {
        'about': about_info,
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def portfolio(request):
    template = loader.get_template('landing/portfolio.html')

    categorias = Categoria.objects.all()
    header = Header.objects.all().first()

    context = {
        'categorias': categorias,
        'header': header,
    }

    return HttpResponse(template.render(context, request))
