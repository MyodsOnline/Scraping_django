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

function executeCopyFileLogic() {
    const target_datetime = document.getElementById('target-datetime').value;
    const closeButton = document.getElementById('close-info');
    const infoBlock = document.getElementById('info');
    const statusElement = document.getElementById("status-msg");

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
        infoBlock.style.display = 'flex';
        console.log(data.status)
        if (data.status === "error") {
          infoBlock.style.backgroundColor = "rgba(163, 44, 44, 1)";
          statusElement.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M10 14.9902V15.0002" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 5V12" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 19C14.9706 19 19 14.9706 19 10C19 5.02944 14.9706 1 10 1C5.02944 1 1 5.02944 1 10C1 14.9706 5.02944 19 10 19Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          `;
        } else if (data.status === "success") {
          infoBlock.style.backgroundColor = "rgba(58, 94, 55, 1)";
          statusElement.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15.0001 7L8.00004 14L5 11" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 19C14.9706 19 19 14.9706 19 10C19 5.02944 14.9706 1 10 1C5.02944 1 1 5.02944 1 10C1 14.9706 5.02944 19 10 19Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          `;
        }
    })
    .catch(error => {
        console.error('Ошибка:', error);
        document.getElementById('datetime-msg').textContent = 'Произошла ошибка при открытии файла.';
        infoBlock.style.display = 'block';
    });
}
