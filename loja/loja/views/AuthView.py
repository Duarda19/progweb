from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from loja.forms.AuthForm import LoginForm, RegisterForm

def login_view(request):
    loginForm = LoginForm()
    message = None
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        loginForm = LoginForm(request.POST)
        
        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                _next = request.GET.get('next')
                if _next:
                    return redirect(_next)  # Redireciona para a página que o usuário queria acessar antes de ser redirecionado ao login
                else:
                    return redirect("/")  # Redireciona para a home após o login
            else:
                message = {'type': 'danger', 'text': 'Dados de usuário incorretos'}
    
    context = {
        'form': loginForm,
        'message': message,
        'title': 'Login',
        'button_text': 'Entrar',
        'link_text': 'Registrar',
        'link_href': '/register',
    }
    
    return render(request, 'auth/auth.html', context)

def register_view(request):
    registerForm = RegisterForm()
    message = None
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        registerForm = RegisterForm(request.POST)
        
        if registerForm.is_valid():
            # Verificando se existe usuário ou e-mail com esse cadastro
            verifyUsername = User.objects.filter(username=username).first()
            verifyEmail = User.objects.filter(email=email).first()
            
            if verifyUsername is not None:
                message = {'type': 'danger', 'text': 'Já existe um usuário com este username!'}
            elif verifyEmail is not None:
                message = {'type': 'danger', 'text': 'Já existe um usuário com este e-mail!'}
            else:
                try:
                    # Criando o novo usuário
                    user = User.objects.create_user(username=username, email=email, password=password)
                    message = {'type': 'success', 'text': 'Conta criada com sucesso!'}
                except Exception as e:
                    message = {'type': 'danger', 'text': f'Ocorreu um erro ao tentar criar o usuário: {str(e)}'}
        
    context = {
        'form': registerForm,
        'message': message,
        'title': 'Registrar',
        'button_text': 'Registrar',
        'link_text': 'Login',
        'link_href': '/login',
    }
    
    return render(request, 'auth/auth.html', context)

def logout_view(request):
    logout(request)
    message = {'type': 'success', 'text': 'Você foi deslogado com sucesso!'}
    return render(request, 'auth/auth.html', {'message': message, 'title': 'Login'})
