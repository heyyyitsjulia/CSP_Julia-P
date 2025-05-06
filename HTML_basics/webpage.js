let images = [ "https://www.foodandwine.com/thmb/i9SamRQmWvCB0uf-uHxRdIBG37o=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/cioppino-FT-RECIPE0521-4699a9c202574e5cb10232128b0aa90a.jpg"]
let counter = 0

function change(){
    if (counter < images.length){
        document.getElementById("img").src = images[counter]
        counter += 1
    }else{
        counter = 0 
        document.getElementById("img").src = images[counter] 
    }
    
}
function show(){
    if(document.getElementById("language").style.display==="block"){
        document.getElementById("language").style.display="none"
        document.getElementById("button").innerHTML="Show More!"
    }else{
        document.getElementById("language").style.display="block"
         document.getElementById("button").innerHTML="show less..."
    }
}
