import urllib.request
import json
from django import template
register = template.Library()

#a is the array to contain the book's title, book cover, author's full name, author photo, and publishers, in that order. Note: there can be multiple publishers.
def exerciseapi(theid):
    a = []
    response = urllib.request.urlopen('https://alabibliotheque.pythonanywhere.com/books/' + str(theid) + '.json')
    html = response.read()
    data = json.loads(html.decode('utf8'))
    title = data['title'] #book's title
    book_pic = data['cover']
    book_desc = data['summary']
    authorid = data['author']
    publisherids = data['publishers']
    a.append(title)
    a.append(book_pic)
    a.append(book_desc)
    response2 = urllib.request.urlopen('http://alabibliotheque.pythonanywhere.com/authors/' + str(authorid) + '.json')
    html2 = response2.read()
    data2 = json.loads(html2.decode('utf8'))
    authorfullname = data2['name'] #books's author
    author_pic = data2['photo']
    author_bio = data2['bio']
    a.append(authorfullname)
    a.append(author_pic)
    a.append(author_bio)

    for publisherid in publisherids:
        response3 = urllib.request.urlopen('http://alabibliotheque.pythonanywhere.com/publishers/' + str(publisherid) + '.json')
        html3 = response3.read()
        data3 = json.loads(html3.decode('utf8'))
        publishername = data3['name'] #books's publisher
        a.append(publishername)

    return a

register.filter('get_json', exerciseapi)