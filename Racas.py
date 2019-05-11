class racaDnd(object):
    '''
        Classe racaDnd.
        Esta á classe pai de racas, por padrão é assumido a raca humana.
    '''
    def __init__(self,nome='humano',forc=1,des=1,con=1,int=1,sab=1,car=1):
        '''
        Construtor da Classe racaDnd. Por padrão é assumida a raça humana

        :param nome: str, nome da raca (padrão 'humano')
        :param forc: int, valor de incremento no atributo Força
        :param des: int, valor de incremento no atributo Destreza
        :param con: int, valor de incremento no atributo Constituição
        :param int: int, valor de incremento no atributo Inteligência
        :param sab: int, valor de incremento no atributo Sabedoria
        :param car: int, valor de incremento no atributo Carisma
        '''
        self.nomeRaca = nome
        self.incForca = forc
        self.incDestreza = des
        self.incConstituicao = con
        self.incInteligencia = int
        self.incSabedoria = sab
        self.incCarisma = car

    def setDescricaoRaca(self,descricao):
        self.descricaoRaca = descricao

    def setIncAtributo(self,atributo='',val_inc=0):

        if (len(atributo) > 0):
            if ('FOR' in atributo.upper()):
                self.incForca = val_inc
            elif ('DES' in atributo.upper()):
                self.incDestreza = val_inc
            elif ('CON' in atributo.upper()):
                self.incConstituicao = val_inc
            elif ('INT' in atributo.upper()):
                self.incInteligencia = val_inc
            elif ('SAB' in atributo.upper()):
                self.incSabedoria = val_inc
            elif ('CAR' in atributo.upper()):
                self.incCarisma = val_inc

###Definicação da Classe Filha RacaAnao
class racaAnao(racaDnd):

    def __init__(self,nome='anao',forc=0,des=0,con=2,int=0,sab=0,car=0):

        strDesc = 'Reinos ricos de antiga grandeza, salões '
        strDesc += 'esculpidos nas raízes das montanhas, o eco '
        strDesc += 'de picaretas e martelos nas minas profundas e '
        strDesc += 'nas forjas ardentes, um compromisso com o clã'
        strDesc += 'e a tradição, e um ódio impetuoso contra'
        strDesc += 'goblins e orcs – essas linhas comuns'
        strDesc += 'unem todos os anões.'

        self.setDescricaoRaca(strDesc)

        self.visao_escuro = [True,' Acostumado à vida subterrânea, você '
                                  'tem uma visão superior no escuro e na '
                                  'penumbra. Você enxerga na penumbra a '
                                  'até 18 metros como se fosse luz plena, '
                                  'e no escuro como se fosse na penumbra. '
                                  'Você não pode discernir cores no escuro, '
                                  'apenas tons de cinza']

        self.resiliencia = 'Você possui vantagem em testes de resistência ' \
                           'contra venenos e resistência contra dano de veneno'

        self.treinamento_combate = 'proficiência com machados de batalha, ' \
                                   'machadinhas, martelos leves e martelos de guerra.'

        self.tracos_raciais = {'idade': 'Adultos aos 50 anos e vivem 350 anos',
                               'tendencia': 'tendem ao bem e justiça',
                               'tamanho': 'Médio',
                               'deslocamento': 7.5,
                               'visao_escuro':self.visao_escuro,
                               'resiliencia':self.resiliencia,
                               'treinamento_combate':self.treinamento_combate}

        super().__init__(nome,forc,des,con,int,sab,car)

humano = racaDnd()
print(humano.nomeRaca)
anao = racaAnao()
print(anao.nomeRaca)
print('Força do Anão incrementa em ',anao.incForca)
print('Destreza do Anão incrementa em ',anao.incDestreza)
print('Constituição do Anão incrementa em ',anao.incConstituicao)
print('Inteligência do Anão incrementa em ',anao.incInteligencia)
print('Sabedoria do Anão incrementa em ',anao.incSabedoria)
print('Carisma do Anão incrementa em ',anao.incCarisma)
print(anao.descricaoRaca)

