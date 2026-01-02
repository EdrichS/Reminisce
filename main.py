from db_utils import connect_db, get_chat_rowid, fetch_messages_for_chat
from message_utils import get_message_content
from convert_time import convert_apple_time
from output_utils import export_to_txt

DB_PATH = "/Users/edrich/Reminisce/Copy_chat.db"
TARGET_CHAT_IDENTIFIER = "+1234566789" #Change this to the person's number

def build_transcript():
    connect = connect_db(DB_PATH)
    chat_id = get_chat_rowid(connect, TARGET_CHAT_IDENTIFIER)
    rows = fetch_messages_for_chat(connect, chat_id)

    transcript = []
    for row in rows:
        rowid, text, attributed_body, date, is_from_me = row
        message_text = get_message_content(text, attributed_body)
        message_time = convert_apple_time(date)
        sender = "Yourname" if is_from_me else "Their name" 
        #Change this to your name and the other person's name
    
        transcript.append({
            "datetime": message_time,
            "sender": sender,
            "message": message_text
        })

    return transcript

if __name__ == "__main__":
    transcript = build_transcript()
    export_to_txt(transcript)
    print("Transcript generated! Enjoy Reminiscing!")
    print(f"Sicnerely, Edddy")