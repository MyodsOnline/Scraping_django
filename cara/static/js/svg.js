// блок настройки отображения svg схемы с библиотекой Panzoom
const element = document.getElementById('scheme')
const panzoom = Panzoom(element, {
    maxScale: 7,
    minScale: 1,
    cursor: 'auto'
});
const parent = element.parentElement;

parent.addEventListener('wheel', panzoom.zoomWithWheel);

// Открыть/закрыть схему при клике на кнопку
document.getElementById('graph_button').addEventListener('click', function () {
    const graphDiv = document.getElementById('svg_content');
    if (graphDiv.style.display === 'none' || graphDiv.style.display === '') {
        graphDiv.style.display = 'flex';
        this.textContent = 'Скрыть схему';
    } else {
        graphDiv.style.display = 'none';
        this.textContent = 'Открыть схему';
    }
});


// блок взаимодействия элементов схемы с полем input и окрашивание элементов
document.addEventListener('DOMContentLoaded', () => {
    // установка переменных для взаимодействия со схемой
    const inputStatus = document.getElementById('input_status');
    const selectedIds = new Set();
    const originalStrokes = new Map();
    const parentVetvId = 'vetvs';
    const parentNodeId = 'nodes';

    // добавление/удаление элементов в поле input
    function updateInputStatus() {
        inputStatus.value = Array.from(selectedIds).join(', ');
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
        updateInputStatus();
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
});