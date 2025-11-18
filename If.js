function count(){
const NumIn = document.getElementById("NumIn").value;
let message = ""
let NumInToInt= parseInt(NumIn)
if(NumInToInt >= 10){
    message = "Nilai lebih dari atau sama dengan 10"
}
else{
    message = "Nilai kurang dari 10"
}
if(NumInToInt < 0){
    message = "Hasil negatif" 
}
document.getElementById("result").innerHTML = message
}