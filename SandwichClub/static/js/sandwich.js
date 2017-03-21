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
}

makeIngredient = function(code){
    var block = document.createElement("div");
    block.className = "ingredient";

    //will be an image at some point
    block.appendChild(document.createTextNode(ing[code.toString()]));

    document.getElementById("sandwich-recipe").appendChild(block);
}
