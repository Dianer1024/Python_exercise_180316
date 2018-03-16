from pygal_maps_world.i18n import COUNTRIES

#引入了一个countries类，提供不同国家的国别码

def get_country_code(country_name):
    """根据制定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    #如果没有找到国家，就返回None
    return None


