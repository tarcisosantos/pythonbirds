class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=56):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass


if __name__ == '__main__':
    paulo = Homem(nome='Tarciso')
    renzo = Pessoa(nome='Renzo')
    luciano = Homem(paulo, renzo, nome='Luciano')

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
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), luciano.nome_e_atributo_de_classe())

    pesssoa = Pessoa('Anonimo')
    print(isinstance(pesssoa, Pessoa))
    print(isinstance(pesssoa, Homem))
    print(isinstance(paulo, Homem))
    print(isinstance(paulo, Pessoa))
