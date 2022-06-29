const encode = document.querySelector('.menu_encode_EN');
const decode = document.querySelector('.menu_decode_DE');
const decodeMenu = document.querySelector('.menu_decode_bar');
const encodeMenu = document.querySelector('.menu_encode_bar');
const encodeList = document.querySelector('.menu_encode_bar_link1');
const decodeList = document.querySelector('.menu_encode_bar_link2');


function MouseHoverEvent (){
    console.log("son");
    // encodeMenu.classList.add('show');
    encodeMenu.classList.toggle('hidden');
}



function MouseHoverEvent2 (){
    console.log("son2");
    // encodeMenu.classList.add('show');
    decodeMenu.classList.toggle('hidden2')
}

function init (){
    encode.addEventListener("click", MouseHoverEvent);

    decode.addEventListener("click", MouseHoverEvent2);
}
init();