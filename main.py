#!/usr/bin/python3
from metodos.lista import *
from metodos.crear import *
from metodos.delete import *
from metodos.update import *

print("todos")
list_all_table("ac_products")
print("--------------------------------------------------")
"""crear_ac_tenant(1, "prueba")
crear_customer(1, 1, 'jimmer', 'hernandez')
crear_ac_invoices(1, 1, 1, "abril", "2020", 1, 1, 1)
crear_ac_products(1, 1, "papel", "una hoja de papel", 1)
crear_ac_invoice_items(1, 1, 1, 1, 1, 1, 1)"""
print("customer id = 1")
list_table_id("ac_products", "1")
print("--------------------------------------------------")
print("Todos")
list_table_id()
update_table(1, 'customer', 'FIRST_NAME=Tony, LAST_NAME=Stark')
print("Update")
list_table_id("customer", "1")
