import re

# Texto de exemplo
texto = "Para mais informações, ligue para (11) 98765-4321 ou (21) 1234-5678. Você também pode entrar em contato pelo número 0800-123-4567."


# Expressão regular para celulares
padrao_telefone = r'(?:'r'(?:\(\d{2}\)|\d{2})'r'[\s-]*\d{4,5}[\s-]*\d{4}'r'|'r'0800(?:[-\s]\d+)+'r')'

# Extraindo telefones
telefones_encontrados = re.findall(padrao_telefone, texto)

# Exibindo os resultados
print("Telefones encontrados:")
for telefone in telefones_encontrados:
    print(telefone)



