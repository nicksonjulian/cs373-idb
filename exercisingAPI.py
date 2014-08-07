import urllib.request
import json

def exerciseapi(bookid):
    response = urllib.request.urlopen('http://alabibliotheque.pythonanywhere.com/books/' + str(bookid) + '.json')
    html = response.read()
    data = json.loads(html.decode('utf8'))
    title = data['title'] #book's title 
    authorid = data['author']
    publisherid = data['publishers']

    response2 = urllib.request.urlopen('http://alabibliotheque.pythonanywhere.com/authors/' +  str(authorid) + '.json')
    html2 = response2.read()
    data2 = json.loads(html2.decode('utf8'))
    authorfullname = data2['name'] #books's author
    
    response3 = urllib.request.urlopen('http://alabibliotheque.pythonanywhere.com/publishers/' +  str(publisherid) + '.json')
    html3 = response3.read()
    data3 = json.loads(html3.decode('utf8'))
    publishername = data3['name'] #books's author

    #print(authorfullname + "   " + title + " " + publishername) #test
