from mysql import connector
import git

mydb = connector.connect(
  host="localhost",
  user="root",
  passwd="Messias10"
)

print(mydb)

list = []
#Configurando o ponteiro
mycursor = mydb.cursor()

num = 1
while num == 1:
  #Listando os bancos de dados cadastrados
  mycursor.execute("SHOW DATABASES")
  databases = mycursor.fetchall()
  #Mostrando e adicionando nomes, na lista para comparação
  for x in databases:
    print(x)
    list.append(x)

  #Recebendo dado de usuário
  nome = input("Digite um nome: ")

  #Comparando o nome desejado com o nome existente
  val = False
  for j in list:
    if nome in j:
      val = True

  #Verificando se pode realizar criar o banco ou não
  if val == True:
    print("\nO nome digitado ja existe. Por favor tente novamente\n")
  else:
    createbase = """CREATE DATABASE """ + nome
    mycursor.execute(createbase)
    print("Banco de Dados criado com sucesso!!")

  num = int(input("\nDigite 1 para inserir um novo banco ou 0 para sair: \n"))


git.Git('/home/nathan/Documentos').clone('https://github.com/NathanMessias/teste.git')
repo = git.Repo('/home/nathan/Documentos/teste')
o = repo.remotes.origin
o.pull()


print("Obrigado por me usar!")
