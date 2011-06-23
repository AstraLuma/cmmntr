from .models import Conversation, Comment

def conversation(request):
	url = request.GET.('url')
	if not url:
		return #FIXME: Do something
	
