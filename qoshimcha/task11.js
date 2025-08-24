const month = 23
if (month == 12 || month ==  1 || month == 2) {
    console.log('Qish');
}else if (month >= 3 && month <= 5) {
    console.log('Bahor');
}else if (month >= 6 && month <= 8) {
    console.log('Yoz');
}else if (month >= 9 && month <= 11) {
    console.log('kuz');
}else{
    console.log('Error: wrong month number');
}