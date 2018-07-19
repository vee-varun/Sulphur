from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# -------------------------------------------------------------------------
class Category(models.Model):
    
    # Category Name, like games, tech, movies etc.
    name = models.CharField(max_length=200)

    # This will be the cover pic foe the individual category
    cover_pic = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)

    # Date Created
    date_created = models.DateTimeField()

    # URL to a particular category page
    url = models.SlugField(null=True, blank=True)

    # Keywords to be in HTML meta tag
    keywords = models.CharField(null=True, max_length=200, blank=True)

    # Description to be in HTML meta tag
    description = models.CharField(null=True, max_length=300, blank=True)

    # Set if it is in navbar
    in_nav = models.BooleanField(default=0)

    # Set if this link inside the footer
    in_footer = models.BooleanField(default=0)

    # Set if the category is not suppose to shown in the website
    unlisted = models.BooleanField(default=0)


    def __str__(self):
        return self.name


# -------------------------------------------------------------------------
class Post(models.Model):

    # This is the title of the post
    title = models.CharField(max_length=200, null=True, blank=True)

    # This will be the cover pic foe the individual post
    cover_pic = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)

    # This is the main contentof the post
    content = RichTextUploadingField(null=True, blank=True)

    # This is the ID of the author of the post which is related to the model User in the app admin
    author = models.ForeignKey('sadmin.User', on_delete=models.CASCADE)

    # DateTime on which the post is published
    pub_date = models.DateTimeField()

    # It is the number of views
    view_count = models.PositiveIntegerField(null=True, default=0, blank=True)

    # URL to a post
    url = models.CharField(max_length=600, null=True, blank=True)

    # Set if the post is not supposed to be shown
    unlisted = models.BooleanField(default=0)

    # Date of post last modified 
    last_modified = models.DateTimeField()

    # SET if this is a static page. If this is SET so 
    is_page = models.BooleanField(default=0)

    # SET if this is in navbar
    in_nav = models.BooleanField(default=0)

    # SET if this is in footer
    in_footer = models.BooleanField(default=0)

    # keywords in HTML meta tag
    keywords = models.CharField(max_length=200, null=True, blank=True)

    # description in HTML meta tag
    description = models.CharField(max_length=300, null=True, blank=True)

    # SET if it is a social link
    social = models.BooleanField(default=0)

    # This is the ID of the category of the post which is related to the model Category in app blog
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


