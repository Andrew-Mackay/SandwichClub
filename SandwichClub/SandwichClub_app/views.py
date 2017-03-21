from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from django.core.urlresolvers import reverse
from SandwichClub_app.forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from SandwichClub_app.models import *
from django.db.models import Q
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    context_dict = {}
    """ context needed (?)
        Sandwich of the week
        popular sandwiches/users/idk
    """
    response = render(request, 'index.html', context=context_dict)
    return response

def login(request):
	return HttpResponse("Login page")

@login_required
def create_sandwich(request):
    form = SandwichForm()
    #return render(request, 'create_sandwich.html', context={'thing':'thing'})
    if request.method == 'POST':
        form = SandwichForm(request.POST, request.FILES)
        if form.is_valid():
            new_sandwich = form.save(commit=False)
            #user = request.user
            userprofile = UserProfile.objects.get(user=request.user)
            print userprofile
            new_sandwich.maker = userprofile
            #print new_sandwich
            print new_sandwich.maker
            new_sandwich.save()
            return redirect('sandwich',new_sandwich.sid)
        else:
            print(form.errors)

    context_dict = {'form':form}
    return render(request, 'create_sandwich.html', context=context_dict)


def sandwich(request,sid):
    try:
        sandwich = Sandwich.objects.get(sid=sid)
    except Sandwich.DoesNotExist:
        return render(request, 'sandwich.html', context={'dne':'True'})

    context_dict = {'sandwich':sandwich}
    return render(request, 'sandwich.html', context=context_dict )

def search(request):
    query = request.GET.get('query')
    sandwich_list = Sandwich.objects.filter(
        Q(title__icontains =query) |
        Q(description__icontains =query)|
        Q(recipe__icontains =query)
        ).distinct().order_by("-created")

    paginator = Paginator(sandwich_list, 5) # Show 5 sandos per page
    page = request.GET.get('page')
    
    try:
        sandwich = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        sandwich = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        sandwich = paginator.page(paginator.num_pages)

    context_dict = {'sandwiches':sandwich}
	
    return render(request, 'search.html', context=context_dict)

def top_ten(request):
    ranking = Sandwich.objects.order_by('-rating')[:10]
    context_dict= {'rankings': ranking}

    return render(request, 'top_ten.html', context=context_dict)

def latest(request):
    recent = Sandwich.objects.order_by('-created')[:5]
    context_dict= {'latest': recent}

    return render(request, 'latest.html', context=context_dict)

def randomsando(request):
    idlist = Sandwich.objects.values_list('sid',flat = True)
    randid = random.choice(idlist)

    return redirect('sandwich', sid = randid)

def register(request):
	return HttpResponse("Registration page")

def categories(request):
	return HttpResponse("Categories page")

def about(request):
	return HttpResponse("About page")
'''
@login_required
def register_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('index')
        else:
            print(form.errors)

    context_dict = {'form':form}

    return render(request, 'profile_registration.html', context_dict)
'''
class MyRegistrationView(RegistrationView):
	def get_success_url(self, user):
		return reverse('index')

		
@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')

    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'website': userprofile.website, 'picture': userprofile.picture})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)

    return render(request, 'profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form})
	


