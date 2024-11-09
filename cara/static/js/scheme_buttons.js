function toggleVisibility(elementToShowId, elementToHideId, buttonToActivateId, buttonToDeactivateId) {
    const elementToShow = document.getElementById(elementToShowId);
    const elementToHide = document.getElementById(elementToHideId);
    const buttonToActivate = document.getElementById(buttonToActivateId);
    const buttonToDeactivate = document.getElementById(buttonToDeactivateId);

    if (elementToShow.style.visibility === "visible") {
        elementToShow.style.visibility = "hidden";
        buttonToActivate.classList.remove("active_scheme_button");
    } else {
        elementToShow.style.visibility = "visible";
        buttonToActivate.classList.add("active_scheme_button");
    }

    elementToHide.style.visibility = "hidden";
    buttonToDeactivate.classList.remove("active_scheme_button");
}

document.getElementById("to_info").addEventListener("click", function() {
    toggleVisibility("selected_elements", "consumption_values", "to_info", "to_consumption");
});

document.getElementById("to_consumption").addEventListener("click", function() {
    toggleVisibility("consumption_values", "selected_elements", "to_consumption", "to_info");
});
