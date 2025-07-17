import os
import sys
from datetime import datetime

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    final_path = os.path.join(base_path, relative_path)
    return final_path

def mes_atual():
    return datetime.now().month

meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }

def mes_pt(mes):
    return meses.get(mes)

def mes_inv(mes):
    inv = {e: n for n, e in meses.items()}
    return inv.get(mes)

def meses_pt(meses_nums):
    return [meses.get(m) for m in meses_nums]

def dia_semana(dia_da_semana):
    dias = {
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sábado",
        6: "Domingo"
    }
    
    return dias.get(dia_da_semana)