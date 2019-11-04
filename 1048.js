var input = "400\n"
var lines = input.split('\n');
let salario = parseFloat(lines.shift());
let nsalario=0.0
if(salario>0 && salario<=400){
    nsalario=salario+salario*0.15;
    console.log(`Novo salario: ${nsalario.toFixed(2)}`)
    console.log(`Reajuste ganho: ${(nsalario-salario).toFixed(2)}`)
    console.log(`Em percentual: 15 %`);
}else if(salario>400 && salario<=800){
    nsalario=salario+salario*0.12;
    console.log(`Novo salario: ${nsalario.toFixed(2)}`)
    console.log(`Reajuste ganho: ${(nsalario-salario).toFixed(2)}`)
    console.log(`Em percentual: 12 %`);
}else if(salario>800 && salario<=1200){
    nsalario=salario+salario*0.1
    console.log(`Novo salario: ${nsalario.toFixed(2)}`)
    console.log(`Reajuste ganho: ${(nsalario-salario).toFixed(2)}`)
    console.log(`Em percentual: 10 %`);
}else if(salario>1200 && salario<=2000){
    nsalario=salario+salario*0.07
    console.log(`Novo salario: ${nsalario.toFixed(2)}`)
    console.log(`Reajuste ganho: ${(nsalario-salario).toFixed(2)}`)
    console.log(`Em percentual: 7 %`);
}else{
    nsalario=salario+salario*0.04
    console.log(`Novo salario: ${nsalario.toFixed(2)}`)
    console.log(`Reajuste ganho: ${(nsalario-salario).toFixed(2)}`)
    console.log(`Em percentual: 4 %`);
} 
