from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.contrib.auth.models import User

@login_required
def index(request):
	return HttpResponse('this is index. welcome ' + request.user.get_full_name())
	#return HttpResponseRedirect('/play/')

def logout_view(request):
	logout(request)
	HttpResponse("Logged out!")
	return HttpResponseRedirect('/login/')

@login_required
def hello(request):
	return HttpResponse('hellow newmann')
