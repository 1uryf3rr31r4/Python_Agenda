from datetime import date
data_registro=date.today().strftime('%d/%m/%Y')
contatos=list()


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
    if len(contatos)>0:
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

                if escolha==str(1):
                    novo_nome=input('Digite um novo nome para o contato: ')
                    contato['nome']=novo_nome
                    return
                elif escolha==str(2):
                    novo_tel=input('Digite um novo telefone para o contato: ')
                    contato['telefone']=novo_tel
                    return
                elif escolha==str(3):
                    return
                else:
                    print('Opção Inválida')
        print('Não existe usuário cadastrado com o e-mail informado.')
    else:
        print('Não há contatos registrados na agenda')


def main():
    escolha=''
    while escolha!=str(6):
        menu()
        escolha=input('>> ')

        if escolha==str(1):
            adicionar_contato()

        else:
            if escolha == str(6):
                print('Fim do Programa')
            else:
                print('Escohla Inválida')

if __name__=='__main__':
    main()