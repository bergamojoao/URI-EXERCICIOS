var input = "2.0 4.0 7.5 8.0\n6.4";
var lines = input.split('\n');
const linha1 =lines[0].split(' ');

let pesos=[2,3,4,1]
let notas = [parseFloat(linha1.shift()),parseFloat(linha1.shift()),parseFloat(linha1.shift()),parseFloat(linha1.shift())];
let media = 0
notas.map((v,i)=>{
    media += v*pesos[i]
})
let div = 0
pesos.map((v)=>div+=v)
media= media/div;
console.log(`Media: ${media.toFixed(1)}`)
if(media>=7){
    console.log("Aluno aprovado.")

}else if(media<7 && media>=5){
    console.log("Aluno em exame.")
    let exame = parseFloat(lines[1]);
    console.log(`Nota do exame: ${exame.toFixed(1)}`)
    media=(media+exame)/2
    if(media>=5){
        console.log("Aluno aprovado.")
    }else{
        console.log("Aluno reprovado.")
    }
    console.log(`Media final: ${media.toFixed(1)}`)

}else{
    console.log("Aluno reprovado.")
}


