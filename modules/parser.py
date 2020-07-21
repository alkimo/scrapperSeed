import argparse
import time
import os

def initParse():
    # Initiate the parser
    parser = argparse.ArgumentParser()

    # Link da pesquisa do facebook ads
    parser.add_argument("-url", help="Url do ad do facebook")

    # Nome do browser a ser usado
    parser.add_argument("-b", help="Browser a ser utilizado: Chrome ou Firefox")

    # Nome da pasta para salvar os dados
    parser.add_argument("-n", help="Nome da pasta a ser salvo os dados")

    # Read arguments from the command line
    args = parser.parse_args()

    if(args.url == None):
        args.url = "https://www.google.com"

    if(args.b == None):
        args.b = "Chrome"

    if(args.n == None):
        args.n = os.path.basename(args.url)
        # args.n = time.strftime("%Y%m%d-%H%M%S")

    return args