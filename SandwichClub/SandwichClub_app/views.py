from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from django.core.urlresolvers import reverse
from SandwichClub_app.forms import UserProfileForm
from django.shortcuts import redirect


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

def profile(request):
	return HttpResponse("Profile page")

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