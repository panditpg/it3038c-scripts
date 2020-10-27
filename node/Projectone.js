// setTimeout.js
let cue = 'The folks are here!';

//But the cue will not announce till 4000ms have passed with setTimeout
setTimeout(function() {
    return console.log(cue);

}, 4000);

// I'll execute as soon as it's done.
console.log('Waiting for the folks now. The folks are here!');



