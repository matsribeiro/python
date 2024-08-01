class hp50g:
    def __init__(self):
        pass
    
    def receberFormula(self):
        formula = input("Digite a equacao a ser resolvida: ")
        return formula
    
    def operarFormula(self, equacao):
        equacao = equacao.replace(" ", "")
        partes = equacao.split('=')
        espressao = partes[1]
        for op in ['+', '-', '/', '*']:
            n = espressao.split(op)
            if len(n) > 1:
                operador = op
                break
        n1, n2 = hp50g.verificarNumero(self,n[0],n[1])
        resultado = hp50g.calcularEquacao(self, operador, n1, n2)
        return resultado
    
    def verificarNumero(self, n1, n2):
        n1 = int(n1)
        n2 = int(n2)
        return n1, n2
    
    def calcularEquacao(self, operador, n1, n2):
        expressao = f"{n1} {operador} {n2}"
        resultado = eval(expressao)
        return resultado
    
    def mostrarResultado(self,equacao,resultado):
        print(f'\n{equacao} = {resultado}')
        return

def main():
    formula = hp50g()
    equacao = formula.receberFormula()
    resultado = formula.operarFormula(equacao)
    formula.mostrarResultado(equacao,resultado)

if __name__ == "__main__":
    main()