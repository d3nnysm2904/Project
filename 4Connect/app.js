const gridDisplay = document.querySelector("#game-container");
const scoreDisplay = document.querySelector("#score");
const resultDisplay = document.querySelector("#result");
const width = 4;

//create board
function createBoard() {
  for (let i = 0; i < width * width; i++) {
    square = document.createElement("div");
    square.innerHtml = 0;
    gridDisplay;
  }
}
