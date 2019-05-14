class DictionaryDB(object):

    def __init__(self):
        self.tables = []
        self.fields = []
        self.indexes = []
        self.user_constraints = []

        #definição do dicinário tables (tabelas)
        self.setTables()

        #definição do dicionário fields (campos)
        self.setFields()
        #definição do dicionário indexes (índices)
        self.setIndexes()
        #definição do dicionário user_constraints (regras de usuário)
        self.setConstraints()
    def setTables(self):

        self.tables.append(['id_table', 'nome_table'])

        self.tables.append([nId, 'characters'])

        nId = 1
        self.tables.append([nId,'races'])

        nId += 1
        self.tables.append([nId, 'classes'])

        nId += 1
        self.tables.append([nId, 'Backgrounds'])

        nId += 1
        self.tables.append([nId, 'equipments'])

        nId += 1
        self.tables.append([nId, 'spells'])

        return set_table

    def setFields(self):

        nId = 0

        self.fields.append(['id_field','name_table','name_field','type_field','default_value','identity','primary_key','not_null'])

        # definicao da tabela de characters (personagens)
        nId += 1
        self.fields.append([nId, "characters", "id_char", "int", "", "(1,1)","yes", "not_null"])

        nId += 1
        self.fields.append([nId, "characters", "name_char", "varchar(100)", "", "", "no", "not_null"])

        nId += 1
        self.fields.append([nId, "characters", "level_char", "smallint", "", "", "no", "null"])

        #definicao da tabela races
        nId += 1
        self.fields.append([nId, "races", "id_race", "int", "", "(1,1)", "yes", "not_null"])

        nId += 1
        self.fields.append([nId, "races", "name_race", "varchar(60)", "", "", "no", "not_null"])

        nId += 1
        self.fields.append([nId, "races", "parent_class", "varchar(1)", "'nao'", "", "no", "not_null"])

    def setIndexes(self):
        pass

    def setConstraints(self):
        pass

    #TODO: Definir a construção das tabelas de self.tables
    def buildTable(self):
        pass
