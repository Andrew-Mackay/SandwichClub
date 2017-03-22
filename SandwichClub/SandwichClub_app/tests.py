from django.test import TestCase
from SandwichClub_app.models import UserProfile, Sandwich
from django.contrib.staticfiles import finders
from django.core.urlresolvers import reverse
from django.test import Client

# used for setup, populates database
def runBasicSetup(self):
	try:
		from populate_sando import populate
		populate()
	except ImportError:
		print('The module populate_sando does not exist')
	except NameError:
		print('The function populate() does not exist or is not correct')
	except:
		print('Something went wrong in the populate() function')
		
	self.c = Client()
	

#---------------------------------------Page Tests-------------------------------------------------------
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
		
class ProfilePageTests(TestCase):
	def setUp(self):
		runBasicSetup(self)
			
	def test_profile_using_template(self):
		response = self.client.get(reverse('profile', kwargs ={'username': "SandwichGuru"}))
		self.assertTemplateUsed(response, 'profile.html')
		
class SandwichPageTests(TestCase):
	def setUp(self):
		runBasicSetup(self)
		
	def test_sandwich_page_using_template(self):
		sandwich = Sandwich.objects.get(title="Club sandwich")
		response = self.client.get(reverse('sandwich', kwargs ={'sid':sandwich.sid}))
		self.assertTemplateUsed(response, 'sandwich.html')

class RegistrationPageTests(TestCase):
	def setUp(self):
		self.c = Client()
		
	def test_registration_page_using_template(self):
		response = self.client.get(reverse('registration_register'))
		self.assertTemplateUsed(response, 'registration/registration_form.html')
		
	def test_valid_registration(self):
		response = self.c.post(reverse('registration_register'), {"username":'TestUser', 'email':'te.st@test.com',
												'password1':'12345qwerty', 'password2':'12345qwerty'})
		self.assertEqual(response.status_code, 302)
		
	def test_invalid_registration(self): #Note passwords are different
		response = self.c.post(reverse('registration_register'), {"username":'TestUser', 'email':'te.st@test.com',
												'password1':'12345qwerty', 'password2':'12345qwertye'})
		self.assertEqual(response.status_code, 200) #302 if successful registration
		
class LoginPageTests(TestCase):
	def setUp(self):
		runBasicSetup(self)
		
	def test_login_page_using_template(self):
		response = self.client.get("/accounts/login/")
		self.assertTemplateUsed(response, 'registration/login.html')
		
	def test_valid_login(self):
		response = self.c.post('/accounts/login/', {"username":'SandwichGuru', 'password':'12345qwerty'})
		self.assertEqual(response.status_code, 302)
		
	def test_invalid_login(self):
		response = self.c.post('/accounts/login/', {"username":'SandwichGuru', 'password':'wrongpassword'})
		self.assertEqual(response.status_code, 200)
		
class CreateSandwichPageTests(TestCase):
	def setUp(self):
		runBasicSetup(self)
		
	def test_create_sandwich_page_using_template(self):
		self.client.login(username = "SandwichGuru", password = "12345qwerty")
		response = self.client.get(reverse('create_sandwich'))
		self.assertTemplateUsed(response, 'create_sandwich.html')


#---------------------------------------End of Page Tests------------------------------------------------

class ModelTests(TestCase):

	def setUp(self):
		runBasicSetup(self)
	
	
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