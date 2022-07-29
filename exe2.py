resp=""
texto =  input("informe uma frase: ")
cont=0
for carac in texto:
      if carac==" ":
        if ord(texto[cont+1])>==97 and ord(texto[cont+1])<=122:
           novo cod=ord(carac) +32
           novo carac=chr(novo cod)
           resp=resp+novo carac
      else:
        resp=resp+carac
    cont=cont+1
print(resp)    
