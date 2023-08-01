from classes import *
from functions import *

funcionario = Funcionario('Raphael', 'raphael.meireles@vetorian.com', 19)

funcionario.cadastro_hora('126', 'Julho') # cadastrando horas no mes de julho
funcionario.cadastro_hora('120', 'Junho')

funcionario.cadastro_salario_hora('Junho', 15)
funcionario.cadastro_salario_hora('Julho', 15)

infoFuncionario(funcionario)
calculaSalario(funcionario, 'Junho')

