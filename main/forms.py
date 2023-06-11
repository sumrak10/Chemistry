from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Question
from django.contrib.auth.models import User

class QuestionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'UserForm'
        self.helper.form_class = 'greenForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Отправить', css_class="btn-success"))
    class Meta:
        model = Question
        fields = ["fio", "contacts", "text"]

class ChangeUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChangeUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'UserForm'
        self.helper.form_class = 'greenForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Сохранить', css_class="btn-success"))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class UserLoginForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
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

class UserRegForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserRegForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'UserForm'
        self.helper.form_class = 'greenForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Зарегистрироваться', css_class="btn-success"))
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email"]
        widgets = {
            'password': forms.PasswordInput(),
        }