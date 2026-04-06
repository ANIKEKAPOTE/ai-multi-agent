from db import get_connection

def save_note(text):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO notes (content) VALUES (%s)", (text,)
    )

    conn.commit()
    cur.close()
    conn.close()

    return f"📝 Note saved: {text}"