document.getElementById("fileInput").addEventListener("change", function (event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        const data = new Uint8Array(e.target.result);
        const workbook = XLSX.read(data, { type: "array" });
  
        // Leer la primera hoja
        const sheetName = workbook.SheetNames[0];
        const sheet = workbook.Sheets[sheetName];
  
        // Convertir la hoja a JSON
        const jsonData = XLSX.utils.sheet_to_json(sheet);
  
        // Procesar y renderizar la clasificación
        renderTable(jsonData);
      };
      reader.readAsArrayBuffer(file);
    }
  });
  
  function renderTable(data) {
    const tableBody = document.querySelector("#table tbody");
    tableBody.innerHTML = ""; // Limpiar la tabla
  
    data.forEach((row) => {
      const tr = document.createElement("tr");
      const playerCell = document.createElement("td");
      const pointsCell = document.createElement("td");
      const setsCell = document.createElement("td");
      const scoreCell = document.createElement("td");
  
      // Datos del jugador
      playerCell.textContent = row["Jugador"] || row["Player"];
      pointsCell.textContent = row["Puntos"] || row["Points"];
      setsCell.textContent = row["Sets Ganados"] || row["Sets"];
      scoreCell.textContent = row["Puntaje Total"] || row["Score"];
  
      tr.appendChild(playerCell);
      tr.appendChild(pointsCell);
      tr.appendChild(setsCell);
      tr.appendChild(scoreCell);
      tableBody.appendChild(tr);
    });
  }
  
