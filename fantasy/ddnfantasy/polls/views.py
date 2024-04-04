# views.py

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Choice, Question
from django.http import HttpResponse, JsonResponse
from teams.models import Team
from django.http import JsonResponse

def index(request):
    latest_question_list = Question.objects.all()[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        try:
            selected_choice_id = request.POST['choice']
            selected_choice = question.choices.get(pk=selected_choice_id)
        except (KeyError, Choice.DoesNotExist):
            return JsonResponse({'success': False, 'error': "Invalid choice selection."})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Mark that the user has voted by setting has_voted to True
            request.session['has_voted'] = True
            # Sort choices based on vote counts
            sorted_choices = question.choices.all().order_by('-votes')
            # Retrieve the latest vote counts for all choices
            vote_counts = {choice.id: choice.votes for choice in sorted_choices}
            return JsonResponse({'success': True, 'vote_counts': vote_counts})
    else:
        return JsonResponse({'success': False, 'error': "Method not allowed."}, status=405)
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
