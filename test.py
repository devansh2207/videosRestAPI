import requests

BASE = "http://127.0.0.1:5000/" 

data = [
    {"likes": 72, "name": "Abcd" , "views": 1705},
    {"likes": 103, "name": "Devansh" , "views": 2207},
    {"likes": 281, "name": "How to make a REST API" , "views": 5076},
    {"likes": 1000, "name": "How to play a guitar" , "views": 14320},
    {"likes": 950, "name": "How to play a violin" , "views": 9788}
]

# response = requests.put(BASE + "video/"+ "0", data[0])
# response = requests.put(BASE + "video/"+ "1", data[1])
# response = requests.put(BASE + "video/"+ "2", data[2])
# response = requests.put(BASE + "video/"+ "3", data[3])

# response = requests.get(BASE + "video/"+ "3")

# response = requests.patch(BASE + "video/"+ "3", data[4])

# response = requests.get(BASE + "video/"+ "3")

# response = requests.patch(BASE + "video/"+ "3", {"name"="How to play drums"})

# response = requests.get(BASE + "video/"+ "3")

# response = requests.put(BASE + "video/"+ "4", data[0])

response = requests.get(BASE + "video/"+ "4")

print(response.json())
