from django import forms


class CustomRadioSelect(forms.RadioSelect):
    option_template_name = 'landing/custom/radio-option-custom.html'


class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    option_template_name = 'landing/custom/checkbox-multiple-custom.html'


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'email@ejemplo.com'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Escribe aquí tu duda o comentario'}),
                              required=True)
