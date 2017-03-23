"use strict";

//returns a file-friendly name for a string
var slug = function(str){
    str = str.toLowerCase();
    str = str.replace(" ","-");
    return str;
};

// Displays an ingredient tile with the given code
var makeIngredient = function(ingredient){
    var block = document.createElement("div");
    block.className = "ingredient";
    block.style.backgroundImage = "url('../../static/img/"+slug(ingredient)+".jpg')";
    block.style.backgroundSize = "100% 100%";
    block.appendChild(document.createTextNode(ingredient));

    document.getElementById("sandwich-recipe").appendChild(block);
};

//cleans up user input strings
var cleanstr = function(str){
    str = str.trim();           //removes whitespace from either side
    str = str.toLowerCase();    //normalizes capitalization
    str = str.replace(/\s{2,}/g, ' '); //removes double spaces
    var i;
    for(i=0;i<str.length;i+=1){ //capitalizes each word
        if(i===0 || str.charAt(i-1)===' '){
            str = str.substr(0,i) + str.charAt(i).toUpperCase() + str.substr(i+1);
        }
    }
};

//adds an ingredient (for use in create_sandwich.html)
var addIng = function(){
    var ingredient = document.getElementById("recipe_input_box").value;
    document.getElementById("recipe_input_box").value = "";
    makeIngredient(ingredient);
    var rec = document.getElementById("id_recipe");
    rec.value = (rec.value + ingredient + ',');
};

window.onload = function(){
    var i;
    if(document.getElementById("sandwich-recipe").getAttribute("create")==="true"){
        //set up create sandwich recipe
        document.getElementById("ing_submit").addEventListener("click",addIng);
    } else{
        //displays the sandwich's recipe
        var recipe = document.getElementById("recipe").innerHTML.split(",");
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
    }
};
