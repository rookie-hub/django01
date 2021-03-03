def get_name(fl,l):
    f_name=f'{fl} {l}'
    return f_name

def get_fname(fl,l,midd=''):
    if midd:
        f_name = f'{fl} {midd} {l}'
    else:
        f_name=f'{fl} {l}'
    return f_name