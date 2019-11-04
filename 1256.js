var input = "2\n13 9\n44 45 49 70 27 73 92 97 95\n7 8\n35 12 2 17 19 51 88 86";
var lines = input.split('\n');
let casos = parseInt(lines.shift());
let i =0
while(i<casos){
    [tamanhoStr,chavesStr] = lines.shift().split(' ');
    let tamanho = parseInt(tamanhoStr);
    let chaves = parseInt(chavesStr);
    let j=0
    v = new Array(tamanho)
    ch = lines.shift().split(' ');
    for (let index = 0; index <tamanho; index++) {
        v[index]=""
    }
    while(j<chaves){
        k = parseInt(ch.shift())
        v[k%tamanho] +=" -> "+k
        j+=1
    }
    v.forEach((element,index) => {
        console.log(index+element+" -> \\")
    });
    if(i!=casos-1)
        console.log()
    i+=1
}