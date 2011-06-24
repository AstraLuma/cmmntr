from django.shortcuts import render, get_object_or_404, redirect
from .models import Conversation, Comment

def filterurl(url):
	"""filterurl(string) -> string
	Modifies the URL to reduce duplicate pages.
	"""
	#TODO: Sort query string, remove google's added parameters
	#TODO: Check fragment for JS pages (#!)
	return url

def convlist(request, _=None):
	url = filterurl(request.GET.('url'))
	if not url:
		return #FIXME: Do something
	if not request.user.is_authenticated():
		return redirect('django.contrib.auth.views.login')
	convs = Conversation.objects.filter(page=url)
	return render(request, 'convlist.html', {
		'conversations': convs,
		})
	
def conversation(request, cid):
	conv = get_object_or_404(Conversation, cid)
	if not request.user.is_authenticated():
		return redirect('django.contrib.auth.views.login')
	return render(request, 'conversation.html', {
		'conversation': conv,
		})

def postcomment(request):
	if not request.user.is_authenticated():
		return redirect('django.contrib.auth.views.login')
	if request.method != 'POST':
		return #FIXME: Do something
	url = filterurl(request.POST.get('url'))
	if not url:
		return #FIXME: Do something
	user = request.user
	text = request.POST['text']
	conv = Conversation(url=url, user=user, text=text)
	conv.save()
	return ""
