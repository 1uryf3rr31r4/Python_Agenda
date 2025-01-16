from datetime import date
data_registro=date.today().strftime('%d/%m/%Y')
contatos=list()


def menu():
    print('Programa Agenda'.center(100,' '))
    print('1 - Adicionar contato')
    print('2 - Alterar contato')
    print('3 - Procurar contato')
    print('4 - Remover contato')
    print('5 - Ver contatos')
    print('6 - Sair')

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
    email = ''
    if len(contatos)>0:
        email=input('Digite o e-mail do contato que deseja alterar: ')
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

def ver_contatos():
    if len(contatos)>0:
        contatos_ordenados=sorted(contatos,key=lambda contato:contato['nome']+' '+contato['sobrenome'])
        for indice, contato in enumerate(contatos_ordenados, start=1):
            print(f"Contato {indice}".center(100, ' '))
            print(f"Nome: {contato['nome']} {contato['sobrenome']}")
            print(f"E-mail: {contato['email']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Data de Registro: {contato['data']}")
    else:
        print('Não há contatos registrados na agenda')

def main():
    escolha=''
    while escolha!=str(6):
        menu()
        escolha=input('>> ')

        if escolha==str(1):
            adicionar_contato()
        elif escolha==str(2):
            alterar_contato()
        elif escolha==str(5):
            ver_contatos()

        else:
            if escolha == str(6):
                print('Fim do Programa')
            else:
                print('Escolha Inválida')

if __name__=='__main__':
    main()