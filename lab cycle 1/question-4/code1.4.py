#function to read the entered word
def read_word(word):
  print("the entered word is : ",word)
#function to get substrings
def substrings_of(word):
  sub_list=[]
  for i in range(len(word)):
    for j in range(i+1,len(word)+1):
      sub_list.append(word[i:j])
  return sub_list
#function to find PALINDROMIC SEQUENCES
def pal(word):
  list=[]
  for i in range(len(word)):
    for j in range(i+1,len(word)+1):
      sub=word[i:j]
      if sub == sub[::-1]:
        list.append(sub)
  return list
#FUNCTION TO SELECT substrings of length k
def sel_len(subs,k):
  list=[]
  for each in subs:
    if len(each)==k:
      list.append(each)
  return (list)   
word = input("enter word here : ")
read_word(word)
n=len(word)
print("\nthe length of word is : ", n) 
#finding the length of the word entered
print("the substrings are : ")
subs_list=substrings_of(word)
for i in subs_list:
  print(i,end=" ")
rev=pal(word)

#selecting substrings of lengh k
print()
g= int(input("enter length to select substrings : "))
length_list= sel_len(subs_list,g)
print("list of substring with length",g,"=",length_list)
#selecting palindromic sequences from the substrings
print("the palindromic sequences include : ")
for i in rev:
  print(i, end=" ")
print("\n") #next line
#distinct_list= list(set(subs_list))
distinct_substrings = [substring for substring in subs_list if len(set(substring)) == len(substring)]
#selecting susbstrings with distinct charachters
print("the list with distinct charachters : ",distinct_substrings)
#possible substrings of length K with N distinct charachters
k= int (input("enter length to find substrings with distinct charachters"))
new_list= sel_len(distinct_substrings,k)
print("\n")#next line
print("substrings of length",k,"with N distinct charachters", new_list)
