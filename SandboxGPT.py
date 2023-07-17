import http.client
import json

conn = http.client.HTTPSConnection("oa.api2d.net")
payload = json.dumps({
   "model": "text-embedding-ada-002",
   "input": "Hello"
})
headers = {
   'Authorization': 'Bearer fk210080-JpczqMVnOsDZQapvRp0tc5DtZzZzhrHi',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}
conn.request("POST", "/v1/embeddings", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))