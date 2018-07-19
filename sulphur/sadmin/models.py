from django.db import models

# Create your models here.
class User(models.Model):

    # login id of the user e.gg sirajalam049
    login = models.CharField(max_length=60)

    # password of the user when logging in
    password = models.CharField(max_length=250)

    # full name of the user
    full_name = models.CharField(max_length=50)

    # gender of the user. 0 means female and 1 for male
    gender = models.BooleanField(default=1)

    # email address of the user for reset the password
    email = models.EmailField()

    # Date of registration
    reg_date = models.DateTimeField()

    # Name to be displayed when logged in
    display_name = models.CharField(max_length=30)

    # When the post is modified last time
    last_modified = models.DateTimeField()

    # Profile picture for the user
    user_pic = models.CharField(max_length=250)

    def __str__(self):
        return self.full_name