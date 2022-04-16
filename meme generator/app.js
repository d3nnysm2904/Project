const imgUrl = document.querySelector("#text");
const buttonCreate = document.querySelector("#imgFile");
const memeImg = document.querySelector("#meme-img");

console.log(imgUrl.value);
buttonCreate.addEventListener("click", function createImg(e) {
  e.preventDefault();
  const newImg = document.createElement("img");
  newImg.setAttribute("src", imgUrl.value);
  newImg.classList.add("newImg");
  memeImg.appendChild(newImg);
});
