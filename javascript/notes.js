let images = ["https://gardenandgun.com/wp-content/uploads/2024/02/Atlantic-Beach_Terry-Ward.jpg", "https://texascooppower.com/wp-content/uploads/2021/02/wildflowers-cover-2.jpg", "https://img.freepik.com/free-photo/sunset-time-tropical-beach-sea-with-coconut-palm-tree_74190-1075.jpg?semt=ais_hybrid&w=740", "https://static.wikia.nocookie.net/d7fbdcef-11f8-4ae9-a214-806ecdc55531/scale-to-width/755"]
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

function hello(){
    document.getElementById("title").innerHTML = "Hello World!"
}
function hover(){
    document.getElementById("img").src = "https://texascooppower.com/wp-content/uploads/2021/02/wildflowers-cover-2.jpg"
}
function leave(){
    document.getElementById("img").src = "https://gardenandgun.com/wp-content/uploads/2024/02/Atlantic-Beach_Terry-Ward.jpg"
}
function hidden(){
    document.getElementById("meme").style.display = "block"
}