from exemplo_csv_class import Csv_Processador

arquivo_csv = './teste.csv'
filtro = 'estado'
limite = 'SP'
filtro2 = 'data'
dia = '10/01/2024'

arquivo_CSV = Csv_Processador(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por([filtro,filtro2],[limite,dia]))


# print('############################')

# arquivo_csv2 = './teste2.csv'
# filtro2 = 'estado'
# limite2 = 'RJ'

# arquivo_CSV2 = Csv_Processador(arquivo_csv2)
# arquivo_CSV2.carregar_csv()
# print(arquivo_CSV2.filtrar_por(filtro2,limite2))
# print(arquivo_CSV2.filtrar_por('data','10/01/2024'))