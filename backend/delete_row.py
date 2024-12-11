import sqlite3

def delete_row(table_name, id):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    for i in id:
        cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (i,))
        conn.commit()
    conn.close()

if __name__ == "__main__":
    delete_row("links", range(4, 12))