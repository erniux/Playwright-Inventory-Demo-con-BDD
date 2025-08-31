import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    # Lanzar Chromium en modo headed (visible)
    with sync_playwright() as p:
        # Detectar si estamos en CI (GitHub Actions)
        is_ci = os.getenv("CI") == "true"

        browser = p.chromium.launch(
            headless=is_ci,  # en CI = headless; local = headed
            slow_mo=500 if not is_ci else 0
        )
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    # Crear un contexto/nueva página para cada test
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
