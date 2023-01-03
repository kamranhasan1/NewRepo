
# append()
# extend()
# insert()
# pop(), pop(index)
# remove()
# count()
# sort()
# copy()
# extend()
l1 = [1, 3, 4, 5, "Hello", "LPU"]
l2 = ["hi",1,2,3,4,5,6]

l1.extend(l2)
print(l1)

# pop(), pop(index)
a=[1,2,3,4]
a.pop(1)
print(a)



# insert()
l=[1,2,3,4]
l.insert(4,"hi")
print(l)


# remove
a=[1,2,3,4,5,6,4]
a.remove(4)
print(a)

# short
l = [4, 9, 1, 4, 2, 10, 7]
l.sort()

print(l)

l.sort(reverse = True)
print(l)




l=["hi","qrs","psr"]
l.sort()
print(l)


l= [[8, 3], [2, 6], [7, 3], [4, 2]]
l.sort(key=lambda x:x[1])
print(l)


# copy
l = [1, 2, "hi", "fire"]

x = l

x[0] = 4

print(l)

x = l.copy()

print(x)

# Take a sequence of numbers as input and
# print True if it is already sorted, otherwise print False

# 12 78 43 56 89

st=input()
st=st.split()
st=[int(i)for i in st]
print(st)
a=st.copy()
a.sort()
if (a==st):
    print(True)
else:
    print(False)

