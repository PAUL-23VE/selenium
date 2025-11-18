import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By

# Ingresar a la pagina
driver = wd.Edge()
driver.get('file:///C:/Users/paulv/OneDrive/Desktop/Gestion%20Pruebas/Gestion%20de%20Pruebas/PruebaSelenium/index.html')
time.sleep(3)

# Crear clientes
cedula_input = driver.find_element(By.ID, 'clienteCedula')
nombre_input = driver.find_element(By.ID, 'clienteNombre')
apellido_input = driver.find_element(By.ID, 'clienteApellido')
correo_input = driver.find_element(By.ID, 'clienteCorreo')
telefono_input = driver.find_element(By.ID, 'clienteTelefono')
btnAgregar = driver.find_element(By.XPATH, "//button[text()='Agregar Cliente']")

# Con cedula = 1001
cedula_input.send_keys('1001')
time.sleep(1)
nombre_input.send_keys('JOSE')
time.sleep(1)
apellido_input.send_keys('LOPEZ')
time.sleep(1)
correo_input.send_keys('ADASDAS@gmail.com')
time.sleep(1)
telefono_input.send_keys('9999999999')
time.sleep(1)
btnAgregar.click()
time.sleep(2)

# Con cedula = 1002
cedula_input.send_keys('1002')
time.sleep(1)
nombre_input.send_keys('PAUL')
time.sleep(1)
apellido_input.send_keys('VELASTEGUI')
time.sleep(1)
correo_input.send_keys('DSFSDFSDDSF@gmail.com')
time.sleep(1)
telefono_input.send_keys('9999999999')
time.sleep(1)
btnAgregar.click()
time.sleep(2)

# Modificar Cliente con cedula 1001
obtener_cliente = driver.find_element(By.XPATH, "//strong")
if obtener_cliente.text == "JOSE LOPEZ":
    btnEditar = driver.find_element(By.CLASS_NAME, 'edit').click()
    time.sleep(1)

nombre_input.clear()
time.sleep(1)
apellido_input.clear()
time.sleep(1)
correo_input.clear()
time.sleep(1)
telefono_input.clear()
time.sleep(1)

nombre_input.send_keys("JOSEEEEEEEEEEE")
time.sleep(1)
apellido_input.send_keys("RESCALVO")
time.sleep(1)
correo_input.send_keys("ASDASAAAAAAAAA@gmail.com")
time.sleep(1)
telefono_input.send_keys("9999999999")
time.sleep(1)
btnAgregar.click()
time.sleep(2)

# Eliminar cliente con cedula 1001
obtener_editado = driver.find_element(By.XPATH, "//strong")
if obtener_editado.text == "JOSEEEEEEEEEEE RESCALVO":
    btnEliminar = driver.find_element(By.CLASS_NAME, 'delete').click()
    time.sleep(1)

# Crear una cuenta de ahorro
navegar_cuentas = driver.find_element(By.XPATH, "//button[text()='Cuentas']").click()
time.sleep(2)
btnAgregar_cuenta = driver.find_element(By.XPATH, "//button[@onclick='agregarCuenta()']").click()
time.sleep(1)

# Crear una cuenta Corriente 
seleccionar_cuenta = driver.find_element(By.XPATH, "//option[@value='Corriente']").click()
time.sleep(1)
btnAgregar_cuenta = driver.find_element(By.XPATH, "//button[@onclick='agregarCuenta()']").click()
time.sleep(1)

# Desactivar la cuenta corriente 


# Realizar un depósito con fecha 18-11-2025
navegar_cuentas = driver.find_element(By.XPATH, "//button[text()='Depósitos']").click()
time.sleep(1)
input_fecha = driver.find_element(By.ID, "depositoFecha")
time.sleep(1)
input_fecha.send_keys("18-11-2025")
time.sleep(1)

monto = driver.find_element(By.ID, "depositoMonto")
monto.send_keys("111")
time.sleep(1)

btnAgregar_deposito = driver.find_element(By.XPATH, "//button[text()='Agregar Depósito']").click()
time.sleep(1)


# Realizar un depósito con fecha 11-11-2024
input_fecha.clear()
time.sleep(1)
input_fecha.send_keys("11-11-2025")
time.sleep(1)
monto.clear()
time.sleep(1)
monto.send_keys("500")
time.sleep(1)
btnAgregar_deposito = driver.find_element(By.XPATH, "//button[text()='Agregar Depósito']").click()
time.sleep(3)

# Eliminar el deposito con fecha 11-11-2025
cards = driver.find_elements(By.CLASS_NAME, "card")

for card in cards:
    if "2025-11-11" in card.text:
        btnEliminar = card.find_element(By.XPATH, ".//button[text()='Eliminar']")
        btnEliminar.click()
        print("Depósito eliminado correctamente")
        break
else:
    print("No se encontró el depósito con la fecha indicada")
time.sleep(3)


