import { createCanvas, loadImage } from 'canvas';
import * as fs from 'fs';

// Constants for the screen size
const SCREEN_WIDTH = 800;
const SCREEN_HEIGHT = 400;

// Colors
const WHITE = '#FFFFFF';

// Create a canvas
const canvas = createCanvas(SCREEN_WIDTH, SCREEN_HEIGHT);
const ctx = canvas.getContext('2d');

// Load the cat image
const catImage = await loadImage('Scratchcat.png'); // Make sure you have an image of the cat

// Set up initial cat position and movement variables
let catX = 0;
const catSpeed = 5;
let movingRight = true;
let roundTrip = 0;

// Create a function to handle the game loop
function gameLoop() {
    // Clear the screen
    ctx.fillStyle = WHITE;
    ctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);

    // Update cat position
    if (movingRight) {
        catX += catSpeed;
    } else {
        catX -= catSpeed;
    }

    // Check if the cat reaches the right end
    if (catX >= SCREEN_WIDTH) {
        movingRight = false;
        roundTrip += 1;
    } else if (catX <= 0) {
        movingRight = true;
        if (roundTrip > 0) {
            console.log("Meow"); // Print "Meow" after each round trip
        }
    }

    // Blit the cat on the canvas
    ctx.drawImage(catImage, catX, 300); // 300 is the y-coordinate for the floor

    // Save the canvas as an image (optional)
    const out = fs.createWriteStream(__dirname + '/output.png');
    const stream = canvas.createPNGStream();
    stream.pipe(out);

    // Set the game loop to run again
    setTimeout(gameLoop, 1000 / 60); // 60 FPS
}

// Start the game loop
gameLoop();