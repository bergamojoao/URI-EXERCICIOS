var input = "6.0 8.0 10.0";
var lines = input.split(' ');

var a = parseFloat(lines.shift());
var b = parseFloat(lines.shift());
var c = parseFloat(lines.shift());

if(b>a){
    let aux = a;
    a=b;
    b=aux;
}
if(c>a){
    let aux = a;
    a=c;
    c=aux;
}
if(c>b){
    let aux = b;
    b=c;
    b=aux;
}

if(a>=b+c){
    console.log("NAO FORMA TRIANGULO");
}else{
    if(Math.pow(a,2)==Math.pow(b,2)+Math.pow(c,2)){
        console.log("TRIANGULO RETANGULO");
    }
    if(Math.pow(a,2)>Math.pow(b,2)+Math.pow(c,2)){
        console.log("TRIANGULO OBTUSANGULO");
    }
    if(Math.pow(a,2)<Math.pow(b,2)+Math.pow(c,2)){
        console.log("TRIANGULO ACUTANGULO");
    }
    if(a==b && a==c){
        console.log("TRIANGULO EQUILATERO");
    }else if(a==b || c==a || b==c){
        console.log("TRIANGULO ISOSCELES");
    }
}