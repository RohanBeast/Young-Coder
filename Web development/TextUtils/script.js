let textArea = document.getElementById('text');
let word = document.getElementById('text1');
let spaces = document.getElementById('text2');
let wpm = document.getElementById('text3');
let a = document.getElementById('text4');

function analyze() {
    const text = textArea.value;

    var words = text.length;
    
    let space = 0;
    for (item of text){
        if (item == ' ') {
            space++;
            words -= 1;
        }
    };

    function speed(length) {
        let x = length/250;
        let seconds = x * 60;

        return seconds;
    }
    
    spaces.innerText = `Spaces: ${String(space)}`;
    word.innerText = `Words: ${words}`;
    wpm.innerText = `Reading Time: ${speed(words)}seconds`;
    a.innerText = '';
}

function spac() {
    const text = textArea.value;
    text.trim();

    a.innerText = text;
    spaces.innerText = ``;
    word.innerText = ``;
    wpm.innerText = ``;
}

function capital() {
    const text = textArea.value;
    let n = text.toUpperCase();
    
    a.innerText = n;
    spaces.innerText = ``;
    word.innerText = ``;
    wpm.innerText = ``;
}