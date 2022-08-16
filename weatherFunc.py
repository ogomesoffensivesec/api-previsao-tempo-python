import traceback
from datetime import date
from itertools import count
from rich.console import Console
from rich.table import Table
from rich import print
import time
import os
from rich.progress import track
from collections.abc import MutableMapping
import requests
from rich.padding import Padding
from rich.panel import Panel
data = date.today()
console = Console()
def clear(): return os.system('cls')


def panelLayout(text):
    return console.print(Panel(Padding(f'''{text}''', 1), title=f"[red] Ferramenta de Previsão no Tempo [/] {data}"))


def menu():  # Menu Principal
    while True:
        clear()
        console.print(Panel(Padding('''1 - Previsão do tempo
99 - Sair

Obs.: Somente a insersão de [yellow]NÚMEROS INTEIROS[/] são permitidos!

Escola uma opção''', 1), title=f"[red] Ferramenta de Previsão no Tempo [/] {data}"))
        try:
            #console.print(Panel(Padding((), 1), title="[red] Ferramenta de Previsão no Tempo [/] {data}"))
            imenu = int(input('Opção:  '))
            clear()
            return imenu
            break
        except ValueError:
            itext = 'Insira um número inteiro válido'
            clear()
            #console.print(Panel(Padding(f'{text}' , 1), title="[red] Ferramenta de Previsão no Tempo [/] {data}"))
            panelLayout('Digite um número [green]inteiro válido [/]')
            time.sleep(1)

        except KeyboardInterrupt:
            clear()
            #console.print('PARA SAIR DIGITE [red]"SAIR"[/]')
            panelLayout('Para sair, basta digitar "99"')
            time.sleep(1)


def previsaoTempo():  # Pesquisa se o nome do LOCAL EXISTE e retorna a sua TEMPERATURAe uma BREVE DESCRIÇÃO!
    while True:
        panelLayout('Digite o seu Estado, Cidade ou País')
        city = input('Digite: ')
        clear()

        if len(city) >= 4:
            try:
                # link do open_weather: https://openweathermap.org/
                API_KEY = "826fd8ffa8fb980079864f3644d3e75b"
                link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br"
                requisicao = requests.get(link)
                requisicao_dic = requisicao.json()
                descricao = requisicao_dic['weather'][0]['description']
                temperatura = requisicao_dic['main']['temp'] - 273.15
                temperaturafinal = round(temperatura, 3)
                #console.print(f'{descricao.title()} - {temperaturafinal}º')
                # console.print(f'''Está [blue]{descricao.title()}[/] em {city}.
            # A temperatura atual é [blue]{temperaturafinal}º[/]''')
                panelLayout(
                    f'[green]Carregando informações sobre o clima de {city} hoje...[/]')
                for procurarclima in track(range(5),):
                    time.sleep(2)
                clear()
                panelLayout(f'''Está [blue]{descricao.title()}[/] em {city}.
A temperatura atual é [blue]{temperaturafinal}ºC[/]''')
                input('Tecle para voltar ao Menu Principal')
                clear()
                break
            except Exception as e:
                clear()
                panelLayout(
                    '[red] ERRO NA DIGITAÇÃO DO LOCAL![/] [red on black] TENTE NOVAMENTE[/]')
                time.sleep(3)
                clear()
        else:
            panelLayout('[red] SIGLAS NÃO SÃO PERMITIDAS[/]')
            time.sleep(2)
            clear()


# def coletarGeoLoc(cidade):
#   loc = Nominatim(user_agent='GetLoc')
#    getLoc = loc.geocode(cidade)
#
#    getLat = getLoc.latitude
#    getLon =  getLoc.longitude
#   return getLat,getLon
