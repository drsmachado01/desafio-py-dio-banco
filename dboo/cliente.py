from pessoa_fisica import PessoaFisica

class Cliente(PessoaFisica):
    endereco = ""
    contas = []

    def realizar_transacao(self, conta, transacao):
        pass


    def adicionar_conta(self, conta):
        # TODO inserir validacao
        self.contas.append(conta)