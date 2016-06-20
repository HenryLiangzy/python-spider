import urllib
from urllib import request
import re
#functions area
def getImgAddress(string):
    # this function is to return an array of picture address
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
    #this method is to get the img name
    # this method isn't finish yet
    name=[]
    for address in array:
        print(address)
        address=re.findall(r'', address)
        address.append(address)
    
    print(name)
    return name
def downloadImg(array):
    #this method hasn;t finish
    return ''
    
    

data =[]
data=data.append('BT')

url_values = urllib.parse.urlencode(data)
# url = "http://www.hacg.li/wp/?s"
url="http://www.baidu.com"
full_url = url # + url_values

#data = urllib.request.urlopen(full_url).read()
#data = data.decode('UTF-8')
# print(url_values)
# print(full_url)
# print(data)

response=request.urlopen(url)
info=response.info()
# print (info)
page=response.read().decode()
imgAdd=getImgAddress(page)
name=getImgName(imgAdd)


def write(data,name):
    #this method is to write the data into files
    #keep this method incase some download operation
    file=open(name,'wb')
    file.write(data.read())