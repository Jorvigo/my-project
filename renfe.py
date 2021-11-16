
from behave import *
from selenium.webdriver.common.by import By


@given('en el portal de renfe')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.get("https://www.renfe.com/es/es")

@when('selecciono origen madrid')
def step_impl(context):
    context.driver = webdriver.Chrome()
    origen = driver.find_element(By.CSS_SELECTOR, "rf-awesomplete.rf-input-autocomplete:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
    origen.click()
    origen.sendkeys

@and('selecciono destino barcelona')
def step_impl(context):
    context.driver = webdriver.Chrome()
    link_serie = driver.find_element(By.CSS_SELECTOR, ".ListSdbr > li:nth-child(1) > a:nth-child(1)")
    link_serie.click()

@then('behave will test it for us!')
def step_impl(context):
    context.driver = webdriver.Chrome()
    assert context.failed is False

@then('behave will test it for us!')
def step_impl(context):
 link_episodio = context.driver.find_elements_by_css_selector, #episodeList > li:nth-child(2) > a > p
 if link_eposidio =
    assert link_episodio.text == 'Episodio 998'