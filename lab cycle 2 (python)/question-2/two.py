def duplicate(l):
    l=set(l)
    dup_list=list(l)
    print("after removing duplicates",dup_list)
    return (dup_list)
def f(x):
    return x**2-x
def sort_it(ls):
    ls.sort()
    return (ls)
def merge(ls,ms):
    return (ls+ms)

#reading a string
my_string = str (input("enter string containing numbers seperated by a space :\n "))
s_list= my_string.split()
print(s_list)
new_list = [int(x) for x in s_list]
print(new_list)
#rotating the list
k= int (input("enter position of elements to rotate : "))
print(new_list[-k:])
print(new_list[:-k])
print("rotated list : ",new_list[-k:]+new_list[:-k])
#creating a tuple from a list
tuple_list={x for x in new_list}
print("the tuple list is : ",tuple_list)
#removing duplicates
duplicate= duplicate(new_list)
#list transformation
transformed_list= [f(x) for x in new_list]
print("original list : ",new_list)
print("new list : ",transformed_list)
#sorting
my_string2 = str (input("enter another string of integers seperated by a space :\n"))
s2_list=my_string2.split()
new_list2 = [int(x) for x in s2_list]
print("the sorted lists are : ")
print(sort_it(new_list))
print(sort_it(new_list2))
print("the merged list : ",merge(new_list,new_list2))




      



