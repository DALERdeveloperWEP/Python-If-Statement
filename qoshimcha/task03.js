let str = 'A'
if (str.charCodeAt() >= 65 && str.charCodeAt() <= 90) {
    console.log('Katta harf');
}else if(str.charCodeAt() >= 97 && str.charCodeAt() <= 122){
    console.log('Kichik harf');
}else{
    console.log('bunday harf yoq');
}