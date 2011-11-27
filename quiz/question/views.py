#coding=utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from question.models import *
from datetime import datetime
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
		obj_list = Question.objects.all().order_by('-id')
	except:
		pass
	variables = RequestContext(request,{'obj_list':obj_list})
	return render_to_response("q_all.html",variables)

def quiz_create(requset):
	obj_list = []
	isCreated = False;
	quiz_info=""
	if requset.method == "POST":
		level = requset.POST['level']
		class_type = requset.POST['class_type']
		q_num = requset.POST['q_num']
		if( level and class_type and q_num ):
			## create a quiz with q_num questions.
			isCreated = True
			_class=""

			if(class_type=="e"):
				_class=u'容易'
			elif ( class_type=="m"):
				_class=u'中等'
			elif (class_type=="h"):
				_class=u'困难'
			
			quiz_info = u'考试等级：%s,  难度：%s,  题目数目：%s个' % (level,_class,q_num)
			## obj_list - generate here.
			## just for test
			obj_list = Question.objects.all().filter(level=level,class_type=class_type);
	variables = RequestContext(requset,{'obj_list':obj_list,'isCreated':isCreated,'quiz_info':quiz_info})
	return render_to_response("quiz-create.html",variables)

def quiz(request):
	result = 0
	r_count = 0
	w_count = 0
	w_obj_list = []
	user = request.user
	if request.method == "POST":
		info = request.POST
		for q in info:
			tmp = []
			try:
				tmp = Question.objects.get(id=q)
				### 目前仅支持单选类别，未来需要加上判断题目类型，如果
				### 是多选则进行for循环依次判断答案是否正确
				if ( info[q] == str(tmp.get_right_answer()[0].id) ):
					r_count += 1
				else:
					w_count += 1
					w_obj_list.append(tmp)
			except:
				pass
	
	if(r_count+w_count):
		result = 100*r_count/(r_count + w_count) 
	record = Record(user=user,pub_date=datetime.now(),result=result,notes="",)
	record.save()
	for w_q in w_obj_list:
		record.wrong_question.add(w_q)
	record.save()
	
	variables = RequestContext(request,{
		'result':result,
		'r_count':r_count,
		'w_count':w_count,
		'w_obj_list':w_obj_list,})
	return render_to_response("quiz.html",variables)

def show_record(request):
	user = request.user
	obj_list = Record.objects.all().order_by('-id')
	variables = RequestContext(request,{'obj_list':obj_list})
	return render_to_response("record.html",variables)
