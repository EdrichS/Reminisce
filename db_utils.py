import sqlite3

def connect_db(db_path):

    connect = sqlite3.connect(db_path)
    return connect

def get_chat_rowid(connect, chat_identifier):
    # Gets the ROWID of the chat for the specific conversation

    cursor = connect.cursor()
    cursor.execute("Select ROWID FROM chat WHERE chat_identifier = ?", (chat_identifier, ))
    row = cursor.fetchone()
    if row is None: 
        raise ValueError(f"Chat not found for identifier {chat_identifier}")
    return row[0]

def fetch_messages_for_chat(connect, chat_id):
    # Returns all messages for a chat ordered by date

    cursor = connect.cursor()
    cursor.execute("""
                   SELECT m.ROWID, m.text, m.attributedBody, m.date, m.is_from_me
                   FROM message m
                   JOIN chat_message_join cmj
                        ON m.ROWID =cmj.message_id
                   WHERE cmj.chat_id = ?
                   ORDER BY m.date
                   """, (chat_id,))
    return cursor.fetchall()