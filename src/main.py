import math
import sys


print("FarmTech Solutions funcionando!")
print("Olá, fazendeiro\n")
nome = input("Qual o seu nome? ")
print("Bem-vindo,", nome)
cultura = "Cana-de-açúcar"   # guarda texto (str)
area = 1500.0                 # guarda número decimal (float)
ruas = 80                     # guarda número inteiro (int)

print(cultura)  # mostra: Cana-de-açúcar
print(area)     # mostra: 1500.0
print(ruas)     # mostra: 80

# Criar lista vazia
nomes = []

# Adicionar item
nomes.append("Talhão A")
nomes.append("Talhão B")

# Ver todos
print(nomes)         # ['Talhão A', 'Talhão B']

# Ver por posição (começa do 0!)
print(nomes[0])      # Talhão A
print(nomes[1])      # Talhão B

# Atualizar uma posição
nomes[0] = "Talhão C"

# Deletar uma posição
nomes.pop(0)

opcao = input("Digite 1 para Cana ou 2 para Laranja: ")

if opcao == "1":
    print("Você escolheu Cana-de-açúcar")
elif opcao == "2":
    print("Você escolheu Laranja")
else:
    print("Opção inválida!")
    
    import math, sys

# ── Vetores ──────────────────────────────────────────────
nomes    = []
culturas = []
areas    = []
insumos  = []
qtds     = []
ruas     = []

# ── Cálculo de área ──────────────────────────────────────
def calc_area(cultura):
    if cultura == "1":  # Cana → Retângulo
        c = float(input("  Comprimento (m): "))
        l = float(input("  Largura (m): "))
        return round(c * l, 2), c
    else:               # Laranja → Elipse
        a = float(input("  Semi-eixo maior (m): "))
        b = float(input("  Semi-eixo menor (m): "))
        return round(math.pi * a * b, 2), a

# ── Cálculo de insumo ────────────────────────────────────
def calc_insumo(comp_rua):
    nome   = input("  Nome do insumo (ex: herbicida): ")
    dose   = float(input("  Dose (mL por metro): "))
    n_ruas = int(input("  Número de ruas: "))
    total  = (dose * comp_rua * n_ruas) / 1000  # converte para litros
    return nome, round(total, 2), n_ruas

# ── CRUD ─────────────────────────────────────────────────
def cadastrar():
    print("\n── Cadastro ──")
    nome = input("  Nome do talhão: ")
    print("  Cultura: 1-Cana  2-Laranja")
    c = input("  Escolha: ")
    cultura = "Cana-de-açúcar" if c == "1" else "Laranja"
    area, comp = calc_area(c)
    ins, qtd, n = calc_insumo(comp)

    nomes.append(nome); culturas.append(cultura)
    areas.append(area); insumos.append(ins)
    qtds.append(qtd);   ruas.append(n)
    print(f"\n  ✔ Área: {area} m²  |  Insumo: {qtd} L de {ins}")

def exibir():
    if not nomes:
        print("\n  Nenhum registro."); return
    print(f"\n{'#':<4}{'Talhão':<15}{'Cultura':<18}{'Área(m²)':<12}"
          f"{'Insumo':<15}{'Qtd(L)':<10}{'Ruas'}")
    print("─"*74)
    for i in range(len(nomes)):
        print(f"{i:<4}{nomes[i]:<15}{culturas[i]:<18}{areas[i]:<12}"
              f"{insumos[i]:<15}{qtds[i]:<10}{ruas[i]}")

def atualizar():
    exibir()
    if not nomes: return
    i = int(input("\n  Índice a atualizar: "))
    print("  Recadastrando posição", i)
    nomes[i] = input("  Novo nome: ")
    print("  1-Cana  2-Laranja")
    c = input("  Cultura: ")
    culturas[i] = "Cana-de-açúcar" if c == "1" else "Laranja"
    areas[i], comp = calc_area(c)
    insumos[i], qtds[i], ruas[i] = calc_insumo(comp)
    print("  ✔ Registro atualizado.")

def deletar():
    exibir()
    if not nomes: return
    i = int(input("\n  Índice a deletar: "))
    for v in [nomes, culturas, areas, insumos, qtds, ruas]:
        v.pop(i)
    print("  ✔ Registro removido.")

# ── Menu ─────────────────────────────────────────────────
def menu():
    opcoes = {"1": cadastrar, "2": exibir,
              "3": atualizar, "4": deletar}
    while True:
        print("""
╔══════════════════════════════════╗
║     FarmTech Solutions 🌾        ║
╠══════════════════════════════════╣
║  1. Cadastrar nova área          ║
║  2. Exibir registros             ║
║  3. Atualizar registro           ║
║  4. Deletar registro             ║
║  5. Sair                         ║
╚══════════════════════════════════╝""")
        op = input("  Opção: ").strip()
        if op == "5":
            print("  Encerrando... Até logo! 👋")
            sys.exit()
        elif op in opcoes:
            opcoes[op]()
        else:
            print("  Opção inválida.")

if __name__ == "__main__":
    menu()
    


