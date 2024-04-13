from django.shortcuts import render, redirect
from site_app.models import Pessoa

def home(request):
    nome = ""
    nascimento = ""
    email = ""
    pais = ""
    dados = Pessoa.objects.all()
    nome_pesquisa = request.GET.get("nome_pesquisa")  

    if request.method == "POST":
        nome = request.POST.get("nome")
        nascimento = request.POST.get("nascimento")
        email = request.POST.get("email")
        pais = request.POST.get("pais")
        Pessoa.objects.create(nome=nome,
                              nascimento=nascimento,
                              email=email,
                              pais=pais)

    return render(request, "site_app/global/home.html", context={"dados": dados, "nome": nome, "nascimento": nascimento, "email": email, "pais": pais})

def criar(request):
    nome = ""
    nascimento = ""
    email = ""
    pais = ""
        
    if request.POST:
        nome = request.POST.get("nome")
        nascimento = request.POST.get("nascimento")
        email = request.POST.get("email")
        pais = request.POST.get("pais")
        Pessoa.objects.create(nome=nome,
                              nascimento=nascimento,
                              email=email,
                              pais=pais)

    return render(request, "site_app/partials/criar.html", context={"nome": nome, "nascimento": nascimento, "email": email, "pais": pais})

def pesquisar(request):
    dados = {}
    if request.GET:
        nome_filter = request.GET.get("nome")
        dados["pessoas"] = Pessoa.objects.filter(nome__icontains=nome_filter)       
    else: 
        dados["pessoas"] = Pessoa.objects.all()           
    return render(request, "site_app/partials/pesquisar.html",dados)

def deletar(request, id=0):
    pessoa = {}
    if id:
        pessoa = Pessoa.objects.get(id=id)
        pessoa.delete()
        return redirect('deletar')
    
    nome_filter = request.GET.get("nome")
    if nome_filter:
        pessoa["pessoas"] = Pessoa.objects.filter(nome__icontains=nome_filter)       
    else: 
        pessoa["pessoas"] = Pessoa.objects.all()
    
    return render(request, "site_app/partials/deletar.html", context=pessoa)

def atualizar(request, id=0):
    pessoa = {}
    if id:
        if request.POST:
            pessoa = Pessoa.objects.get(id=id)
            pessoa.nome = request.POST.get("nome",pessoa.nome)
            pessoa.nascimento = request.POST.get("nascimento",pessoa.nascimento)
            pessoa.email = request.POST.get("email",pessoa.email)
            pessoa.pais = request.POST.get("pais", pessoa.pais)
                        
            pessoa.save()
        
            return redirect ('atualizar')
        
        pessoa["pessoa"] = Pessoa.objects.get(id=id)        
        return render(request, "site_app/partials/update.html",pessoa)         
     
    nome_filter = request.GET.get("nome")
    if nome_filter:
        pessoa["pessoas"] = Pessoa.objects.filter(nome__icontains=nome_filter)       
    else: 
        pessoa["pessoas"] = Pessoa.objects.all()         
   
    return render(request, "site_app/partials/atualizar.html", context=pessoa)
