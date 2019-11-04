var input = "10 5 3";
var lines = input.split(' ');

var a = parseInt(lines.shift());
var b = parseInt(lines.shift());
var c = parseInt(lines.shift());

let aant= a;let bant =b;let cant=c;

if(a>b){
    let aux = a;
    a=b;
    b=aux;
}
if(c<a){
    let aux = a;
    a=c;
    c=aux;
}
if(c<b){
    let aux = b;
    b=c;
    c=aux;
}

console.log(a+"\n"+b+"\n"+c+"\n\n"+aant+"\n"+bant+"\n"+cant)

