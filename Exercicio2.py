class Nodo:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None for _ in range(10)]

    def funcao_hash(self, sigla):
        sigla = sigla.upper()
        if sigla == "DF":
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10

    def inserir(self, sigla, nome_estado):
        pos = self.funcao_hash(sigla)
        novo = Nodo(sigla, nome_estado)
        novo.proximo = self.tabela[pos]
        self.tabela[pos] = novo

    def imprimir(self):
        for i in range(10):
            print(f"{i}:", end=" ")
            atual = self.tabela[i]
            while atual:
                print(f"{atual.sigla}->", end="")
                atual = atual.proximo
            print("None")

# Lista de todos os estados + DF
estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"),
    ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
    ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
    ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"),
    ("SE", "Sergipe"), ("TO", "Tocantins")
]

# Estado fictício
estado_ficticio = ("PL", "Piettro Lino Lorenzon")

tabela = TabelaHash()

# Impressão antes de qualquer inserção
print("Figura 1: Impressão da tabela hash antes de inserir qualquer informação")
tabela.imprimir()

# Inserção dos 26 estados + DF
for sigla, nome in estados:
    tabela.inserir(sigla, nome)

# Impressão após inserir estados e DF
print("\nFigura 2: Impressão da tabela hash após inserir os 26 estados e o Distrito Federal")
tabela.imprimir()

# Inserção do estado fictício
tabela.inserir(*estado_ficticio)

# Impressão após inserir estado fictício
print("\nFigura 3: Impressão da tabela hash após inserir os 26 estados, o Distrito Federal e o estado fictício")
tabela.imprimir()
