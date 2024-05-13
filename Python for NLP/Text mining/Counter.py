with open('output.txt') as f:
    text = f.read()

Counter_S = 0
Counter_S_nom = 0
Counter_S_gen = 0
Counter_S_dat = 0
Counter_S_acc = 0
Counter_S_ins = 0
Counter_S_abl = 0
Counter_S_sg = 0
Counter_S_pl = 0
Counter_S_m = 0
Counter_S_f = 0
Counter_S_n = 0
Counter_A = 0
Counter_ADV = 0
Counter_PR = 0
Counter_APRO = 0
Counter_ADVPRO = 0
Counter_ANUM = 0
Counter_CONJ = 0
Counter_INTJ = 0
Counter_NUM = 0
Counter_PART = 0
Counter_V = 0
Counter_SPRO = 0

for i in range(len(text)):
    if "SPRO" in text[i]:
        Counter_SPRO += 1
    elif "S" in text[i]:
        if "��" in text[i]:
            Counter_S_nom += 1
        elif "���" in text[i]:
            Counter_S_gen += 1
        elif "���" in text[i]:
            Counter_S_dat += 1
        elif "���" in text[i]:
            Counter_S_acc += 1
        elif "����" in text[i]:
            Counter_S_ins += 1
        elif "��" in text[i]:
            Counter_S_abl += 1
        if "��" in text[i]:
            Counter_S_sg += 1
        elif "��" in text[i]:
            Counter_S_pl += 1
        if "���" in text[i]:
            Counter_S_m += 1
        elif "���" in text[i]:
            Counter_S_f += 1
        elif "����" in text[i]:
            Counter_S_n += 1
        Counter_S += 1
    elif "PART" in text[i]:
        Counter_PART += 1
    elif "ADVPRO" in text[i]:
        Counter_ADVPRO += 1
    elif "ADV" in text[i]:
        Counter_ADV += 1
    elif "APRO" in text[i]:
        Counter_APRO += 1
    elif "ANUM" in text[i]:
        Counter_ANUM += 1
    elif "A" in text[i]:
        Counter_A += 1
    elif "PR" in text[i]:
        Counter_PR += 1
    elif "CONJ" in text[i]:
        Counter_CONJ += 1
    elif "INTJ" in text[i]:
        Counter_INTJ += 1
    elif "NUM" in text[i]:
        Counter_NUM += 1
    elif "V" in text[i]:
        Counter_V += 1


print(f"����� � ����� ������������: ��������������� - {Counter_S}, ����� �������:\n"
      f"    � ������������ ������ - {Counter_S_nom}({round(Counter_S_nom/Counter_S, 2)}%);\n"
      f"    � ����������� ������ - {Counter_S_gen}({round(Counter_S_gen/Counter_S, 2)}%);\n"
      f"    � ��������� ������ - {Counter_S_dat}({round(Counter_S_dat/Counter_S, 2)}%);\n"
      f"    � ����������� ������ - {Counter_S_acc}({round(Counter_S_acc/Counter_S, 2)}%);\n"
      f"    � ������������ ������ - {Counter_S_ins}({round(Counter_S_ins/Counter_S, 2)}%);\n"
      f"    � ���������� ������ - {Counter_S_abl}({round(Counter_S_abl/Counter_S, 2)}%);\n"
      f"    � ������������ ����� - {Counter_S_sg}({round(Counter_S_sg/Counter_S, 2)}%);\n"
      f"    �� ������������� ����� - {Counter_S_pl}({round(Counter_S_pl/Counter_S, 2)}%);\n"
      f"    � ������� ���� - {Counter_S_m}({round(Counter_S_m/Counter_S, 2)}%);\n"
      f"    � ������� ���� - {Counter_S_f}({round(Counter_S_f/Counter_S, 2)}%);\n"
      f"    � ������� ���� - {Counter_S_n}({round(Counter_S_n/Counter_S, 2)}%);\n"
      f"�������������� - {Counter_A};\n"
      f"������� - {Counter_ADV};\n"
      f"��������� - {Counter_PR};\n"
      f"�����������-�������������� - {Counter_APRO};\n"
      f"�����������-��������������� - {Counter_SPRO};\n"
      f"������������ ������� - {Counter_ADVPRO};\n"
      f"������������-�������������� - {Counter_ANUM};\n"
      f"������ - {Counter_CONJ};\n"
      f"���������� - {Counter_INTJ};\n"
      f"������������ - {Counter_NUM};\n"
      f"������ - {Counter_PART};\n"
      f"�������� - {Counter_V}.")
