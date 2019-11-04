var input = "10\n4\n32\n34\n543\n3456\n654\n567\n87\n6789\n98";
var lines = input.split('\n');
let n = parseInt(lines.shift());
let j=0
let array=[]
while(j<n){
    array[j]=parseInt(lines.shift());
    j+=1
}
array.sort((a,b)=>{
    if(a%2==0 && b%2!=0)
        return -1;
    if(a%2!=0 && b%2==0)
        return 1
    if(a%2==0 && b%2==0)
        if(a>b)
            return 1
        else if(a<b)
            return -1
        else return 0;
    if(a%2!=0 && b%2!=0)
        if(a>b)
            return -1
        else if(a<b)
            return 1
        else return 0;
})
array.forEach((element)=>console.log(element))