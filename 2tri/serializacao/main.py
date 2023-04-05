import json

from people import PeopleSW

with open('people.json','r') as f:
    data = json.load(f)

resultados = data[0]['results']
a = []
for dados in resultados[0]:
    a.append(dados)

for people in resultados:
    print(people)
