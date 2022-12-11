t = (12, 4, "str", True, None)
#t = (5)
t1, t2, t3, t4, t5 = t
print(t[0])
a= 15
b= 17
'''
temp = a
a = b
b = temp
print(a,b)
'''
    # (17, 15)
a, b = b, a
print(a,b)
#print(t3)

t[5]  =13
t += (15, 23)

for i in t:
    print(i)