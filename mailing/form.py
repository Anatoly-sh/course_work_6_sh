from crispy_forms.layout import Submit
from django import forms
from crispy_forms.helper import FormHelper


from mailing.models import Client, MailSetting


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

    class Meta:
        model = Client
        exclude = ('author',)


class MailSettingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MailSettingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

    class Meta:
        model = MailSetting
        exclude = ('launched_date', 'author', 'status',)
