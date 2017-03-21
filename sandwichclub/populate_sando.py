import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					  'SandwichClub.settings')
						
import django
import random
django.setup()
from SandwichClub_app.models import Sandwich, UserProfile, User
	
def populate():
	
	
	users =[
	{"username":"SandwichGuru",
	"website":"http://guru.hu/webshop.aspx"},
	{"username":"SandwichMasta",
	"website":"https://www.youtube.com/user/SANDWICHMASTA"},
	{"username":"TheWeeSandwichClub",
	"website":""},
	{"username":"TheBritishSandwichAssociation",
	"website":"http://new.sandwich.org.uk/"},
	{"username":"SandwichMania",
	"website":""},
	]
	sandwiches=[
	{"title" : "Triple-decker steak sandwich",
	"description":"The king of sandwiches, this meaty skyscraper is a Ramsay gastro classic, perfect with a glass of peppery Pinotage",
	"recipe":"bread,mayonnaise,garlic,lettuce,beef,onion,beef,tomato,beef,bread"},
	{"title" : "Salt beef club",
	"description":"An indulgent solo supper of a layered sandwich with sliced beef and creamy dressing ",
	"recipe":"bread,oliveoil,mayonnaise,mustard,chive,avocado,lettuce,beef,bread"},
	{"title" : "BLT - Bacon Lettuce Tomato",
	"description":"Nothing fancy, just delicious - this is the definitive recipe for a no-nonsense Bacon, Lettuce and Tomato sandwich.",
	"recipe":"bread,lettuce,tomato,bacon,mayonnaise,bread"},
	{"title" : "Best-ever crab sandwich",
	"description":"A classic crab sandwich made a bit more substantial with a few of Barney's favourite flavours",
	"recipe":"bread,mayonnaise,ketchup,mustard,pepper,crab,bread"},
	{"title" : "Green club sandwich",
	"description":"This healthy sandwich is packed full of goodness to keep you going until dinner",
	"recipe":"bread,houmous,avocado,tomato,bread"},
	{"title" : "Camembert sandwich",
	"description":"A cheese sandwich that is anything but ordinary - oozing with camembert and topped with cranberry sauce to give it a Christmas kick",
	"recipe":"bread,brie,cranberrysauce,vinegar,butter,bread"},
	{"title" : "Roast Pork and Pickled Cucumber Sandwich",
	"description":"Make quick pickles by combining cucumber, vinegar, oil, brown sugar, salt, and pepper; they give the sandwich an extra zing",
	"recipe":"bread,pickle,porkloin,pepper,mayonnaise,bread"},
	{"title" : "Open prawn cocktail sandwich",
	"description":"A lighter version of the classic prawn cocktail, treat yourself to this satisfying yet low-fat lunch",
	"recipe":"bread,prawn,cucumber,cherrytomato,lemon,dill,ketchup,mayonnaise,bread"},
	{"title" : "Club sandwich",
	"description":"This layered sandwich, a favourite of gastro-pubs across the country, makes a tasty meal for one",
	"recipe":"bread,bacon,chicken,salad,boiledegg,tomato,mayonnaise,bread"},
	{"title" : "Turkey & bacon club",
	"description":"Satisfy your hunger with this tasty and hearty club sandwich, perfect for weekend breakfast",
	"recipe":"bread,bacon,turkey,butter,mayonnaise,mustard,lettuce,avocado,bread"},]
	
	
	users2 = []
	for usar in users:
		users2.append(add_user(usar["username"],usar["website"]))
	
	for sando in sandwiches:
		i = random.randint(0, len(users2)-1)
		r = random.randint(0,5)
		add_sando(sando['title'],sando['description'],sando['recipe'], users2[i], r)
		
	for uzar in UserProfile.objects.all():
		print("- {0}".format(str(uzar)))
		
	for sandowitch in Sandwich.objects.all():
		print("- {0}".format(str(sandowitch)))
		
def add_sando(title,description,recipe,maker,rating):
	print(title, description, recipe, maker)
	s = Sandwich.objects.get_or_create(title = title, maker = maker)[0]
	s.description = description
	s.recipe = recipe
	s.rating = rating
	s.save()
	return s
	
def add_user(username,website):
	user = User.objects.get_or_create(username = username)[0]
	#print(user)
	u = UserProfile.objects.get_or_create(user= user)[0]
	#print(u)
	u.website = website
	#print (u.website)
	u.save()
	return u
	
if __name__ == '__main__':
	print('Starting population script...')
	populate()