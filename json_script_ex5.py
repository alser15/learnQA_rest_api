import json

json_text = """{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}"""


# Все сообщение
print(json.loads(json_text)["messages"][1])

# Значение message
print(json.loads(json_text)["messages"][1]["message"])

# Значение timestamp
print(json.loads(json_text)["messages"][1]["timestamp"])