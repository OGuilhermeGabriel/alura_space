from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User

def login(request):
    form = LoginForms()
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
                return redirect('cadastro')
            
            #capturando as informações das credenciais
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            #verificar se já existe um usuário com o msm nome
            if User.objects.filter(username=nome).exists():
                return redirect()        

            #cadastrando o usuário 
            usuario = User.objects.create_user(
                username=nome,
                email= email,
                password= senha 
            )
            #gravando o usuário
            usuario.save()
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form':form})
