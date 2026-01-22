import sqlite3

from sqlalchemy import DATE

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# Aggregation with HAVING
query = """
select o.order_id,sum(p.price*l.quantity) 
from orders o join line_items l on o.order_id=l.order_id 
    join products p on l.product_id=p.product_id 
    group by o.order_id order by o.order_id limit 5;
"""

# Execute and fetch results
cursor.execute(query)
results = cursor.fetchall()
print(results)

conn.close()
####### Task 2 #######
# Connect to the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# Aggregation with HAVING
query = """
select c.customer_name,avg(b.total_price) as avrg from customers c left join (
select o.customer_id as customer_id_b,sum(p.price*l.quantity) as total_price 
from orders o join line_items l on o.order_id=l.order_id 
join products p on l.product_id=p.product_id 
group by o.order_id
) b on c.customer_id=b.customer_id_b
group by c.customer_id;
"""

# Execute and fetch results
cursor.execute(query)
results = cursor.fetchall()
print(results)

conn.close()
####### Task 4 #######


conn = sqlite3.connect("company.db")
cursor = conn.cursor()

try:

    query = """
    select c.customer_id from customers c where c.customer_name ='Perez and Sons';
    """
    cursor.execute(query)
    customer_id=cursor.fetchone()[0]
    print("Customer ID:", customer_id)

    query = """
    select product_id from products order by price limit 5;"""
    cursor.execute(query)
    product_ids=[]
    results = cursor.fetchall()
    for row in results:
        product_ids.append(row[0])
    print("Product IDs:", product_ids)

    query = """
    select employee_id from employees where first_name='Miranda' and last_name='Harris';
    """
    cursor.execute(query)
    employee_id=cursor.fetchone()[0]
    print("Employee ID:", employee_id)
    cursor.execute("INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, ?) RETURNING order_id", (customer_id, employee_id,DATE('now')))
    new_order_id = cursor.fetchone()[0]
    for p_id in product_ids:
        cursor.execute("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)", (new_order_id, p_id, 10))
    conn.commit()  # Commit transaction

    cursor.execute("""
            select *
            from line_items l
            join products p ON l.product_id = p.product_id
            WHERE l.order_id = ?
        """, (new_order_id,))
    for row in cursor.fetchall():
         print(row)

except Exception as e:
    conn.rollback()  # Rollback transaction if there's an error
    print("Error:", e)

conn.close()
####### Task 4 #######
# Connect to the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# Aggregation with HAVING
query = """
select e.employee_id,e.first_name,e.last_name,count(order_id) as ocount
from employees e  join orders o on e.employee_id=o.employee_id 
group by e.employee_id,e.first_name,e.last_name having count(o.order_id)>5;
"""

# Execute and fetch results
cursor.execute(query)
results = cursor.fetchall()
print(results)

conn.close()