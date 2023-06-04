from Contact import Contact
from HashTable import HashTable
from Node import Node
from OrderedList import OrderedList
from PerformanceTests import tests_report
from UnorderedList import UnorderedList


def menu_message():
    print('\nMENU PRINCIPAL')
    print('1 - Inserir contato')
    print('2 - Pesquisar contato')
    print('3 - Remover contato\n')
    print('4 - Teste com timeit')
    print('Escolha uma opção acima ou aperte 9 para sair:\n')


def new_contact():
    print('Informe o nome do contato:')
    name = input()
    print('Informe o e-mail do contato')
    email = input()
    print('Informe o telefone do contato')
    phone_number = int(input())
    return Contact(name, email, phone_number)


def main():
    unordered_contacts_list = UnorderedList()
    ordered_contacts_list = OrderedList()
    hash_contacts_list = HashTable(10)

    menu_message()
    while (op := int(input())) != 9:
        if op == 1:
            # contact = new_contact()
            contact1 = Contact('haha', 'asdas', 123123)
            contact2 = Contact('teste', 'asdas', 123123)
            # print('1 - Inserir em uma lista não ordenada')
            # print('2 - Inserir em uma lista ordenada')
            # print('2 - Inserir em uma tabela Hash\n')
            # while 0 < (op1 := int(input())) > 4:
            #     print('Opção inválida, escolha outra\n')
            # if op1 == 1:
            # unordered_contacts_list.add(Contact('teste','asdas',123123))
            unordered_contacts_list.add(Contact('abc','asdas',123123))
            unordered_contacts_list.add(contact1)
            # unordered_contacts_list.add(contact)
            print(f'Lista não ordenada(tamanho:{unordered_contacts_list.size()}): {unordered_contacts_list}')
                # print(Contact('teste','asdas',123123))
            # if op1 == 2:
            # ordered_contacts_list.add(Contact('teste','asdas',123123))
            # ordered_contacts_list.add(Contact('abc','asdas',123123))
            ordered_contacts_list.add(contact1)
            # ordered_contacts_list.add(contact)
            print(f'Lista ordenada(tamanho:{ordered_contacts_list.size()}): {ordered_contacts_list}')
            # if op1 == 3:
            while hash_contacts_list.get(contact1.name):
                print('Nome existente, informe outro contato')
                contact1 = new_contact()
            hash_contacts_list.put(contact1.name, [contact1.email, contact1.phone_number])
            hash_contacts_list.put(contact2.name, [contact2.email, contact2.phone_number])
            print(f'Hash (tamanho:{hash_contacts_list.size()}): {hash_contacts_list}')
            # hash_contacts_list.put(contact)
        elif op == 2:
            # print('1 - Pesquisar na lista não ordenada')
            # print('2 - Pesquisar na lista ordenada')
            # print('3 - Pesquisar na tabela Hash\n')
            # while 0 < (op2 := int(input())) > 4:
            #     print('Opção inválida, escolha outra\n')
            print('Qual o nome da pessoa que você deseja encontrar?')
            name = input()
            # name = 'teste'
            # if op2 == 1:
            print(f'{name} está na lista não ordenada!' if unordered_contacts_list.search(name) else f'Não existe {name} na lista não ordenada!')
            print(f'{name} está na lista ordenada!' if ordered_contacts_list.search(name) else f'Não existe {name} na lista ordenada!')
            # print(hash_contacts_list.get(name))
            print(f'{name} está na HashTable!' if hash_contacts_list.get(name) else f'Não existe {name} na HashTable!')

        elif op == 3:
            # print('1 - Remover na lista não ordenada')
            # print('2 - Remover na lista ordenada')
            # print('3 - Remover na tabela Hash\n')
            # while 0 < (op3 := int(input())) > 4:
            #     print('Opção inválida, escolha outra\n')
            print('Qual o nome da pessoa que você deseja remover?')
            # name = input()
            name = 'teste'
            # if op3 == 1:
            if unordered_contacts_list.remove(name):
                print(f'Lista não ordenada após a remoção de {name}:[ {unordered_contacts_list}]')
            else:
                print(f'Não existe {name} na lista não ordenada')
            if ordered_contacts_list.remove(name):
                print(f'Lista ordenada após a remoção de {name}:[ {ordered_contacts_list}]')
            else:
                print(f'Não existe {name} na lista ordenada')
            if hash_contacts_list.delete(name):
                print(f'Hash após remoção de {name}:[ {hash_contacts_list}]')
            else:
                print(f'Não existe {name} na HashTable')

        elif op == 4:
            tests_report()

        else:
            print('Opção inválida, escolha outra\n')
        menu_message()


if __name__ == '__main__':
    main()
