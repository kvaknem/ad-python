#!/usr/bin/python3.5


import random
import string
import sys
import getch
import os


def generate(n):
	book = {}
	for i in range(n):
		book['name'+str(i)] = int(''.join([random.choice(string.digits) for x in range(7)]))
	return book

def list_book(book):
	for name,tel in book.items():
		print('Name = {} \t  Phone = {}'.format(name,tel))

def add(book):
	new_name = input('Enter new name: ')
	new_phone = input('Enter new phone: ')
	book[new_name] = int(new_phone)
	print('Record storred!!')
	return book

def delete(book):
	new_name = input('Enter name or phone to delete: ')
	if new_name in book.keys() or new_name in str(book.values()):
		for name, phone in list(book.items()):
			if new_name == name or new_name == str(phone):
				del book[name]
	else:
		print('Not Found !!')

	return book

def change_book(book):
	new_name = input('Enter name to change: ')
	if new_name in book.keys():
		del book[new_name]
		new_name = input('Enter New name : ')
		new_phone = input('Enter New Phone : ')
		book[new_name] = new_phone
	return book

def myhelp():
#	os.system('clear')

	print('Select : \n\
1 - List Book\n\
2 - Add record\n\
3 - Delete record\n\
4 - Change record')



def selector(book):
	case = { '1': list_book, '2': add, '3': delete, '4': change_book,}
#	print(case)
	while True:
		
		a = getch.getch()
#		myhelp()
		if a in case.keys():
			myhelp()
#			print(a)

			case[a](book)


		if a == 'a':
			break
	return book









#generate(15)
book = generate(20)

#print(book)

#book = add(book)

#list_book(book)


#book = delete(book)

#book = change_book(book)
#list_book(book)


selector(book)
