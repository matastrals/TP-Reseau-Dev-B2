const WebSocket = require('ws');

// il faut installer "prompt" avec "npm install prompt-sync"
const prompt = require('prompt-sync')();
webSocket = new WebSocket("ws://127.0.0.1:13543");
webSocket.addEventListener('open', function (event) {
data = webSocket.onmessage = (event) => {
    console.log(event.data);
}
let name = prompt("What want you to say ? : ");
webSocket.send(name)
data = webSocket.onmessage = (event) => {
    console.log(event.data);
}
});


