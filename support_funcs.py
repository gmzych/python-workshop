from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_for_visibility_of_element(driver_instance,xpath,time_to_wait=10):
    elem = WebDriverWait(driver_instance,time_to_wait).until(EC.visibility_of_element_located((By.XPATH,xpath)))
    return elem

def wait_for_visibility_of_elements(driver_instance,xpath,time_to_wait=10):
    elems = WebDriverWait(driver_instance,time_to_wait).until(EC.visibility_of_all_elements_located((By.XPATH,xpath)))
    return elems