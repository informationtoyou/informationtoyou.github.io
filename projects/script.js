const p5 = require('node-p5');

function sketch(p) {
    p.setup = () => {
        let canvas = p.createCanvas(200, 200);
        setTimeout(() => {
            p.saveCanvas(canvas, 'myCanvas', 'png').then(filename => {
                console.log(`saved the canvas as ${filename}`);
            });
        }, 100);
    }
    p.draw = () => {
        p.background(50);
        p.text('hello world!', 50, 100);
    }
}

let p5Instance = p5.createSketch(sketch);