# %%
import numpy as np
DEFAULT_PATH = 'ASTR19_F25_group_project_data.txt'

# %%
def hm2m(string):
    l = string.split(':')
    l = [int(i) for i in l]
    m = l[0]*60 + l[1]
    return m

# %%
def get_data(filename = DEFAULT_PATH, types = (int,int,float),funcs = (None,hm2m,None)):
    datalist = []
    with open(filename,'r') as file:
        lines = file.readlines()
    for i,l in enumerate(lines):
        items = l.split()
        if items[0].lower() == '#column':
            label = ''.join([c for c in items[1] if c.isalnum()])
            description = ' '.join(items[2:])
            datalist.append({'label':label, 'description':description, 'data':[]})
        else:
            for n,val in enumerate(items):
                if funcs is not None:
                    if funcs[n] is not None:
                        val = funcs[n](val)
                elif types is not None:
                    if types[n] is not None:
                        val = funcs[n](val)
                datalist[n]['data'].append(val)
    for i in range(len(datalist)):
        datalist[i]['data'] = np.array(datalist[i]['data'], dtype=types[i])
    return datalist

# %%
def main():
    d = get_data()
    for i in d:
        print(str(i))
        print(i['data'].dtype)

# %%
if __name__ == "__main__":
    main()


