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
    })