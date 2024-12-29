import { renderClassificationTable } from './classification.js';
import { renderMatchesTable } from './matches.js';


const excelPath = './data/resultados.xlsx';

fetch(excelPath)
  .then(response => response.arrayBuffer())
  .then(data => {
    const workbook = XLSX.read(data, { type: 'array' });

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
        const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });

        const classificationRange = { startRow: 0, endRow: 10, startCol: 0, endCol: 13 };
        renderClassificationTable(sheetName, jsonData, classificationRange);

        const startRow = 1;
        const playerColIndex = 14;
        const startCol = 15;
        renderMatchesTable(sheetName, jsonData, startRow, playerColIndex, startCol);
      }
    });
  })
  .catch(error => console.error('Error al cargar el archivo Excel:', error));
