from django.db import models
from django.contrib.auth.models import User


class WorkStations(models.Model):
    WorkStationName = models.CharField(max_length=150)


class orders(models.Model):
    EsmeProject = models.CharField(max_length=300)
    TooleJabeh = models.CharField(max_length=150)
    ArzeJabeh = models.CharField(max_length=150)
    ErtefaeJabeh = models.CharField(max_length=150)
    TedadeRang = models.CharField(max_length=150)

    NobateChap_CHOICES = (
        ('A', 'اول'),
        ('T', 'تکرار'),
    )
    NobateChap = models.CharField(max_length=20, choices=NobateChap_CHOICES)

    NoeChap_CHOICES = (
        ('O', 'افست'),
        ('F', 'فلکسو'),
        ('LS', 'لمینیت '),
        ('LV', 'تکرار'),
    )
    NoeChap = models.CharField(max_length=20, choices=NoeChap_CHOICES)

    MavadAvvaliye1_CHOICES = (
        ('T', 'تحریر'),
        ('G', 'گلاسه'),
        ('K', 'کرافت '),
        ('M', 'مومی'),
        ('PC', 'پشت چسبدار'),
        ('IB', 'ایندربرد'),
        ('PT', 'پشت طوسی '),
        ('D', 'دوپلکس'),
        ('V3', 'ورق 3 لایه'),
        ('V5', 'ورق 5 لایه'),
        ('TK', 'ترکیبی '),
    )
    MavadAvvaliye1 = models.CharField(
        max_length=20, choices=MavadAvvaliye1_CHOICES)

    MavadAvvaliye2_CHOICES = (
        ('S', 'سینگل'),
        ('V', 'ورق'),
    )
    MavadAvvaliye2 = models.CharField(
        max_length=20, choices=MavadAvvaliye2_CHOICES)

    MavadAvvaliye3_CHOICES = (
        ('T', 'تحریر'),
        ('G', 'گلاسه'),
        ('K', 'کرافت '),
        ('M', 'مومی'),
        ('PC', 'پشت چسبدار'),
        ('IB', 'ایندربرد'),
        ('PT', 'پشت طوسی '),
        ('D', 'دوپلکس'),
        ('V3', 'ورق 3 لایه'),
        ('V5', 'ورق 5 لایه'),
        ('S', 'سینگل'),
        ('V', 'ورق'),
    )
    MavadAvvaliye3 = models.CharField(
        max_length=20, choices=MavadAvvaliye3_CHOICES)

    MavadAvvaliye4_CHOICES = (
        ('T', 'تحریر'),
        ('G', 'گلاسه'),
        ('K', 'کرافت '),
        ('M', 'مومی'),
        ('PC', 'پشت چسبدار'),
        ('IB', 'ایندربرد'),
        ('PT', 'پشت طوسی '),
        ('D', 'دوپلکس'),
        ('V3', 'ورق 3 لایه'),
        ('V5', 'ورق 5 لایه'),
        ('S', 'سینگل'),
        ('V', 'ورق'),
    )
    MavadAvvaliye4 = models.CharField(
        max_length=20, choices=MavadAvvaliye4_CHOICES)

    Behdashti_CHOICES = (
        ('O', 'بهداشتی'),
        ('F', 'غیر بهداشتی'),
    )
    Behdashti = models.CharField(max_length=20, choices=Behdashti_CHOICES)

    Rol_CHOICES = (
        ('O', 'رول'),
        ('F', 'غیر رول'),
    )
    Rol = models.CharField(max_length=20, choices=Rol_CHOICES)

    TarahiGraphici_CHOICES = (
        ('O', 'طراحی گرافیکی دارد'),
        ('F', 'طراحی گرافیکی ندارد'),
    )
    TarahiGraphici = models.CharField(
        max_length=20, choices=TarahiGraphici_CHOICES)

    TarrahiStructure_CHOICES = (
        ('O', 'طراحی استراکچر دارد'),
        ('F', 'طراحی استراکچر ندارد'),
    )
    TarrahiStructure = models.CharField(
        max_length=20, choices=TarrahiStructure_CHOICES)

    NemooneSazi_CHOICES = (
        ('O', 'نمونه سازی دارد'),
        ('F', 'نمونه سازی ندارد'),
    )
    NemooneSazi = models.CharField(max_length=20, choices=NemooneSazi_CHOICES)

    Axasi_CHOICES = (
        ('O', 'عکاسی دارد'),
        ('F', 'عکاسی ندارد'),
    )
    Axasi = models.CharField(max_length=20, choices=Axasi_CHOICES)

    Ghaleb_CHOICES = (
        ('O', 'قالب دارد'),
        ('F', 'قالب ندارد'),
    )
    Ghaleb = models.CharField(max_length=20, choices=Ghaleb_CHOICES)

    NemooneMahsool_CHOICES = (
        ('O', 'نمونه محصول دارد'),
        ('F', 'نمونه محصول ندارد'),
    )
    NemooneMahsool = models.CharField(
        max_length=20, choices=NemooneMahsool_CHOICES)

    NemooneBasteBandi_CHOICES = (
        ('O', 'نمونه بسته بندی دارد'),
        ('F', 'نمونه بسته بندی ندارد'),
    )
    NemooneBasteBandi = models.CharField(
        max_length=20, choices=NemooneBasteBandi_CHOICES)

    Celiphone_CHOICES = (
        ('O', 'سلفون دارد'),
        ('F', 'سلفون ندارد'),
    )
    Celiphone = models.CharField(max_length=20, choices=Celiphone_CHOICES)

    UV_CHOICES = (
        ('O', 'یو وی دارد'),
        ('F', 'یو وی ندارد'),
    )
    UV = models.CharField(max_length=20, choices=UV_CHOICES)

    Verni_CHOICES = (
        ('O', 'ورنی دارد'),
        ('F', 'ورنی ندارد'),
    )
    Verni = models.CharField(max_length=20, choices=Verni_CHOICES)

    TedadDarGhaleb = models.CharField(max_length=150)
    SharheMavadAvaliye1 = models.CharField(max_length=300)
    SharheMavadAvaliye2 = models.CharField(max_length=300)
    SharheMavadAvaliye3 = models.CharField(max_length=300)
    SharheMavadAvaliye4 = models.CharField(max_length=300)
    ShomareSefaresh = models.CharField(max_length=30)
    ArzeShitChapi = models.CharField(max_length=150)
    TooleShitChapi = models.CharField(max_length=150)
    ShomareHavale = models.CharField(max_length=30)

    def __str__(self):
        return self.EsmeProject

    def __unicode__(self):
        return u'%s' % (self.EsmeProject)


