
// функция подставления значения в поле инпут
let input = document.getElementById('inputlist');
function onInputChange() {
    const selectedValue = input.value;
    console.log(selectedValue)
}
input.addEventListener('change', onInputChange);


// функция удаления значений из поля инпут при клике на кнопке
let clearButton = document.getElementById('clear');
function clearInput() {
    if (input.value) {
        input.value='';
    }
}
clearButton.addEventListener('click', clearInput);


// открыть/закрыть схему при клике на кнопку
document.getElementById('graph').addEventListener('click', function() {
    var graphDiv = document.querySelector('.graph');
    if (graphDiv.style.display === 'none' || graphDiv.style.display === '') {
        graphDiv.style.display = 'flex';
        this.textContent = 'Скрыть схему';
    } else {
        graphDiv.style.display = 'none';
        this.textContent = 'Открыть схему';
    }
});


// функция добавления имени сетевого элемента в поле инпут при клике на графике
document.querySelectorAll('path').forEach(item => {
    item.addEventListener('click', function() {
        var dataSvg = this.getAttribute('id');
        var option = document.querySelector('option[data-svg="' + dataSvg + '"]');
        if (option) {
            document.getElementById('inputlist').value = option.value;
        }
    });
});
