from django.test import TestCase
from SandwichClub_app.models import UserProfile, Sandwich
# Create your tests here.

print("hello1")
class ModelTests(TestCase):
    print("hello2")
    def test_testing(self):
        print("Hello3")

    def setUp(self):
        print("Hello4")
        try:
            from populate_sando import populate
            print("hello5")
            populate()
            print("hello6")
        except ImportError:
            print('The module populate_sando does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function')
	
	
	
	def get_user_profile(self, name):
		from SandwichClub_app.models import UserProfile
		try:                  
			user = UserProfile.objects.get(name=name)
		except UserProfile.DoesNotExist:    
			user = None
		return user	



	def get_sandwich(self, name):
		from SandwichClub_app.models import Sandwich
		try:                  
			sandwich = Sandwich.objects.get(name=name)
		except Sandwich.DoesNotExist:    
			sandwich = None
		return sandwich


	def test_SandwichGuru_user_added(self):
		user = self.get_user_profile('SandwichGuru')
		self.assertIsNotNone(user)