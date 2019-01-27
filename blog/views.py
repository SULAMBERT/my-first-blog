# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def post_list(request):
	posts=Post.objects.all().order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts': posts})#posts is django template tags 
	# return HttpResponse("hey")

