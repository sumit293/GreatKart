from django.shortcuts import render


print("views in homeHtml")
def home(request):
    return render(request, 'home.html')
