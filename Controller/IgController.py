import requests
import json

def process_instagram_profile(username):
    url = "https://www.save-free.com/process"
    headers = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Length": "52",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "HstCfa4752989=1690994010962; HstCla4752989=1690994010962; ... (add the other cookies)",
    "Origin": "https://www.save-free.com",
    "Referer": "https://www.save-free.com/id/profile-downloader/",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "X-Valy-Cache": "accpted"
    }

    payload = {
        "instagram_url": username,
        "type": "profile",
        "resource": "save"
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        try:
            parsed_json = response.json()
            return parsed_json

        except json.JSONDecodeError:
            return {"error": "Unable to parse JSON response."}
    else:
        return {"error": f"Request failed with status code {response.status_code}"}