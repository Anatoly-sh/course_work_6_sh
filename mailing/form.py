from crispy_forms.layout import Submit, Layout
from django import forms
from crispy_forms.helper import FormHelper


from mailing.models import Client


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        # exclude = ('author',)

