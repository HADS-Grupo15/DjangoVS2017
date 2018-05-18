"""
Definition of forms.
"""

from django import forms
from app.models import QuizQuestion,QuizChoice,Question,Choice,User,Topic
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class QuestionForm(forms.ModelForm):

        class Meta:
            model = Question
            fields = ('question_text',)

class ChoiceForm(forms.ModelForm):

        class Meta:
            model = Choice
            fields = ('choice_text',)

class QuizQuestionForm(forms.ModelForm):

        class Meta:
            model = QuizQuestion
            fields = ('question_text','topic')

class QuizChoiceForm(forms.ModelForm):

        class Meta:
            model = QuizChoice
            fields = ('choice_text',)

class UserForm(forms.ModelForm):

        class Meta:
            model = User
            fields = ('email','nombre',)

#TOPIC_CHOICES_INCL_ALL = (
#    #(lo que se guardará, lo que se mostrará),
#    ('', 'Todos'),
#    ('Trabajo_final_HADS','Trabajo final HADS'),
#    ('Evaluación_HADS', 'Evaluación HADS'),
#    ('Informática','Informática'),
#    ('Otro','Otro'),
#)

#class TopicForm(forms.Form):
#    topic = forms.CharField(label='Ordenar por tema:', widget=forms.Select(choices=TOPIC_CHOICES_INCL_ALL))

class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = ('topic',)


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
