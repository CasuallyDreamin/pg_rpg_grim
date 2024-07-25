def player_physics(dt=0,friction_ac=0.17, pl = None, l = False,r = False,j = False):
    ms = 0.5

    if (l and r) or (not r and not l):
        if pl.physics['vel'][0] != 0:
            if pl.physics['vel'][0] > 0:
                if pl.physics['vel'][0] - friction_ac*dt < 0:
                    pl.physics['vel'][0] = 0
                else:
                    pl.physics['vel'][0] -= friction_ac*dt
            else:
                if pl.physics['vel'][0] + friction_ac*dt > 0:
                    pl.physics['vel'][0] = 0
                else:
                    pl.physics['vel'][0] += friction_ac*dt
        else:
            return
    
    if r and not l:
        pl.physics['vel'][0] = ms
    
    if l and not r:
        pl.physics['vel'][0] = -ms
    

def update_pos(ent_list):
    for ent in ent_list:
        ent.pos = (ent.physics['vel'][0]+ent.pos[0], ent.physics['vel'][1]+ent.pos[1])
    return ent_list
    