import requests

url = "https://openai.api2d.net/v1/chat/completions"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer fk210080-JpczqMVnOsDZQapvRp0tc5DtZzZzhrHi'
}

content = input("请输入：")
data = {
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": f"{content}"}]
}

response = requests.post(url, headers=headers, json=data)

print("Status Code", response.status_code)
print( response.json()['choices'][0]['message']['content'])

