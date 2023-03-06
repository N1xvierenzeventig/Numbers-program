nm1 = int(input("Write your first number down."))
nm2 = int(input("Write your second number down."))
nm3 = int(input("Write your third number down."))
nm4 = int(input("Write your fourth number down."))
nm5 = int(input("Write your fifth number down."))





def the_lowest_number(nm1, nm2, nm3, nm4, nm5):
    if nm1<= nm2 and nm1 <= nm3 and nm1<= nm3 and nm1 <= nm5:
        return nm1
    elif nm2<= nm3 and nm2<= nm3 and nm2<= nm5:
        return nm2
    elif nm3<= nm3 and nm3<= nm5:
        return nm3
    elif nm4<= nm5:
        return nm4
    else:
        return nm5



print(the_lowest_number(nm1,nm2,nm3,nm4,nm5))