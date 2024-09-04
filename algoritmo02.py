
#algoritmo02

def contar_letra_a(str):

    str = str.lower()
    
    quantidade = str.count('a')
    
    return quantidade

str = input("Digite uma string para verificar a quantidade de vezes que a letra 'a' (maiúscula ou minúscula) aparece: ")

quantidade = contar_letra_a(str)

print(f"A letra 'a' aparece {quantidade} vez(es) na string.")
