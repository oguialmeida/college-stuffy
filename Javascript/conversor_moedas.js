function moeda() {
    var dolar = 5.26
    while (true) {
        try {
            var escolha = prompt('\nEscolha a moeda para ser convertida. \n 1 - Dolar; \n 2 - Real; \n 0 - Sair')
            if (escolha === '1') {
                const quantia = prompt('\n Digite quantos Dolares quer converter para Real (favor utilizar . para separar casas decimais)')
                quantiaFloat = parseFloat(quantia)
                if (isNaN(quantiaFloat)) {
                    window.alert("Tipo incorreto de dados, tente novamente!")
                }
                else {
                    let vreal = quantia / dolar
                    window.alert('\n USD$' + vreal.toFixed(2))
                }
            }
            else if (escolha === '2') {
                const quantia = prompt('\n Digite quantos Reais quer converter para Dolar (favor utilizar . para separar casas decimais)')
                quantiaFloat = parseFloat(quantia)
                if (isNaN(quantiaFloat)) {
                    window.alert("Tipo incorreto de dados, tente novamente!")
                }
                else {
                    let vdolar = quantia * dolar
                    window.alert('\n USD$' + vdolar.toFixed(2))
                }
            }
            else if (escolha === '0') break
            else { window.alert('\n Não compreendi, poderia repetir?') }
        }
        catch (e) { window.alert('\n Não compreendi, poderia repetir?') }
    }
}
moeda()
