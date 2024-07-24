class entity:
    def __init__(self, hp = 100,
                att = 10,
                dfns = 1,
                eq = {'wep':'','arm':''},
                inv = [],
                sprite = None,
                pos = None):
        self.hp = hp
        self.att = att
        self.dfns = dfns
        self.eq = eq
        self.inv = inv
        self.sprite = sprite
        self.pos = pos

    physics = {'vel':[0,0],
               'acc':[0,0],
               }
    
class item:
    def __init__(self, name = '',sprite=None, att_buff = 1, def_buff = 1, req = {'dex':0, 'str':0, 'int':0}):
        self.name = name
        self.att_buff = att_buff
        self.def_buff = def_buff
        self.req = req
        self.sprite = sprite