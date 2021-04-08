console.log("================================")
console.log(" C A I X A  E L E T R Ô N I C O ")
console.log("================================")

var saque = parseInt(prompt("Digite o valor que gostaria de sacar: "));

var tot = saque;
var cedula = 100;
var totced = 0;

while(true){
    if (tot >= cedula){
    totced += 1
    }
    else{
        if (totced > 0){
            alert("Total de "+ totced + " cédulas de R$ "+ cedula);
        }
        if (cedula == 100){
            cedula = 50
        }
        else if (cedula == 50){
            cedula = 20
        }
        else if (cedula == 20){
            cedula = 10
        }
        else if (cedula == 10){
            cedula = 5
        }
        else if (cedula == 5) {
            cedula = 1
        }
        if (tot == 0) {
            break;
        }
    }
}


console.log("Valor de saque" + saque)
console.log("OBRIGADO VOLTE SEMPRE!")