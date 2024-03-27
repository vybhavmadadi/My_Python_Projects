#Tutorial on requests library

#Grab contents of a website using a website https://xkcd.com/353/
import requests

# r = requests.get('https://xkcd.com/353/') # Will get the response code return from the website

# # print(r) # Prints the response code
# # print(dir(r)) # Prints out what attribures are available for this requests.get
# # print(help(r)) # Detailed explanation of what are the available attributes
# print(r.text) # Shows content in html text format

# #Download the image from the page in Python
# #Image url is https://imgs.xkcd.com/comics/python.png

# r = requests.get('https://imgs.xkcd.com/comics/python.png')

# # print(r.content) # Shows the content in bytes
# # Take contents and save it in a file.
# # with open('comic.png', 'wb') as f: #Open the file 'comic.png' in write bytes mode, if file does not exist, create it
# #     f.write(r.content) #Copy the content of the image to the file in bytes

# # Check status code of the website
# print(r.status_code) #HTTP status code is returned, like 200, 4xx, 5xx
# print(r.ok) #Will return a True for any response lower than 3xx and False for anything highter than 3xx

# #More details of the status
# print(r.headers)

#Advance features
#Using https://httpbin.org for this part

#You can add parameters to url, but passing them through dictionary has better control
# payload = {'page': 2, 'count': 25}

# r = requests.get('https://httpbin.org/get', params=payload)

# print(r.text)
# print(r.url)

# #Posting something to using a url
# payload = {'username': 'Vybhav', 'password': 'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)

# # print(r.text)
# # print(r.json())
# r_dict = r.json()
# print(r_dict['form'])

# #Using auth requests
# r = requests.get('https://httpbin.org/basic-auth/vybhav/testing', auth=('vybhav', 'testing'))

# print(r.text)

#Adding timeouts to not wait until long for you to get response
# r = requests.get('https://httpbin.org/delay/1', timeout=3) #URL used here responds after 1 sec
r = requests.get('https://httpbin.org/delay/5', timeout=3) #URL used here responds after 5 sec
print(r)
