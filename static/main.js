const stars = document.querySelector("#stars");
const colors = ["#fff", "#333", "#eee", "#777"]
for(let i = 0; i < 100; i++){
    const star = document.createElement("div");
    star.classList.add("star");
    star.style.top = (Math.random() * window.innerHeight + 10) + "px";
    star.style.left = (Math.random() * window.innerWidth + 10) + "px";
    star.style.background = colors[Math.floor(Math.random() * colors.length)];
    stars.appendChild(star)
}
window.addEventListener("scroll", reveal)
const sections = document.querySelectorAll(".reveal");
function reveal(){
    for(let i = 0; i < sections.length; i++){
        var windowheight = window.innerHeight;
        var revealheight = sections[i].getBoundingClientRect().top;
        var reveal_point = 150;

        if(revealheight < windowheight - reveal_point){
            sections[i].classList.add("active")
        } else {
            sections[i].classList.remove("active")
        }
    }
}
const ph = document.querySelector("#ph");
const wh = document.querySelector("#wh");
window.addEventListener("load", () => {
    document.body.style.opacity = 1;
})