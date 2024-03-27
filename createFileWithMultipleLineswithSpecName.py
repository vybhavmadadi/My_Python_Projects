# with open('test.txt', 'w') as new_file:
#     for i in range(1,8):
#         name = "line{}\n".format(i)
#         new_file.write(name)
#         print("wrote the", name)

with open('test.txt', 'r') as read_file:
    lines = read_file.readlines()
    print(lines[3])