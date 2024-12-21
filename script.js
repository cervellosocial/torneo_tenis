async function loadExcel() {
    try {
        const response = await fetch('data/resultados.xlsx'); // Asegúrate de que la ruta es correcta
        const data = await response.arrayBuffer();
        const workbook = XLSX.read(data, { type: 'array' });

        // Leer todas las hojas del Excel
        const sheets = workbook.SheetNames;
        const tables = [];

        sheets.forEach(sheetName => {
            const sheet = workbook.Sheets[sheetName];
            const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 }); // Leer como matriz

            // Detectar si la hoja contiene la estructura de clasificación
            const headers = jsonData[0] || [];
            const expectedHeaders = ["Posición", "Jugador", "Puntos", "P.J", "P.G", "P.P", "S.G", "S.P", "J.G", "J.P", "D.J"];
            const isClassificationTable = expectedHeaders.every(header => headers.includes(header));

            if (isClassificationTable) {
                tables.push({ name: sheetName, data: jsonData });
            }
        });

        renderTables(tables);
    } catch (error) {
        console.error('Error al cargar el archivo Excel:', error);
    }
}

function renderTables(tables) {
    const container = document.querySelector('#table-container');
    container.innerHTML = ''; // Limpiar contenido previo

    tables.forEach(table => {
        const section = document.createElement('div');
        section.className = 'classification-section';

        const title = document.createElement('h3');
        title.textContent = `Clasificación: ${table.name}`;
        section.appendChild(title);

        const tableElement = document.createElement('table');
        tableElement.className = 'classification-table';

        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        table.data[0].forEach(header => {
            const th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        tableElement.appendChild(thead);

        const tbody = document.createElement('tbody');
        table.data.slice(1).forEach(row => {
            const tr = document.createElement('tr');
            row.forEach(cell => {
                const td = document.createElement('td');
                td.textContent = cell !== undefined ? cell : ''; // Asegurar contenido válido
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
        tableElement.appendChild(tbody);

        section.appendChild(tableElement);
        container.appendChild(section);
    });
}

// Ejecutar la función al cargar la página
loadExcel();
