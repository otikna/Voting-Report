import requests

header = {
'Authorization': 'Token Your-Token',
'Content-Type': 'application/json'
}

url = "https://api.cognitus.ai/api/v1/entity"

data=[]
with open("data.txt", "r", encoding="UTF-8") as f:
    veri = f.readlines()
    for s in veri:
        data.append(s)

for s in data:
    response = requests.post(url, json={"text":s}, headers=header).json()
    for i in response:
        if i[1] == "I-LOC":
            with open("result.txt", "a", encoding="UTF-8") as f:
                f.write("\n"+i[0])

