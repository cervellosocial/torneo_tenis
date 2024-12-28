// Ruta del archivo Excel en la carpeta data
const excelPath = './data/resultados.xlsx';

fetch(excelPath)
  .then(response => response.arrayBuffer())
  .then(data => {
    const workbook = XLSX.read(data, { type: 'array' });

    // Hojas específicas a procesar
    const sheetsToRead = [
      'Sumario 1A', 
      'Sumario 2A', 
      'Sumario 3A', 
      'Sumario Infantil', 
      '2a', 
      '3a', 
      'infantil'
    ];

    sheetsToRead.forEach(sheetName => {
      const sheet = workbook.Sheets[sheetName];
      if (sheet) {
        // Leer todas las filas como matriz
        const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });

        // Detectar la fila con los encabezados correctos
        const headerIndex = jsonData.findIndex(row =>
          row.some(cell => String(cell).trim().toLowerCase() === 'posición') &&
          row.some(cell => String(cell).trim().toLowerCase() === 'jugador')
        );

        if (headerIndex !== -1) {
          // Obtener un rango limitado después de los encabezados
          const rowsToRead = 10; // Cambia este valor según el tamaño de la tabla que deseas
          const tableData = jsonData.slice(headerIndex, headerIndex + rowsToRead);

          // Convertir los datos en formato JSON con encabezados
          const dataWithHeaders = XLSX.utils.sheet_to_json(XLSX.utils.aoa_to_sheet(tableData));
          renderTable(dataWithHeaders, sheetName);
        } else {
          console.warn(`Encabezados no encontrados en la hoja ${sheetName}`);
        }
      } else {
        console.warn(`La hoja ${sheetName} no existe en el archivo.`);
      }
    });
  })
  .catch(error => console.error('Error al cargar el archivo Excel:', error));

// Función para renderizar la tabla
function renderTable(data, sheetName) {
  const tableSection = document.createElement('section');
  tableSection.innerHTML = `<h2>Clasificación - ${sheetName}</h2>`;
  const table = document.createElement('table');
  table.innerHTML = `
    <thead>
      <tr>
        <th>Posición</th>
        <th>Jugador</th>
        <th>Puntos</th>
        <th>P.J</th>
        <th>P.G</th>
        <th>P.P</th>
        <th>S.G</th>
        <th>S.P</th>
        <th>J.G</th>
        <th>J.P</th>
        <th>D.J</th>
      </tr>
    </thead>
    <tbody></tbody>
  `;

  const tableBody = table.querySelector('tbody');

  data.forEach(row => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${row['Posición'] || '-'}</td>
      <td>${row['Jugador'] || '-'}</td>
      <td>${row['Puntos'] || '-'}</td>
      <td>${row['P.J'] || '-'}</td>
      <td>${row['P.G'] || '-'}</td>
      <td>${row['P.P'] || '-'}</td>
      <td>${row['S.G'] || '-'}</td>
      <td>${row['S.P'] || '-'}</td>
      <td>${row['J.G'] || '-'}</td>
      <td>${row['J.P'] || '-'}</td>
      <td>${row['D.J'] || '-'}</td>
    `;
    tableBody.appendChild(tr);
  });

  tableSection.appendChild(table);
  document.querySelector('main').appendChild(tableSection);
}
