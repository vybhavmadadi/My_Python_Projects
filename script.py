import sys
import requests


print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('Vybhav!'))


r = requests.get("https://www.google.com.au")


print(r.status_code)
