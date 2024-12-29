export function renderMatchesTable(sheetName, jsonData, startRow, playerColIndex, startCol) {
  const players = extractPlayers(jsonData, startRow, playerColIndex);
  const matchesTable = buildMatchesArray(players, jsonData, startRow, startCol);
  renderTableWithDiagonal(matchesTable, `Encuentros Cruzados - ${sheetName}`);
}

function extractPlayers(data, startRow, playerColIndex) {
  // Encuentra la primera fila no vacía
  const firstValidRowIndex = data.findIndex((row, index) => index >= startRow && row[playerColIndex]);
  if (firstValidRowIndex === -1) {
    console.warn('No se encontraron jugadores en la columna especificada.');
    return [];
  }

  // Extrae los jugadores desde la primera fila válida
  return data
    .slice(firstValidRowIndex)
    .map(row => row[playerColIndex])
    .filter(player => player); // Filtra cualquier valor vacío
}

function buildMatchesArray(players, data, startRow, startCol) {
  const matchesArray = [];

  // Crear fila de encabezados
  const headersRow = [''].concat(players); // La primera celda está vacía
  matchesArray.push(headersRow);

  // Crear filas con jugadores y resultados
  players.forEach((player, rowIndex) => {
    const row = [player]; // Primera celda con el nombre del jugador
    for (let colIndex = 0; colIndex < players.length; colIndex++) {
      // Si no hay datos, ponemos un valor vacío
      const cellValue = data[startRow + rowIndex]?.[startCol + colIndex] || '';
      row.push(cellValue);
    }
    matchesArray.push(row);
  });

  return matchesArray;
}

function renderTableWithDiagonal(data, title) {
  const section = document.createElement('section');
  section.innerHTML = `<h2>${title}</h2>`;
  const table = document.createElement('table');
  table.classList.add('matches'); // Añadir clase 'matches' para estilos

  const tbody = document.createElement('tbody');

  data.forEach((row, rowIndex) => {
    const tr = document.createElement('tr');
    row.forEach((cell, colIndex) => {
      const td = document.createElement(rowIndex === 0 || colIndex === 0 ? 'th' : 'td');

      // Estilizar diagonal
      if (rowIndex > 0 && colIndex > 0 && rowIndex === colIndex) {
        td.classList.add('diagonal'); // Clase diagonal desde CSS
        td.textContent = '';
      } else {
        td.textContent = cell || '-';
      }

      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });

  table.appendChild(tbody);
  section.appendChild(table);
  document.querySelector('main').appendChild(section);
}
