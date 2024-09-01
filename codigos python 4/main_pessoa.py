from Pessoas import Pessoa
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

pessoa = Pessoa("João", "12345-6", "2024-01-01", status=True)
pessoa.imprimir_informacoes()

print("\n")

pessoa_fisica = PessoaFisica("Ana", "98765-4", "2023-12-01", status=True, dataNascimento="2000-01-01", cpf="000.111.222-33", rg="15975388-1")
pessoa_fisica.imprimir_informacoes()

print("\n")

pessoa_juridica = PessoaJuridica("Empresa XYZ", "54321-0", "2022-11-01", status=True, dataAberturaEmpresa="2020-05-15", cnpj="12.345.678/0001-00")
pessoa_juridica.imprimir_informacoes()

pessoa.nome = "João Silva"
pessoa.imprimir_informacoes()

print("\n")

pessoa_fisica.cpf = "123.456.789-00"
pessoa_fisica.imprimir_informacoes()

print("\n")

try:
    pessoa_juridica.cnpj = "12.345.678/0001-0"  
except ValueError as e:
    print(f"Erro: {e}")

pessoa_juridica.cnpj = "98.765.432/0001-99" 
pessoa_juridica.imprimir_informacoes()