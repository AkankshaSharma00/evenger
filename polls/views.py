from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import * 

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')
	
class DetailView(generic.DetailView):
	model = Question
	template_name = 'detail.html'

	def get_object(self):
		return get_object_or_404(Question, pk=self.kwargs['polls_id'])

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'results.html'

	def get_object(self):
		return get_object_or_404(Question, pk=self.kwargs['polls_id'])

def vote(request,polls_id):
	question = get_object_or_404(Question, pk=polls_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
			'question':question,
			'error_message':"You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('results',args=(question.id,)))
