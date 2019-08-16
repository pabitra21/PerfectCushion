from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category,Product

def index(request):
    text_var='this is my first django app webpage'
    return HttpResponse(text_var)

#http://localhost:8000/shop/cotton-cushions/
#http://localhost:8000/shop/polyester-cushions/
#http://localhost:8000/shop/

def allProdCat(request,c_slug=None):
    category_name=None
    products=None
    if c_slug!=None:
        print("i am in if")
        category_name=get_object_or_404(Category,slug=c_slug)
        print(category_name)
        products =Product.objects.filter(category=category_name,available=True)
        print("if ",products)
    else:
        print("i am in else")
        products=Product.objects.all().filter(available=True)
        print("else",products)
    return render(request,'shop/category.html',{'category':category_name,'products':products})