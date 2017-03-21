from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	# The additional attributes we wish to include.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	# Override the __unicode__() method to return out something meaningful!
	# As using Python 2.7 defined __unicode__ too.
	def __str__(self):
		return self.user.username

	def __unicode__(self):
		return self.user.username

#I'm not sure if I'm doing this right -miles
class Sandwich(models.Model):
	#generates a unique id for each sandwich
	sid = models.CharField(primary_key=True,unique=True,max_length=10,default=uuid.uuid4)
	
	# maker of sandwich
	#maker = models.ForeignKey(UserProfile.user, on_delete=models.CASCADE)
	#commented out because migrations were failing

	title = models.CharField(max_length=100)
	description = models.CharField(max_length=2000) #length is arbitrary

	# Recipe of the sandwich, stored as a string of comma
	# separated ingredients (without any spaces).
	# Ex: "br,lt,tm,bc,ma,br" is, from bottom to top,
	# bread, lettuce, tomato, bacon, mayonnaise, bread
	recipe = models.CharField(max_length=100)


	picture = models.ImageField(upload_to='sandwich_images',blank=True)
	rating = models.IntegerField(default=5) #out of 5(?)

	#Date user created the sandwich used to get the latest sandwich
	created =  models.DateTimeField(default=timezone.now)

	
	def title_slug(self):
		return self.title.lower().replace(" ","-")

	def __unicode__(self):
		return self.title

	# methods to be implemented
