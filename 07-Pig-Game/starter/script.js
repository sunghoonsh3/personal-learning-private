"use strict";

const rollDice = document.querySelector(".btn--roll");
const holdDice = document.querySelector(".btn--hold");
const updateGame = document.querySelector(".btn--new");
const dice = document.querySelector(".dice");
const active = document.querySelector(".player--active");
let player = "#current--0";
let score = "#score--0";
let playerOneScore = 0;
let playerTwoScore = 0;
let currentScore = 0;

// turn off the dice when the game starts

dice.style.display = 'none'; // this hides the "dice"

// rolls the dice and updates the score
function updateScore() {

  dice.style.display = ''; // revert back to its original 
  let randomNumber = Math.trunc(Math.random() * 6) + 1;

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

function holdScore() {

  if (player === "#current--0")  {
    score = "#score--0";
    playerOneScore += currentScore;
    document.querySelector(score).textContent = playerOneScore;
    return (player = "#current--1", currentScore = 0); 
  }

  else {
    score = "#score--1";
    playerTwoScore += currentScore;
    document.querySelector(score).textContent = playerTwoScore;
    return (player = "#current--0", currentScore = 0);
  }
}

function newGame() {
  playerOneScore = 0;
  playerTwoScore = 0;
  currentScore = 0;
  document.querySelectorAll(".score")[0].textContent = 0;
  document.querySelectorAll(".score")[1].textContent = 0;
  document.querySelectorAll(".current-score")[0].textContent = 0;
  document.querySelectorAll(".current-score")[1].textContent = 0;

  // remember that querySelector only applies to the first one that matches its condition

}

function updateBackground() {
  active.classList.remove("player--active");
}

rollDice.addEventListener("click", updateScore);
holdDice.addEventListener("click", holdScore);
updateGame.addEventListener("click", newGame);


/* Without the parentheses, I am just referencing the function. 
With it, however, I am calling the function immediately and it thus executes even if 
I did not click the button. */