
# Return Boolean. True if logged in and false otherwise
def is_loggedin(request):
    if 'active' in request.session:
        if request.session['active'] == True:
            return True
        else:
            return False
    else:
        return False

# It will log out and delete all the session data of a user.
def logout(request):
    for key in request.session.keys():
        try:
            del request.session['key']
        except KeyError:
            pass
    try:
        del request.session['active']
    except KeyError:
        pass
    return