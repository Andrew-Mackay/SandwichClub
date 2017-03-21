import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SandwichClub.settings')

import django
django.setup()
from SandwichClub_app.models import Sandwich

def populate():

    sandwiches = [
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
        "recipe":"bread,bacon,turkey,butter,mayonnaise,mustard,lettuce,avocado,bread"},
        ]

    for sando in sandwiches:
        add_sando(sando['title'],sando['description'],sando['recipe'])

    for sandowitch in Sandwich.objects.all():
        print("- {0}".format(str(sandowitch)))

#####
def add_sando(title,description,recipe):
              s = Sandwich.objects.get_or_create(title = title)[0]
              s.description = description
              s.recipe = recipe
              s.save()
              return s

if __name__ == '__main__':
    print('Starting population script...')
    populate()
