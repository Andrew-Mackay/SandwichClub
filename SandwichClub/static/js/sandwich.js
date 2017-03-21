var ing = {}; //ingredients
ing.br = "Bread";
ing.bc = "Bacon";
ing.lt = "Lettuce";
ing.tm = "Tomato";

window.onload = function(){
    var recipe = document.getElementById("recipe").innerHTML.split(",");
    for(var i=0;i<recipe.length;i++){
        makeIngredient(recipe[i]);
    }

    rating_span = document.getElementById("rating");
    rating = Number(rating_span.innerHTML);
    rating_span.innerHTML = "";
    for(var i=0;i<rating;i++){
        rating_span.innerHTML += "★";
    }
    for(var i=0;i<5-rating;i++){
        rating_span.innerHTML += "☆";
    }
}

makeIngredient = function(code){
    var block = document.createElement("div");
    block.className = "ingredient";

    var img = document.createElement("img");
    img.setAttribute("src","../../static/img/"+ing[code]+".jpg");
    img.setAttribute("alt",ing[code]);
    block.appendChild(img);

    document.getElementById("sandwich-recipe").appendChild(block);
}
