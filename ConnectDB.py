import pyodbc   #para importar executar em prompty de comando, dentro do diretório Python o comando pip install pyodbc
class ConnectDB(object):
    def __init__(self,try_connect=False,driver='none',server='none',database='none',user='none',password='none'):

        self.driver = driver
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.str_conn = ''
        self.connection = object
        self.has_error = False
        self.error_conn = ''

        if (try_connect):
            self.connect()

    def connect(self):

        self.clearErrors()

        if(self.str_conn == 'none' or self.str_conn == ''):
            self.str_conn = self.setStringConnection()

        if(self.str_conn != 'none' or self.str_conn != ''):
            try:
                self.connection = pyodbc.connect(self.str_conn)
            except Exception as e:
                self.error_conn = 'Tentativa de conexão com o banco, acarretou em erro: ' + str(e)
                self.has_error = True
        else:
            self.has_error = True
            self.error_conn = 'Não foi definida uma string de conexão'

    def closeConnection(self):

        self.clearErrors()

        try:
            self.connection.close()
        except Exception as e:
            self.error_conn = 'Erro na tentativa de encerrar a conexão: ' + str(e)
            self.has_error = True

        return not self.has_error

    def setStringConnection(self,driver='none',server='none',database='none',user='none',password='none'):

        if(driver == 'none' and self.driver != 'none'):
            str_driver = self.driver
        else:
            str_driver = driver

        self.driver = str_driver

        if(server == 'none' and self.server != 'none'):
            str_server = self.server
        else:
            str_server = server

        self.server = str_server

        if(database == 'none' and self.database != 'none'):
            str_database = self.database
        else:
            str_database = database

        self.database = str_database

        if (user == 'none' and self.user != 'none'):
            str_user = self.user
        else:
            str_user = user

        self.user = str_user

        if (password == 'none' and self.password != 'none'):
            str_pwd = self.password
        else:
            str_pwd = password

        self.password = str_pwd

        stringConnection = 'DRIVER={' + str_driver + '};SERVER=' + str_server + ';DATABASE=' + str_database + \
                            ';UID=' + str_user + ';PWD=' + str_pwd + ';'

        self.str_conn = stringConnection

        return stringConnection

    def hasError(self):
        return self.has_error

    def clearErrors(self):
        self.has_error = False
        self.error_conn = ''