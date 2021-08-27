import pyodbc


class BancoDeDados:


    def __init__(self) -> None:
        
        #PRODUÇÃO
        self.server = ''
        self.database = ''
        self.username = ''
        self.password = ''

        #TESTE
        #self.server = ''
        #self.database = ''
        #self.username = ''
        #self.password = ''


    def __enter__(self) -> 'Conexão':

        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' 
        + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        self.cursor = self.cnxn.cursor()
        return self.cursor


    def __exit__(self, exc_type, exc_value, exc_trace) -> None:

        self.cnxn.commit()
        self.cursor.close()
        self.cnxn.close()



