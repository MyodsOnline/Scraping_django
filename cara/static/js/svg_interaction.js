// блок взаимодействия элементов схемы с полем input и окрашивание элементов
document.addEventListener('DOMContentLoaded', () => {
    // установка переменных для взаимодействия со схемой
    const inputVetvStatus = document.getElementById('input_status'); //inputStatus
    const selectedIds = new Set();
    const originalStrokes = new Map();
    const parentVetvId = 'vetvs';
    const parentNodeId = 'nodes';

    // добавление/удаление элементов в поле input
    function updateVetvInputStatus() {
        inputVetvStatus.value = Array.from(selectedIds).join(', ');
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
        updateVetvInputStatus();
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