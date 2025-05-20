#O código permite criar um login e senha, 
# e depois só permite o acesso quando o usuário digitar as credenciais corretas.

login= ''
senha= ''
user=str (input('Crie seu login'))
password=str (input('Crie sua senha'))

while True:
  login=str (input('Digite seu login'))
  senha=str (input('Digite sua senha'))
  if login==user and senha==password:
    break
  else:
    print ('Login ou senha incorretos, tente novamente')
print('Login efetuado com sucesso!')