from django.shortcuts import render, redirect
from django.utils import timezone
from hashlib import sha256
from .lib.utils import first_word
from sadmin.models import User
from .forms import signupform

#If any user is there, so it sends to the index page, else configuration page is visible
def index(request):
    users = User.objects.all()
    if len(users) < 1:
        return render(request, 'config.html', {'signupform': signupform})
    else:
        return render(request, 'index.html')

def config(request):
    if request.method == 'POST':
        
        #Checking the incoming form with the defined form class
        configform = signupform(request.POST)
        if configform.is_valid():

            #Collecting the cleaned data
            data = {
                'username': configform.cleaned_data['username'],
                'password': configform.cleaned_data['password'],
                'full_name': configform.cleaned_data['full_name'],
                'email': configform.cleaned_data['email'],
                'gender': configform.cleaned_data['gender'],
                'reg_date': timezone.now(),
                'last_modified': timezone.now(),
                'user_pic': 'default.jpg',
                'display_name': first_word(configform.cleaned_data['full_name']),
            }

            # This is the instance of the model User
            new_user = User(
                login = data['username'],
                password =  sha256(data['password'].encode('utf-8')).hexdigest(),
                full_name = data['full_name'],
                gender = data['gender'],
                email = data['email'],
                reg_date = data['reg_date'],
                display_name = first_word(data['full_name']),
                last_modified = data['last_modified'],
                user_pic = data['user_pic'],
            )
            # return render(request, 'debug.html', data)
            # Feeding in the database
            new_user.save()

            #Creating the login session
            request.session['active'] = True
            current_user = User.objects.get(login = data['username'])
            
            request.session['username'] = current_user.login
            request.session['full_name'] = current_user.full_name
            request.session['gender'] = current_user.gender
            request.session['email'] = current_user.email

            request.session['reg_date_year'] = current_user.reg_date.year
            request.session['reg_date_month'] = current_user.reg_date.month
            request.session['reg_date_day'] = current_user.reg_date.day
            request.session['reg_date_hour'] = current_user.reg_date.hour
            request.session['reg_date_minute'] = current_user.reg_date.minute
            request.session['reg_date_second'] = current_user.reg_date.second

            
            request.session['display_name'] = current_user.display_name
        
            request.session['last_modified_year'] = current_user.last_modified.year
            request.session['last_modified_month'] = current_user.last_modified.month
            request.session['last_modified_day'] = current_user.last_modified.day
            request.session['last_modified_hour'] = current_user.last_modified.hour
            request.session['last_modified_minute'] = current_user.last_modified.minute
            request.session['last_modified_second'] = current_user.last_modified.second

            request.session['user_pic'] = current_user.user_pic


            #Sending user onto login page from where it will be redirected to the dashboard
            return redirect('/sadmin/')


        else:
            msg = {
                'message': 'Config Form is Invalid [sulphur.views.py Line: 87]',
            }
            return render(request, 'debug.html', msg)
    else:
        msg = {
                # 'message': 'INVALID ACCESS | Request Method is  n\'t  POST [sulphur.views.py line:92]',/
                'message': request.method
            }
        return render(request, 'debug.html', msg)

