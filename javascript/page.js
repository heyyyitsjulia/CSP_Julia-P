let images = ["https://www.wwf.org.uk/sites/default/files/styles/content_slide_image/public/2020-08/Small_WW22392.jpg?h=0e753701&itok=lCMX5Gse"]
let counter = 0 

function change(){
    if (counter < images.length){
        document.getElementById("img").src = images[counter]
        counter += 1
    }else{
        counter = 0 
        document.getElementById("img").style.display ==="none"
    }
}
function hover(){
    document.getElementById("img").style.display=== "none"
}