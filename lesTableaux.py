# pas de tableau intrinsequment à python
# ce 'est pas naturel dans python
# il faut faire appel a une librairie externe
# from array import array
# creation d'un tableau d'entiers (integers) on ecrit tableau = array('i')



import array as arr

a=arr.array('i',[1,2 ,3,5,7])
b=arr.array('i',[11,13])
c=arr.array('i')
c=a+b

print ("Array a = ",a)
print ("Array b = ",b)
print("Array c = ",c)

print ("c[0] = "+str(c[0]))
