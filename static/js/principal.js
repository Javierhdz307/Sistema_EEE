document.addEventListener("DOMContentLoaded", () => {
    const botones = document.querySelectorAll(".switch-btn");
    const tablas = document.querySelectorAll(".tabla-contenedor");

    botones.forEach(btn => {
        btn.addEventListener("click", () => {

            // quitar selección previa
            botones.forEach(b => b.classList.remove("activo"));

            // seleccionar botón actual
            btn.classList.add("activo");

            // ocultar todas las tablas
            tablas.forEach(t => t.classList.add("oculto"));

            // mostrar la tabla correspondiente
            const target = btn.getAttribute("data-target");
            document.getElementById(target).classList.remove("oculto");
        });
    });
});

document.getElementById("buscar-alumno").addEventListener("input", function() {
    let q = this.value;

    if (q.length < 2) return;

    fetch(`/citas/buscar-alumno/?q=${q}`)
        .then(res => res.json())
        .then(data => {
            if (data.error) return;

            // Llenar campos
            document.getElementById("alumno-id").value = data.IddAlumno;
            document.getElementById("alumno-nombre").value = data.NombreAlumno;
            document.getElementById("alumno-apellido").value = data.ApellidoAlumno;
            document.getElementById("alumno-edad").value = data.EdadAlumno;
            document.getElementById("alumno-encargado").value = data.EncargadoAlumno;

            // Seleccionar automáticamente en el select del form
            document.getElementById("id_alumno").value = data.IddAlumno;
        });
});
document.getElementById("buscar-personal").addEventListener("input", function() {
    let q = this.value;

    if (q.length < 2) return;

    fetch(`/citas/buscar-personal/?q=${q}`)
        .then(res => res.json())
        .then(data => {
            if (data.error) return;

            // Llenar campos
            document.getElementById("personal-nombre").value = data.nombre;
            document.getElementById("personal-apellido").value = data.apellido;

            // Seleccionar automáticamente en el select del form
            document.getElementById("id_personal").value = data.id;
        });
});


document.getElementById("buscarAlumno").addEventListener("input", function() {
    let q = this.value;

    if (q.length < 2) {
        document.getElementById("resultadosBusqueda").innerHTML = "";
        return;
    }

    fetch(`/paei/buscar-alumno/?q=${q}`)
        .then(res => res.json())
        .then(data => {
            let html = "";
            data.results.forEach(a => {
                html += `<div class='item' data-id='${a.id}' data-nombre='${a.nombre}'>
                            ${a.nombre} (${a.nie})
                         </div>`;
            });

            document.getElementById("resultadosBusqueda").innerHTML = html;

            document.querySelectorAll(".item").forEach(item => {
                item.addEventListener("click", function() {
                    document.getElementById("buscarAlumno").value = this.dataset.nombre;
                    document.getElementById("alumno_id").value = this.dataset.id;
                    document.getElementById("resultadosBusqueda").innerHTML = "";
                });
            });
        });
});
function filtrarPorAlumno(id) {
    const url = new URL(window.location.href);
    url.searchParams.set("alumno", id);
    window.location.href = url.toString();
}
