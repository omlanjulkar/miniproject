import requests

API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def query(prompt):
    payload = {
        "inputs": f"<s>[INST] {prompt} [/INST]",
        "parameters": {
            "max_new_tokens": 100,
            "return_full_text": True
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    # DEBUG: print full response details
    print("Status Code:", response.status_code)
    print("Raw Response:", response.text)

    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "raw": response.text}

# Basic loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = query(user_input)

    if "error" in response:
        print("Error:", response["error"])
        print("Raw response:", response["raw"])
    elif isinstance(response, list) and "generated_text" in response[0]:
        print("AI:", response[0]["generated_text"].split("[/INST]")[-1].strip())
    else:
        print("Unexpected response format:", response)
