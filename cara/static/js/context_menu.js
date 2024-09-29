const contextMenu = document.getElementById('context-menu');
const enableBtn = document.getElementById('enable-btn');
const disableBtn = document.getElementById('disable-btn');

let currentPath = null;

// Обработчик правого клика на SVG элементе path
document.querySelectorAll('path').forEach(path => {
    path.addEventListener('contextmenu', (e) => {
        e.preventDefault();
        currentPath = path;

    // Показать контекстное меню
    const dashArray = currentPath.getAttribute('stroke-dasharray');
    enableBtn.disabled = (dashArray === '0'); // Если элемент включен, отключаем кнопку "Включить"
    disableBtn.disabled = (dashArray !== '0'); // Если элемент отключен, отключаем кнопку "Отключить"

    // Позиционируем меню рядом с курсором
    contextMenu.style.top = `${e.clientY}px`;
    contextMenu.style.left = `${e.clientX}px`;
    contextMenu.style.display = 'block';
    });
});

// Обработчик клика для кнопки "Включить"
enableBtn.addEventListener('click', () => {
    if (currentPath) {
        currentPath.setAttribute('stroke-dasharray', '0');
    }
    hideContextMenu();
});

// Обработчик клика для кнопки "Отключить"
disableBtn.addEventListener('click', () => {
    if (currentPath) {
        currentPath.setAttribute('stroke-dasharray', '5 3');
    }
    hideContextMenu();
});

// Скрытие контекстного меню
function hideContextMenu() {
    contextMenu.style.display = 'none';
};

// Скрывать меню при клике вне его
document.addEventListener('click', (e) => {
    if (!contextMenu.contains(e.target)) {
        hideContextMenu();
    }
});

// Скрыть контекстное меню при клике с правой кнопкой мыши вне элемента
document.addEventListener('contextmenu', (e) => {
    if (!e.target.closest('path')) {
        hideContextMenu();
    }
});