const b1 = document.querySelector(".b1");
const b2 = document.querySelector(".b2");

b1.addEventListener("click", function (){
    window.location.href = '../add_book/';
    console.log("Hello there");
});

b2.addEventListener("click", function (){
    window.location.href = '../search_book/';
});
