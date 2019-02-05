# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post

 

def post_list(request):
	posts=Post.objects.all()
	return render(request, 'blog/post_list.html',{'posts': posts})#posts is django template tags 
	# return HttpResponse("hey")


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})




