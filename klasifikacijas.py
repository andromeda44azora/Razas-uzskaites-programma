class Raža:
    def __init__(self, nosaukums, tips, daudzums, suga):
        self.nosaukums = nosaukums
        self.tips = tips
        self.daudzums = daudzums
        self.suga = suga

class Ābols(Raža):
    def __init__(self, daudzums, suga, šķirne):
        super().__init__("Ābols", "auglis", daudzums, suga)
        self.šķirne = šķirne

def procesa_dati(data):
    if data['Augļi']:
        if data['Suga'] == 'Ābols':
            return Ābols(data['Daudzums'], data['Suga'], data['Šķirna nosauk.'] if data['Zināma šķ.'] else 'Nezināma')
        else:
            return Raža(data['Suga'], 'auglis', data['Daudzums'], data['Suga'])
    elif data['Dārzeņi']:
        return Raža(data['Suga'], 'dārzenis', data['Daudzums'], data['Suga'])

def aprēķināt_kopējo_ābolu_svaru(saraksts):
    kopējais_svars = 0
    for ieraksts in saraksts:
        if isinstance(ieraksts, Ābols):
            kopējais_svars += ieraksts.daudzums
    return kopējais_svars


def aprēķināt_ievārījuma_daudzumu(ābolu_svars):
    return ābolu_svars / 2