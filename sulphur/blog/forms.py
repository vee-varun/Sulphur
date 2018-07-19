from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Category

# Form for posting new post
class new_post_form(forms.Form):
    category_list = []
    
    categories = Category.objects.all()
    for record in categories:
        tup = (record.id, record.name)
        category_list.append(tup)

    
    title = forms.CharField(label='Title', max_length=60)

    cover_pic = forms.ImageField(label='Cover Pic')

    content = forms.CharField(widget=CKEditorUploadingWidget())

    keywords = forms.CharField(label='Keywords', max_length=60)

    description = forms.CharField(label='Description', max_length=300)

    category = forms.ChoiceField(label='Category', widget=forms.Select, choices=category_list)

# Form for posting new post
class xedit_post_form(forms.Form):
    category_list = []
    
    categories = Category.objects.all()
    for record in categories:
        tup = (record.id, record.name)
        category_list.append(tup)

    
    title = forms.CharField(label='Title', max_length=60)

    content = forms.CharField(widget=CKEditorUploadingWidget())

    keywords = forms.CharField(label='Keywords', max_length=60)

    description = forms.CharField(label='Description', max_length=300)

    category = forms.ChoiceField(label='Category', widget=forms.Select, choices=category_list)

# Form for posting new nav link
class new_nav_form(forms.Form):

    name = forms.CharField(label = 'Navlink Name', max_length=10)

    url = forms.URLField(widget=forms.URLInput())

# Form for posting new foot content
class new_foot_form(forms.Form):
    
    title = forms.CharField(label='Heading (Optional)', max_length=20, required=False)

    content = forms.CharField(label='Body', widget=CKEditorUploadingWidget())

    url = forms.URLField(label='Enter Link (Optional)', widget=forms.URLInput(), required=False)

# Form for posting new pages
class new_page_form(forms.Form):

    title = forms.CharField(label='Title', max_length=60)

    cover_pic = forms.ImageField(label='Cover Pic', required=False)

    content = forms.CharField(widget=CKEditorUploadingWidget(), required=False)

    keywords = forms.CharField(label='Keywords', max_length=60, required=False)

    description = forms.CharField(label='Description', max_length=300, required=False)

class xedit_page_form(forms.Form):

    title = forms.CharField(label='Title', max_length=60)

    content = forms.CharField(widget=CKEditorUploadingWidget(), required=False)

    keywords = forms.CharField(label='Keywords', max_length=60, required=False)

    description = forms.CharField(label='Description', max_length=300, required=False)


class new_category_form(forms.Form):
    
    name = forms.CharField(label='Category Name', max_length=20)

    cover_pic = forms.ImageField(label='Cover Pic')

    keywords = forms.CharField(label='Keywords', max_length=60)

    description = forms.CharField(label='Description', max_length=300)

class xedit_category_form(forms.Form):
    
    name = forms.CharField(label='Category Name', max_length=20)

    keywords = forms.CharField(label='Keywords', max_length=60)

    description = forms.CharField(label='Description', max_length=300)
