#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [i for i in range(20) if i % 2 == 0]
print_reversed_list_integer(my_list)
