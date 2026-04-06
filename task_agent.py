from db import get_connection

def create_task(text):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO tasks (title, status) VALUES (%s, %s)",
        (text, "pending")
    )

    conn.commit()
    cur.close()
    conn.close()

    return f"✅ Task created: {text}"