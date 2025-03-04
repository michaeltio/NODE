import requests

url = "http://localhost:11434/api/generate"

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    payload = {
        "model": "llama2",
        "prompt": user_input,
        "stream": False

    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        json_response = response.json()  
        print("Sukses! Response:", response.json())
        if "response" in json_response:
            return json_response["response"]
    else:
       return "error bro"
