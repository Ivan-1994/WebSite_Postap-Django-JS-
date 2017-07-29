from django.conf.urls import url
from . import views
from main.sitemaps import StaticSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticSitemap,
}
urlpatterns = [
    #service
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^clanzone$', views.clanzone, name='clanzone'),
    url(r'^sostavclan$', views.sostavclan, name='sostavclan'),
    url(r'^online$', views.online, name='online'),
    url(r'^granatu$', views.granatu, name='granatu'),
    url(r'^lekarstva$', views.lekarstva, name='lekarstva'),
    url(r'^minu$', views.minu, name='minu'),
    url(r'^patronu$', views.patronu, name='patronu'),
    url(r'^yeda$', views.yeda, name='yeda'),

    #новичкам
    url(r'^ob_harakteristiki$', views.ob_harakteristiki, name='ob/1'),
    url(r'^ob_umenia$', views.ob_umenia, name='ob/2'),
    url(r'^ob_perki$', views.ob_perki, name='ob/3'),
    url(r'^ob_pervueshagi$', views.ob_pervueshagi, name='ob/4'),
    url(r'^ob_shmot$', views.ob_shmot, name='ob/5'),
    url(r'^ob_zonu$', views.ob_zonu, name='ob/6'),
    url(r'^ob_kreditu$', views.ob_kreditu, name='ob/7'),

    #полезно
    #url(r'^kraft_him$', views.kraft_him, name='kraft_him'),
    url(r'^um_rem$', views.um_rem, name='um_rem'),
    url(r'^zavodu_proizvodstvo$', views.pr_zv, name='zavodu_proizvodstvo'),
    #other

    url(r'^info$', views.info, name='info'),
    url(r'^o_nas$', views.o_nas, name='o_nas'),
    url(r'^nzh_shop$', views.nzh_shop, name='nzh_shop'),
    url(r'^remont$', views.remont, name='remont'),
    url(r'^rem_or_zv$', views.rem_or_zv, name='rem_or_zv'),
    url(r'^or_kraft$', views.or_kraft, name='or_kraft'),
    url(r'^qvest$', views.qvest, name='qvest'),
    url(r'^news$', views.news, name='news'),
    url(r'^torgovetsinfo$', views.torgovetsinfo, name='torgovets'),
    url(r'^$', views.news),
]
