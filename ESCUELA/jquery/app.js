/* Selecting elements  */
// same as jQuery()
$("ul");
/* this will select all uls */
// just like document.querySelectorAll
//this give u an object
$("h1").get(); //this gives an array instead of an obj
$("h1").get(0); //first h1
$("ul li"); //all li inside ul
$("*"); //everything in the page

$("h1").text(); //get the text inside h1
$("h1").text("Volcanooo"); //changin text inside to volcanooo

$("li").html(); //get the first li of the page
// $("li").html("lol"); //changes all li to lol

$("a").attr("href"); //this act like getAttribute
//$("a").attr("href", "google.com"); //this acts like setAttribute

const objImg = {
  src: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Reunion_2004_1.jpg/440px-Reunion_2004_1.jpg",
  alt: "lava",
};

$("img").attr(objImg); //this selects all img and changes all hrfef

$("inputs").eq(0); //gets index of whatever we are selecting

$("inputs").val(); //gets the value from inputs
$("inputs").val();
