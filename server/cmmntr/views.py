from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from .models import Conversation, Comment


def json(obj, status=None):
	import json
	resp = HttpResponse(json.dumps(obj), mimetype='application/json')
	if status:
		resp.status_code = status
	return resp

def filterurl(url):
	"""filterurl(string) -> string
	Modifies the URL to reduce duplicate pages.
	"""
	#TODO: Sort query string, remove google's added parameters
	#TODO: Check fragment for JS pages (#!)
	return url

def convlist(request, _=None):
	url = filterurl(request.GET.get('url'))
	if not url:
		return #FIXME: Do something
	if not request.user.is_authenticated():
		return redirect_to_login(next=request.get_full_path())
	convs = Conversation.objects.filter(page=url)
	return render(request, 'convlist.html', {
		'conversations': convs,
		})
	
def conversation(request, cid):
	conv = get_object_or_404(Conversation, cid)
	if not request.user.is_authenticated():
		return redirect_to_login(next=request.get_full_path())
	return render(request, 'conversation.html', {
		'conversation': conv,
		})

def postcomment(request, cid):
	if not request.user.is_authenticated():
		return json({'status': 'error', 'error': ['LOGIN', 'User not logged in']}, status=403)
	if request.method != 'POST':
		return json({'status': 'error', 'error': ['NOTPOST', 'Not a POST request']}, status=405)
	
	if cid == 'new':
		conv = Conversation()
		conv.save()
	else:
		conv = get_object_or_404(Conversation, cid)
	
	url = filterurl(request.POST.get('url'))
	if not url:
		return json({'status': 'error', 'error': ['NOURL', 'No URL given']}, status=400)
	user = request.user
	text = request.POST['text']
	
	 = Comment(url=url, user=user, text=text)
	conv.save()
	return json({'status': 'ok'})
