// app.js
const fetch = require('node-fetch'); // npm install node-fetch@2
const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Type something to convert to speech: ', async (text) => {
    try {
        const response = await fetch('http://127.0.0.1:5000/speak', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });

        const buffer = await response.arrayBuffer();
        const filePath = 'output.mp3';
        fs.writeFileSync(filePath, Buffer.from(buffer));
        console.log(`Audio saved as ${filePath}`);
        
        // Optional: Play the audio (Linux/macOS example)
        // require('child_process').exec(`start ${filePath}`); // Windows
        // require('child_process').exec(`afplay ${filePath}`); // macOS
        // require('child_process').exec(`mpg123 ${filePath}`); // Linux

    } catch (error) {
        console.error('Error:', error);
    } finally {
        rl.close();
    }
});