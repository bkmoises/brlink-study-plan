dic = {}
resultado = 0
i = 0

while i < 3:
  nome = input("Digite o nome do aluno: ")
  nota = input("Digite a nota do aluno: ")
  dic[nome] = nota
  i += 1
for i in dic.values():
  resultado += int(i)

print(resultado)
