//"choice" is the user's choice
//"choice1" is the choice of the computer
let choice = "rock";
let choice1 = Math.floor(Math.random() * 3);

let rock = true;
let paper = true;
let scissors = true;
let rock1 = true;
let paper1 = true;
let scissors1 = true;

switch (choice) {
  case "rock":
    	choice = !rock;
    	console.log("You choose rock.");
      break;
  case "paper":
    	choice = !paper;
    	console.log("You choose paper.");
      break;
  case "scissors":
    	choice = !scissors;
    	console.log("You choose scissors.");
      break;
  default:
    	console.log("You haven't choose an item yet.")
}

switch (choice1) {
  case 0:
    	choice1 = !rock1;
    	console.log("Computer choose rock.");
      break;
  case 1:
    	choice1 = !paper1;
    	console.log("Computer choose paper.");
      break;
  case 2:
    	choice1 = !scissors1;
    	console.log("Computer choose scissors.");
      break;
}

if (!rock == !rock1) { 
  console.log("Both choose rock.");
  console.log("Rock against rock cancel each other.");
  console.log("Nobody win, try again!");
} else if (!rock == !paper1) {
  console.log("You choose rock and the computer choose paper.");
  console.log("Paper covers rock.");
  console.log("You lose.");
} else if (!rock == !scissors1) {
  console.log("You choose rock and the comptuer choose scissors.");
    console.log("Rock destroys scissors.");
  console.log("You win!");
} else if (!paper == !rock1) {
  console.log("You choose paper and the computer choose rock.");
  console.log("Paper covers rock.");
  console.log("You win!");
} else if (!paper == !paper1) {
  console.log("Both choose paper.");
  console.log("Paper cons paper end in a draw.");
  console.log("Nobody lose, try again !");
} else if (!paper == !scissor1) {
  console.log("You choose paper and the compurter choose scissors.");
  console.log("Scissors cut paper.");
  console.log("You lose!");
} else if (!scissors == !rock1) {
  console.log("You choose scissors and the computer choose rock.");
  console.log("Rock destroys scissors.");
  console.log("You lose!");
} else if (!scissors == !paper1) {
  console.log("You choose scissors and the computer  choose paper.");
  console.log("Scissors cut paper.");
  console.log("You win!");
} else if (!scissors == !scissors1) {
	console.log("Both choose scissors.");
  console.log("Scissors vs. scissors: equality!");
  console.log("Try again.");
}