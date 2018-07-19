from django.shortcuts import render, redirect
from .forms import loginform
from sulphur.lib import authentication
from .models import User
from hashlib import sha256
# Create your views here.



def sadmin(request):
    if authentication.is_loggedin(request):
        return redirect('dashboard/')
    else:
        return render(request, 'sadmin/login.html', {'loginform' : loginform})

# This will login the user and send to the dashboard
def login(request):
    # Checking if the user is already loggedin
    if authentication.is_loggedin(request):
        return redirect('../dashboard/')
    else:
        # Validating the login form came from login.html
        logindetails = loginform(request.POST)

        if logindetails.is_valid():
            # Extracting the data from login form
            data = {
                'username': logindetails.cleaned_data['username'],
                'password': logindetails.cleaned_data['password'],
            }
            data['password'] = sha256(data['password'].encode('utf-8')).hexdigest()

            # Getting the record by username
            try:
                u =  User.objects.get(login = data['username'])
            # sending to login if it is wrong
            except User.DoesNotExist:
                return render(request, 'sadmin/login.html', {'loginform': loginform, 'message': 'Username is incorrect',})
            
            if u.password == data['password']:
                # logging in
                request.session['active'] = True

                # Adding the current logged in data into the session
                request.session['id'] = u.id
                request.session['username'] = u.login
                request.session['full_name'] = u.full_name
                request.session['gender'] = u.gender
                request.session['email'] = u.email
                
                request.session['reg_date_year'] = u.reg_date.year
                request.session['reg_date_month'] = u.reg_date.month
                request.session['reg_date_day'] = u.reg_date.day
                request.session['reg_date_hour'] = u.reg_date.hour
                request.session['reg_date_minute'] = u.reg_date.minute
                request.session['reg_date_second'] = u.reg_date.second

                request.session['display_name'] = u.display_name
                
                request.session['last_modified_year'] = u.last_modified.year
                request.session['last_modified_month'] = u.last_modified.month
                request.session['last_modified_day'] = u.last_modified.day
                request.session['last_modified_hour'] = u.last_modified.hour
                request.session['last_modified_minute'] = u.last_modified.minute
                request.session['last_modified_second'] = u.last_modified.second

                request.session['user_pic'] = u.user_pic

                return redirect('/sadmin/')
            else:
                return render(request, 'sadmin/login.html', {'loginform': loginform, 'message': 'Password is incorrect'})
        else:
            return render(request, 'sadmin/login.html', {'loginform': loginform, 'message': 'Form is not valid [sadmin.views.py Line: 57]'})
            

def logout(request):
    authentication.logout(request)
    return redirect('/')
        
def dashboard(request):
    if authentication.is_loggedin(request):
        return render(request, 'sadmin/dashboard.html')
    else:
        return redirect('../')



            