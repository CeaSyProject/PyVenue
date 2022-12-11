'''
a = 5
a = [12, 3, 4]
a = [12, "string", True, 12.4, None]    
#   0       1       2      3    4       5
#   -5      -4      -3     -2  -1       5
b = [12, True, "string", 3.5, None ]
#   0      1        2       3   4

#print(a==b)
# list[m:n]     --> [m:n-1]
print(a[2])
# m = 0; n = n
print(a[ : ])
print(a[2:4])

#print(a[5])
print(a[-5])
print(a[-1:-3])
print(a[-3:-1])

print(a[:5:2])
print(a[::-2])

print(a[5:0:-1])

if 13 not in a:
    print('true')
else:
    print("false")

print(a*2)
print(a+[13,4])
print(len(a))

c = [
    [12,4,5],
    [34,1,4],
    [
        [1,2,4],
        [12,3,True]
    ],
]

print([12,4,5] in c)
print(c[2][1][2])

# Mutability
a[0] = 13
print(a[0])

a[0:2] = [14, "str2"]
print(a[0:2])

a[0:2] = []
print(a[0])

for i in a:
    print(i)

# Methods and functions

'''
a = [12, "string", True, 12.4, None] 
b = [12,4,5,7]
c = ["str1", "str2"]
print(len(a))

print(max(c))
print(min(b))


#a += [5]
# a.append(5)
#a.append([12,43])

#a += [12,43]
#a.extend([12,42])

a.insert(0, 15)

#a.remove(12)
a.pop()
d = a.pop(0)
print(d)

