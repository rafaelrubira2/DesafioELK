import random
import time
from faker import Faker

print ("======== Gerador de Log ========")
print ("====== Trabalho Final ELK ======")

fake = Faker('pt_BR')

dep_list =["TI", "Financeiro", "RH", "Marketing"]

log = open("app.log" , "w")

log.write ("nome;endereco;ocupacao;depto;email;salario\n")

while True:
  nome = fake.name()
  endereco = fake.address()
  ocupacao = fake.job()
  email = fake.email()
  salario = random.uniform(1302.00, 9999.99)
  depto = dep_list[random.randint(0,3)]
  print (nome,endereco,ocupacao,depto,email,salario)
  log_val = nome.strip()+";"+endereco.strip()+";"+ocupacao.strip()+";"+depto.strip()+";"+email.strip()+";"+str(salario).strip()
  log.write(log_val.replace("\n",","))
  log.write("\n")
  time.sleep(random.uniform(0.5,3))

log.close()
