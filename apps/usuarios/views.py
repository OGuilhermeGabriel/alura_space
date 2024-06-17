from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages 

def login(request):
    form = LoginForms()

    #validando que o método é "post"
    if request.method == 'POST':
        form = LoginForms(request.POST)

        #validando o formulário de login
        if form.is_valid():
            #buscando as informações do formulário
            nome= form['nome_login'].value()
            senha= form['senha'].value()

            #autenticando os usuários dados os respectivos parâmetros
            usuario = auth.authenticate(
                request,
                username= nome, 
                password= senha
            )

            #validando o usuário
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, f'Erro ao efetuar login')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form':form})
    
def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        #validação do formulário
        if form.is_valid():

            #validação da senha
            if form["senha_1"].value() != form["senha_2"].value():
                #redirecionando o usuário p/ página
                messages.error(request, 'Senhas não são iguais')
                return redirect('cadastro')
            
            #capturando as informações das credenciais
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            #verificar se já existe um usuário com o msm nome
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente!')
                return redirect()        

            #cadastrando o usuário 
            usuario = User.objects.create_user(
                username=nome,
                email= email,
                password= senha 
            )
            #gravando o usuário
            usuario.save()
            messages.success(request,'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form':form})

def logout(request):
    auth.logout(request)
    messages.success(request,'Logout efetuado com sucesso!')
    return redirect('login')    