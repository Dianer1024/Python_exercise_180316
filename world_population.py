import json
import pygal
from countries import get_country_code

#将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#找到每个国家2010年的人口数量，创建一个包含人口数量的字典
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        #python不能把包含小数点的字符串转换为整数         population = int(pop_dict['Value'])会报错
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population

#根据人口数量将所有的国家分成5组
cc_pop1, cc_pop2, cc_pop3, cc_pop4, cc_pop5 ={},{},{},{},{}
for cc, pop in cc_population.items():
    if pop < 1000000:
        cc_pop1[cc] = pop
    elif pop < 10000000:
        cc_pop2[cc] = pop
    elif pop < 100000000:
        cc_pop3[cc] = pop
    elif pop < 1000000000:
        cc_pop4[cc] = pop
    else:
        cc_pop5[cc] = pop


wm = pygal.maps.world.World()
wm.title = 'World population in 2010'
wm.add('0-1m', cc_pop1)
wm.add('1-10m', cc_pop2)
wm.add('10-100m', cc_pop3)
wm.add('100m-1bn', cc_pop4)
wm.add('>1bn', cc_pop5)
wm.render_to_file("world_population.svg")
