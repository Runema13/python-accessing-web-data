import re

# Texto de exemplo
texto = "Olá, você pode entrar em contato comigo pelo e-mail joao.silva@example.com ou pelo suporte em contato@empresa.com. Também temos um e-mail alternativo: info@empresa.com.br."

# Expressão regular para e-mails
padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Extraindo e-mails
emails_encontrados = re.findall(padrao_email, texto)

# Exibindo os resultados
print("Endereços de e-mail encontrados:")
for email in emails_encontrados:
    print(email)



