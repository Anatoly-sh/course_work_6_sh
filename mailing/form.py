from crispy_forms.layout import Submit
from django import forms
from crispy_forms.helper import FormHelper


from mailing.models import Client


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

    class Meta:
        model = Client
        exclude = ('author',)
