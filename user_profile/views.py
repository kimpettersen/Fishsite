#the app user_profile contains all logic that have something to do with an
#individual user. As in: manage your own Trips and Fish, see your own profile,
#and generall statistic.
from django.shortcuts import render
from django.forms.models import modelformset_factory
from django.forms import ModelForm
from user_profile.models import Trip, Fish

#TODO: Add User authentication. User need to be logged in to do any of this.

def index(request):
    #Returns an index page that currently contains all navigation. 
    #Acts temporeraly as a 'Root' Directory.
    return render(request, 'user_profile/index.html')
    
def edit_trips(request):
    #Method calls generate_form() with params for the 'Trip' objects
    return generate_form(request,
                Trip,
                '/user_profile/edit_trips',
                'Trips',
                'Succesfully updated trips',
                )
    
def edit_fish(request):
    #Method calls generate_form() with params for the 'Fish' objects
    return generate_form(request,
                Fish,
                '/user_profile/edit_fish',
                'Fish',
                'Succesfully updated fish',
                )

def generate_form(request, current_object, form_action, object_name, success_message):
    #Method creates a form from the passed object.
    #The method returns all forms that is saved pluss one extra blank form.
    #Uses 'form.html' to display content
    #TODO -Make the amount of extra forms dynamic. This gives the oportunity to
    #add as many new objects as decired.
    #-Add the logged in user to the created object.
    CurrentFormSet = modelformset_factory(current_object, extra=1)
    info_string = ''
    if request.method == 'POST':
        formset = CurrentFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            info_string = success_message
        else:
            info_string = 'The form did not validate. Please try again'
    else:
        formset = CurrentFormSet()
    #Data to be rendered. Contains a formset, the action the form will perform
    #the name of the object and an info string that contains problems occured.
    data = {'formset' : formset,
            'action' : form_action,
            'object_name' : object_name,
            'info' : info_string            
            }
    return render(request, 'user_profile/form.html', data)

def profile(request):
    #Returns a list of the 5 heaviest fish in the db. renders a 'User profile'
    fish_list = Fish.objects.all().order_by('-weight')[:5]
    return render(request, 'user_profile/profile.html', 
                    {'fish_list': fish_list})
