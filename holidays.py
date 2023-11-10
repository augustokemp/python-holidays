from dateutil.easter import easter
from dateutil.relativedelta import relativedelta
from datetime import date

class MyConfig:

    @property
    def DATE_NOW(self):
        return date.now()

    @property
    def FERIADOS_NACIONAIS(self):
        """
        Dict de feriados.
        Chave: date, Value: str
        """
        current_year = self.DATE_NOW.year
    
        # Feriados em datas fixas
        datas = [
            (1, 1, "Ano Novo"),
            (4, 21, "Dia de Tiradentes"),
            (5, 1, "Dia do Trabalhador"),
            (7, 20, "Aniversário de Balneário Camboriú"),
            (9, 7, "Independência do Brasil"),
            (10, 12, "Nossa Senhora Aparecida"),
            (11, 2, "Dia de Finados"),
            (11, 15, "Proclamação da República"),
            (12, 25, "Natal"),
        ]
        feriados = {}
    
        for y in [current_year - 1, current_year, current_year + 1]:
    
            data_pascoa = easter(y)
    
            # Feriados em datas móveis
            feriados[data_pascoa] = "Páscoa"
            feriados[data_pascoa - relativedelta(days=2)] = "Sexta-feira Santa"
            feriados[data_pascoa - relativedelta(days=47)] = "Carnaval"
            feriados[data_pascoa + relativedelta(days=60)] = "Corpus Christi"
    
            # Feriados em datas fixas
            for d in datas:
                feriados[date(y, d[0], d[1])] = d[2]
    
        # Sorted
        return {data: feriados[data] for data in sorted(feriados)}
