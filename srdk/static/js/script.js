const dropArea = document.getElementById("drop-area");

// Предотвращаем стандартное поведение
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

// Добавляем/убираем класс при перетаскивании
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, () => dropArea.classList.add('hover'), false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, () => dropArea.classList.remove('hover'), false);
});

// Обработка события "drop"
dropArea.addEventListener('drop', handleDrop, false);

function handleDrop(e) {
    const files = e.dataTransfer.files; // Получаем файлы
    handleFiles(files); // Обрабатываем файлы
}

function handleFiles(files) {
    const file = files[0]; // Получаем первый файл (или обработать несколько файлов)
    if (file && file.name.endsWith('.xlsx')) {
        const formData = new FormData();
        formData.append('file', file);

        // Отправляем файл на сервер
        fetch('/your/upload/url/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log('Успех:', data);
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    } else {
        alert('Пожалуйста, загрузите файл .xlsx');
    }
}