from crispy_forms.layout import Submit, Layout
from django import forms
from crispy_forms.helper import FormHelper


from mailing.models import Client, MailSetting


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


class MailSettingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MailSettingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'


class MailSettingForm(forms.ModelForm):
    class Meta:
        model = MailSetting
        # fields = '__all__'
        exclude = ('launched_date',)
