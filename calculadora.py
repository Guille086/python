class Calculadora:
    primer_numero, segundo_numero, resultado = None, None, None

    def __init__(self,p,s): #constructor
        self.primer_numero = p
        self.segundo_numero = s

    def sumar(self):
        self.resultado = self.primer_numero + self.segundo_numero

    def restar(self):
        self.resultado = self.primer_numero - self.segundo_numero

    def multiplicar(self):
        self.resultado = self.primer_numero * self.segundo_numero

    def dividir(self):
        if(self.segundo_numero != 0):

            self.resultado = self.primer_numero / self.segundo_numero
        else:
            self.resultado = "División por cero"

    def get_resultado(self):
        return self.resultado
    
casio = Calculadora(33,80)
casio.sumar()
print(casio.get_resultado())