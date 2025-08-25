#seperator nad end keyword
'''strings ni seperate chese keywrd sep
p=char(input("enter character-")
print('c','m','l','r',sep=',')
print('c','m','l','r',sep='&')
print('c','m','l','r',sep='')
print('c','m','l','r',sep='** ')
#end
print('c','m','l','r',sep=',',end='\n')
print('rahul','rami')
print('c','m','l','r',sep=',',end=',,,,')
print('rahul','rami',sep=',',end='^_^')
print('ciel',end=' ^0^')'''

'''boolean_val = True
print(type(boolean_val))
#string->sequence of characters-no,spcae,symbols
string_value = 'py cls :)'
print(type(string_value))
print(string_value)
#tuple--collection of elements. , imp in tuple,immutable-can nvr update or delete,u can delete entire var
r=(2,9,0,9,8)
print(r)
#list -mutable can update or delete,[ ]
u = [8,'a','b',8,4,'j',7]
print(u)
#dictionary--key,value elements(used in jango ,flask imp )
#keys immutable
#synatax=={key:value,key:value..}
student_data = {'name':'ch','rollno':35,'phnno':(2787344983243),'address':'vij'}
print(student_data)'''
################################################
#3-3-2025
#set datatype remaining.

#.union(set,[set1.....]) or |- returns both sets of all elements
'''set1 = {1,2,4,5}
set2 = {8,9,6,7}
r = set1.union(set2)
print(r)
#or
r1 = set1|set2
print(r1)'''

#.intersection(set,[set...]) or & --returns set of elements common to both
'''s3 = {3,4,6,8}
s4 = {9,2,6,7}
s5 = {6,4,3,8}
r = s3.intersection(s4,s5)
print(r)
#or
r1 = s3&s4&s5'''

#.difference -
'''s3 = {3,4,6,8}
s4 = {9,2,6,7}
print(s3.difference(s4))
#or
print(s3-s4)'''

#.symmetric_difference or ^ 
'''s3 = {3,4,6,8}
s4 = {9,2,6,7}
print(s3.symmetric_difference(s4))
print(s3^s4)'''
#modifying methods..
#set1.update(set2,[set3...]) or set1 |= set2
'''s3 = {3,4,6,8}
s4 = {9,2,6,7}
print(s3.update(s4))
print("afetr up:",s3)'''

#.intersection_update or &=
'''s3 = {3,4,6,8}
s4 = {9,2,6,7}
s4.intersection_update(s3)
print(s4)'''

#.difference_update or -=: modifies the set,updating and removig the common element
'''s3 = {3,4,6,8}
s4 = {9,2,6,7}
print(s3)
s3.difference_update(s4)
print(s3)'''

#.symmetric_difference_update or ^=:
'''s3 = {3,4,6,8}
s4 = {9,2,6,7}
s3.symmetric_difference_update(s4)
print(s3)'''

#.isdisjoint - returns true if both sets hv no elmnt i n common
#no operators for dis one
'''s3 = {3,4,6,8}
s4 = {9,2,6,7}
print(s3.isdisjoint(s4))'''

#.issubset <= :returns true or false
'''s3 = {3,4,6,8}
s4 = {9,2,6,7}
print(s3.issubset(s4))'''

#.issuperset >=
'''s3 = {3,4,5,6,7,8}
s4 = {6,7}
print(s3.issuperset(s4))'''

#SET METHODS OVER~~~~~~~~~

























