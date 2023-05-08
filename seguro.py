class Cliente:
    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, endereco, contato):
        self._nome = nome.title()
        self._sobrenome = sobrenome.title()
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._rg = rg
        self._endereco = endereco
        self._contato = contato

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def rg(self):
        return self._rg

    @property
    def endereco(self):
        return self._endereco

    @property
    def contato(self):
        return self._contato

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"


class Segurado(Cliente):
    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, endereco, contato, beneficiarios, apolices):
        super().__init__(nome, sobrenome, data_nascimento, cpf, rg, endereco, contato)
        self._beneficiarios = beneficiarios
        self._apolices = apolices

    @property
    def beneficiarios(self):
        return self._beneficiarios

    @property
    def apolices(self):
        return self._apolices

    def premio_total(self):
        premio_total = 0
        for apolice in self._apolices:
            premio_total += apolice.valor_premio
        return premio_total


class Beneficiario(Cliente):
    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, tipo_benef, endereco, contato):
        super().__init__(nome, sobrenome, data_nascimento, cpf, rg, endereco, contato)
        self._tipo_benef = tipo_benef

    @property
    def tipo_benef(self):
        return self._tipo_benef


class Apolice:
    def __init__(self, numero_apolice, tipo_apolice, valor_premio, segurado, corretor, inicio_vigencia, fim_vigencia, status):
        self._numero_apolice = numero_apolice
        self._tipo_apolice = tipo_apolice
        self._valor_premio = valor_premio
        self._segurado = segurado
        self._corretor = corretor
        self._inicio_vigencia = inicio_vigencia
        self._fim_vigencia = fim_vigencia
        self._status = status

    @property
    def apolice(self):
        return self._numero_apolice

    @property
    def tipo_apolice(self):
        return self._tipo_apolice

    @property
    def valor_premio(self):
        return self._valor_premio

    @property
    def segurado(self):
        return self._segurado

    @property
    def corretor(self):
        return self._corretor

    @property
    def inicio_vigencia(self):
        return self._inicio_vigencia

    @property
    def fim_vigencia(self):
        return self._fim_vigencia

    @property
    def status(self):
        return self._status

class Corretor:
    def __init__(self, nome, sobrenome, numero_susep, apolices, contato):
        self._nome = nome.title()
        self._sobrenome = sobrenome.title()
        self._numero_susep = numero_susep
        self._apolices = apolices
        self._contato = contato

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def numero_susep(self):
        return self._numero_susep

    @property
    def apolices(self):
        return self._apolices

    @property
    def contato(self):
        return self._contato

    def comissao_total(self):
        comissao_total = 0
        for apolice in self._apolices:
            comissao_total += (apolice.valor_premio * 0.01)
        return comissao_total


cliente1 = Cliente("josé", "da silva", "1980-01-01", 1234567890, 123456789, 5521999887785)
segurado1 = Segurado("rafael", "rolli", 1, 2, 3, 4, 5, 6, (7, 8, 9))
print(cliente1.apolices)