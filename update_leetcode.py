import requests

USERNAME = "gtfoold"

URL = "https://leetcode.com/graphql"
QUERY = """
{
  matchedUser(username: "%s") {
    submitStats {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
""" % USERNAME

response = requests.post(URL, json={'query': QUERY})
data = response.json()

if "data" in data and data["data"]["matchedUser"]:
    stats = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]
    easy = stats[1]["count"]
    medium = stats[2]["count"]
    hard = stats[3]["count"]

    with open("README.md", "r", encoding="utf-8") as file:
        content = file.readlines()

    new_content = []
    for line in content:
        if "🟢 **Легкий уровень:**" in line:
            line = f"- 🟢 **Легкий уровень:** `{easy}`\n"
        elif "🟡 **Средний уровень:**" in line:
            line = f"- 🟡 **Средний уровень:** `{medium}`\n"
        elif "🔴 **Сложный уровень:**" in line:
            line = f"- 🔴 **Сложный уровень:** `{hard}`\n"
        new_content.append(line)

    with open("README.md", "w", encoding="utf-8") as file:
        file.writelines(new_content)

    print("README.md успешно обновлен!")
else:
    print("Ошибка: не удалось получить данные с LeetCode.")
