document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('data').addEventListener('change', function() {
        var selectedDate = this.value;
        fetch('/get_times/?date=' + selectedDate)
            .then(response => response.json())
            .then(data => {
                var timeInput = document.getElementById('time');
                timeInput.innerHTML = '';
                data.times.forEach(function(time) {
                    var option = document.createElement('option');
                    option.value = time;
                    option.textContent = time;
                    timeInput.appendChild(option);
                });
            });
    });
});
