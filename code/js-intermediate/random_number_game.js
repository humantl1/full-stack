console.log('hello world');
const number = Math.ceil(Math.random() * 10)
while(true) {
    let guess = Number(prompt("Guess a number 1 - 10"));
    if (guess === number) {
        break;
    }
    alert("Guess again");
}
alert("You guessed the number!");