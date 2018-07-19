from blog import models
# This will fetch the data from the database.

# Fetches the latest 5 posts
def top_posts(offset, limit):
    record_list = models.Post.objects.filter(is_page=0).filter(in_footer=0).filter(in_nav=0).filter(unlisted=0)[offset - 1:limit]
    return record_list

# Return all the nav records
def all_navs():
    nav_list = models.Post.objects.filter(in_nav = 1).filter(unlisted = 0)
    return nav_list

# Return all the footer records
def all_foots():
    foot_list = models.Post.objects.filter(in_footer = 1).filter(unlisted=0)
    return foot_list

# Return all the static pages
def all_pages():
    pages_list = models.Post.objects.filter(is_page=1).filter(unlisted = 0)
    return pages_list

# Return all the categories
def all_categories():
    category_list = models.Category.objects.all().filter(unlisted = 0)
    return category_list