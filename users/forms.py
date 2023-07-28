from django import forms
from django.contrib.auth.forms import UserChangeForm

from users.models import User


class CastomUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):        # скрыть в форме пароль
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()

