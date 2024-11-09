// блок настройки отображения svg схемы с библиотекой Panzoom
    const schemeElement = document.getElementById('scheme');
    const panzoom = Panzoom(schemeElement, {
        maxScale: 3,          // Максимальный масштаб
        minScale: 0.2,        // Минимальный масштаб
        initialScale: 0.35,   // Начальный масштаб
        initialX: 0,          // Начальное смещение по X
        initialY: window.innerHeight * 0.45 // Начальное смещение по Y
    });

    // Устанавливаем точные начальные стили сразу после инициализации Panzoom
    schemeElement.style.transform = 'scale(0.35) translate(0, 45vh)';

    // Обработчик масштабирования колесиком мыши
    schemeElement.addEventListener('wheel', panzoom.zoomWithWheel);

    // Обработчик для кнопки "Сбросить масштаб"
    document.getElementById('to_home').addEventListener('click', () => {
        panzoom.reset({
            animate: true,
            duration: 200,
            easing: "easeInOut"
        });
        schemeElement.style.transformOrigin = '50% 50%';
        schemeElement.style.transition = 'transform 200ms ease-in-out';
        schemeElement.style.transform = 'scale(0.35) translate(0, 45vh)';
    });


// блок взаимодействия элементов схемы svg с полем input и окрашивание элементов
document.addEventListener('DOMContentLoaded', () => {
    // установка переменных для взаимодействия со схемой
    const inputElementStatus = document.getElementById('input_status'); // hidden элемент, value передаем на поиск в БД
    const selectedElements = document.getElementById('selected_elements'); // блок для отображения на фронте
    const selectedElementsList = document.getElementById('selected_elements_list'); // массив измененных элементов
    const toInfoElement = document.getElementById('to_info') // включение/отключение отображения по клику
    const selectedElementsDelete = document.getElementById('selected_elements_delete')
    const selectedIds = new Set();
    const originalStrokes = new Map();
    const parentVetvId = 'vetvs';
    const parentNodeId = 'nodes';

    // добавление/удаление элементов в поле input
    function updateElementInputStatus() {
        inputElementStatus.value = Array.from(selectedIds).join(', ');
        // Оборачиваем каждое значение в тег <span>
        const spanElements = Array.from(selectedIds).map(id => `<span class="element">${id}</span>`).join(' ');
        // Добавляем строки с <span> в элемент <p>
        selectedElementsList.innerHTML = spanElements;
        // Проверяем, есть ли элементы в inputElementStatus для присвоения класса
        if (inputElementStatus.value.length > 0) {
            toInfoElement.classList.add('colored');
        } else {
            toInfoElement.classList.remove('colored');
            selectedElements.style.display = "none";
        }
    }

    // выбор элемента по клику, изменение окраски элемента
    function toggleSelection(element) {
        const id = element.id;

        if (selectedIds.has(id)) {
            selectedIds.delete(id);
            element.querySelectorAll('path').forEach(path => {
                if (originalStrokes.has(path)) {
                    path.setAttribute('stroke', originalStrokes.get(path));
                }
            });
        } else {
            selectedIds.add(id);
            element.querySelectorAll('path').forEach(path => {
                if (!originalStrokes.has(path)) {
                    originalStrokes.set(path, path.getAttribute('stroke'));
                }
                path.setAttribute('stroke', 'rgb(255, 0, 0)');
            });
        }
        updateElementInputStatus();
    }

    // добавляем клики для каждого элемента g
    document.querySelectorAll('svg g[id]').forEach(element => {
        element.addEventListener('click', () => {
            const id = element.id;
            if (id !== parentNodeId && id !== parentVetvId) {
                toggleSelection(element);
            }
        });
    });

    // отобразить/скрыть список элементов
    toInfoElement.addEventListener('click', function() {
        if (toInfoElement.classList.contains('colored')) {
        // Проверяем текущее состояние элемента и переключаем видимость
            if (selectedElements.style.display === "none" || selectedElements.style.display === "") {
                selectedElements.style.display = "block";
            } else {
                selectedElements.style.display = "none";
            }
        }
    });

    selectedElementsDelete.addEventListener('click', function() {
        location.reload()
    });
});