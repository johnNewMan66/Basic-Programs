# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:15:29 2020

@author: Asus
"""
class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list():
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

if __name__=="__main__":
    llist=linked_list()
    llist.head=node(1)
    second=node(2)
    third=node(3)
    llist.head.next=second
    second.next=third
    llist.printlist()
    