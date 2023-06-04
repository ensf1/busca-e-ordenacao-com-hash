from uuid import uuid4

from HashTable import HashTable
from OrderedList import OrderedList
from UnorderedList import UnorderedList
from Contact import Contact

import timeit
from random import randint

repeat = 100000
unordered_list = UnorderedList()
ordered_list = OrderedList()
hash_table = HashTable(repeat + 1)


def random_contact():
    return Contact(str(uuid4()), str(uuid4()), randint(100000000, 999999999))


def test_unordered_list_add():
    unordered_list.add(random_contact())


test_unordered_list_add.__name__ = 'add da lista não ordenada'


def test_ordered_list_add():
    ordered_list.add(random_contact())


test_ordered_list_add.__name__ = 'add da lista ordenada'


def test_hash_table_put():
    hash_table.put((contact := random_contact()).name, list([contact.email, contact.phone_number]))


test_hash_table_put.__name__ = 'put da HashTable'


def test(method):
    time = timeit.timeit(stmt=method, number=repeat)
    print(f'Função testada: {method.__name__}')
    print(f'teste repetido {repeat} vezes')
    print(f'tempo de duração do teste: {time}')
    print(f'tempo médio de duração do teste: {time / repeat}')
    print('\n' + '-' * 20 + '\n')


def tests_report():
    test(test_unordered_list_add)
    test(test_ordered_list_add)
    test(test_hash_table_put)

