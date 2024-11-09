document.addEventListener("DOMContentLoaded", function () {
    const apGrid = document.querySelector(".ap_grid");
    const svgContent = document.getElementById("svg_content");

    // Изменение grid-template-columns при клике на svg_content
    svgContent.addEventListener("click", () => {
        apGrid.style.gridTemplateColumns = "3fr 2fr";
    });

    // Разворачивание/сворачивание ap_element_list и поворот svg
    const apElements = document.querySelectorAll(".ap_element");

    apElements.forEach(apElement => {
        const svgIcon = apElement.querySelector(".element_name svg"); // Пока просто клик на svg
        const apElementList = apElement.querySelector(".ap_element_list");

        svgIcon.addEventListener("click", () => {
            apElementList.classList.toggle("hidden");
            svgIcon.style.transform = svgIcon.style.transform === "rotate(180deg)" ? "rotate(0deg)" : "rotate(180deg)";
        });
    });

    // Отметка всех checkbox при клике на li.all_aps
    const allApsCheckboxes = document.querySelectorAll(".all_aps input[type='checkbox']");

    allApsCheckboxes.forEach(allApsCheckbox => {
        allApsCheckbox.addEventListener("change", function () {
            const apElementList = this.closest(".ap_element_list");
            const checkboxes = apElementList.querySelectorAll(".single_ap input[type='checkbox']");

            checkboxes.forEach(checkbox => {
                checkbox.checked = allApsCheckbox.checked;
            });
        });
    });

    // Снятие выделения с li.all_aps при изменении single_ap
    const singleApCheckboxes = document.querySelectorAll(".single_ap input[type='checkbox']");

    singleApCheckboxes.forEach(singleApCheckbox => {
        singleApCheckbox.addEventListener("change", function () {
            const apElementList = this.closest(".ap_element_list");
            const allApsCheckbox = apElementList.querySelector(".all_aps input[type='checkbox']");

            if (!this.checked) {
                allApsCheckbox.checked = false;
            } else {
                const allChecked = Array.from(apElementList.querySelectorAll(".single_ap input[type='checkbox']")).every(checkbox => checkbox.checked);
                allApsCheckbox.checked = allChecked;
            }
        });
    });
});
