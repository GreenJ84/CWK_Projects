const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let ballArray = []
const ballCount = 40;

function addBalls() {
    for (let i = 0; i < ballCount; i++){
        let radius = randomNumber(10, 20)
        let ball = {
            radius: radius,
            x: randomNumber(0+radius, canvas.width-radius),
            y: randomNumber(0+radius, canvas.height-radius),
            dx: randomSpeed(-5, 5),
            dy: randomSpeed(-5, 5),
            color: randomColor(),
        }
        ballArray.push(ball);
    }
}
addBalls();

function drawBalls(ball) {
    ctx.beginPath();
    ctx.arc(ball.x, ball.y, ball.radius, 0, 2 * Math.PI);
    ctx.fillStyle = ball.color;
    ctx.fill();
    ctx.strokeStyle = randomColor();
    ctx.stroke();
    ctx.closePath();
}

function moveBalls(ball) {
    drawBalls(ball);
    ball.x += ball.dx
    ball.y += ball.dy
    if (Math.floor(ball.x + ball.y) % 11 == 0) {
        ball.color = randomColor();
    }
    if (ball.x + ball.dx >= canvas.width - ball.radius || ball.x + ball.dx <= 0 + ball.radius) {
        ball.dx *= -1
    }
    if (ball.y + ball.dy >= canvas.height - ball.radius || ball.y + ball.dy <= 0 + ball.radius) {
        ball.dy *= -1
    }
}

function updateScreen() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let ball of ballArray) {
        console.log(ball);
        moveBalls(ball);
    }
}
setInterval(updateScreen, 30);

function randomNumber(min, max) {
    return Math.random() * (max - min) + min;
}

function randomSpeed(min, max){
    let speed = randomNumber(min, max);
    while (speed > -1.5 && speed < 1.5) {
        speed = randomSpeed(min, max);
    }
    return speed;
}

function randomColor() {
    let red = Math.floor(randomNumber(0, 250));
    let green = Math.floor(randomNumber(0, 250));
    let blue = Math.floor(randomNumber(0, 250));
    let opacity = randomNumber(.4, .8).toFixed(2);
    return `rgba(${red}, ${green}, ${blue}, ${opacity})`;
}
