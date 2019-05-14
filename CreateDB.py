from ConnectDB import   ConnectDB

class CreateDB(object):

    self.connection = None

    self.default_driver = 'ODBC Driver 17 for SQL Server'
    self.default_server = 'LAPTOP-QDSU82H0'
    self.default_database = 'P12117MNTDB'
    self.default_user = 'sa'
    self.default_pwd = '123'
    self.connected = False
    self.string_connection = {'driver':'none',
                              'server':'none',
                              'database':'none',
                              'user':'none',
                              'password':'none',
                              'truested_connection':'no'}

    def __init__(self,driver='none',server='none',database='none',user='none',password='none'):

        self.connection = ConnectDB(driver,server,database,user,password)

        if (not self.connection.hasError()):
            self.createDatabase()
        else:
            self.connection.setStringConnection(self.default_driver,self.default_server,self.default_database,
                                                self.default_user,self.default_pwd)
            if (self.connection.connect()):
                self.connected = True
            else:
                self.connected = False

    def getStringConnection(self):

        if ("pyodbc" in str(type(self.connection)).lower() ):

            self.string_connection['driver'] = self.connection.driver
            self.string_connection['server'] = self.connection.server
            self.string_connection['database'] = self.connection.database
            self.string_connection['user'] = self.connection.user
            self.string_connection['password'] = self.connection.password

        return self.string_connection

    def createDatabase(self):
        self.dictionaryDB = DictionaryDB()