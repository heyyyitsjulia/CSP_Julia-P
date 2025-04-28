let images = ["https://pinabresciani.com/wp-content/uploads/2023/01/Italian-seafood-pasta-1200.png", "https://www.foodandwine.com/thmb/i9SamRQmWvCB0uf-uHxRdIBG37o=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/cioppino-FT-RECIPE0521-4699a9c202574e5cb10232128b0aa90a.jpg"]
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
function hover(){
    document.getElementById("img").src = "https://www.foodandwine.com/thmb/i9SamRQmWvCB0uf-uHxRdIBG37o=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/cioppino-FT-RECIPE0521-4699a9c202574e5cb10232128b0aa90a.jpg"
}
function leave(){
    document.getElementById("img").src = "https://pinabresciani.com/wp-content/uploads/2023/01/Italian-seafood-pasta-1200.png"
}