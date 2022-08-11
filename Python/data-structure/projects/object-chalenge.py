class alunos:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
      self.media = (self.nota1 + self.nota2) / 2
      return self.media

    def aprovado(self):
      media = (self.nota1 * self.nota2)  / 2
      if ((self.nota1 * self.nota2) / 2) >= 6:
        return "Aprovado"
      else:
        return "Reprovado"

    def mostra(self):
      print(self.nome)
      print(self.nota1)
      print(self.nota2)

a1 = alunos("Moises", 10, 7)
a2 = alunos("Cleber", 4, 2)


print(a1.media())
print(a1.aprovado())
print(a1.mostra())
