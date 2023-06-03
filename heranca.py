class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5
    
    def acelerar(self):
        print('acelerando...')
    
    def frear(self):
        print('freando...')
    
    def buzinar(self):
        print('Buzinando...')
        
class Uno(Carro):
    modelo = 'Uno'
    marca = 'fiat'
    ano = 1992
    numero_rodas = 4
    quantidade_passageiros = 5
    
uno = Uno()
uno.acelerar()
uno.buzinar()
uno.frear()
    