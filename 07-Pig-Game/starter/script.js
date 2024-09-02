"use strict";

// Selectors
const rollDice = document.querySelector(".btn--roll");
const holdDice = document.querySelector(".btn--hold");
const updateGame = document.querySelector(".btn--new");
const dice = document.querySelector(".dice");
const player0El = document.querySelector(".player--0");
const player1El = document.querySelector(".player--1");
const scoreEls = document.querySelectorAll(".score");
const currentEls = document.querySelectorAll(".current-score");

let currentPlayer = 0;
let scores = [0, 0];
let currentScore = 0;

// Hide the dice initially
dice.style.display = "none";

// Switch Player Function
function switchPlayer() {
  currentEls[currentPlayer].textContent = 0;
  currentScore = 0;
  currentPlayer = currentPlayer === 0 ? 1 : 0;
  player0El.classList.toggle("player--active");
  player1El.classList.toggle("player--active");
}

// Update Score Function
function updateScore() {
  dice.style.display = ""; // Show dice
  const randomNumber = Math.trunc(Math.random() * 6) + 1;
  dice.src = `dice-${randomNumber}.png`;

  if (randomNumber === 1) {
    switchPlayer();
  } else {
    currentScore += randomNumber;
    currentEls[currentPlayer].textContent = currentScore;
  }
}

// Hold Score Function
function holdScore() {
  scores[currentPlayer] += currentScore;
  scoreEls[currentPlayer].textContent = scores[currentPlayer];
  checkWinner();
  switchPlayer();
}

// Check Winner Function
function checkWinner() {
  if (scores[currentPlayer] >= 100) {
    document
      .querySelector(`.player--${currentPlayer}`)
      .classList.add("player--winner");
    document
      .querySelector(`.player--${currentPlayer}`)
      .classList.remove("player--active");
    disableButtons();
  }
}

// Disable Buttons After Win
function disableButtons() {
  rollDice.disabled = true;
  holdDice.disabled = true;
}

// New Game Function
function newGame() {
  scores = [0, 0];
  currentScore = 0;
  currentPlayer = 0;

  scoreEls.forEach((scoreEl) => (scoreEl.textContent = 0));
  currentEls.forEach((currentEl) => (currentEl.textContent = 0));

  player0El.classList.add("player--active");
  player1El.classList.remove("player--active");
  player0El.classList.remove("player--winner");
  player1El.classList.remove("player--winner");

  rollDice.disabled = false;
  holdDice.disabled = false;
  dice.style.display = "none";
}

// Event Listeners
rollDice.addEventListener("click", updateScore);
holdDice.addEventListener("click", holdScore);
updateGame.addEventListener("click", newGame);
