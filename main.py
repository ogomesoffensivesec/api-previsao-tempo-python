import weatherFunc 
import time
while True:
    op_menu = weatherFunc.menu()

    if op_menu == 1:
        weatherFunc.clear()
        weatherFunc.previsaoTempo()
    elif op_menu == 99:
        weatherFunc.panelLayout('Saindo do sistema...')
        time.sleep(1)
        break
    else:
        weatherFunc.clear()
        weatherFunc.panelLayout('[red]Opção Inválida[/]')
        time.sleep(2)
        