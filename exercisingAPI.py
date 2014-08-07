import urllib.request
import json


#a is the array to contain the book's title, author's full name, and publishers, in that order. Note: there can be multiple publishers. 
def exerciseapi(theid, a):
    response = urllib.request.urlopen('http://alabibliotheque.pythonanywhere.com/books/' + str(theid) + '.json')
    html = response.read()
    data = json.loads(html.decode('utf8'))
    title = data['title'] #book's title 
    authorid = data['author']
    publisherids = data['publishers']
    a.append(title)

    response2 = urllib.request.urlopen('http://alabibliotheque.pythonanywhere.com/authors/' +  str(authorid) + '.json')
    html2 = response2.read()
    data2 = json.loads(html2.decode('utf8'))
    authorfullname = data2['name'] #books's author
    a.append(authorfullname)


    for publisherid in publisherids:
        response3 = urllib.request.urlopen('http://alabibliotheque.pythonanywhere.com/publishers/' +  str(publisherid) + '.json')
        html3 = response3.read()
        data3 = json.loads(html3.decode('utf8'))
        publishername = data3['name'] #books's publisher
        a.append(publishername)
