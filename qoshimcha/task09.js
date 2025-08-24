let num1 = 11
let num2 = 12
let num3 = 10
if (num1 == num2 && num2 == num3) {
    console.log('Teng tomonli');
}else if (num1 == num2 || num2 == num3 || num1 == num3) {
    console.log('Teng yonli');
}else{
    console.log('Turli tomonli');
}