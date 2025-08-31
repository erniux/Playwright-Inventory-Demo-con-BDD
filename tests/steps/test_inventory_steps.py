from pytest_bdd import scenarios, given, when, then, parsers

# Vincular el feature file
scenarios("../features/inventory.feature")


@given("I open the inventory demo")
def open_inventory(page):
    page.goto("https://www.ag-grid.com/example-inventory/")


@then("I should see the inventory table")
def check_table(page):
    assert page.is_visible(".ag-root"), "La tabla de inventario no se cargó"


@when(parsers.parse('I search for product "{product}"'))
def search_product(page, product):
    page.fill("input[placeholder='Search product...']", product)


@then(parsers.parse('I should see "{product}" in the results'))
def check_product_exists(page, product):
    page.wait_for_selector(f"text={product}")
    assert page.is_visible(f"text={product}"), f"El producto '{product}' no se encontró"


@then("I should see no results in the table")
def check_no_results(page):
    rows = page.query_selector_all(".ag-center-cols-container .ag-row")
    assert len(rows) == 0, "Se encontraron resultados cuando no debería haber ninguno"


@then("I should see multiple results in the table")
def check_multiple_results(page):
    rows = page.query_selector_all(".ag-center-cols-container .ag-row")
    assert len(rows) > 1, f"Se esperaban múltiples resultados, pero se encontraron {len(rows)}"


@then(parsers.parse('I should see the columns "{columns}"'))
def check_columns(page, columns):
    expected_columns = [col.strip() for col in columns.split(",")]
    header_elements = page.query_selector_all(".ag-header-cell-text")

    # Extraer los textos visibles de los encabezados
    header_texts = [h.inner_text().strip() for h in header_elements]

    for col in expected_columns:
        assert col in header_texts, f"La columna '{col}' no está presente en la tabla"


@when(parsers.parse('I sort the table by "{column}" ascending'))
def sort_table_asc(page, column):
    header = page.locator(f".ag-header-cell-text:has-text('{column}')")
    header.click()  # primer click → ascendente


@when(parsers.parse('I sort the table by "{column}" descending'))
def sort_table_desc(page, column):
    header = page.locator(f".ag-header-cell-text:has-text('{column}')")
    header.click()  # primer click ascendente
    header.click()  # segundo click descendente


@then(parsers.parse('the values in "{column}" should be sorted ascending'))
def check_sorted_asc(page, column):
    col_cells = page.query_selector_all(f".ag-cell[col-id='{column.lower()}']")
    values = [c.inner_text().strip() for c in col_cells if c.inner_text().strip()]
    numeric_values = [float(v.replace("$", "").replace(",", "")) for v in values]
    assert numeric_values == sorted(numeric_values), f"Los valores en '{column}' no están ordenados ascendentemente"


@then(parsers.parse('the values in "{column}" should be sorted descending'))
def check_sorted_desc(page, column):
    col_cells = page.query_selector_all(f".ag-cell[col-id='{column.lower()}']")
    values = [c.inner_text().strip() for c in col_cells if c.inner_text().strip()]
    numeric_values = [float(v.replace("$", "").replace(",", "")) for v in values]
    assert numeric_values == sorted(numeric_values, reverse=True), f"Los valores en '{column}' no están ordenados descendentemente"

 
@when("I go to the next page of the table")
def go_next_page(page):
    first_row = page.inner_text(".ag-center-cols-container .ag-row:first-child")
    page.context._first_row_value = first_row

    # Botón "Next Page"
    page.click("button[aria-label='Next Page']")
    page.wait_for_timeout(1000)


@then("I should see different results compared to the first page")
def check_pagination(page):
    new_first_row = page.inner_text(".ag-center-cols-container .ag-row:first-child")
    assert new_first_row != page.context._first_row_value, \
        f"Los resultados no cambiaron entre páginas"


@when(parsers.parse('I change the page size to "{size}"'))
def change_page_size(page, size):
    # Selector del page size
    page.select_option("select[aria-label='Page Size']", size)
    page.wait_for_timeout(1000)


@then("I should see more rows displayed than with the default size")
def check_page_size(page):
    rows = page.query_selector_all(".ag-center-cols-container .ag-row")
    assert len(rows) > 20, f"Se esperaban más de 20 filas, pero se encontraron {len(rows)}"