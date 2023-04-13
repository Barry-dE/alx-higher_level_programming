#!/usr/bin/python3

class MyList(list):
    def print_sorted(self, sort):
       sort_in_ascending_order =  sorted(sort)
       print(sort_in_ascending_order)

