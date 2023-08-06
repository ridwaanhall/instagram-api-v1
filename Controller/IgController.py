import requests
import json
import random

def code_response(response):
    code = response.status_code
    if code == 200:
        try:
            parsed_json = response.json()
            return parsed_json
        except json.JSONDecodeError:
            return {"error": "Unable to parse JSON response."}
    elif code == 429:
        return {
            "code": 429,
            "message": "Too Many Requests",
            "message_from_owners": "Jangan spam, cooldown 1 menit."
        }
    elif code == 300:
        return {
            "code": 300,
            "message": "Multiple Choices"
        }
    elif code == 301:
        return {
            "code": 301,
            "message": "Moved Permanently"
        }
    elif code == 302:
        return {
            "code": 302,
            "message": "Found (or Moved Temporarily)"
        }
    elif code == 304:
        return {
            "code": 304,
            "message": "Not Modified"
        }
    elif code == 307:
        return {
            "code": 307,
            "message": "Temporary Redirect"
        }
    elif code == 308:
        return {
            "code": 308,
            "message": "Permanent Redirect"
        }
    elif code == 400:
        return {
            "code": 400,
            "message": "Bad Request"
        }
    elif code == 401:
        return {
            "code": 401,
            "message": "Unauthorized"
        }
    elif code == 403:
        return {
            "code": 403,
            "message": "Forbidden"
        }
    elif code == 404:
        return {
            "code": 404,
            "message": "Not Found"
        }
    elif code == 405:
        return {
            "code": 405,
            "message": "Method Not Allowed"
        }
    elif code == 406:
        return {
            "code": 406,
            "message": "Not Acceptable"
        }
    elif code == 407:
        return {
            "code": 407,
            "message": "Proxy Authentication Required"
        }
    elif code == 408:
        return {
            "code": 408,
            "message": "Request Timeout"
        }
    elif code == 409:
        return {
            "code": 409,
            "message": "Conflict"
        }
    elif code == 410:
        return {
            "code": 410,
            "message": "Gone"
        }
    elif code == 411:
        return {
            "code": 411,
            "message": "Length Required"
        }
    elif code == 412:
        return {
            "code": 412,
            "message": "Precondition Failed"
        }
    elif code == 413:
        return {
            "code": 413,
            "message": "Payload Too Large"
        }
    elif code == 414:
        return {
            "code": 414,
            "message": "URI Too Long"
        }
    elif code == 415:
        return {
            "code": 415,
            "message": "Unsupported Media Type"
        }
    elif code == 416:
        return {
            "code": 416,
            "message": "Range Not Satisfiable"
        }
    elif code == 417:
        return {
            "code": 417,
            "message": "Expectation Failed"
        }
    elif code == 418:
        return {
            "code": 418,
            "message": "I'm a teapot"
        }
    elif code == 421:
        return {
            "code": 421,
            "message": "Misdirected Request"
        }
    elif code == 422:
        return {
            "code": 422,
            "message": "Unprocessable Entity"
        }
    elif code == 431:
        return {
            "code": 431,
            "message": "Request Header Fields Too Large"
        }
    elif code == 451:
        return {
            "code": 451,
            "message": "Unavailable For Legal Reasons"
        }
    elif code == 500:
        return {
            "code": 500,
            "message": "Internal Server Error"
        }
    elif code == 501:
        return {
            "code": 501,
            "message": "Not Implemented"
        }
    elif code == 502:
        return {
            "code": 502,
            "message": "Bad Gateway"
        }
    elif code == 503:
        return {
            "code": 503,
            "message": "Service Unavailable"
        }
    elif code == 504:
        return {
            "code": 504,
            "message": "Gateway Timeout"
        }
    elif code == 505:
        return {
            "code": 505,
            "message": "HTTP Version Not Supported"
        }
    elif code == 511:
        return {
            "code": 511,
            "message": "Network Authentication Required"
        }
    else:
        return {"error": f"Request failed with status code {code}"}

