"use strict";

// Displays an ingredient tile with the given code
var makeIngredient = function(ingredient){
    var block = document.createElement("div");
    block.className = "ingredient";

    var img = document.createElement("img");
    img.setAttribute("src","../../static/img/"+slug(ingredient)+".jpg");
    img.setAttribute("alt",ingredient);
    block.appendChild(img);

    document.getElementById("sandwich-recipe").appendChild(block);
};

//returns a file-friendly name for a string
var slug = function(str){
    str = str.toLowerCase();
    str = str.replace(" ","-");
    return str;
};

window.onload = function(){
    //displays the sandwich's recipe
    var recipe = document.getElementById("recipe").innerHTML.split(",");
    var i;
    for(i=0;i<recipe.length;i+=1){
        makeIngredient(recipe[i]);
    }

    // displays the sandwich's rating
    var rating_span = document.getElementById("rating");
    var rating = Number(rating_span.innerHTML);
    rating_span.innerHTML = "(";
    for(i=0;i<rating;i+=1){ rating_span.innerHTML += "★"; }
    for(i=0;i<5-rating;i+=1){ rating_span.innerHTML += "☆"; }
    rating_span.innerHTML += ")";

};
