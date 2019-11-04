var input = "2\n5\n4";
var lines = input.split('\n');

let count=0
j=0

function countFib(n){
    if(n==0)
        return 0
    else if(n==1)
        return 1
    else{
        count+=2
        return countFib(n-1)+countFib(n-2)
    } 
}

let qtd = parseInt(lines.shift())

while(j<qtd){
    n=parseInt(lines.shift());
    count=0
    countStr=""
    fib=countFib(n)
    countStr = count.toString()
    console.log(`fib(${n}) = ${count} calls = ${fib}`)
    j+=1
}