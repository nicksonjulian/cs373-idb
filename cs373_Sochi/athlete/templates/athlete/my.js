$.getJSON( 'http://alabibliotheque.pythonanywhere.com/books/1.json', function(data){
    var items = [];
    $.each(data, function(key, value){
         items.push( "<li id='" + key + "'>" + val + "</li>" );
    });
    $( "<ul/>", {
        "class": "my-new-list",
        html: items.join( "" )
        }).appendTo( "body" );
});