from .models import Category

#for displaying categories from the navbar
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
