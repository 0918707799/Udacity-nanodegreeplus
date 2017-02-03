var dognum = [0,0,0,0,0,0,0];
var dogobj ={};

var $name = $('#name');
var $num = $('#num');
// var $img = $('#image');



$("#dog li").click(function() {
    $name.text($(this).text());
    id = Number(this.id);
    var imgName = 'img/img'+id+'.jpg';
    // $num.text(imgName);
    dogobj[imgName] = id;
    // $("#imghld").append('<img src="' +imgName + '">');
    $( "#imghld > img" ).replaceWith('<img src="' +imgName + '">');

});

function getProperty(propertyName) {
    return dogobj[propertyName];
};

// Example of getProperty function
// getProperty("key1");


$( "#imghld" ).click(function() {
    var img = $(this).find("img");
    var img_path = img.attr("src");
    var $num = $('#num');
    var dogid = dogobj[img_path];
    dognum[dogid] = dognum[dogid]+1;
    $num.text("ClickCount is :: " + dognum[dogid]);
});
