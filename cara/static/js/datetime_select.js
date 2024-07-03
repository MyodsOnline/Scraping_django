document.getElementById('date-input').addEventListener('input', function() {
        const timeInput = document.getElementById('time-input');
        if (this.value) {
            timeInput.disabled = false;
        } else {
            timeInput.disabled = true;
        }
    });