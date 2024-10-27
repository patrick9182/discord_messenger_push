import http.client
import json
import sys
import os
from dotenv import load_dotenv

load_dotenv()  # 讀取 .env 檔案

# 從 .env 中獲取 token
token = os.getenv("DISCORD_TOKEN")

header_data = { 
    "Content-Type": "application/json", 
    "User-Agent": "DiscordBot", 
    "Authorization": token  
} 

def get_connection(): 
    return http.client.HTTPSConnection("discord.com", 443) 

def send_message(conn, channel_id, message_data, token): 
    try: 
        header_data["Authorization"] = token
        conn.request("POST", f"/api/v10/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
        
        if 199 < resp.status < 300: 
            print("Message Sent.") 
        else: 
            print(f"HTTP {resp.status}: {resp.reason}")
    except Exception as e: 
        print("Error:", e) 

def main(config_path): 
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
            channel_id = config_data['Config'][0]['channelid']  # config.json
            message = config_data['Config'][0]['message']  # config.json

        message_data = { 
            "content": message, 
            "tts": False
        } 

        send_message(get_connection(), channel_id, json.dumps(message_data), token) 
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <config_path>")
        sys.exit(1)
    config_path = sys.argv[1]
    main(config_path)
