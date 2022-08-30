from re import search, match, findall
print(match('.', 'abc'))

print(search('abc', 'sauhieuhaiuwqpwsjghcbfhvabcwiwq'))

print(findall('abc', 'oiaeaoiwyauiwabcopawjoaiwoawkdabcpaiowjaohwawkaabc'))

# Classes de caracteres

print(findall('[aeiou]', 'Fabio Faria'))

# fazer match com qualquer valor que NAO SEJA um dos caracteres especificos

print(findall('[^aeiou]', 'Fabio Faria'))

# Match com range

print(findall('[a-f]', 'Fabio Faria'))

print(findall('[a-fA-Z]', 'Fabio Faria'))

print(findall('[a-zA-F]', 'Fabio Faria'))

print(findall('[a-zA-Z0-9]', 'Fabio Faria'))

# Ou substituir a linha 24 por

print(findall('\w', 'Fabio Faria'))

# raw string
# usar o r' serve pra evitar de ficar adicionando \\ no inicio de cada caracter - sugestivo de usar sempre no pattern
text = '\\section\n'

print(match(r'\\section', text))

# Repetições
# Quantidades especificas
print(match(r'\d{4}', '1234'))

# Quantidades minimas

print(match(r'\d{2,}', '1234'))

# Pegar o minimo possivel

print(match(r'\d{2,}?', '1234'))

# Min max

print(match(r'\d{2,4}', '12345678'))
# usar ? para pegar o minimo, fazendo uma greedy search

# 0 ou 1 ocorrencia

print(match(r'\d??', '12345678')) # deixa preguicoso usando ??

print(match(r'\d?', '12345678')) # deixa ganancioso usando ?

# 0 ou mais vezes

print(match(r'\d*', '12345678')) # deixa ganancioso usando * preguicoso usando ?

# 1 ou mais vezes

print(match(r'\d+', '12345678')) # deixa ganancioso usando + preguicoso usando ? -- exige ao menos 1 ocrrencia


## Exemplo

teste = 'attr1="value1" attr2="value2"'

print(findall(r'".+?"', teste)) # me retorna apenas os values. importante utilizar o ? para fazer a busca



