from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	#Note:Notice that we didn't put the parentheses after timezone.now 
	#  since we don't actually want to execute that function at that point, we just want to pass in the actual function as default value
	date_posted = models.DateTimeField(default = timezone.now)
	#Note: User created post and then the user was deleted then do we want to delete the post
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):  #Note: Represent the object by its title
		return self.title

