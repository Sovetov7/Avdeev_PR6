import json as jso
from datetime import datetime

with open("competitors2.json", encoding="UTF-8") as file:
    file_json = jso.load(file)
json: dict = file_json
with open("results_RUN.txt", "r", encoding="UTF-8") as file:
    file_txt = sorted(file.split('\n'), key=lambda x: (int(x.split()[0]), x.split()[1]))
    result = []
    for i in range(0, len(file_txt), 2):
        result.append(
            [file_txt[i].split()[0],
            datetime.strptime(file_txt[i].split()[2], "%H:%M:%S,%f") - datetime.strptime(file_txt[i+1].split()[2], "%H:%M:%S,%f")])
    result = sorted(result, key=lambda x:x[1])
    print("| Занятое место | Нагрудный номер | Имя | Фамилия | Результат |")
    i = 1

    for x in result:
        print('|', ' | '.join([
            f'{str(i):13}',
            f'{x[0]:15}',
            f'{file_json[x[0]]["Surname"]:11}',
            f'{file_json[x[0]]["Name"]:11}',
            f'{(datetime.strptime(str(x[1]), "%H:%M:%S,%f")).strptime("%M:%S,%f")[:-4]:9}']), '|')
        i += 1
