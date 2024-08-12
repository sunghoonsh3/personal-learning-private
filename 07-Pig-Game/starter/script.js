"use strict";

const rollDice = document.querySelector(".btn--roll");
let dice = document.querySelector(".dice");

const playerOneID = "#current--0";
const playerTwoID = "#current--1";

let currentScore = 0;

// rolls the dice and updates the score
function updateScore(player) {
  let randomNumber = Math.trunc(Math.random() * 6) + 1;

  console.log(randomNumber);

  switch (randomNumber) {
    case 1:
      dice.src = "dice-1.png";
      break;
    case 2:
      dice.src = "dice-2.png";
      break;
    case 3:
      dice.src = "dice-3.png";
      break;
    case 4:
      dice.src = "dice-4.png";
      break;
    case 5:
      dice.src = "dice-5.png";
      break;
    case 6:
      dice.src = "dice-6.png";
      break;
  }

  currentScore += randomNumber;
  document.querySelector(player).textContent = currentScore;
}

rollDice.addEventListener("click", function () {
  updateScore(playerOneID);
});

/* Without the parentheses, I am just referencing the function. 
With it, however, I am calling the function immediately and it thus executes even if 
I did not click the button. */
