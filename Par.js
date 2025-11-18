function kali(){
let FirstNumber = document.getElementById("FirstNumber").value;
let SecondNumber = document.getElementById("SecondNumber").value;
hasil3 = parseInt(FirstNumber) * parseInt(SecondNumber);
document.getElementById("result").innerHTML = hasil3;
}
function tambah(){
let FirstNumber = document.getElementById("FirstNumber").value;
let SecondNumber = document.getElementById("SecondNumber").value;
hasil1 = parseInt(FirstNumber) + parseInt(SecondNumber);
document.getElementById("result").innerHTML = hasil1;
}
function kurang(){
let FirstNumber = document.getElementById("FirstNumber").value;
let SecondNumber = document.getElementById("SecondNumber").value;
hasil2 = parseInt(FirstNumber) - parseInt(SecondNumber);
document.getElementById("result").innerHTML = hasil2;
}
function bagi(){
let FirstNumber = document.getElementById("FirstNumber").value;
let SecondNumber = document.getElementById("SecondNumber").value;
hasil4 = parseInt(FirstNumber) / parseInt(SecondNumber);
document.getElementById("result").innerHTML = hasil4;
}
function remove(){
document.getElementById("FirstNumber").value = "";
document.getElementById("SecondNumber").value = "";
document.getElementById("result").innerHTML = "";
}