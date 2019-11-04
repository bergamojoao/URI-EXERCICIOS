var input = "0 100\n1 100\n2 100\n3 100\n10 10\n3467 9350\n0 0";
var lines = input.split('\n');

let count=1
j=1
let countStr=""
lines.forEach(element => {
    [nStr,baseStr]=element.split(' ')
    base=parseInt(baseStr)
    n=parseInt(nStr);
    if(n!=0 && base != 0){
        count=1
        countStr=""
        countFib(n)
        countStr = count.toString()
        console.log(`Case ${j}: ${n} ${base} ${parseInt(countStr[countStr.length-1],10)%base}`)
    }
    
});

function countFib(n){
    if(n==0)
        return
    else if(n==1)
        return
    else{
        countFib(n-1)
        countFib(n-2)
        count+=2
    } 
}