user_agents = [
    {
        "user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
        "browser": "Microsoft Edge",
        "version": "88",
        "os": "Windows 7 (64-bit)"
    },
    {
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "browser": "Mozilla Firefox",
        "version": "78",
        "os": "Windows 8.1 (64-bit)"
    },
    {
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "browser": "Google Chrome",
        "version": "92",
        "os": "macOS High Sierra (10.13.6)"
    },
    {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "browser": "Mozilla Firefox",
        "version": "91",
        "os": "Windows 10 (64-bit)"
    },
    {
        "user_agent": "Mozilla/5.0 (Linux; Android 11; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
        "browser": "Google Chrome",
        "version": "94",
        "os": "Samsung Galaxy A51 (Android 11)"
    },
    {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
        "browser": "Internet Explorer",
        "version": "11",
        "os": "Windows 10 (64-bit)"
    },
    {
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "browser": "Google Chrome",
        "version": "94",
        "os": "macOS Big Sur (11.5.2)"
    },
    {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "browser": "Google Chrome",
        "version": "93",
        "os": "Windows 10 (64-bit)"
    },
    {
        "user_agent": "Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36",
        "browser": "Google Chrome",
        "version": "94",
        "os": "Samsung Galaxy S9 (Android 10)"
    },
    {
        "user_agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "browser": "Google Chrome",
        "version": "94",
        "os": "Windows 7 (64-bit)"
    },
    {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.8.1.697 Yowser/2.5 Safari/537.36",
        "browser": "Yandex Browser",
        "version": "21.8.1.697",
        "os": "Windows 10 (64-bit)"
    },
    {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "browser": "Google Chrome",
        "version": "92",
        "os": "Windows 10 (64-bit)"
    },
    {
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "browser": "Google Chrome",
        "version": "94",
        "os": "macOS Catalina (10.15.7)"
    },
    {
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/92.0",
        "browser": "Mozilla Firefox",
        "version": "92",
        "os": "Windows 8.1 (64-bit)"
    },
    {
        "user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "browser": "Google Chrome",
        "version": "94",
        "os": "Windows 7 (32-bit)"
    },
    {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "browser": "Mozilla Firefox",
        "version": "91",
        "os": "Windows 10 (64-bit)"
    },
    {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
        "browser": "Safari",
        "version": "15.0",
        "os": "iPhone (iOS 15)"
    },
    {
        "user_agent": "Mozilla/5.0 (Linux; Android 11; SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36",
        "browser": "Google Chrome",
        "version": "94",
        "os": "Samsung Galaxy S20 Ultra (Android 11)"
    },
    {
        "user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 OPR/71.0.3770.171",
        "browser": "Opera",
        "version": "71.0.3770.171",
        "os": "Windows 7 (32-bit)"
    },
    {
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
        "browser": "Safari",
        "version": "15.1",
        "os": "macOS Big Sur (11.6.2)"
    },
    {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.8.1.697 Yowser/2.5 Safari/537.36",
        "browser": "Yandex Browser",
        "version": "21.8.1.697",
        "os": "Windows 10 (64-bit)"
    }
    # Add more User-Agent strings here...
  ]

def get_random_user_agent():
  return random.choice(user_agents)["user_agent"]

def process_instagram_profile(username):
    url = "https://www.save-free.com/process"
    headers = {
        "Origin": "https://www.save-free.com",
        "Referer": "https://www.save-free.com/id/profile-downloader/",
        "User-Agent": get_random_user_agent(),
        "X-Valy-Cache": "accpted"
    }

    payload = {
        "instagram_url": username,
        "type": "profile",
        "resource": "save"
    }

    response = requests.post(url, data=payload, headers=headers)

    # Call code_response function to handle response status code
    response_data = code_response(response)

    # Check if there was an error in code_response
    if "error" in response_data:
        return response_data

    # If response code is 200, we have a successful response
    if response.status_code == 200:
        try:
            parsed_json = response.json()
            return parsed_json
        except json.JSONDecodeError:
            return {"error": "Unable to parse JSON response."}
    else:
        # For other response codes, return the response_data from code_response
        return response_data

def process_instagram_story(username):
    url = "https://www.save-free.com/process"
    headers = {
        "Origin": "https://www.save-free.com",
        "Referer": "https://www.save-free.com/id/profile-downloader/",
        "User-Agent": get_random_user_agent(),
        "X-Valy-Cache": "accpted"
    }
  
    payload = {
        "instagram_url": username,
        "type": "story",
        "resource": "save"
    }

    response = requests.post(url, data=payload, headers=headers)

    # Call code_response function to handle response status code
    response_data = code_response(response)

    # Check if there was an error in code_response
    if "error" in response_data:
        return response_data

    # If response code is 200, we have a successful response
    if response.status_code == 200:
        try:
            parsed_json = response.json()
            return parsed_json
        except json.JSONDecodeError:
            return {"error": "Unable to parse JSON response."}
    else:
        # For other response codes, return the response_data from code_response
        return response_data

def process_instagram_media():
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
    "User-Agent": get_random_user_agent(),
    "X-Requested-With": "XMLHttpRequest",
    "X-Valy-Cache": "accpted"
    }
  
    payload = {
        "instagram_url": "https://www.instagram.com/p/CvldjpRPVXx/",
        "type": "media",
        "resource": "save"
    }

    response = requests.post(url, data=payload, headers=headers)

    # For debugging purposes, print the actual response content
    print("Response content:", response.content)
    try:
        parsed_json = response.json()
        return parsed_json
    except json.JSONDecodeError:
        # If unable to parse JSON, return the error message
        return {"error": "Unable to parse JSON response."}