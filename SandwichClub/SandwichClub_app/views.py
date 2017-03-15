from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from django.core.urlresolvers import reverse
from SandwichClub_app.forms import UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from SandwichClub_app.models import UserProfile


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

#def profile(request):
	#return HttpResponse("Profile page")

def register(request):
	return HttpResponse("Registration page")

def categories(request):
	return HttpResponse("Categories page")

def about(request):
	return HttpResponse("About page")

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
	
class MyRegistrationView(RegistrationView):
	def get_success_url(self, user):
		return reverse('register_profile')
		
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