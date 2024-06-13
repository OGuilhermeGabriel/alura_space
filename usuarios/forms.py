from django import forms   

#criando um formulário para a tela de login
class LoginForms(forms.Form):
    nome_login= forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex: João Silva"
            }
        )
    )
    senha= forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha"
            }
        )
    )

#criando um formulário para o cadastro
class CadastroForms(forms.Form):
    nome_cadastro= forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: João da Silva"
            }
        )
    )
    email= forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: joaosilva@gmail.com"
            }
        )
    )
        
    senha_1= forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

    senha_2= forms.CharField( 
        label="Confirme sua senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )

    #método para validar o nome do usuário durante o cadastro
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        #caso o nome esteja correto
        if nome: 
            nome = nome.strip()
            #validação p/ tratar espaços vazios
            if " " in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome
    
    #validando as senhas
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        #validando as duas senhas 
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2