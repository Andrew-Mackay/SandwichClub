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
	"description":"The king of sandwiches, this meaty skyscraper is a Ramsay gastro classic, perfect with a glass of Black Peppery Pinotage",
	"recipe":"Bread,Mayonnaise,Garlic,Lettuce,Beef,Onion,Beef,Tomato,Beef,Bread",
	"picture":"/sandwich_images/tripledeckerbeef.jpg"},
	{"title" : "Salt Beef club",
	"description":"An indulgent solo supper of a layered sandwich with sliced Beef and creamy dressing ",
	"recipe":"Bread,Olive Oil,Mayonnaise,Mustard,Chive,Avocado,Lettuce,Beef,Bread",
	"picture":"/sandwich_images/saltbeefclub.jpg"},
	{"title" : "BLT - Bacon Lettuce Tomato",
	"description":"Nothing fancy, just delicious - this is the definitive recipe for a no-nonsense Bacon, Lettuce and Tomato sandwich.",
	"recipe":"Bread,Lettuce,Tomato,Bacon,Mayonnaise,Bread",
	"picture":"/sandwich_images/blt.jpg"},
	{"title" : "Best-ever Crab sandwich",
	"description":"A classic Crab sandwich made a bit more substantial with a few of Barney's favourite flavours",
	"recipe":"Bread,Mayonnaise,Ketchup,Mustard,Black Pepper,Crab,Bread",
	"picture":"/sandwich_images/bestCrab.jpg"},
	{"title" : "Green club sandwich",
	"description":"This healthy sandwich is packed full of goodness to keep you going until dinner",
	"recipe":"Bread,Houmous,Avocado,Tomato,Bread",
	"picture":"/sandwich_images/greenclub.jpg"},
	{"title" : "Camembert sandwich",
	"description":"A cheese sandwich that is anything but ordinary - oozing with camembert and topped with cranberry sauce to give it a Christmas kick",
	"recipe":"Bread,Brie,Cranberry Sauce,Vinegar,Butter,Bread",
	"picture":"/sandwich_images/camembert.jpg"},
	{"title" : "Roast Pork and Pickled Cucumber Sandwich",
	"description":"Make quick Pickles by combining cucumber, Vinegar, oil, brown sugar, salt, and Black Pepper; they give the sandwich an extra zing",
	"recipe":"Bread,Pickle,Pork Loin,Black Pepper,Mayonnaise,Bread",
	"picture":"/sandwich_images/roastporkcucumber.jpg"},
	{"title" : "Open prawn cocktail sandwich",
	"description":"A lighter version of the classic prawn cocktail, treat yourself to this satisfying yet low-fat lunch",
	"recipe":"Bread,Prawn,Cucumber,Tomato,Lemon,Dill,Ketchup,Mayonnaise,Bread",
	"picture":"/sandwich_images/openprawn.jpg"},
	{"title" : "Club sandwich",
	"description":"This layered sandwich, a favourite of gastro-pubs across the country, makes a tasty meal for one",
	"recipe":"Bread,Bacon,Chicken,Salad,Boiled Egg,Tomato,Mayonnaise,Bread",
	"picture":"/sandwich_images/club-sandwich.jpg"},
	{"title" : "Turkey & Bacon club",
	"description":"Satisfy your hunger with this tasty and hearty club sandwich, perfect for weekend breakfast",
	"recipe":"Bread,Bacon,Turkey,Butter,Mayonnaise,Mustard,Lettuce,Avocado,Bread",
	"picture":"/sandwich_images/turkeybaconclub.jpg"},]


	users2 = []
	for usar in users:
		users2.append(add_user(usar["username"],usar["website"]))

	for sando in sandwiches:
		i = random.randint(0, len(users2)-1) # used to select random user to assign sandwich to
		r = random.randint(0,5) # used to provide sandwiches with a randomized rating
		add_sando(sando['title'],sando['description'],sando['recipe'],sando['picture'], users2[i], r)


def add_sando(title,description,recipe,picture,maker,rating):
	s = Sandwich.objects.get_or_create(title = title, maker = maker)[0]
	s.description = description
	s.recipe = recipe
	s.rating = rating
	s.picture = picture
	s.save()
	return s

def add_user(username,website):
	user = User.objects.get_or_create(username = username)[0]
	user.set_password("12345qwerty")
	user.save()
	u = UserProfile.objects.get_or_create(user= user)[0]
	u.website = website
	u.save()
	return u

if __name__ == '__main__':
	print('Starting population script...')
	populate()
	print('Population complete.')
