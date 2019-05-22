import string
import os
import json

from functools import lru_cache
from ConnectDB import ConnectDB

class CreateDB(object):

    def __init__(self,driver='none',server='none',database='none',user='none',password='none'):

        self.connection = ConnectDB(driver,server,database,user,password)
        self.string_connection = {'driver': 'none',
                                  'server': 'none',
                                  'database': 'none',
                                  'user': 'none',
                                  'password': 'none',
                                  'truested_connection': 'no'}
        self.has_error = False
        self.str_error = ''
        self.str_createDB = ''
        self.path = ''
        self.file_table_json = None
        self.json = None
        self.script_ddl = ''

        if (self.connection != None):

            self.dictionary_database()

            if (self.json != None):
                self.create_table()

            self.connection.closeConnection()

        else:
            self.connection.setStringConnection(self.default_driver,self.default_server,self.default_database,
                                                self.default_user,self.default_pwd)
            if (self.connection.connect()):
                self.connected = True
            else:
                self.connected = False

            if (self.connected):
                self.createDatabase()

    def get_string_connection(self):

        if ("pyodbc" in str(type(self.connection)).lower() ):
            self.string_connection['driver'] = self.connection.driver
            self.string_connection['server'] = self.connection.server
            self.string_connection['database'] = self.connection.database
            self.string_connection['user'] = self.connection.user
            self.string_connection['password'] = self.connection.password

        return self.string_connection

    
    # TODO: Definir a construção das tabelas de self.tables
    def create_table(self):

        self.str_createDB = ''
        self.clear_error()

        try:

            lst_tables = self.json.get('tables')[0].get('list_of_tables')

            for item in lst_tables:

                if (not self.has_table(item.get('name_table'))):
                    self.script_ddl += "CREATE TABLE " + item.get('name_table') + '(\n'
                    count_line = 0

                    for item_colunm in item.get('list_of_fields'):
                        count_line += 1

                        self.script_ddl += '\t '
                        self.script_ddl += item_colunm.get('name_field')       #nome do campo
                        self.script_ddl += ' ' + item_colunm.get('type_field')  #tipo de campo

                        default_value = item_colunm.get('default_value')

                        if (default_value != ''):
                            self.script_ddl += ' ' + default_value  # valor padrão

                        identity = item_colunm.get('identity')

                        if (identity != ''):
                            self.script_ddl += ' identity' + identity

                        type_key = item_colunm.get('type_key')

                        if (type_key != ''):
                            if ('primary' in type_key):
                                self.script_ddl += ' primary key'
                            elif('foreign' in type_key):
                                foreign_table = item_colunm.get('foreign_table')
                                foreign_field = item_colunm.get('foreign_field')
                                has_foreign_key = (foreign_table != '' and foreign_field != '')

                                if(has_foreign_key):
                                    self.script_ddl += ' foreign key references ' + foreign_table + '(' + foreign_field + ')'

                        is_null = item_colunm.get('is_null')

                        if ('no' in is_null):
                            self.script_ddl += ' not null'
                        elif ('yes' in is_null):
                            self.script_ddl += ' null'

                        if (count_line < len(item.get('list_of_fields'))):
                            self.script_ddl += ', \n'
                        else:
                            self.script_ddl += ')\n\n '

            if (self.script_ddl != ''):
                try:
                    self.connection.connection.cursor().execute(self.script_ddl)
                    self.connection.connection.cursor().commit()

                except Exception as e:
                    try:
                        self.connection.connection.cursor().rollback()
                    except Exception as e:
                        self.set_error('Problemas para executar o rollback. ', str(e))

                    self.set_error('Não foi possível criar tabelas no banco. ', str(e))

        except Exception as e:
            self.set_error('Não foi possível criar tabelas no banco. ', str(e))

    @lru_cache(maxsize=32,typed=False)
    def has_table(self,str_table = ''):

        bool_has_table = False
        self.clear_error()

        try:
           if (self.connection.connection.cursor().tables(str_table).fetchone() != None):
                bool_has_table = True

        except Exception as e:
            self.set_error('Problemas com a conexão com o banco de dados. ',e)
            bool_has_table = True

        return bool_has_table

    def dictionary_database(self):

        self.clear_error()

        try:
            self.path = os.getcwd() + '\\database\\jsonfiles\\'

            if (os.path.exists(self.path)):
                self.file_table_json = open(self.path + 'tables.json')
                self.json = json.load(self.file_table_json)

        except Exception as e:
            self.set_error('Problema com o arquivo tables.json', e)

    def set_error(self,msg_error,e = Exception):

        self.has_error = True
        self.str_error = msg_error + str(e)

    def clear_error(self):

        self.has_error = False
        self.str_error = ''