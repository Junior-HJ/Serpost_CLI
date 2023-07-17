import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Obtiene información de un envío de Serpost.')

        self.parser.add_argument('-t', type=str, required=True, help='Número de seguimiento a consultar.')
        
    def parse_args(self):
        return self.parser.parse_args()
