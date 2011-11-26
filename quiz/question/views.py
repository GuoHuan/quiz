from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from question.models import *

def show_question_by_id(request,q_id):
	obj = '' 
	try:
		obj = Question.objects.get(id=q_id)
	except:
		pass
	variables = RequestContext(request,{'obj':obj})
	return render_to_response("question.html",variables)

def show_all_questions(request):
	obj_list = []
	try:
		obj_list = Question.objects.all()
	except:
		pass
	variables = RequestContext(request,{'obj_list':obj_list})
	return render_to_response("q_all.html",variables)

def quiz_create(requset):
	if requset.method == "POST":
		level = requset.POST['level']
		class_type = requset.POST['class_type']
		q_num = requset.POST['q_num']
		if( level && class_type && q_num ):
			## create a quiz with q_num questions.
			obj_list = []
			variables = RequestContext(requset,{'obj_list':obj_list})
			return render_to_response("quiz.html",variables)
	return HttpResponseRedirect("/create_quiz/")

