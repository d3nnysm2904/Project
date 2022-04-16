const imgUrl = document.querySelector("#text");
const buttonCreate = document.querySelector("#img-file");
const memeImg = document.querySelector("#meme-img");
const topText = document.querySelector("#topText");
const bottomText = document.querySelector("#bottomText");

buttonCreate.addEventListener("click", function createImg(e) {
  e.preventDefault();

  const newImg = document.createElement("img");
  const topT = document.createElement("h2");
  const bottomT = document.createElement("h2");
  newImg.setAttribute("src", imgUrl.value);
  newImg.classList.add("newImg");
  bottomT.innerText = bottomText.value;
  bottomT.classList.add("bottomT");
  topT.innerText = topText.value;
  topT.classList.add("topT");
  memeImg.appendChild(newImg);
  memeImg.appendChild(topT);
  memeImg.appendChild(bottomT);
});
