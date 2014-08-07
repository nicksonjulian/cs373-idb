import urllib.request
import json

def exerciseapi(theid):
    response = urllib.request.urlopen('http://alabibliotheque.pythonanywhere.com/books/' + str(theid) + '.json')
    html = response.read()
    data = json.loads(html.decode('utf8'))
    title = data['title'] #book's title 
    authorid = data['author']

    response2 = urllib.request.urlopen('http://alabibliotheque.pythonanywhere.com/authors/' +  str(authorid) + '.json')
    html2 = response2.read()
    data2 = json.loads(html2.decode('utf8'))
    authorfullname = data2['name'] #books's author

    #print(authorfullname + "   " + title) #test
