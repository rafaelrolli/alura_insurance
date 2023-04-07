class Segurado:

    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, endereco, contato, beneficiarios):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__rg = rg
        self.__endereco = endereco
        self.__contato = contato
        self.__beneficiarios = beneficiarios

    def nome_completo(self):
        return "{} {}".format(self.__nome, self.__sobrenome)

class Beneficiario:

    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, tipo_benef, endereco, contato):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__rg = rg
        self.__tipo_benef = tipo_benef
        self.__endereco = endereco
        self.__contato = contato

class Apolice:
    def __init__(self, apolice, tipo_apolice, valor_premio, segurado, corretor, inicio_vigencia, fim_vigencia, status):
        self.__apolice = apolice
        self.__tipo_apolice = tipo_apolice
        self.__valor_premio = valor_premio
        self.__segurado = segurado
        self.__corretor = corretor
        self.__inicio_vigencia = inicio_vigencia
        self.__fim_vigencia = fim_vigencia
        self.__status = status

class Corretor:
    def __init__(self, nome, sobrenome, numero_susep, apolices, contato):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__numero_susep = numero_susep
        self.__apolices = apolices
        self.__contato = contato