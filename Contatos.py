
# Lista de contatos
contatos = []

# função para adicionar um novo contato
def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    favorito = False  # Começa como não favorito
    contato = {"nome": nome,"telefone": telefone,"email": email,"favorito": favorito}
    contatos.append(contato)
    print("Contato adicionado com sucesso!")

#Função para ver os contatos
def ver_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
    for i, contato in enumerate(contatos):
        print(f"{i + 1}. {contato['nome']} - {contato['telefone']} - {contato['email']}")
    
           
#Função para faviritar/ desfavoritar contato
def favoritar_contato():
    ver_contatos()
    indice = int(input("Digite o número do contato que seseja marcar/desmarcar")) -1
    if 0 <= indice < len(contatos):
        contatos[indice]["favorito"] = not contatos[indice]["favorito"]
        estado = "favorito" if contatos[indice]["favorito"] else "normal"
    print(f"Contato marcado como {estado}.")


# Função para editar um contato
def editar_contato():
    ver_contatos()
    try:
        indice = int(input("Digite o número do contato que deseja editar: ")) - 1
        if 0 <= indice < len(contatos):
            contatos[indice]["nome"] = input("Novo nome: ")
            contatos[indice]["telefone"] = input("Novo telefone: ")
            contatos[indice]["email"] = input("Novo email: ")
            print("Contato atualizado com sucesso!")
        else:
            print("Contato não encontrado.")
    except ValueError:
        print("Digite um número válido.")

#Função para deletar um contato
def apagar_contato():
    ver_contatos()
    indice = int(input("Digite o número do contato que deseja excluir: ")) - 1
    if 0 <= indice < len(contatos):
        excluido = contatos.pop(indice)
        print(f"Contatdo excluido")
        return
    
while True:
 print("\---nAgenda de contatos---")
 print("1. Adicionar contato")
 print("2. Ver lista de contatos")
 print("3. Ver lista de favoritos")
 print("4. Editar contatos")
 print("5. Marcar ou desmarcar favorito")
 print("6. Apagar um contato")
 print("7. sair")  
 escolha = input("Digite a sua escolha: ")

 if escolha =="1":
    adicionar_contato()
    
 elif escolha =="2":
    ver_contatos()

 elif escolha =="3":
    ver_favoritos()     

 elif escolha =="4":
    editar_contato()

 elif escolha =="5":
    favoritar_contato()

 elif escolha == "6":
    apagar_contato()
     
 elif escolha == "7":
    break
 
print("Fehando Programa")
