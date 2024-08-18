document.addEventListener('DOMContentLoaded', function() {
    // Находим кнопку Confirm и добавляем ей обработчик события click
    const confirmButton = document.querySelector('#datetime-container button[type="submit"]');

    confirmButton.addEventListener('click', function(event) {
        event.preventDefault();

        let target_datetime = document.getElementById('target-datetime').value;
        let csrfTokenElement = document.querySelector('input[name="csrfmiddlewaretoken"]');
        let csrfToken = csrfTokenElement ? csrfTokenElement.value : '';

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
        })
        .catch(error => {
            console.error('Ошибка:', error);
            document.getElementById('datetime-msg').textContent = 'Произошла ошибка при открытии файла.';
        });
    });
});
