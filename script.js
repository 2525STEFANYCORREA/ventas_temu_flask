document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("pedidoForm");
    const container = document.getElementById("registrosContainer");
    const counter = document.getElementById("totalRegistros");
    const alertBox = document.getElementById("formAlert");
    const spinner = document.getElementById("spinner");

    if (!form || !container || !counter) return;

    // Datos iniciales: se mantienen en memoria y se renderizan con JavaScript.
    let registros = [
        {
            nombre: "Ejemplo de pedido",
            correo: "cliente@ejemplo.com",
            descripcion: "Bolso casual para uso diario.",
            categoria: "Moda",
            estado: "Solicitud de cotización"
        }
    ];

    const campos = {
        nombre: document.getElementById("nombre"),
        correo: document.getElementById("correo"),
        descripcion: document.getElementById("descripcion"),
        categoria: document.getElementById("categoria"),
        estado: document.getElementById("estado")
    };

    function validarCampo(campo) {
        const valor = campo.value.trim();
        let valido = true;

        if (campo.id === "nombre") {
            valido = valor.length >= 3;
        } else if (campo.id === "correo") {
            valido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor);
        } else if (campo.id === "descripcion") {
            valido = valor.length >= 10;
        } else if (campo.id === "categoria" || campo.id === "estado") {
            valido = valor !== "";
        }

        campo.classList.toggle("is-valid", valido);
        campo.classList.toggle("is-invalid", !valido);
        return valido;
    }

    Object.values(campos).forEach((campo) => {
        if (!campo) return;
        campo.addEventListener("input", () => validarCampo(campo));
        campo.addEventListener("blur", () => validarCampo(campo));
        campo.addEventListener("change", () => validarCampo(campo));
    });

    function mostrarAlerta(mensaje, tipo) {
        alertBox.className = `alert alert-${tipo}`;
        alertBox.textContent = mensaje;
        alertBox.classList.remove("d-none");

        setTimeout(() => {
            alertBox.classList.add("d-none");
        }, 3500);
    }

    function actualizarContador() {
        const cantidad = registros.length;
        counter.textContent = `${cantidad} ${cantidad === 1 ? "registro" : "registros"}`;
    }

    function renderizarRegistros() {
        container.innerHTML = "";

        // Condición solicitada: mensaje diferente cuando no hay datos.
        if (registros.length === 0) {
            container.innerHTML = `
                <div class="col-12">
                    <div class="alert alert-warning rounded-4">
                        Aún no existen pedidos registrados.
                    </div>
                </div>`;
            actualizarContador();
            return;
        }

        // Estructura repetitiva para renderizar los registros.
        registros.forEach((registro, index) => {
            const col = document.createElement("div");
            col.className = "col-md-6 col-lg-4";

            const card = document.createElement("div");
            card.className = "card dynamic-card h-100";

            const body = document.createElement("div");
            body.className = "card-body";

            const title = document.createElement("h5");
            title.className = "card-title";
            title.textContent = registro.nombre;

            const email = document.createElement("p");
            email.className = "small text-muted mb-2";
            email.textContent = registro.correo;

            const description = document.createElement("p");
            description.className = "card-text";
            description.textContent = registro.descripcion;

            const badge = document.createElement("span");
            badge.className = "badge rounded-pill bg-light text-dark me-2";
            badge.textContent = registro.categoria;

            const status = document.createElement("span");
            status.className = "badge rounded-pill text-bg-success";
            status.textContent = registro.estado;

            const deleteButton = document.createElement("button");
            deleteButton.className = "btn btn-outline-danger btn-sm rounded-pill mt-3";
            deleteButton.textContent = "Eliminar";
            deleteButton.addEventListener("click", () => {
                registros.splice(index, 1);
                renderizarRegistros();
                mostrarAlerta("El registro fue eliminado correctamente.", "warning");
            });

            body.appendChild(title);
            body.appendChild(email);
            body.appendChild(description);
            body.appendChild(badge);
            body.appendChild(status);
            body.appendChild(document.createElement("br"));
            body.appendChild(deleteButton);

            card.appendChild(body);
            col.appendChild(card);
            container.appendChild(col);
        });

        actualizarContador();
    }

    form.addEventListener("submit", (event) => {
        event.preventDefault();

        const validaciones = Object.values(campos).map(validarCampo);
        const formularioValido = validaciones.every(Boolean);

        if (!formularioValido) {
            mostrarAlerta("Revisa los campos marcados antes de registrar el pedido.", "danger");
            return;
        }

        spinner.classList.remove("d-none");

        // Simulación de carga.
        setTimeout(() => {
            const nuevoRegistro = {
                nombre: campos.nombre.value.trim(),
                correo: campos.correo.value.trim(),
                descripcion: campos.descripcion.value.trim(),
                categoria: campos.categoria.value,
                estado: campos.estado.value
            };

            registros.push(nuevoRegistro);
            renderizarRegistros();
            mostrarAlerta("¡Pedido registrado correctamente!", "success");

            form.reset();
            Object.values(campos).forEach((campo) => {
                campo.classList.remove("is-valid", "is-invalid");
            });

            spinner.classList.add("d-none");
        }, 650);
    });

    form.addEventListener("reset", () => {
        setTimeout(() => {
            Object.values(campos).forEach((campo) => {
                campo.classList.remove("is-valid", "is-invalid");
            });
        }, 0);
    });

    renderizarRegistros();
});


function confirmarEliminacion(nombre) {
    return window.confirm("¿Deseas eliminar el producto \"" + nombre + "\"? Esta acción se realizará en MySQL.");
}
