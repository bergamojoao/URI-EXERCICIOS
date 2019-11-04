var input = "3\n3 -2\n-8 0\n0 8";
var lines = input.split('\n');
let qtd = parseInt(lines.shift());
let j=0
while(j<qtd){
    [xStr,yStr] = lines.shift().split(' ')
    let x = parseInt(xStr);
    let y = parseInt(yStr);
    console.log(y==0? "divisao impossivel" : (x/y).toFixed(1) )
    j+=1
}