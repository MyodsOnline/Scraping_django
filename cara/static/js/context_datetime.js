// блок выбора даты и времени среза расчета
document.addEventListener('DOMContentLoaded', function() {
    const calendarIcon = document.querySelector('.datetime-wrapper');
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
    // Сохранение изменений и выполнение кода
    saveButton.addEventListener('click', function(event) {
        event.preventDefault();
        // Проверяем, было ли изменено значение
        if (modalDatetime.value !== originalValue) {
            datetimeInput.value = modalDatetime.value;
            modal.style.display = 'none';
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
    const target_datetime = document.getElementById('target-datetime').value;
    const closeButton = document.getElementById('close-info');
    const infoBlock = document.getElementById('info');

    let csrfTokenElement = document.querySelector('input[name="csrfmiddlewaretoken"]');
    let csrfToken = csrfTokenElement ? csrfTokenElement.value : '';

    // закрытие модального окна уведомлений
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
        return response.json();
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
