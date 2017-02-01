
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");
    // grab the value of input box with id="street"
    var streetStr = $('#street').val();
    // grab the value of input box with id="city"
    var cityStr = $('#city').val();
    var address = streetStr + ', ' + cityStr;

    // to print something in the top
    $greeting.text('So, your new place "' + address + '"?');
    var streetviewUrl = 'http://maps.googleapis.com/maps/api/streetview?size=600x300&location=' + address + '';

    $("body").append('<img class="bgimg" src="' +streetviewUrl + '">');
    // load streetview

    // YOUR CODE GOES HERE!  f508166573154aaca4e4037279e85f58

    // Example provided in NY times api page
    // var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    // url += '?' + $.param({
    //     'api-key': "f508166573154aaca4e4037279e85f58",
    //     'q': "san francisco"
    // });
    // __OR

    var nytimesUrl = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q='+cityStr+'&sort=newest&api-key=f508166573154aaca4e4037279e85f58';
    // $greeting.text(nyTimesURL);
    $.getJSON( nytimesUrl, function( data ){
        $nytHeaderElem.text('New York Times Articles About -->' + cityStr);

        articles = data.response.docs;
        for (var i = 0; i < articles.length; i++) {
                var article = articles[i];
                $nytElem.append('<li class="article">' + '<a href="'+
                article.web_url+'">'+article.headline.main+'</a>'+'<p>'+
                article.snippet+'</p>'+'</li>');
        };
    })

    return false;
};

$('#form-container').submit(loadData);
