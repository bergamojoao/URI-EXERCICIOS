var input = "4\n11\n0";
var lines = input.split('\n');
j=0
let n=parseInt(lines.shift());
while(n!=0){
    soma=0
    j=0
    while(j<5){
        if(n%2==0){
            soma+=n
            n+=2
            j+=1
        }else n+=1
    }
    console.log(soma)
    n=parseInt(lines.shift());
}