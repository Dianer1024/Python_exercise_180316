import pygal.maps.world

#测试美洲几个国家的人口地图

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add("Worth America", ['ca', 'mx', 'us'])
wm.add("South America", ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.add("South America", ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])

wm.render_to_file("americas.svg")
