from datetime import datetime

class Cliente:
    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, endereco, contato):
        self._nome = nome.title()
        self._sobrenome = sobrenome.title()
        self._data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
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

    def __str__(self):
        return f"Nome: {self.nome_completo()}\n" \
               f"Data de nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}\n" \
               f"CPF: {self.cpf}\n" \
               f"RG: {self.rg}\n" \
               f"Endereço: {self.endereco}\n" \
               f"Contato: {self.contato}\n"


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
        for apolice in self.apolices:
            premio_total += apolice.valor_premio
        return premio_total

    def __str__(self):
        return super().__str__() + f"Beneficiários: {self.beneficiarios}\n" \
                                   f"Apólices: {self.apolices}"


class Beneficiario(Cliente):
    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, tipo_benef, endereco, contato):
        super().__init__(nome, sobrenome, data_nascimento, cpf, rg, endereco, contato)
        self._tipo_benef = tipo_benef

    @property
    def tipo_benef(self):
        return self._tipo_benef

    def __repr__(self):
        return super().nome_completo()


class Apolice:
    def __init__(self, numero_apolice, tipo_apolice, valor_beneficio, valor_premio, inicio_vigencia, fim_vigencia, status):
        self._numero_apolice = numero_apolice
        self._tipo_apolice = tipo_apolice
        self._valor_beneficio = valor_beneficio
        self._valor_premio = valor_premio
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
    def valor_beneficio(self):
        return self._valor_beneficio

    @property
    def valor_premio(self):
        return self._valor_premio

    @property
    def inicio_vigencia(self):
        return self._inicio_vigencia

    @property
    def fim_vigencia(self):
        return self._fim_vigencia

    @property
    def status(self):
        return self._status

    def __repr__(self):
        return str(self.apolice)

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

    def __getitem__(self, item):
        return self.apolices[item]


class CalculadoraComissao:
    def __init__(self, apolices):
        self.apolices = apolices

    def calcula_comissao(self):
        comissao_total = 0
        for apolice in self.apolices:
            if apolice.tipo_apolice == 1:
                comissao = 0.005 * apolice.valor_premio + 100.0 + (1000.0 if apolice.valor_beneficio > 850000.0 else 0.0)
            elif apolice.tipo_apolice == 2:
                comissao = 75.5 + 0.0035 * apolice.valor_premio
            elif apolice.tipo_apolice == 3:
                comissao = 0.002 * apolice.valor_premio
            else:
                comissao = 200.0
            comissao_total += comissao
        return comissao_total

    def __str__(self):
        return f"{self.calcula_comissao()}"




# cliente1 = Cliente("josé", "da silva", "1980-01-01", 1234567890, 123456789, "Rua X, 999 / Apto 101", 999887785)
apolice1 = Apolice(1234, 1, 950000.00, 1000.00, "2020-07-01", "2050-06-30", 1)
apolice2 = Apolice(1235, 1, 53000, 1350.00, "2020-07-01", "2050-06-30", 1)
beneficiario1 = Beneficiario("giorgian", "de arrascaeta", "02/03/1994", 3456789012, 345678912, 1, "Rua Z, 777 / Apto 303", 964314975)
beneficiario2 = Beneficiario("gabriel", "barbosa", "05/11/1996", 4567890123, 456789123, 1, "Rua AA, 666 / Apto 404", 946546557)
segurado1 = Segurado("rafael", "rolli", "27/05/1990", 2345678901, 234567891, "Rua Y, 888 / Apto 202", 9756464643, [beneficiario1, beneficiario2], [apolice1, apolice2])
# print(segurado1)

corretor1 = Corretor("jorge", "sampaoli", 123456, [apolice1, apolice2], 998876452)
print(CalculadoraComissao(corretor1))
