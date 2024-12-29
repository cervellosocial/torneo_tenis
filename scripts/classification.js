export function renderClassificationTable(sheetName, jsonData, range) {
  const classificationTable = extractTable(jsonData, range);
  renderTable(classificationTable, `Clasificación - ${sheetName}`);
  renderLegend(); // Agregar la leyenda debajo de la tabla de clasificación
}

function extractTable(data, range) {
  return data
    .slice(range.startRow, range.endRow)
    .map(row => row.slice(range.startCol, range.endCol));
}

function renderTable(data, title) {
  const section = document.createElement('section');
  section.innerHTML = `<h2>${title}</h2>`;
  const table = document.createElement('table');
  table.classList.add('classification'); // Agregar la clase principal

  const tbody = document.createElement('tbody');

  data.forEach((row, rowIndex) => {
    const tr = document.createElement('tr');
    row.forEach((cell, colIndex) => {
      // Determinar si es encabezado o celda de datos
      const isHeader = rowIndex === 0;
      const td = document.createElement(isHeader ? 'th' : 'td');

      // Asignar clases específicas
      if (isHeader) {
        td.classList.add('header-cell'); // Clase para encabezados
      } else if (colIndex === 0) {
        td.classList.add('position-cell'); // Clase para la columna de posiciones
      }

      // Asignar contenido
      td.textContent = cell || '-';
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });

  table.appendChild(tbody);
  section.appendChild(table);
  document.querySelector('main').appendChild(section);
}


function renderLegend() {
  const legendSection = document.createElement('section');
  legendSection.classList.add('legend');
  legendSection.innerHTML = `
    <h3>Leyenda</h3>
    <ul>
      <li><b>P.J</b>: Partidos jugados</li>
      <li><b>P.G</b>: Partidos ganados</li>
      <li><b>P.P</b>: Partidos perdidos</li>
      <li><b>S.G</b>: Sets ganados</li>
      <li><b>S.P</b>: Sets perdidos</li>
      <li><b>J.G</b>: Juegos ganados</li>
      <li><b>J.P</b>: Juegos perdidos</li>
      <li><b>D.J</b>: Diferencia de juegos</li>
    </ul>
  `;
  document.querySelector('main').appendChild(legendSection);
}
