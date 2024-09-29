// блок настройки отображения svg схемы с библиотекой Panzoom
const element = document.getElementById('scheme')
const panzoom = Panzoom(element, {
    maxScale: 7,
    minScale: 1,
    cursor: 'auto'
});
const parent = element.parentElement;

parent.addEventListener('wheel', panzoom.zoomWithWheel);


// блок выбора даты и времени среза расчета
document.addEventListener('DOMContentLoaded', function() {
    const calendarIcon = document.querySelector('.calendar-icon');
    const modal = document.getElementById('datetime-modal');
    const saveButton = document.getElementById('save-datetime');
    const cancelButton = document.getElementById('cancel-datetime');
    const datetimeInput = document.getElementById('target-datetime');
    const modalDatetime = document.getElementById('modal-datetime');

    let originalValue = modalDatetime.value;

    // Открытие модального окна
    calendarIcon.addEventListener('click', function() {
        modal.style.display = 'flex';
        originalValue = modalDatetime.value = datetimeInput.value;
    });

    // Сохранение изменений и выполнение кода copy_file.js
    saveButton.addEventListener('click', function(event) {
        event.preventDefault();

        // Проверяем, было ли изменено значение
        if (modalDatetime.value !== originalValue) {
            datetimeInput.value = modalDatetime.value;
            modal.style.display = 'none';

            // Выполнение кода из copy_file.js
            executeCopyFileLogic();
        } else {
            modal.style.display = 'none';
        }
    });

    // Закрытие модального окна без сохранения
    cancelButton.addEventListener('click', function(event) {
        event.preventDefault();
        modal.style.display = 'none';
    });
});

// Функция для выполнения логики из copy_file.js
function executeCopyFileLogic() {
    let target_datetime = document.getElementById('target-datetime').value;
    let csrfTokenElement = document.querySelector('input[name="csrfmiddlewaretoken"]');
    let csrfToken = csrfTokenElement ? csrfTokenElement.value : '';

    const closeButton = document.getElementById('close-info');
    const infoBlock = document.getElementById('info');

    closeButton.addEventListener('click', function() {
        infoBlock.style.display = 'none';
    });

    if (!csrfToken) {
        document.getElementById('datetime-msg').textContent = 'CSRF token не найден.';
        return;
    }

    fetch('/cara/bars_fetch/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken
        },
        body: new URLSearchParams({
            'target_datetime': target_datetime
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Ошибка сети');
        }
        return response.json(); // Проверяем, что ответ в формате JSON
    })
    .then(data => {
        document.getElementById('datetime-msg').textContent = data.message;
        infoBlock.style.display = 'block';
    })
    .catch(error => {
        console.error('Ошибка:', error);
        document.getElementById('datetime-msg').textContent = 'Произошла ошибка при открытии файла.';
        infoBlock.style.display = 'block';
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const closeButton = document.getElementById('close-info');
    const infoBlock = document.getElementById('info');

    closeButton.addEventListener('click', function() {
        infoBlock.style.display = 'none';
    });
});