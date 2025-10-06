async function cargarDatos() {
  try {
    const response = await fetch("resultados.json");
    const data = await response.json();

    const jugadores = data.jugadores.map(j => {
      const total = j.rondas.reduce((a, b) => a + b, 0);
      return { nombre: j.nombre, total };
    });

    // Ordenar por puntos (de mayor a menor)
    jugadores.sort((a, b) => b.total - a.total);

    const tbody = document.querySelector("#tablaClasificacion tbody");
    tbody.innerHTML = "";

    jugadores.forEach((j, index) => {
      const fila = document.createElement("tr");
      fila.innerHTML = `
        <td>${index + 1}</td>
        <td>${j.nombre}</td>
        <td>${j.total}</td>
      `;
      tbody.appendChild(fila);
    });
  } catch (error) {
    console.error("Error cargando los datos:", error);
  }
}

cargarDatos();

