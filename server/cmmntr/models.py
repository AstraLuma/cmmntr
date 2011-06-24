from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
	page = models.URLField(primary_key=True)
	founder = models.ForeignKey(User)
	topic = models.CharField(length=32)
	
	def __unicode__(self):
		return self.topic
	
	def clean_topic(self):
		if not self.topic:
			t = self.comment_set.order_by('date')[0] # First comment made
			t = t.text # Grab the text
			try:
				t = t.text[:t.find('.')+1] # Get the first sentence ...
			except ValueError: # ... if there's a period
				pass
			self.topic = t # it'll truncate itself
			if self.topic != t: # Got shortened
				# Add ellipses
				self.topic = self.topic[:-1] + u"\u2026"

	@models.permalink
	def get_absolute_url(self):
		return ('cmmntr.views.conversation', self.id)

class Comment(models.Model):
	conversation = models.ForeignKey(Conversation)
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	#parent = models.ForeignKey('self', null=True, blank=True) #Don't think I want to do this for now
	text = models.TextField()
