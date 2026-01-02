import binascii
import re

def decode_apple_attributed_body(blob):
    """
    Decode message.attributedBody stored as bytes in Apple's NSAttributedString format.
    Works without any macOS-specific frameworks.
    """
    if blob is None:
        return None

    try:
        # If blob is bytes, convert to str for processing
        if isinstance(blob, bytes):
            raw_bytes = blob
        else:
            # sometimes data may be stored as hex string
            hex_data = str(blob).replace('\n', '').replace(' ', '')
            raw_bytes = binascii.unhexlify(hex_data)

        # Decode to UTF-8 ignoring errors
        decoded_text = raw_bytes.decode('utf-8', errors='ignore')

        # Extract text between NSString and NSDictionary markers
        match = re.search(r'NSString.(.*?)NSDictionary', decoded_text, re.DOTALL)

        if match:
            result = match.group(1).strip()
            # Strip leading control byte if present
            return result[1:] if len(result) > 0 else result
        else:
            # Fallback: keep any printable characters/emoji
            return "".join(re.findall(r'[^\x00-\x1F\x7F-\x9F]+', decoded_text))

    except Exception as e:
        # For debugging only; in production, just return None
        return None


def get_message_content(text, attributed_body):
    """
    Determine the best textual representation of a message.
    Works for all messages in the database.
    """

    # 1. Plain text first (fastest, preferred)
    if text and text.strip():
        return text

    # 2. Decode attributed_body
    decoded = decode_apple_attributed_body(attributed_body)
    if decoded and decoded.strip():
        return decoded

    # 3. Fallback for non-text content
    return "[Non-text message]"
