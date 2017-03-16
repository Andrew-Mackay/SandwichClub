from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

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
	# Title of the sandwich, as a string
	title = models.CharField(max_length=100)

	# Recipe of the sandwich, stored as a string of comma
	# separated ingredients (without any spaces).
	# Ex: "br,lt,tm,bc,ma,br" is, from bottom to top,
	# bread, lettuce, tomato, bacon, mayonnaise, bread
	recipe = models.CharField(max_length=100)

	# Other attributes
	picture = models.ImageField(upload_to='sandwich_images', blank=False)
	description = models.CharField(max_length=2000) #length is arbitrary
	rating = models.IntegerField() #out of 5(?)

	def title_slug(self):
		return self.title.lower().replace(" ","-")

	# methods to be implemented
