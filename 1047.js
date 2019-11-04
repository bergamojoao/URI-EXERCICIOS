var input = "7 7 7 7";
var lines = input.split(' ');

var hini = parseInt(lines.shift());
var mini = parseInt(lines.shift());
var hfim = parseInt(lines.shift());
var mfim = parseInt(lines.shift());

let horas=0
let minutos=0
let j=0
aux=hini
while(hini!=hfim || (j==0 && mini>=mfim)){
    if(hini==24)
        hini=0
    horas+=1
    if(hini==aux && j!=0 && mini<=mfim){
        horas=24
        break
    }   
    hini+=1   
    j+=1
}
if(mini>mfim){
    horas-=1
}
aux=mini
j=0
while(mini!=mfim){
    if(mini==60)
        mini=0
    minutos+=1
    if(mini==aux && j!=0){
        horas+=1
    }   
    mini+=1   
    j+=1
}

console.log(`O JOGO DUROU ${horas} HORA(S) E ${minutos} MINUTO(S)`)