let lines_list = [
	{name: "ВЛ 750 кВ Ленинградская АЭС – Ленинградская", start: "НСС Ленинградской АЭС", end: "ДИ ПС 750 кВ Ленинградская", idOIK: "NoYet"},
	{name: "ВЛ 750 кВ Белозерская – Ленинградская", start: "ДД Диспетчера ЦДУ", end: "ДИ ПС 750 кВ Ленинградская", idOIK: "NoYet"},
	{name: "ВЛ 750 кВ Калининская АЭС – Ленинградская", start: "ДД  Диспетчера ЦДУ", end: "ДИ ПС 750 кВ Ленинградская", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Балти – Кингисеппская (Л-374)", start: "ДД Elering AS", end: "ДИ ПС 330 кВ Кингисеппская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Бологое – Окуловская", start: "ДД Тверского РДУ", end: "ДИ ПС 330 кВ Окуловская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Великорецкая – Резекне (Л 309)", start: "ДД  Новгородского РДУ", end: "ДД Augstsprieguma tikls", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Виру – Кингисеппская (ВЛ 373)", start: "ДД Elering AS", end: "ДИ ПС 330 кВ Кингисеппская", idOIK: "NoYet"},
	{name: "КЛ 330 кВ Волхов-Северная – Завод Ильич №1", start: "ДИ ПС 330 кВ Волхов-Северная", end: "ДИ ПС 330 кВ Завод Ильич", idOIK: "NoYet"},
	{name: "КЛ 330 кВ Волхов-Северная – Завод Ильич №2", start: "ДИ ПС 330 кВ Волхов-Северная", end: "ДИ ПС 330 кВ Завод Ильич", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Восточная – Волхов-Северная №1", start: "ДИ ПС 330 кВ Восточная", end: "ДИ ПС 330 кВ Волхов-Северная", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Восточная – Волхов-Северная №2", start: "ДИ ПС 330 кВ Восточная", end: "ДИ ПС 330 кВ Волхов-Северная", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Восточная – Выборгская I цепь", start: "ДИ ПС 330 кВ Восточная", end: "ДИ ПС 400 кВ Выборгская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Восточная – Выборгская II цепь", start: "ДИ ПС 330 кВ Восточная", end: "ДИ ПС 400 кВ Выборгская", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Восточная – Колпино I цепь", start: "ДИ ПС 330 кВ Восточная", end: "ДИ ПС 330 кВ Колпино", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Восточная – Колпино II цепь", start: "ДИ ПС 330 кВ Восточная", end: "ДИ ПС 330 кВ Колпино", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Восточная – Октябрьская I цепь", start: "ДИ ПС 330 кВ Восточная", end: "ДД Ленинградского РДУ", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Восточная – Октябрьская II цепь", start: "ДИ ПС 330 кВ Восточная", end: "ДД Ленинградского РДУ", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Восточная – Парнас", start: "ДИ ПС 330 кВ Восточная", end: "ДИ ПС 330 кВ Парнас", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Восточная – Ржевская I цепь", start: "ДИ ПС 330 кВ Восточная", end: "ДИ ПС 330 кВ Ржевская", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Восточная – Ржевская II цепь", start: "ДИ ПС 330 кВ Восточная", end: "ДИ ПС 330 кВ Ржевская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Восточная – Южная", start: "ДИ ПС 330 кВ Восточная", end: "ДИ ПС 330 кВ Южная", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Выборгская – Каменногорская", start: "ДИ ПС 400 кВ Выборгская", end: "ДИ ПС 330 кВ Каменногорская", idOIK: "NoYet"},
	{name: "ВЛ 400 кВ Выборгская – Кюми (ЛЛн-1)", start: "ДИ ПС 400 кВ Выборгская", end: "ДД Fingrid", idOIK: "NoYet"},
	{name: "ВЛ 400 кВ Выборгская – Юлликкяля (ЛЛн-2)", start: "ДИ ПС 400 кВ Выборгская", end: "ДД Fingrid", idOIK: "NoYet"},
	{name: "ВЛ 400 кВ Выборгская – Юлликкяля (ЛЛн-3)", start: "ДИ ПС 400 кВ Выборгская", end: "ДД Fingrid"},
	{name: "ВЛ 330 кВ Гатчинская – Кингисеппская", start: "ДИ ПС 330 кВ Гатчинская", end: "ДИ ПС 330 кВ Кингисеппская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Гатчинская – Лужская", start: "ДИ ПС 330 кВ Гатчинская", end: "ДИ ПС 330 кВ Лужская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Гатчинская – Южная", start: "ДИ ПС 330 кВ Гатчинская", end: "ДИ ПС 330 кВ Южная", idOIK: "NoYet"},
	{name: "КЛ 330 кВ Завод Ильич – Василеостровская", start: "ДИ ПС 330 кВ Завод Ильич", end: "ДИ ПС 330 кВ Василеостровская", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Западная – Пулковская", start: "ДИ ПС 330 кВ Западная", end: "ДИ ПС 330 кВ Пулковская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Зеленогорск – Каменногорская", start: "ДИ ПС 330 кВ Зеленогорск", end: "ДИ ПС 330 кВ Каменногорская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Кингисеппская – Псков", start: "ДИ ПС 330 кВ Кингисеппская", end: "ДД Новгородского РДУ", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Киришская ГРЭС – Восточная I цепь", start: "ДИ Киришской ГРЭС", end: "ДИ ПС 330 кВ Восточная", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Киришская ГРЭС – Восточная II цепь", start: "НСС Киришской ГРЭС", end: "ДИ ПС 330 кВ Восточная", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Киришская ГРЭС – Сясь", start: "НСС Киришской ГРЭС", end: "ДИ ПС 330 кВ Сясь", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Киришская ГРЭС – Тихвин-Литейный", start: "НСС Киришской ГРЭС", end: "ДИ ПС 330 кВ Тихвин-Литейный", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Киришская ГРЭС – Чудово", start: "НСС Киришской ГРЭС", end: "ДД Новгородского РДУ", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Копорская – Гатчинская", start: "ДИ ПС 750 кВ Копорская", end: "ДИ ПС 330 кВ Гатчинская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Копорская – Кингисеппская", start: "ДИ ПС 750 кВ Копорская", end: "ДИ ПС 330 кВ Кингисеппская", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Копорская – Ленинградская АЭС", start: "ДИ ПС 750 кВ Копорская", end: "НСС Ленинградской АЭС", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Копорская – Пулковская", start: "ДИ ПС 750 кВ Копорская", end: "ДИ ПС 330 кВ Пулковская", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Ленинградская – Кингисеппская", start: "ДИ ПС 750 кВ Ленинградская", end: "ДИ ПС 330 кВ Кингисеппская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Ленинградская – Колпино I цепь", start: "ДИ ПС 750 кВ Ленинградская", end: "ДИ ПС 330 кВ Колпино", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Ленинградская – Колпино II цепь", start: "ДИ ПС 750 кВ Ленинградская", end: "ДИ ПС 330 кВ Колпино", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Ленинградская – Чудово", start: "ДИ ПС 750 кВ Ленинградская", end: "ДД Новгородского РДУ", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Ленинградская – Южная I цепь", start: "ДИ ПС 750 кВ Ленинградская", end: "ДИ ПС 330 кВ Южная", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Ленинградская – Южная II цепь", start: "ДИ ПС 750 кВ Ленинградская", end: "ДИ ПС 330 кВ Южная", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Ленинградская – Центральная", start: "ДИ ПС 750 кВ Ленинградская", end: "ДИ ПС 330 кВ Центральная", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Ленинградская АЭС – Восточная", start: "ДИ Ленинградской АЭС", end: "ДИ ПС 330 кВ Восточная", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Ленинградская АЭС – Гатчинская", start: "ДИ Ленинградской АЭС", end: "ДИ ПС 330 кВ Гатчинская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Ленинградская АЭС – Западная", start: "ДИ Ленинградской АЭС", end: "ДИ ПС 330 кВ Западная", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Новосокольники – Талашкино", start: "ДД Новгородского РДУ", end: "ДД Тверского РДУ", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Полоцк – Новосокольники (Л 345)", start: "ДД ГПО «Белэнерго»", end: "ДД Новгородского РДУ", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Псков – Лужская", start: "ДД  Новгородского РДУ", end: "ДИ ПС 330 кВ Лужская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Псков – Тарту (Л-358)", start: "ДД  Новгородского РДУ", end: "ДД Elering AS", idOIK: "NoYet"},
	{name: "КЛ 330 кВ Северная – Василеостровская", start: "ДИ ПС 330 кВ Северная", end: "ДИ ПС 330 кВ Василеостровская", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Северная – Парнас", start: "ДИ ПС 330 кВ Северная", end: "ДИ ПС 330 кВ Парнас", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Северо-Западная ТЭЦ – Восточная", start: "НСС Северо-Западной ТЭЦ", end: "ДИ ПС 330 кВ Восточная", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Северо-Западная ТЭЦ – Выборгская", start: "НСС Северо-Западной ТЭЦ", end: "ДИ ПС 400 кВ Выборгская", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Северо-Западная ТЭЦ – Зеленогорск", start: "НСС Северо-Западной ТЭЦ", end: "ДИ ПС 330 кВ Зеленогорск", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Северо-Западная ТЭЦ – Северная", start: "НСС Северо-Западной ТЭЦ", end: "ДИ ПС 330 кВ Северная", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Сясь – Петрозаводск", start: "ДИ ПС 330 кВ Сясь", end: "ДД Карельского РДУ", idOIK: "NoYet"},
	{name: "ВЛ 330 кВ Чудово – Окуловская", start: "ДД Новгородского РДУ", end: "ДИ ПС 330 кВ Окуловская", idOIK: "NoYet"},
	{name: "КВЛ 330 кВ Южная – Пулковская I цепь", start: "ДИ ПС 330 кВ Южная", end: "ДИ ПС 330 кВ Пулковская", idOIK: "NoYet"},
	{name: "КЛ 330 кВ Южная – Пулковская №2", start: "ДИ ПС 330 кВ Южная", end: "ДИ ПС 330 кВ Пулковская", idOIK: "NoYet"},
	{name: "КЛ 330 кВ Южная – Центральная", start: "ДИ ПС 330 кВ Южная", end: "ДИ ПС 330 кВ Центральная", idOIK: "NoYet"},
	{name: "КЛ 330 кВ Южная ТЭЦ – Южная №1 (КБ-41)", start: "ДД Ленинградского РДУ", end: "ДИ ПС 330 кВ Южная", idOIK: "NoYet"},
	{name: "КЛ 330 кВ Южная ТЭЦ – Южная №2 (КБ-4)", start: "ДД Ленинградского РДУ", end: "ДИ ПС 330 кВ Южная", idOIK: "NoYet"},
]

const loop = document.getElementById('loop')
const pa = document.getElementById('pa')
const comb = document.getElementById('comb')
const textField = document.getElementById('text');
const hiddenInput = document.getElementById('input_status');

textField.addEventListener('input', function() {
    hiddenInput.value = textField.value;
});

textField.addEventListener('input', function() {
    textField.value = textField.value.replace(/\D/g, '');
});

// блок кода для создания списка в html datalist
let optionsList = document.getElementById('options');
let input = document.getElementById('inputlist');
let clearButton = document.getElementById('clear');

for (const line of lines_list) {
  const option = document.createElement('option');
  option.value = line.name;
  optionsList.appendChild(option);
}

function onInputChange() {
    const selectedValue = input.value;
    console.log(selectedValue)
    fillTable();
}


// блок кода для создания таблицы с аварийными процессами
const elements = [
    "Отключение ВЛ 330 кВ Сясь - Петрозаводск с отказом выключателя В 310 на ПС 330 кВ Петрозаводск и работой УРОВ на отключение ВЛ 330 кВ Кондопога - Петрозаводск", 
    "Отключение сб. ш. АТ-3 ПС 330 кВ Сясь", 
    "Аварийный небаланс Кольской ЭС",
    "Отключение ВЛ 330 кВ Сясь - Петрозаводск с отказом выключателя В-312 на ПС 330 кВ Петрозаводск и работой УРОВ на отключение 2 СШ 330 кВ ПС 330 кВ Петрозаводск"];

const tbody = document.querySelector('tbody');
function fillTable() {
    elements.forEach(element => {
    const tr = document.createElement('tr');
    const th = document.createElement('th');
    const td = document.createElement('td');
    const input = document.createElement('input');

    input.setAttribute('type', 'checkbox');
    input.setAttribute('name', element);

    th.appendChild(input);
    td.textContent = element;

    tr.appendChild(th);
    tr.appendChild(td);

    tbody.appendChild(tr);
    });
}
input.addEventListener('change', onInputChange);


// очистка input и tbody
function clearInput() {
    if (input.value) {
        input.value='';
        tbody.innerHTML = ''
    }
}
clearButton.addEventListener('click', clearInput);


// выбор и отмена выбора всех checkbox
const masterCheck = document.getElementById('master_check')
function checkAll() {
    let tbodyCheckbox = document.querySelectorAll('tbody input[type="checkbox"]');    
    if (this.checked) {
        tbodyCheckbox.forEach(function(checkbox) {
            checkbox.checked = true;
        });
    } else {
        tbodyCheckbox.forEach(function(checkbox) {
            checkbox.checked = false;
        });
    }
};
masterCheck.addEventListener('change', checkAll);
