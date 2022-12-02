import json as jso
from datetime import datetime

with open("competitors2.json", encoding="UTF-8") as file:
    file_json = jso.load(file)

result: dict = {}
json: dict = file_json
with open("results_RUN.txt", "r", encoding="UTF-8") as lines:
    for lin in lines:
        values: list = lin.split()
        num: int = values[0]
        sf: str = values[1]
        if str == "start":
            result[num] = {}
            result[num]["start"] = datetime.strptime(values[2], "%H:%M:%S,%f")
        elif str == "finish":
            result[num]["end"] = datetime.strptime(values[2], "%H:%M:%S,%f")
            result[num]["result"] = result[num]["end"] - result[num]["start"]
        else:
            pass
    sorted_result = dict(sorted(result.items(), key=lambda item: item[1]["result"]))
    mesto = 0
    print("| Занятое место | Нагрудный номер | Имя | Фамилия | Результат |")
    for ident, value in sorted_result.items():
        mesto += 1
        Name = json[str(ident)]["Name"]
        Surname = json[str(ident)]["Surname"]
        print(f"| " + mesto + f" | " + ident + f" | " + Name + f" | " + Surname + f" | " + sorted_result + f" |")


