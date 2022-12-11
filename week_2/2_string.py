str1 = "string1"

# char
#print(str[0])
str1 = 's'
print(type(str1))
for i in str1:
    print(i)

str1 = "string1 g"

if "g" in str1:
    print("True")
else:
    print("False")

# chr
# ASCII 2^8 chars
# Unicode 2^16 chars 65356
a = chr(2324)
# print(a)

# print(ord("औ"))
a = "string1"
print(len(a))

print(type(str(True)))

# a[0] = 'N'
a += " string2 "
a *= 2
print(a)

a = a.replace('g','n')
print(a)