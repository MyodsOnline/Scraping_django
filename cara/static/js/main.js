


// Подключение Select2
$(document).ready(connect_select2());

function connect_select2(){
    $('.sel2').select2({
        placeholder: "Выберите элемент",
        allowClear: true,
        closeOnSelect: false,
        templateResult: function(option){
            if (!option.element){
                return option.text;
            }
            if ($(option.element).is(":hidden")){
                return null;
            };
            return option.text;
        }
    });
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("pageContent").classList.remove("hidden");
});




// Проверка, что отправляемые данные не пустые
document.getElementById("select_form").addEventListener("submit", function(event){
    if (document.getElementById("id_select_field").value === ""){
        event.preventDefault();
        alert("Выберите элемент");
    }
})




// Запуск Загрузочного экрана при клике по кнопке расчет
var button = document.getElementById("calc");
button.addEventListener("click", function (event) {
    if (document.getElementById("id_select_field").value === ""){
        event.preventDefault();
        alert("Выберите элемент");
        document.getElementsByClassName("select2-search__field")[0].focus();
    }
    else {
        document.getElementById("pre_loader").style.display = "block";
    }
});


// Для поля с фильтрами
var filter_div = document.getElementsByClassName("filter")[0];

filter_div.addEventListener("mouseenter", function(){
    this.setAttribute("contenteditable", "true");
});

document.addEventListener("click", function(event){
    if (event.target !== filter_div){
        filter_div.setAttribute("contenteditable", "false");
    };
});

filter_div.addEventListener("focus", function(){
    this.classList.remove("placeholder");
    this.innerHTML = "";
})

filter_div.addEventListener("blur", function(){
    if (this.textContent === ""){
        this.classList.add("placeholder");
        this.innerHTML = "Введите фильтр";
    };
});



// Задание фильтров
function filter(text_filter){
    $('.sel2').find('option').each(function(){
        if($(this).text().includes(text_filter)){
            $(this).removeAttr("hidden");
        } else {
            $(this).attr("hidden", true);
        }
        connect_select2();
    });
};

var filter_but = document.getElementById("filter_but")

filter_but.addEventListener("click", function(){
    filter_but.classList.add("active");

    setTimeout(function(){
        if (filter_div.innerText !== "Введите фильтр"){
            filter(filter_div.innerText);
        };
        filter_but.classList.remove("active");
    }, 0);

});




// Добавление статуса кнопок к данным отправки
function update_set_data(){
    var set_data = {"repeat_calc": $("#repeat_calc").hasClass("active"),
                    "auto_calc": $("#auto_calc").hasClass("active"),
                    "comb_calc": $("#comb_calc").hasClass("active"),
                    "set_temp": $("#text").val()}

    $('#input_status').attr({value: JSON.stringify(set_data)});
}

// Обработчик события input для поля ввода с id "text"
$('#text').on('input', function() {
    update_set_data();
});

// Блокируем ввод всего, кроме целочисленных значений
const textField = document.getElementById('text');
textField.addEventListener('input', function() {
    textField.value = textField.value.replace(/\D/g, '');
});


// Задаём активацию кнопок настройки расчета
var set_buts = document.getElementsByClassName("set_but");
for (let i=0; i<set_buts.length; i++){

    // Добавляем обновление стиля кнопкам настройки
    set_buts[i].addEventListener('click', function(){
        if (this.classList.contains("active")){
            this.classList.remove('active');
            this.textContent = this.textContent.replace(" (ВКЛЮЧЕНО)","");
        } else {
            this.classList.add('active');
            this.textContent += " (ВКЛЮЧЕНО)";
        }
        // Обновляем данные в скрытом инпуте
        update_set_data();
    });
};

// Обновление статуса кнопок настройки при загрузке документа
update_set_data();

// Какая то дурацкая проблема с шириной input select

$(".select2-search__field").removeAttr("style");

// Запуск цикличного расчета
setTimeout(function(){
    if ($("#repeat_calc").hasClass("active")){
        button.click();
    };
}, 3000);