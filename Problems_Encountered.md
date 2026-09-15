These were the challenges and problems that I encountered making this project. The goal of this file is to help debug and understand certain steps taken when problems arise or for future development. 

1. Certain messages have *NULL* or empty values because of multiple possible causes like special characters, images sent, stickers, etc. So from the message table, instead of reading directly from message.text directly, I have to read from the message.attributedBody column instead. The problem with this is that the information in this column is in binary plist. I had to convert this and deserialize using *plistlib* to convert to string.

2. Another problem is Apple timestamps. When looking at the message table, you can see that the values in the date column is initially unrecognizable. An example of this is: 720563780607959296
After searching it up, I found out that this was in nano seconds, AND in Mac Absolute Time or Mac Absolute Epoch. (Mac Absolute Epoch measures time in nano seconds since Jan. 1, 2001, UTC)

To convert this:
    - Divide the number by 1,000,000,000 or 10^9 (Nanoseconds to seconds)
    - Add 978,307,200 (Convert from Mac Absolute Epoch to Unix Time)
    - Subtract 18,000 (*OPTIONAL* Convert UTC to EST)
    - Then in python convert to date.

3. Understanding how Apple saves and reads the messages, pairing them with the person and number. There are 4 crucial tables to remember to incapsulate this, *chat*, *handle*, *message*, and *chat_message_join*.
    chat - saves the unique identifier number saved in the ROWID table
    handle - shows full information about the other person: Phone number, email, Apple ID
    message - contains the actual message/text received or sent
    chat_message_join - connects the message.text to the chat_id (Who the text is to/from)