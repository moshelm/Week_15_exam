from typing import List, Dict, Any




def get_customers_by_credit_limit_range(conn):
    """Return customers with credit limits outside the normal range."""
    query = "SELECT c.customerName ,c.creditLimit FROM customers c WHERE creditLimit > 100000 or creditLimit < 10000;"
    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res

def get_orders_with_null_comments(conn):
    """Return orders that have null comments."""
    query = """SELECT o.orderNumber, o.comments FROM orders o 
    WHERE comments IS NULL
    ORDER BY o.orderDate
    """
    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res

def get_first_5_customers(conn):
    """Return the first 5 customers."""
    query = """SELECT c.customerName, c.contactLastName, c.contactFirstName FROM customers c 
    ORDER BY  c.contactLastName LIMIT 5;"""
    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res
def get_payments_total_and_average(conn):
    """Return total and average payment amounts."""
    query = """SELECT SUM(p.amount) AS total , AVG(p.amount) as AVERAGE, MIN(p.amount) AS minimum, MAX(p.amount) AS maximum FROM payments p;"""
    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res
def get_employees_with_office_phone(conn):
    """Return employees with their office phone numbers."""

def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""

def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""

def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """Return customers and payments for last names matching pattern."""
    pass
