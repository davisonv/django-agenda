import email
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    
    user = auth.authenticate(username=usuario, password=senha)

    if not user:
        messages.error(request,'Usuário e/ou senha inválidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Usuário autenticado.')
        return redirect('dashboard')

def logout(request):
    auth.logout(request)
    return redirect('login')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    
    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/cadastro.html')
    
    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail inválido')
        return render(request, 'accounts/cadastro.html')
    
    if len(senha) < 6:
        messages.error(request, 'A senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')
    
    if len(usuario) < 6:
        messages.error(request, 'O usuário precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')
    
    if senha != senha2:
        messages.error(request, 'As senhas não conferem.')
        return render(request, 'accounts/cadastro.html')
    
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Este usuário já existe.')
        return render(request, 'accounts/cadastro.html')
    
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Este email já existe.')
        return render(request, 'accounts/cadastro.html')
    
    user = User.objects.create_user(
        username=usuario, 
        email=email, 
        password=senha, 
        first_name=nome, 
        last_name=sobrenome
    )
    user.save()
    
    messages.success(request, 'Usuário registrado com sucesso!')
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
