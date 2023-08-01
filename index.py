from classes import *

tv = Televisor('L41N', 'SERIAL EXPERIMENTS LAIN')
controle = ControleRemoto(tv)

controle.sintonizaCanal('S7')
controle.trocaCanal('S7')

print(tv.canal_atual)

print(tv.lista_canais)