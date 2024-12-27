

document.addEventListener("DOMContentLoaded", function () {
    const elements = {
        typeRoulette: document.getElementById("type_roulette"),
        neighbors: document.getElementById("neighbors"),
        limiteGames: document.getElementById("limite_games"),
        probability: document.getElementById("probability"),
        initButton: document.querySelector('button[value="init"]'),
        clearButton: document.querySelector('button[value="clear"]') // Asegúrate de tener este selector correcto
    };

    const validations = {
        typeRoulette: { required: true, message: "Por favor, seleccione un tipo de ruleta" },
        neighbors: { min: 1, max: 4, message: "Debe estar entre 1 y 4" },
        limiteGames: { min: 1, max: 15, message: "Debe estar entre 1 y 15" },
        probability: { min: 10, max: 100, message: "Debe estar entre 10 y 100" }
    };

    // Listener para typeRoulette
    elements.typeRoulette?.addEventListener("change", function () {
        const isValid = !!this.value;
        const message = validations.typeRoulette.message;
        toggleErrorClass(this, !isValid);
        showError(this, isValid ? "" : message);
        validateForm();
    });

    // Listeners para otros campos
    ["neighbors", "limiteGames", "probability"].forEach(field => {
        elements[field]?.addEventListener("input", function () {
            validateField(this, field);
        });
    });

    // Listener para el botón de limpieza
    elements.clearButton?.addEventListener("click", function (e) {
        e.preventDefault(); // Evitar que el formulario se envíe

        // Resetear los campos a sus valores predeterminados o vacíos
        elements.typeRoulette.value = '';
        elements.neighbors.value = '';
        elements.limiteGames.value = '';
        elements.probability.value = 50; // Valor inicial definido en forms.py

        // Remover clases de error
        ["typeRoulette", "neighbors", "limiteGames", "probability"].forEach(field => {
            toggleErrorClass(elements[field], false);

            // Remover mensajes de error
            const errorDiv = elements[field].parentElement.querySelector(".text-red-500");
            if (errorDiv) {
                errorDiv.textContent = '';
            }
        });

        // Actualizar el estado del botón de envío
        toggleButtonState(elements.initButton, false);
    });

    function validateField(element, type) {
        const value = parseInt(element.value);
        const { min, max, message } = validations[type];
        const isValid = !isNaN(value) && value >= min && value <= max;

        toggleErrorClass(element, !isValid);
        showError(element, isValid ? "" : message);
        validateForm();
    }

    function validateForm() {
        // Validar cada campo y mostrar errores si es necesario
        ["typeRoulette", "neighbors", "limiteGames", "probability"].forEach(field => {
            const element = elements[field];
            if (field === "typeRoulette") {
                const isValid = !!element.value;
                const message = validations[field].message;
                toggleErrorClass(element, !isValid);
                showError(element, isValid ? "" : message);
            } else {
                const value = parseInt(element.value);
                const { min, max, message } = validations[field];
                const isValid = !isNaN(value) && value >= min && value <= max;
                toggleErrorClass(element, !isValid);
                showError(element, isValid ? "" : message);
            }
        });

        // Determinar si el formulario es válido
        const isValid = [
            !!elements.typeRoulette?.value,
            validateRange(elements.neighbors?.value, validations.neighbors.min, validations.neighbors.max),
            validateRange(elements.limiteGames?.value, validations.limiteGames.min, validations.limiteGames.max),
            validateRange(elements.probability?.value, validations.probability.min, validations.probability.max)
        ].every(Boolean);

        toggleButtonState(elements.initButton, isValid);
    }

    function validateRange(value, min, max) {
        const num = parseInt(value);
        return !isNaN(num) && num >= min && num <= max;
    }

    function toggleErrorClass(element, hasError) {
        element.classList.toggle("border-red-500", hasError);
    }

    function showError(element, message) {
        // Buscar contenedor de error existente
        let errorDiv = element.parentElement.querySelector(".text-red-500");

        // Si no existe, crear uno
        if (!errorDiv) {
            errorDiv = document.createElement("p");
            errorDiv.classList.add("text-red-500", "text-xs", "italic");
            element.parentElement.appendChild(errorDiv);
        }

        // Mostrar mensaje
        errorDiv.textContent = message;
    }

    function toggleButtonState(button, isEnabled) {
        if (button) {
            button.disabled = !isEnabled;
            button.classList.toggle("opacity-50", !isEnabled);
        }
    }

    // Inicializar validaciones al cargar la página
    validateForm();
});