from django.shortcuts import render



def home(request):
  context = {}
  return render(request, 'store/home.html', context)
