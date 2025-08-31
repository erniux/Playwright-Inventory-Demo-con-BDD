# Playwright Inventory Demo (Python + BDD)

# Playwright Inventory Demo (Python + BDD)

[![Playwright Tests](https://github.com/erniux/Playwright-Inventory-Demo-con-BDD/actions/workflows/tests.yml/badge.svg)](https://github.com/erniux/Playwright-Inventory-Demo-con-BDD/actions/workflows/tests.yml)  
[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)  
[![Playwright](https://img.shields.io/badge/playwright-installed-119e1a)](https://playwright.dev/)

Este proyecto es un framework de pruebas automatizadas...



Este proyecto es un **framework de pruebas automatizadas** usando:
- [Playwright](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/)
- [Pytest-BDD](https://pytest-bdd.readthedocs.io/en/latest/)

Las pruebas se realizan sobre demos públicas de **AG-Grid**:
- Inventario: https://www.ag-grid.com/example-inventory/
- Paginación: https://www.ag-grid.com/javascript-data-grid/pagination/

## 🚀 Instalación

Clona el repositorio y entra al proyecto:

```bash
git clone https://github.com/erniux/Playwright-Inventory-Demo-con-BDD.git
cd playwright_inventory_demo

## Crear un entorno Virtuale instalar las dependencias


python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
playwright install

## Ejecución
```
pytest -v  
pytest -v tests/features/inventory.feature  
pytest -k "Verify sorting by Price"
```

