n = input('digite algo: ')
print('é um número?',n.isnumeric()) #numerico
print('é alfabético?' ,n.isalpha()) #alfabeto
print('é alfabeto e numérico?',n.isalnum()) #alfabeto e numerico
print('todas as letras estão maiúsculas?',n.isupper()) #ver se TODOS estão com letras maiusculas
print('todas as letras estão minusculas?',n.islower()) #ver se TODOS estão em minisculo
print('é um número que pode ser impresso?',n.isprintable()) #ver se ele pode ser impresso
print('ele tem espaço?',n.isspace()) #ver se é um espaço (com nada)
print('Possui a primeira palavra maiúscula e o restante minúsculas?',n.istitle())
print('Possui letras ou números?', n.isalnum())
print('Possui números de 0 a 9?', n.isdecimal())
