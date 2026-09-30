import sqlite3

# Auto-delete aagama irukka indha line irukkanum
_ = sqlite3.connect

DB_FILE = "pocket_smart.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_all_expenses():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, amount FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "title": row[1], "amount": row[2]} for row in rows]

def add_expense_db(title: str, amount: float):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (title, amount) VALUES (?, ?)", (title, amount))
    conn.commit()
    conn.close()

def delete_expense_db(expense_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

