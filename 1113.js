var input = "5 4\n7 2\n3 8\n2 2";
var lines = input.split('\n');
lines.forEach(element => {
    [xStr,yStr] = element.split(' ')
    x = parseInt(xStr);
    y = parseInt(yStr);
    if(x>y)
        console.log("Decrescente")
    else if(x<y)
        console.log("Crescente")
    else return
});