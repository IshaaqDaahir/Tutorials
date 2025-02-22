/* document.body.addEventListener("click", (event) => {
    document.write(event.currentTarget);
}); */

document.body.addEventListener("keydown", (event) => {
    // document.write(event.key);
});

const button = document.querySelector("#click-me-btn");

button.addEventListener("click", (event) => {
    // document.write(event.target);
    // document.write(event.type);
    event.stopPropagation();
    alert("You clicked me!");
});

const form = document.querySelector("#name-form");

form.addEventListener("submit", (event) => {
    event.preventDefault();
    document.write(event.target.name.value);
});

window.addEventListener("load", () => {
    window.alert("The page has loaded!");
});

/* window.addEventListener("resize", () => {
    console.log(window.innerWidth);
    console.log(window.innerHeight);
}); */

window.addEventListener("scroll", () => {
    console.log("v scroll position", window.scrollY);
    console.log("h scroll position", window.scrollX);
});