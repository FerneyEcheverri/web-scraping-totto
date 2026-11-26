
const contenedor = document.getElementById("productos");

async function cargarProductos() {
    try {
        const respuesta = await fetch("data/productos.json");

        if (!respuesta.ok) {
            throw new Error("No se pudo consultar el catálogo.");
        }

        const productos = await respuesta.json();

        if (!Array.isArray(productos) || productos.length === 0) {
            contenedor.innerHTML = `
                <p class="mensaje">
                    Todavía no hay productos disponibles en el catálogo.
                </p>`;
            return;
        }

        contenedor.innerHTML = productos.map(producto => `
            <article class="producto">
                <span class="categoria">
                    ${escaparHTML(producto.categoria || "Sin categoría")}
                </span>

                <h3>${escaparHTML(producto.nombre || "Producto sin nombre")}</h3>

                <p class="descripcion-producto">
                    ${escaparHTML(producto.descripcion || "Sin descripción")}
                </p>

                <div class="datos-producto">
                    <p><strong>Precio:</strong> ${escaparHTML(producto.precio || "No disponible")}</p>
                    <p><strong>Descuento:</strong> ${escaparHTML(producto.descuento || "No disponible")}</p>
                    <p><strong>Disponible:</strong> ${escaparHTML(producto.disponibilidad || "No disponible")}</p>
                </div>
            </article>
        `).join("");

    } catch (error) {
        contenedor.innerHTML = `
            <p class="mensaje">
                No fue posible cargar el catálogo.
                ${escaparHTML(error.message)}
            </p>`;
    }
}

function escaparHTML(valor) {
    return String(valor).replace(/[&<>"']/g, caracter => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
    })[caracter]);
}

cargarProductos();
