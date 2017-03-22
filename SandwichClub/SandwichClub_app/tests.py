from django.test import TestCase
from SandwichClub_app.models import UserProfile, Sandwich
from django.contrib.staticfiles import finders
from django.core.urlresolvers import reverse
# Create your tests here.


class GeneralTests(TestCase):

	def test_test(self):#delete me plz
		test = True
		self.assertTrue(test)

class IndexPageTests(TestCase):

	def test_index_contains_welcome_message(self):
		response = self.client.get(reverse('index'))
		self.assertIn(b'Welcome to Sandwich Club!', response.content)
		
	def test_index_using_template(self):
		response = self.client.get(reverse('index'))
		self.assertTemplateUsed(response, 'index.html')

class AboutPageTests(TestCase):

	def test_about_using_template(self):
		response = self.client.get(reverse('about'))
		self.assertTemplateUsed(response, 'about.html')

class ModelTests(TestCase):

	def setUp(self):
		try:
			from populate_sando import populate
			populate()
		except ImportError:
			print('The module populate_sando does not exist')
		except NameError:
			print('The function populate() does not exist or is not correct')
		except:
			print('Something went wrong in the populate() function')
	
	
	
	def get_user_profile(self, name):
		from SandwichClub_app.models import UserProfile, User
		try:                  
			user = User.objects.get(username=name)
		except UserProfile.DoesNotExist:    
			user = None
		return user	



	def get_sandwich(self, name):
		from SandwichClub_app.models import Sandwich
		try:
			sandwich = Sandwich.objects.get(title=name)
		except Sandwich.DoesNotExist:    
			sandwich = None
		return sandwich


	def test_SandwichGuru_user_added(self):
		user = self.get_user_profile('SandwichGuru')
		self.assertIsNotNone(user)
		
	def test_Club_sandwich_added(self):
		sandwich = self.get_sandwich("Club sandwich")
		self.assertIsNotNone(sandwich)