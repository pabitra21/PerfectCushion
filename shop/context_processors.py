from .models import Category
def menu_links(request):
    links=Category.objects.all()
    print("@@@@@@@@@@@@",links)
    # print("@@@@@@@@@@@@",links)
    return dict(links=links)
