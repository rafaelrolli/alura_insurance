class Segurado:

    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, endereco, contato, beneficiarios, apolices):
        self.__nome = nome.title()
        self.__sobrenome = sobrenome.title()
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__rg = rg
        self.__endereco = endereco
        self.__contato = contato
        self.__beneficiarios = beneficiarios
        self.__apolices = apolices

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def cpf(self):
        return self.__cpf

    @property
    def rg(self):
        return self.__rg

    @property
    def endereco(self):
        return self.__endereco

    @property
    def contato(self):
        return self.__contato

    def nome_completo(self):
        return "{} {}".format(self.__cadastro.nome, self.__cadastro.sobrenome)

    def premio_total(self):
        premio_total = 0
        for apolice in self.__apolices:
            premio_total += apolice.valor_premio
        return premio_total

class Beneficiario:

    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, tipo_benef, endereco, contato):
        self.__nome = nome.title()
        self.__sobrenome = sobrenome.title()
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__rg = rg
        self.__tipo_benef = tipo_benef
        self.__endereco = endereco
        self.__contato = contato

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def cpf(self):
        return self.__cpf

    @property
    def rg(self):
        return self.__rg

    @property
    def tipo_benef(self):
        return self.__tipo_benef

    @property
    def endereco(self):
        return self.__endereco

    @property
    def contato(self):
        return self.__contato

class Apolice:
    def __init__(self, numero_apolice, tipo_apolice, valor_premio, segurado, corretor, inicio_vigencia, fim_vigencia, status):
        self.__numero_apolice = numero_apolice
        self.__tipo_apolice = tipo_apolice
        self.__valor_premio = valor_premio
        self.__segurado = segurado
        self.__corretor = corretor
        self.__inicio_vigencia = inicio_vigencia
        self.__fim_vigencia = fim_vigencia
        self.__status = status

    @property
    def apolice(self):
        return self.__numero_apolice

    @property
    def tipo_apolice(self):
        return self.__tipo_apolice

    @property
    def valor_premio(self):
        return self.__valor_premio

    @property
    def segurado(self):
        return self.__segurado

    @property
    def corretor(self):
        return self.__corretor

    @property
    def inicio_vigencia(self):
        return self.__inicio_vigencia

    @property
    def fim_vigencia(self):
        return self.__fim_vigencia

    @property
    def status(self):
        return self.__status

class Corretor:
    def __init__(self, nome, sobrenome, numero_susep, apolices, contato):
        self.__nome = nome.title()
        self.__sobrenome = sobrenome.title()
        self.__numero_susep = numero_susep
        self.__apolices = apolices
        self.__contato = contato

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def numero_susep(self):
        return self.__numero_susep

    @property
    def apolices(self):
        return self.__apolices

    @property
    def contato(self):
        return self.__contato

    def comissao_total(self):
        comissao_total = 0
        for apolice in self.__apolices:
            comissao_total += (apolice.valor_premio * 0.01)
        return comissao_total