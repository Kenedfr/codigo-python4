from calculadora import Calculadora

calc = Calculadora(valorA=10, valorB=5, operacao='+')
calc.mostrarResultado()

calc.operacao = '-'
calc.mostrarResultado()

calc.operacao = '*'
calc.mostrarResultado()

calc.operacao = '/'
calc.mostrarResultado()

calc.operacao = '%'
calc.mostrarResultado()

calc.valorB = 0
calc.operacao = '/'
calc.mostrarResultado()
