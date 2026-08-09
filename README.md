# Estruturas de Dados em Python 🧬

Repositório contendo a implementação prática de estruturas de dados clássicas desenvolvidas em Python para fins acadêmicos.

---

## 📄 Arquivos do Projeto

### 1. `Exercicio1.py` — Fila de Atendimento com Prioridade
* **Estrutura:** Lista Encadeada Simples (`ListaEncadeada` e `Nodo`).
* **Funcionamento:** Sistema interativo via terminal que gerencia uma fila de espera. 
* **Regra de Negócio:** Insere cartões prioritários (Amarelos `A`) no início da fila respeitando a ordem de chegada entre eles, e cartões sem prioridade (Verdes `V`) ao final da fila.

---

### 2. `Exercicio2.py` — Tabela Hash de Estados Brasileiros
* **Estrutura:** Tabela Hash (`TabelaHash`) com tratamento de colisões por encadeamento exterior (*Separate Chaining*).
* **Funcionamento:** Mapeia a sigla dos 26 estados brasileiros + DF (e um estado fictício) em uma tabela de 10 posições.
* **Regra de Negócio:** Aplica uma função hash baseada na soma da tabela ASCII das siglas (com exceção do `DF`, direcionado para a posição 7). Mostra a tabela antes e depois do preenchimento.

---

## 🚀 Como Executar

Abra o terminal na pasta do projeto e rode o arquivo desejado:

```bash
# Para o sistema de fila de atendimento:
python Exercicio1.py

# Para a visualização da Tabela Hash:
python Exercicio2.py
