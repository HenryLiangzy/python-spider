from urllib import request
import re


def getImgAddress(string):
    #     this function is to return an array of picture address

    marks=re.findall(r'<img.*?src=\".*?\"*>|<img.*?src=\'.*?\'*>',string)
    srcs=[]
    for mark in marks:

        src=re.findall(r'src=\".*?\"', mark)
        # because it is an array so it should turn to 0 to make it a string
        src=src[0][5:-1]
        # to delete the quote
        srcs.append(src)
        # this step will format an array of address
    #return it 
    return srcs
def getImgName(array):
    name=[]
    for address in array:
        print(address)
        address=re.findall(r'', address)
        address.append(address)
    print(name)
    return name
def downloadImg(array):
    
    print()
response=request.urlopen('http://www.baidu.com')
info=response.info()
print (info)
input=response.read().decode()
imgAdd=getImgAddress(input)
name=getImgName(imgAdd)


def write(data,name):
    file=open(name,'wb')
    file.write(data.read())