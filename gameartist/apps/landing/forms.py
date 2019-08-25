from django import forms

from .models import Solicitud, Target, Mercado, Servicios

MARCA = 'MARCA'
ESPACIO = 'ESPACIO'
SERVICIO = 'SERVICIO'

MARCA_CHOICES = (
    (MARCA, 'Marca'),
    (ESPACIO, 'Espacios (Offline/Online)'),
    (SERVICIO, 'Servicio'),
)


class CustomRadioSelect(forms.RadioSelect):
    option_template_name = 'landing/custom/radio-option-custom.html'


class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    option_template_name = 'landing/custom/checkbox-multiple-custom.html'


class FormularioForm(forms.ModelForm):
    quien_eres = forms.ChoiceField(
        choices=MARCA_CHOICES,
        widget=CustomRadioSelect()
    )

    servicios = forms.ModelMultipleChoiceField(
        queryset=Servicios.objects.all(),
        widget=CustomCheckboxSelectMultiple(),
        required=False
    )

    mercado = forms.ModelMultipleChoiceField(
        queryset=Mercado.objects.all(),
        widget=CustomCheckboxSelectMultiple(),
        required=False
    )

    target = forms.ModelMultipleChoiceField(
        queryset=Target.objects.all(),
        widget=CustomCheckboxSelectMultiple(),
        required=False
    )

    que_buscas = forms.ChoiceField(
        choices=MARCA_CHOICES,
        widget=CustomRadioSelect()
    )

    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'placeholder': 'email@ejemplo.com'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Empresa Ejemplo'}), required=False)

    class Meta:
        model = Solicitud
        fields = {'quien_eres', 'servicios', 'mercado', 'target', 'que_buscas', 'email', 'nombre',}


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'email@ejemplo.com'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Escribe aquí tu duda o comentario'}), required=True)