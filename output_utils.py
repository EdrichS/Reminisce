import pandas as pd

""" 
COMPLETELY OPTIONAL, but this outputs as a .csv file as well
To use you MUST ADD "export_to_csv" on the main.py
def export_to_csv(transcript, filename= "Reminiscing.csv"):
    df = pd.DataFrame(transcript)
    df.to_csv(filename, index = False)
    print(f"Exported as: {filename}") """

def export_to_txt(transcript, filename = "Reminiscing.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for item in transcript:
            dt_str = item['datetime'].strftime("%B %-d, %Y %-I:%M %p") if item['datetime'] else "Unknown time"
            f.write(f"[{dt_str}] {item['sender']}: {item['message']}\n")
    print(f"Exported to {filename}")