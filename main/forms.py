from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.contrib.auth.models import User

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'UserForm'
        self.helper.form_class = 'greenForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Войти', css_class="btn-success"))
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            'password': forms.PasswordInput(),
        }