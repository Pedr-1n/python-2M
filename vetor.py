tam = 5

vet = [0] * tam

for i in range (0, tam):

   vet[i] = int(input("Digite os valores para o vetor: "))  

maior = max(vet)

menor = min(vet)

print("O menor valor do vetor é: ", menor)

print("O maior valor do vetor é: ", maior)