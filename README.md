# Playwright Inventory Demo (Python + BDD)


[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)  
[![Playwright](https://img.shields.io/badge/playwright-installed-119e1a)](https://playwright.dev/)
[![Playwright Tests](https://github.com/erniux/Playwright-Inventory-Demo-con-BDD/actions/workflows/tests.yml/badge.svg)](https://github.com/erniux/Playwright-Inventory-Demo-con-BDD/actions/workflows/tests.yml) 
[![Allure Report](https://img.shields.io/badge/Allure-Report-ff69b4?logo=allure&logoColor=white)](https://erniux.github.io/Playwright-Inventory-Demo-con-BDD/)


Este proyecto es un **framework de pruebas automatizadas** construido con:

- [Playwright](https://playwright.dev/python/)  
- [Pytest](https://docs.pytest.org/)  
- [Pytest-BDD](https://pytest-bdd.readthedocs.io/en/latest/)

Las pruebas se realizan sobre demos públicas de **AG-Grid**:  
- Inventario: https://www.ag-grid.com/example-inventory/  
- Paginación: https://www.ag-grid.com/javascript-data-grid/pagination/  

---

## 🚀 Instalación

Clona el repositorio y entra al proyecto:

```bash
git clone https://github.com/erniux/Playwright-Inventory-Demo-con-BDD.git
cd Playwright-Inventory-Demo-con-BDD
```

Crea un entorno virtual e instala las dependencias:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
playwright install chromium
```

---

## ▶️ Ejecución de pruebas

Ejecutar **todas las pruebas**:

```bash
pytest -v
```

Ejecutar un **feature específico**:

```bash
pytest -v tests/features/inventory.feature
```

Ejecutar un **escenario por nombre**:

```bash
pytest -k "Verify sorting by Price"
```

---

## 📊 Reportes con Allure

Este proyecto usa **[Allure](https://docs.qameta.io/allure/)** para generar reportes de pruebas en formato HTML.

### 🔹 Generar el reporte localmente
1. Instala Allure CLI en tu máquina:
   - En **Mac/Linux** con Homebrew:
     ```bash
     brew install allure
     ```
   - En **Windows** con Scoop:
     ```bash
     scoop install allure
     ```

2. Corre los tests y genera resultados:
   ```bash
   pytest --alluredir=allure-results
   ```

3. Abre el reporte en el navegador:
   ```bash
   allure serve allure-results
   ```

### 🔹 Reportes en CI (GitHub Actions)
En cada ejecución del workflow, los resultados de Allure se guardan como un artefacto descargable:  
- Ve a la pestaña **Actions** en GitHub.  
- Selecciona el último run.  
- Descarga el artefacto llamado **`allure-results`**.  
- Para visualizarlo localmente:  
  ```bash
  allure serve allure-results
  ```

---

## 📂 Escenarios cubiertos

### `inventory.feature`
- Cargar la tabla de inventario  
- Buscar producto existente  
- Buscar producto inexistente  
- Buscar por término parcial (múltiples resultados)  
- Validar columnas (`Name`, `Category`, `Price`)  
- Ordenar por `Price` ascendente y descendente  

### `pagination.feature`
- Cambiar de página y validar registros diferentes  
- Cambiar el tamaño de página (20 → 100 filas)  

---

## ✨ Notas
- La demo de paginación de AG-Grid a veces cambia su implementación, por lo que puede ser inestable.  
- El objetivo del proyecto es **mostrar buenas prácticas de BDD y Playwright en Python** para portafolio profesional.  


