

def menu_message():
    print('1 - Inserir contato')
    print('2 - Pesquisar contato')
    print('3 - Remover contato')
def main():
    menu_message()
    while (op := int(input())) != 9:
        if op == 1:

        elif op == 2:

        else:
            print('Opção inválida, escolha outra\n')
        menu_message()


if __name__ == '__main__':
    main()
