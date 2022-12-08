a = True

if not a:
    print("A is True")
else:
    print("A is False")

b = 18

if (b%3 ==0) and (b%3==1) or a:
    print("chia hết cho 3")
elif b%3 == 1:
    print("chia 3 dư 1")
else:
    print("chia 3 dư 2")