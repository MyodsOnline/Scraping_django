document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('datetime-container').addEventListener('submit', function(event) {
        event.preventDefault();

        let date = document.getElementById('date-input').value;
        let time = document.getElementById('time-input').value;
        let csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        fetch('/cara/bars_fetch/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
            body: new URLSearchParams({
                'date-input': date,
                'time-input': time
            })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('datetime-msg').textContent = data.message;
        })
        .catch(error => {
            document.getElementById('datetime-msg').textContent = 'Произошла ошибка при открытии файла.';
        });
    });
});