class OrderAttachments(models.Model):
    AttachmentFile = models.FileField(upload_to='media/% Y/% m/% d/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    order = models.ForeignKey(
        orders, on_delete=models.CASCADE, default=None, related_name='Attachs2Order')
    ws = models.ForeignKey(
        WorkStations, on_delete=models.CASCADE, default=None)


class ProfileDetail(models.Model):
    tell = models.CharField(max_length=150)
    birthday = models.DateTimeField(auto_now_add=False)
    img = models.ImageField(default='default.png', blank=True)
    madarek1 = models.ImageField(default='default.png', blank=True)
    madarek2 = models.ImageField(default='default.png', blank=True)
    madarek3 = models.ImageField(default='default.png', blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='ProfileDetail2User')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class UserProject(models.Model):
    LastWork = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    order = models.ForeignKey(orders, on_delete=models.CASCADE, default=None)


class Comment(models.Model):
    Message = models.TextField(null=False)
    order = models.ForeignKey(orders, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class Notifications(models.Model):
    Message = models.TextField(null=False)
    R_S_CHOICES = (
        ('S', 'Send'),
        ('R', 'Receive'),
    )
    R_S = models.CharField(max_length=10, choices=R_S_CHOICES)
    R_S = models.CharField(max_length=10, choices=R_S_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

class Material(models.Model):
    CodeKala = models.IntegerField(null=False)
    NameKala = models.CharField(max_length=140)
    Vahed1 = models.CharField(max_length=40)
    Vahed2 = models.CharField(max_length=40)
    NameGorooheKalayi = models.CharField(max_length=140)
    Gramazh = models.IntegerField(null=False)
    ZaribeDoVahed = models.IntegerField(null=False, default=0)
    Arz = models.IntegerField(null=False)
    Tool = models.IntegerField(null=False)
    CodeZirGorooheKalayi = models.IntegerField(null=False)

class DasteMahsool(models.Model):
    CodeMahsool = models.IntegerField(null=False)   
    DasteMahsool = models.CharField(max_length=110)
    VahedShomaresh = models.CharField(max_length=30)

class customers(models.Model):
    CodeYekta = models.IntegerField(null=False)
    CodeTafziliShenavar = models.IntegerField(null=False) 
    NameTafziliShenavar = models.CharField(max_length=220)
    MandeTafzili = models.BigIntegerField(null=False, default=0)
    TarikheIjad = models.DateTimeField()


    