let shower = document.getElementById("shower")
let tbl = document.getElementsByClassName("table")
let popup = document.getElementById("popup")
let raport = document.getElementById("raport")
let command = document.getElementById("command")
let approve = document.getElementById("approve")
let message = document.getElementById("message")
let incedent = document.getElementById("incedent")
let popup_close = document.getElementById("popup_close")
let container = document.getElementById("container")

shower.onclick = () => {
    for (let el of tbl) {
        el.classList.toggle("hidden")
    }
    if (shower.innerText == 'Скрыть все кроме открытых') {
        shower.innerText = 'Показать все заявки';
    } else {
        shower.innerText = 'Скрыть все кроме открытых';
    }
    
}

console.log(popup)

command.onclick = () => {
    popup.style.display = 'flex';
    container.style.background = 'red';
}
popup_close.onclick = () => {
    popup.style.display = 'none';
}