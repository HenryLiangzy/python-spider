from urllib import request
import re


def getImgAddress(string):
    #     this function is to return an array of picture address

    marks=re.findall(r'<img.*?src=\".*?\"*>|<img.*?src=\'.*?\'*>',string)
    srcs=[]
    for mark in marks:
        print(mark)
        src=re.findall(r'src=\".*?\"', mark)
        # because it is an array so it should turn to 0 to make it a string
        src=src[0][5:-1]
        # to delete the quote
        srcs.append(src)
        # this step will format an array of address
    #return it 
    return srcs
response=request.urlopen('http://www.baidu.com')
info=response.info()
print (info)
input=response.read().decode()
getImgAddress(input)



def write(data):
    file=open('web.txt','wb')
    file.write(data.read())