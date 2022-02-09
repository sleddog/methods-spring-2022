var allowedKeys = {
    ArrowLeft: 'left',
    ArrowUp: 'up',
    ArrowRight: 'right',
    ArrowDown: 'down',
    a: 'a',
    b: 'b'
};

var kanomiCode = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a'];

var position = 0;

document.addEventListener('keydown', function(e){
    var inKey = allowedKeys[e.key];
    var requiredKey = kanomiCode[position];
    if (inKey == requiredKey){
        position++;
        if(position == kanomiCode.length){
            activateCheats();
            position = 0;
        }
    } else{
        position = 0;
    }
})

function activateCheats() {
    document.body.style.backgroundImage = "url('cheat/scream.gif')";

    window.alert("cheat activated");
    console.log("cheat activated");
}
