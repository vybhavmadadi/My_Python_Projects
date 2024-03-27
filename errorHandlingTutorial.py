# Error handling tutorial for Python using try

# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass
try:
    f = open('test_copy.txt')
    if f.name == 'test_copy.txt':
        raise Exception # Manually raise an exception and print error defined in the except item
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else: # Runs if there is no exception
    print(f.read())
    f.close()
finally: # Runs irrespective of if there is an exception or not
    print('Executing irrespective')