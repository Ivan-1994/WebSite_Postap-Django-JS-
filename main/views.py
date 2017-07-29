from django.shortcuts import render
import urllib, json
from urllib.request import urlopen

def er404(request):
    return render(request, '404.html')

def news(request):
    return render(request, 'news.html')

def info(request):
    return render(request, 'info.html')

def qvest(request):
    return render(request, 'qvest.html')

def or_kraft(request):
    return render(request, 'or_kraft.html')

def rem_or_zv(request):
    return render(request, 'rem_or_zv.html')

def remont(request):
    return render(request, 'remont.html')

def nzh_shop(request):
    return render(request, 'nzh_shop.html')

def o_nas(request):
    return render(request, 'o_nas.html')

def clanzone(request):
    return render(request, 'clanzone.html')

def sostavclan(request):
    return render(request, 'sostavclan.html')

def torgovetsinfo(request):
    return render(request, 'torgovetsinfo.html')

def ob_harakteristiki(request):
    return render(request, 'pervue_shagi/ob_harakterist.html')

def ob_kreditu(request):
    return render(request, 'pervue_shagi/ob_kreditu.html')

def ob_perki(request):
    return render(request, 'pervue_shagi/ob_perki.html')

def ob_pervueshagi(request):
    return render(request, 'pervue_shagi/ob_pervshagi.html')

def ob_shmot(request):
    return render(request, 'pervue_shagi/ob_shmot.html')

def ob_umenia(request):
    return render(request, 'pervue_shagi/ob_umenia.html')

def ob_zonu(request):
    return render(request, 'pervue_shagi/ob_zonu.html')

def kraft_him(request):
    return render(request, 'polezno/kraft_him.html')

def um_rem(request):
    return render(request, 'um_rem.html')

def pr_zv(request):
    return render(request, 'zavodu_proizvodstvo.html')

def granatu(request):
    return render(request, 'service/granatu.html')

def lekarstva(request):
    return render(request, 'service/lekarstva.html')

def minu(request):
    return render(request, 'service/minu.html')

def patronu(request):
    return render(request, 'service/patronu.html')

def yeda(request):
    return render(request, 'service/yeda.html')


def online(request):
    data = {}
    none_clan = list()
    clan = list()
    clan_sort = list()
    id_clan = (1057, 1058, 1007, 1010, 1001, 1021, 1020, 1004, 1000, 1002, 1016, 1045, 1043,
               1034, 1006, 1033, 1030, 1039, 1052)
    name_clan = ('Black Hearts', 'Black WOLFS', 'Dark Jokers', 'Equilibrium', 'Invisibles',
                 'MaraderZ', 'S.Corp', 'Soldiers of Fortune', 'Администрация', 'Братство Стали',
                 'Бригада', 'ГУВД', 'Миротворцы', 'Орден Джада', 'Особый Комитет', 'СПЕЦНАЗ',
                 'Стражи Яра', 'ХэД Хантерс ', 'Царапычи')
    url = "http://api.unit-online.ru/online"
    data_json = urlopen(url)
    d = json.loads(data_json.read().decode("utf-8"))
    data['invisible'] = d['invisible']
    data['count'] = d['count']
    d = d['users']
    #data['xxx'] = sorted(d, key=lambda personazh: (-personazh['level'], personazh['name']))
    for i in d:
        try:
            i['clan']
            clan.append(i)
        except:
            none_clan.append(i)
    clan = sorted(clan, key=lambda personazh: (-personazh['level'], personazh['name']))
    for a, i in enumerate(id_clan):
        p = 0
        for j in clan:
            if i == j['clan']:
                if p == 0:
                    clan_sort.append({'nameclan': name_clan[a]})
                    p += 1
                clan_sort.append(j)
    data['vclane'] = clan_sort
    data['nevclane'] = sorted(none_clan, key=lambda personazh: (-personazh['level'], personazh['name']))
    return render(request, 'online.html', data)