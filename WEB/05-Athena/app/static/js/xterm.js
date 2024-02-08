import { Terminal } from 'xterm';
import 'xterm/css/xterm.css';

document.addEventListener('DOMContentLoaded', function () {
    // Initialize Xterm.js terminal
    const term = new Terminal();
    term.open(document.getElementById('terminal'));

    // Example on how to handle input
    term.onKey(e => {
        const input = e.key;
        // Process the input (send to backend, display in terminal, etc.)
    });
});