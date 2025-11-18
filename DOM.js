document.getElementById("Heading1").innerHTML = "Selamat datang di DOM Javascript";
function changetext() {
document.getElementById("nama").innerHTML = "Jennifer";
}
function removetext() {
document.getElementById("nama").innerHTML = "";
}
function changeName() {
let name = document.getElementById("name").value;
document.getElementById("result").innerHTML = name;
}
function removeinput() {
document.getElementById("name").value = "";
document.getElementById("result").innerHTML = "";
}