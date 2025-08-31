import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    # Lanzar Chromium en modo headed (visible)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    # Crear un contexto/nueva página para cada test
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
