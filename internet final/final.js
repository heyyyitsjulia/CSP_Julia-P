let images = [ "https://www.datocms-assets.com/19726/1716313326-adobestock_445877528.jpeg", "https://www.hyattvacationclub.com/files/live/sites/hvc-marketing/files/marketing/travel-inspiration/outdoor-adventures/24-503-3181201_WOH_HyattPlaceParkCity_Park_City_Utah_Fall_downtownHVCGettyImages-1277639781_16_9.webp"]
let counter = 0

function change(){
    if (counter < images.length){
        document.getElementById("img 1").src = images[counter]
        counter += 1
    }else{
        counter = 0 
        document.getElementById("img 1").src = images[counter] 
    }
    
}
function show(){
    if(document.getElementById("hidden").style.display==="block"){
        document.getElementById("hidden").style.display="block"
        document.getElementById("button").innerHTML="show less"
    }else{
        document.getElementById("hidden").style.display==="none"
         document.getElementById("button").innerHTML="show more"
    }
}