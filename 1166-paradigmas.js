var input = "1\n2\n0";
var lines = input.split('\n');
j=1
let n=parseInt(lines.shift());
while(n!=0){
    max = Math.pow(2,n)-1;
    console.log(`Teste ${j}`)
    console.log(max)
    console.log()
    j+=1
    n=parseInt(lines.shift());
}