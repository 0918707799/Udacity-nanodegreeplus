var i=0;
var dog1="RUFFY";
$("#name1").text(dog1);
$( "#image1" ).click(function() {
  var $num1 = $('#num1');
  i = i+1;
  $num1.text("Click-Count is: " +i+ "________");
});

var j=0;
var dog2="SCOOBY";
$("#name2").text(dog2);
$( "#image2" ).click(function() {
  var $num2 = $('#num2');
  j = j+1;
  $num2.text("Click-Count is: " +j+ "________");
});
