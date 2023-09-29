import PySimpleGUI as sg
from klasifikacijas import Raža, Ābols, procesa_dati, aprēķināt_kopējo_ābolu_svaru, aprēķināt_ievārījuma_daudzumu


sg.theme('DarkGray4')

saraksts = []

def izveidot_datus_par_uzskaiti(saraksts):
    dati = []
    for raža in saraksts:
        info = f"Nosaukums: {raža.nosaukums}, Suga: {raža.suga}, Daudzums: {raža.daudzums}kg"
        if isinstance(raža, Ābols):
            info += f", Šķirne: {raža.šķirne}"
        dati.append(info)
    return "\n".join(dati)


layout = [
    [sg.Text('Lūdzu, izpildi doto:')],
    [sg.Text('Kas tiek novākts?', size=(15,1)),
                            sg.Checkbox('Augļi', key='Augļi'),
                            sg.Checkbox('Dārzeņi', key='Dārzeņi')],
    [sg.Text('Daudzums:', size=(15,1)), sg.Spin([i for i in range(0,200)],
                                                       initial_value=0, key='Daudzums')],
    [sg.Text('Novāktais pēc sugas:', size=(15,1)), sg.InputText(key='Suga')],
    [sg.Text('Sķirna:', size=(15,1)),
                            sg.Checkbox('Zināma', key='Zināma šķ.'),
                            sg.Checkbox('Nezināma', key='Nezināma šķ.')],
    [sg.Text('Šķirnas nosaukums:', size=(15,1)), sg.InputText(key='Šķirna nosauk.')],
    [sg.Text('Ražas izmantošana:', size=(15,1)), sg.Combo(['Apēšanai', 'Glabāšanai', 'Ievārījumam'], key='Ražas izmantošana')],
    [sg.Text('Pārliecinaties, ka izpildijāt visu pareizi!')],
    [sg.Submit('Iesniegt'), sg.Button('Sākt no jauna'), sg.Button('Parādīt visus datus'), sg.Exit('Iziet')]

]

window = sg.Window('Ražas uzskaites programma', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Iziet':
        break
    elif event == 'Iesniegt':
        raža = procesa_dati(values)
        saraksts.append(raža)
        kopējie_āboli = aprēķināt_kopējo_ābolu_svaru(saraksts)
        ievārījuma_daudzums = aprēķināt_ievārījuma_daudzumu(kopējie_āboli)
        sg.popup(
            f"Pievienots:\n"
            f"Nosaukums: {raža.nosaukums}\n"
            f"Suga: {raža.suga}\n"
            f"Daudzums: {raža.daudzums}kg\n\n"
            f"Kopējais ābolu svars: {kopējie_āboli}kg\n"
            f"Ievārījuma daudzums: {ievārījuma_daudzums}kg"
        )
    elif event == 'Parādīt visus datus':
        uzskaites_dati = izveidot_datus_par_uzskaiti(saraksts)
        if uzskaites_dati:
            sg.popup_scrolled(uzskaites_dati, title="Uzskaites dati")
        else:
            sg.popup("Nav pievienots neviens ieraksts.")
    elif event == 'Sākt no jauna':
        saraksts = []
        window['Daudzums'].update(0)
        window['Suga'].update('')
        window['Šķirna nosauk.'].update('')
        for key in ['Augļi', 'Dārzeņi', 'Zināma šķ.', 'Nezināma šķ.']:
            window[key].update(False)
        print(values)

window.close()
