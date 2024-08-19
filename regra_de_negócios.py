def esolher_operação():
    while True:
        operação_selecionada = input(
            "escolha uma das operações matématicas asseguir:(  +  -  x  / ):"
        )

        if operação_selecionada not in ["+", "-", "x", "/"]:
            print("Erro: A operação selecionada é ínvalida. tente novamente.")
        else:
            return operação_selecionada



