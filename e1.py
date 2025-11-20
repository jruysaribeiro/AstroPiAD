# Function to add names to a list

# Main program
print("\n--- App de Nomes ---")
print("Por favor, insira cinco nomes:\n")

# Get user input for five names
nome1 = input("Nome 1: ")
nome2 = input("Nome 2: ")
nome3 = input("Nome 3: ")
nome4 = input("Nome 4: ")
nome5 = input("Nome 5: ")

lista_nomes = [nome1, nome2, nome3, nome4, nome5]

# Add names to list using the function
# lista = adicionar_nomes_lista(nome1, nome2, nome3, nome4, nome5)

# Print each name using a loop
print("\n--- Lista de Nomes ---")
for nome in lista_nomes:
    print(f"- {nome} é a mais recente aquisição da equipa ESA AstroPi!")

