var input = "21 22";
var lines = input.split(' ');
let E = parseInt(lines.shift());
let D = parseInt(lines.shift());
if(E>D || D>25){
    console.log("Eu odeio a professora!")
}else if(E<=(D-3))
    console.log("Muito bem! Apresenta antes do Natal!")
else{
    console.log("Parece o trabalho do meu filho!")
    E+=2
    if(E<24)
        console.log("TCC Apresentado!")
    else{
        console.log("Fail! Entao eh nataaaaal!")
    }
}

