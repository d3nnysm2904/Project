// let playerRed = "r";
// let playerYellow = "y";

// let currentPlayer = playerRed;

// const gameOver = false;
// let board = undefined;

// const row = 6;
// const columns = 7;

// const boardDiv = document.querySelector("#board");

// function setGame() {
//   board = [];
//   for (let r = 0; r < 6; r++) {
//     let row = [];
//     for (let c = 0; c < 7; c++) {
//       row.push(" ");

//       let tile = document.createElement("div");
//       tile.id = r.toString() + "-" + c.toString();
//       tile.classList.add("tile");
//       document.querySelector("#board").appendChild(tile);
//     }
//     board.push(row);
//   }
// }

// setGame();

const WIDTH = 7;
const HEIGHT = 6;

let currPlayer = 1; // active player: 1 or 2
let board = []; // array of rows, each row is array of cells  (board[y][x])

/** makeBoard: create in-JS board structure:
 *   board = array of rows, each row is array of cells  (board[y][x])
 */

function makeBoard() {
  for (let y = 0; y < HEIGHT; y++) {
    board.push(Array.from({ length: WIDTH }));
  }
}
makeBoard();
