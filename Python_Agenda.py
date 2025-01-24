from datetime import date
data_registro=date.today().strftime('%d/%m/%Y')
contatos=list()
email = ''


def menu():
    print('Programa Agenda'.center(100,'='))
    print('1 - Adicionar contato')
    print('2 - Alterar contato')
    print('3 - Procurar contato')
    print('4 - Remover contato')
    print('5 - Ver contatos')
    print('6 - Sair')
    print('='*100)

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

def procurar_contato():
    if len(contatos)>0:
        email=input('Digite o e-mail do contato: ')
        for contato in contatos:
            if contato['email']==email:
                print(f"Nome: {contato['nome']} {contato['sobrenome']}")
                print(f"Telefone: {contato['telefone']}")
                print(f"Data de registro: {contato['data']}")
                return
            else:
                print('Esse email não consta na agenda')
                return

    print('Não há contatos registrados na agenda')

def remover_contato():
    if len(contatos)>0:
        email=input('Digite o e-mail do contato que deseja remover: ')
        x=0
        while x<len(contatos):
            if contatos[x]['email']==email:
                contatos.remove(contatos[x])
                return True
            x+=1

        print('Contato não encontrado')
    else:
        print('Não há contatos registrados na agenda.')

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
        elif escolha==str(3):
            procurar_contato()
        elif escolha==str(4):
            remover_contato()
        elif escolha==str(5):
            ver_contatos()

        else:
            if escolha == str(6):
                print('Fim do Programa')
            else:
                print('Escolha Inválida')

if __name__=='__main__':
    main()