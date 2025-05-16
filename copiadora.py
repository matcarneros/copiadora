# Mensagem de boas-vindas 

print("---------------------------------")
print("Bem-vindo(a) à Copiadora Digital!") 
print("---------------------------------")
print("-Desenvolvido por Matheus Santos-")
print("---------------------------------")

# Escolha o serviço

def escolha_servico():
    precos = {"DIG": 1.10, "ICO": 1.00, "IPB": 0.40, "FOT": 0.20}
    while True:
        servico = input("Escolha o serviço (DIG/ICO/IPB/FOT): ").upper()
        if servico in precos:
            return precos[servico], servico
        print("Serviço inválido. Tente novamente.")

# Calcular número de páginas com desconto


def num_pagina():
    while True:
        paginas = input("Digite o número de páginas: ")
        if paginas.isdigit():
            paginas = int(paginas)
            if paginas >= 20000:
                print("Quantidade de páginas não permitida.")
                continue
            elif paginas >= 2000:
                return paginas * 0.75, paginas
            elif paginas >= 200:
                return paginas * 0.80, paginas
            elif paginas >= 20:
                return paginas * 0.85, paginas
            return paginas, paginas
        print("Valor inválido. Digite um número inteiro.")

# Serviço extra


def servico_extra():
    precos_extra = {"1": 15, "2": 40, "0": 0}
    while True:
        opcao = input(
            "Escolha o serviço extra (1-Encadernação Simples 15R$, 2-Capa Dura 40R$, 0-Nenhum): ")
        if opcao in precos_extra:
            return precos_extra[opcao]
        print("Opção inválida. Tente novamente.")


# Final
servico_valor, servico_nome = escolha_servico()
n_pagina_valor, n_pagina_total = num_pagina()
extra = servico_extra()

subtotal = servico_valor * n_pagina_valor
total = subtotal + extra

print(f"Total: R$ {total:.2f} (serviço: {servico_valor:.2f} * páginas: {n_pagina_total} + extra: {extra:.2f})")
