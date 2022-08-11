alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open("./contents/archive-clg.txt", "w") as txt:
    for i in alunos:
        txt.write(f"{i}, {alunos[i]}\n")

with open("./contents/archive-clg.txt", "r") as txt:
    for i in txt:
        print(i)
