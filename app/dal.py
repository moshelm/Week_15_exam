from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector import Error

def execute_query(conn : MySQLConnectionAbstract,query,params=None):
    try:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(query,params or ())
            return cursor.fetchall()
    except Error as e:
        print(f'connection failed {e}')
        return []

def get_customers_by_credit_limit_range(conn):
    """Return customers with credit limits outside the normal range."""
    query = "SELECT c.customerName ,c.creditLimit FROM customers c WHERE creditLimit > %s or creditLimit < %s;"
    return execute_query(conn,query,(100000,10000)) 

def get_orders_with_null_comments(conn):
    """Return orders that have null comments."""
    query = """SELECT o.orderNumber, o.comments FROM orders o 
    WHERE comments IS NULL
    ORDER BY o.orderDate
    """
    return execute_query(conn, query)

def get_first_5_customers(conn):
    """Return the first 5 customers."""
    query = """SELECT c.customerName, c.contactLastName, c.contactFirstName FROM customers c 
    ORDER BY  c.contactLastName LIMIT %s;"""
    return execute_query(conn, query,(5,))


def get_payments_total_and_average(conn):
    """Return total and average payment amounts."""
    query = """SELECT SUM(p.amount) AS total , AVG(p.amount) as AVERAGE, MIN(p.amount) AS minimum, MAX(p.amount) AS maximum FROM payments p;"""
    return execute_query(conn, query)


def get_employees_with_office_phone(conn):
    """Return employees with their office phone numbers."""
    query = """SELECT e.firstName , e.lastName, o.phone 
    FROM employees e JOIN offices o on o.officeCode=e.officeCode;"""
    return execute_query(conn,query)


def get_customers_with_shipping_dates(conn):
    """Return customers with their order shipping dates."""
    query = """SELECT c.customerName, o.shippedDate 
    FROM customers c LEFT JOIN orders o ON c.customerNumber=o.customerNumber"""
    return execute_query(conn,query)

def get_customer_quantity_per_order(conn):
    """Return customer name and quantity for each order."""
    query = """SELECT c.customerName, od.quantityOrdered AS quantity_for_each_order
    FROM customers c LEFT JOIN orders o ON c.customerNumber=o.customerNumber 
    JOIN orderdetails od ON o.orderNumber=od.orderNumber ORDER BY c.customerName;"""
    return execute_query(conn,query)

def get_customers_payments_by_lastname_pattern(conn):
    """Return customers and payments for last names matching pattern."""
    query = """SELECT c.customerName, e.firstName, SUM(p.amount) 
    FROM customers c  JOIN employees e ON c.salesRepEmployeeNumber=e.employeeNumber JOIN payments p ON c.customerNumber=p.customerNumber
    WHERE c.contactFirstName LIKE '%Mu%' OR c.contactFirstName LIKE '%ly%'
    GROUP BY c.customerName, e.firstName"""
    return execute_query(conn,query)
