var input = "16 2";
var lines = input.split('\n');

let inicio = parseInt(lines.shift())
let fim = parseInt(lines.shift())
let total=0
if(inicio==fim){
    total=24
}else{
    while(inicio!=fim){
        inicio+=1
        total+=1
        if(inicio==24)
            inicio=0;
    }
}
console.log(`O JOGO DUROU ${total} HORA(S)`)