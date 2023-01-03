from tkinter import N
from wsgiref.validate import InputWrapper


na=input("enter your name\n")
print("good after noon ," + na)


letter=''' Dear <|Name|>,
hello gentel men I am greating fron xyz
you are selected !

date :<|Date |>

'''
name=input("enter your name \n")
date=input("enter Date\n")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)