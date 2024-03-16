#Print following pattern
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for num in range(10):
    for i in range (num):
        print(num, end='')
    print("\n")