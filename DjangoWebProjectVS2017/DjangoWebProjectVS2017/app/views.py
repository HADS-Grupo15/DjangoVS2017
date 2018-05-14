"""
AQUI VAN LAS FUNCIONES 
"""

from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http.response import HttpResponse, Http404
from django.http import HttpResponseRedirect, HttpResponse
from .models import QuizQuestion,QuizChoice,Question,Choice,User
from django.template import loader
from django.core.urlresolvers import reverse
from app.forms import QuizQuestionForm,QuizChoiceForm,QuestionForm, ChoiceForm,UserForm
from django.shortcuts import redirect
import json


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Autor de la web',
            'message':'Datos de contacto',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = {
                'title':'Lista de preguntas de la encuesta',
                'latest_question_list': latest_question_list,
              }
    return render(request, 'polls/index.html', context)

def Quiz_index(request):
    latest_question_list = QuizQuestion.objects.order_by('-pub_date')
    template = loader.get_template('quiz/index.html')
    context = {
                'title':'Lista de preguntas del Quiz',
                'latest_question_list': latest_question_list,
              }
    return render(request, 'quiz/index.html', context)

def detail(request, question_id):
     question = get_object_or_404(Question, pk=question_id)
     #Respuestas asociadas a la pregunta es un String que se colocará en el tag del title, y en el tag de question el valor de question#
     return render(request, 'polls/detail.html', {'title':'Respuestas asociadas a la pregunta:','question': question})

def Quiz_detail(request, question_id):
     question = get_object_or_404(QuizQuestion, pk=question_id)
     #Respuestas asociadas a la pregunta es un String que se colocará en el tag del title, y en el tag de question el valor de question#
     return render(request, 'quiz/detail.html', {'title':'Respuestas asociadas a la pregunta:','question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'title':'Resultados de la pregunta:','question': question})

def Quiz_results(request, question_id):
    question = get_object_or_404(QuizQuestion, pk=question_id)
    return render(request, 'quiz/results.html', {'title':'Resultados de la pregunta:','question': question})


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Vuelve a mostrar el form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "ERROR: No se ha seleccionado una opcion",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Siempre devolver un HttpResponseRedirect despues de procesar
        # exitosamente el POST de un form. Esto evita que los datos se
        # puedan postear dos veces si el usuario vuelve atras en su browser.
        return HttpResponseRedirect(reverse('results', args=(p.id,)))

def choice_add(request, question_id):
        question = Question.objects.get(id = question_id)
        if request.method =='POST':
            form = ChoiceForm(request.POST)
            if form.is_valid():
                choice = form.save(commit = False)
                choice.question = question
                choice.vote = 0
                choice.save() 
                return render(request, 'polls/choice_new.html', {'title':'Pregunta:'+ question.question_text,'form': form})
                #form.save()
        else: 
            form = ChoiceForm()
        #return render_to_response ('choice_new.html', {'form': form, 'poll_id': poll_id,}, context_instance = RequestContext(request),)
        return render(request, 'polls/choice_new.html', {'title':'Pregunta:'+ question.question_text,'form': form})

def question_new(request):
        if request.method == "POST":
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.pub_date=datetime.now()
                question.save()
                #return redirect('detail', pk=question_id)
                #return render(request, 'polls/index.html', {'title':'Respuestas posibles','question': question})
        else:
            form = QuestionForm()
        return render(request, 'polls/question_new.html', {'form': form})

def Quiz_question_new(request):
        if request.method == "POST":
            form = QuizQuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.pub_date=datetime.now()
                question.save()
                #return redirect('qindex')
                #return render(request, 'quiz/index.html', {'question': question})
        else:
            form = QuizQuestionForm()
        return render(request, 'quiz/question_new.html', {'form': form})

def Quiz_choice_add(request, question_id):
        q = QuizQuestion.objects.get(id = question_id)
        error_message = ''
        if request.method =='POST':
            form = QuizChoiceForm(request.POST)
            if QuizChoice.objects.filter(question=q).count() < 4:
                if form.is_valid():
                    choice = form.save(commit = False)
                    choice.question = q
                    #choice.correctAnswer = False
                    choice.vote = 0
                    choice.save()
                    #('qdetail')
                    #return render(request, 'quiz/detail.html', {'title':'Pregunta:'+ question.question_text,'topic':'Tema: '+question.topic,'form': form})#añadirle el flag(?)#
            else:
              error_message = 'ERROR: No se pueden guardar más de 4 opciones por pregunta'
                
        else: 
            form = QuizChoiceForm()
        #return render_to_response ('choice_new.html', {'form': form, 'poll_id': poll_id,}, context_instance = RequestContext(request),)
        return render(request, 'quiz/choice_new.html', {'title':'Pregunta:'+ q.question_text,'topic':'Tema: '+q.topic,'form': form, 'error_message': error_message})#añadirle el flag(?)#

def Quiz_vote(request, question_id):
    p = get_object_or_404(QuizQuestion, pk=question_id)
    try:
        selected_choice = p.quizchoice_set.get(pk=request.POST['choice'])
    except (KeyError, QuizChoice.DoesNotExist):
        # Vuelve a mostrar el form.
        return render(request, 'quiz/detail.html', {
            'question': p,
            'error_message': "ERROR: No se ha seleccionado una opcion",
        })
    else:
        if request.user.is_authenticated():
            try:
                previous_correct_choice = p.quizchoice_set.get(correctAnswer=True)
            except (QuizChoice.DoesNotExist):
                previous_correct_choice = None
            if previous_correct_choice:
                previous_correct_choice.correctAnswer = False
                previous_correct_choice.save()
            selected_choice.correctAnswer = True
            selected_choice.save()
        else:
            selected_choice.votes += 1
            selected_choice.save()
        # Siempre devolver un HttpResponseRedirect despues de procesar
        # exitosamente el POST de un form. Esto evita que los datos se
        # puedan postear dos veces si el usuario vuelve atras en su browser.
        return HttpResponseRedirect(reverse('qresults', args=(p.id,)))

def chart(request, question_id):
    q=Question.objects.get(id = question_id)
    qs = Choice.objects.filter(question=q)
    dates = [obj.choice_text for obj in qs]
    counts = [obj.votes for obj in qs]
    context = {
        'dates': json.dumps(dates),
        'counts': json.dumps(counts),
    }

    return render(request, 'quiz/grafico.html', context)

#def Quiz_chart(request, question_id):
#    q=QuizQuestion.objects.get(id = question_id)
#    qs = QuizChoice.objects.filter(question=q)
#    dates = [obj.choice_text for obj in qs]
#    counts = [obj.votes for obj in qs]
#    context = {
#        'dates': json.dumps(dates),
#        'counts': json.dumps(counts),
#    }

    return render(request, 'quiz/grafico.html', context)

def user_new(request):
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                #return redirect('detail', pk=question_id)
                #return render(request, 'polls/index.html', {'title':'Respuestas posibles','question': question})
        else:
            form = UserForm()
        return render(request, 'polls/user_new.html', {'form': form})

def users_detail(request):
    latest_user_list = User.objects.order_by('email')
    template = loader.get_template('polls/users.html')
    context = {
                'title':'Lista de usuarios',
                'latest_user_list': latest_user_list,
              }
    return render(request, 'polls/users.html', context)