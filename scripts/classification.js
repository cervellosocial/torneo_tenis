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

  // Contenedor para la tabla
  const container = document.createElement('div');
  container.classList.add('table-container');

  const table = document.createElement('table');
  table.classList.add('classification'); // Agregar la clase principal

  const tbody = document.createElement('tbody');

  data.forEach((row, rowIndex) => {
    const tr = document.createElement('tr');
    row.forEach((cell, colIndex) => {
      const isHeader = rowIndex === 0;
      const td = document.createElement(isHeader ? 'th' : 'td');

      if (isHeader) {
        td.classList.add('header-cell');
      } else if (colIndex === 0) {
        td.classList.add('position-cell');
      }

      td.textContent = cell || '-';
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });

  table.appendChild(tbody);
  container.appendChild(table);
  section.appendChild(container);

  // Añadir leyenda después de cada tabla
  const legend = renderLegend();
  section.appendChild(legend);

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
  return legendSection;
}

