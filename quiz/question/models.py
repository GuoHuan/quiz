#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	LEVEL_CHOICES = (
		(u'1',u'等级一'),
		(u'2',u'等级二'),
		(u'3',u'等级三'),
		)
	CLASS_TYPE_CHOICES = (
		(u'e',u'容易'),
		(u'm',u'中等难度'),
		(u'h',u'困难'),
	)
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	description = models.TextField()
	right_count = models.IntegerField()
	wrong_count = models.IntegerField()
	level = models.CharField(max_length=1,choices=LEVEL_CHOICES) #level 1 ; level 2 ;etc...
	class_type = models.CharField(max_length=1,choices= CLASS_TYPE_CHOICES) # easy ; difficult ; hard
	pub_date = models.DateTimeField()

	def __unicode__(self):
		return " %s " % self.title
	
	def get_answer_choice(self):
		return self.answer_set.all()
	def get_right_answer(self):
		return self.answer_set.filter(isRight=True)


class Answer(models.Model):
	question = models.ForeignKey(Question)
	title = models.CharField(max_length=100)
	isRight = models.BooleanField()

	def __unicode__(self):
		return "%s" % self.title

class Record(models.Model):
	user = models.ForeignKey(User)
	pub_date = models.DateTimeField()
	result = models.IntegerField()
	wrong_question = models.ManyToManyField(Question)
	notes = models.TextField()

	def __unicode__(self):
		return "result:%d @ %s " % (self.result , self.pub_date)
	def get_time(self):
		return "%s:%s:%s" % (self.pub_date.hour,self.pub_date.minute,self.pub_date.second)


