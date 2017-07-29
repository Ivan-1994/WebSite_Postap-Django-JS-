from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class StaticSitemap(Sitemap):
    priority = 0.6
    changefreq = 'always'
    
    def items(self):
        return ('clanzone', 'sostavclan', 'online', 'ob/1', 'ob/2', 'ob/3', 'ob/4', 'ob/5', 'ob/6', 'ob/7', 'info',
                'o_nas', 'nzh_shop', 'remont', 'rem_or_zv', 'or_kraft', 'qvest', 'news', 'torgovets', 'granatu',
                'lekarstva', 'minu', 'patronu', 'yeda', 'um_rem', 'zavodu_proizvodstvo')

    def location(self, item):
        return reverse(item)