import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT line_item_id, quantity, l.product_id, product_name, price FROM line_items l JOIN products p ON l.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head(5))
    df['total'] = df['quantity'] * df['price']
    print(df.head(5))
    grouped_df = df.groupby('product_id').agg({
        'line_item_id': 'count',  
        'total': 'sum',           
        'product_name': 'first'   
    }).sort_values('product_name')

    print(grouped_df.head(5))

    grouped_df.to_csv("order_summary.csv")