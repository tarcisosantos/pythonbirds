class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=56):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    paulo = Pessoa(nome='Tarciso')
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(paulo, renzo, nome='Luciano')

    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(f'Nome: {luciano.nome}, tem {luciano.olhos} Olhos!')
    print(f'Nome: {renzo.nome}, tem {renzo.olhos} Olhos!')
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))










