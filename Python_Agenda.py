contato=list()

def menu():
    print('Programa Agenda'.center(100,' '))
    print('Adicionar contato')
    print('Alterar contato')
    print('Procurar contato')
    print('Remover contato')
    print('Ver contatos')
    print('Sair')

def adicionar_contato():
    print('Adicionar Contato')
    email=input('Digite o E-mail: ')
    if len(dados)>0:
        for contato in contatos:
            if email == contato['email']:
                print('Este contato já existe.')
                return True
    
    contatos.append({
        'email':email.lower(),
        'nome':input('Nome: ').strip().capitalize(),
        'sobrenome':input('Sobrenome: ').strip().capitalize(),
        'telefone': input('Telefone: ').strip(),
        'data': date.today().strftime('%d/%m/%Y')
    })

def alterar_contato():
    if len(contatos)>0:
        email:input('Digite o e-mail do contato que deseja alterar: ')
        for contato in contatos:
            if contato['email']==email:
                print(f"Nome do contato: {contato['nome']}")
                print(f"Telefone: {contato['telefone']}")
                print('1 - Alterar nome')
                print('2 - Alterar telefone')
                print('3 - Voltar')
                escolha=input('>> ')


menu()