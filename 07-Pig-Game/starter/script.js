"use strict";

const rollDice = document.querySelector(".btn--roll");
let dice = document.querySelector(".dice");
const active = document.querySelector(".player--active");
let player = "#current--0";
let currentScore = 0;

// rolls the dice and updates the score
function updateScore() {
  let randomNumber = Math.trunc(Math.random() * 6) + 1;

  console.log(randomNumber);

  switch (randomNumber) {
    case 1:
      dice.src = "dice-1.png";
      if (player === "#current--0") {
        currentScore = 0;
        document.querySelector(player).textContent = currentScore;
        return (player = "#current--1");
      } else {
        currentScore = 0;
        document.querySelector(player).textContent = currentScore;
        return (player = "#current--0");
      }
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

function updateBackground() {
  active.classList.remove("player--active");
}

rollDice.addEventListener("click", updateScore);

/* Without the parentheses, I am just referencing the function. 
With it, however, I am calling the function immediately and it thus executes even if 
I did not click the button. */
