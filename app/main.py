from fastapi import FastAPI
from db_init import init_database
from db import get_db_connection
from dal import *
app = FastAPI()

init_database()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/q1/customers-credit-limit-outliers")
def customers_credit_limit_outliers():
    conn = get_db_connection()
    res_data = get_customers_by_credit_limit_range(conn)
    conn.close()
    return {'res':res_data}

@app.get("/q2/orders-null-comments")
def orders_null_comments():
    conn = get_db_connection()
    res_data = get_orders_with_null_comments(conn)
    conn.close()
    return {'res':res_data}

@app.get("/q3/customers-first-5")
def customers_first_5():
    conn = get_db_connection()
    res_data = get_first_5_customers(conn)
    conn.close()
    return {'res':res_data}

@app.get("/q4/payments-total-average")
def payments_total_average():
    conn = get_db_connection()
    res_data = get_payments_total_and_average(conn)
    conn.close()
    return {'res':res_data}

@app.get("/q5/employees-office-phone")
def employees_office_phone():
    conn = get_db_connection()
    res_data = get_employees_with_office_phone(conn)
    conn.close()
    return {'res':res_data}

@app.get("/q6/customers-shipping-dates")
def customers_shipping_dates():
    conn = get_db_connection()
    res_data = get_customers_with_shipping_dates(conn)
    conn.close()
    return {'res':res_data}

@app.get("/q7/customer-quantity-per-order")
def customer_quantity_per_order():
    conn = get_db_connection()
    res_data = get_customer_quantity_per_order(conn)
    conn.close()
    return {'res':res_data}

@app.get("/q8/customers-payments-by-lastname-pattern")
def customers_payments_by_lastname_pattern(pattern: str = "son"):
    pass
