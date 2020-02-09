from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
    CodeKala = models.IntegerField(null=False)
    NameKala = models.CharField(max_length=140)
    Vahed1 = models.CharField(max_length=40)
    Vahed2 = models.CharField(max_length=40)
    NameGorooheKalayi = models.CharField(max_length=140)
    NameMadareGoroohiyeKala = models.CharField(max_length=50, null=True)
    Gramazh = models.IntegerField(null=False)
    ZaribeDoVahed = models.IntegerField(null=False, default=0)
    Arz = models.IntegerField(null=False)
    Tool = models.IntegerField(null=False)
    CodeZirGorooheKalayi = models.IntegerField(null=False)

    def __str__(self):
        return self.NameKala

    def __unicode__(self):
        return u'%s' % (self.NameKala)    


class DasteMahsool(models.Model):
    CodeMahsool = models.IntegerField(null=False)   
    DasteMahsool = models.CharField(max_length=110)
    VahedShomaresh = models.CharField(max_length=30)     

    def __str__(self):
        return self.DasteMahsool

    def __unicode__(self):
        return u'%s' % (self.DasteMahsool)    

class customers(models.Model):
    shomare_yekta = models.IntegerField(null=False)
    code_tafzili_shenavar = models.IntegerField(null=True)
    name_tafzili_shenavar = models.CharField(max_length=110)
    mande_hesab = models.DecimalField(max_digits=15, decimal_places=1)
    tozihat_hesab = models.CharField(max_length=255)
    tarikh_ijad = models.DateTimeField(auto_now_add=True)
    tarikh_akharin_taghir = models.DateTimeField(auto_now=True)
    tel1 = models.CharField(max_length=20)
    tel2 = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    Web = models.CharField(max_length=55)
    addres1 = models.CharField(max_length=190)
    addres2 = models.CharField(max_length=190)
    shahr = models.CharField(max_length=40)
    ostan = models.CharField(max_length=40)
    code_posti = models.IntegerField(null=True)
    keshvar = models.CharField(max_length=40)
    code_eghtesadi = models.CharField(max_length=25)
    telex = models.CharField(max_length=20)
    onvan = models.CharField(max_length=25)
    mobile = models.CharField(max_length=30)
    shomare_hesabe_banki1 = models.CharField(max_length=40)
    shomare_hesabe_banki2 = models.CharField(max_length=40)
    tarikh_tavalod = models.DateTimeField(auto_now_add=False, auto_now=False)
    noe_hesab = models.CharField(max_length=30)
    noe_kharidar_forooshande_dar_darayi = models.CharField(max_length=40)
    code_meli = models.CharField(max_length=40)

    def __str__(self):
        return self.name_tafzili_shenavar

    def __unicode__(self):
        return u'%s' % (self.name_tafzili_shenavar)      


class Templates(models.Model):    
    Code_mahsool = models.IntegerField(null=True)
    Code_ghalebe_asli = models.CharField(max_length=40)
    Daste_mahsool_L = models.ForeignKey(DasteMahsool, on_delete=models.CASCADE, default=None, null=True)
    Daste_mahsool = models.CharField(max_length=140)

    Brand_CHOICES = (
        ('B', 'برونسی'),
        ('K', 'بلوکات'),
    )
    Brand = models.CharField(max_length=10, choices=Brand_CHOICES)

    Name = models.CharField(max_length=25)
    Material_l = models.ForeignKey(Material, on_delete=models.CASCADE, default=None, null=True)
    Material = models.CharField(max_length=140)
    tool_arz_ertefa = models.CharField(max_length=50)
    Formoole_name_mahsool = models.CharField(max_length=130)
    Name_mahsoole_asli = models.CharField(max_length=100)
    Toole_kaghaz = models.CharField(max_length=12)
    Arze_kaghaz = models.CharField(max_length=12)
    Boresh_pish_az_Chap = models.CharField(max_length=4)
    Toole_Sheete_Chapi = models.CharField(max_length=12)
    Arze_sheete_chapi = models.CharField(max_length=12)
    Boresh_pas_az_chap = models.CharField(max_length=4)
    Toole_varagh = models.DecimalField(max_digits=7, decimal_places=2)
    Arze_varagh = models.DecimalField(max_digits=7, decimal_places=2)
    Toole_single = models.DecimalField(max_digits=7, decimal_places=2)
    Arze_single = models.DecimalField(max_digits=7, decimal_places=2)
    Toole_maghzi = models.IntegerField(null=True,default=0)
    Arze_maghzi = models.IntegerField(null=True,default=0)
    toole_sheete_dicut = models.CharField(max_length=8)
    arze_sheete_dicut = models.CharField(max_length=8)
    dastgah_chap = models.CharField(max_length=20)
    dastgah_dicut = models.CharField(max_length=10)
    chasb = models.CharField(max_length=25)
    baste_bandi = models.CharField(max_length=25)
    tedad_dar_baste = models.IntegerField(null=True)
    toole_tigh_be_tigh = models.DecimalField(max_digits=5, decimal_places=2)
    arze_tigh_be_tigh = models.DecimalField(max_digits=5, decimal_places=2)
    toole_mahsool = models.DecimalField(max_digits=5, decimal_places=2)
    arze_mahsool = models.DecimalField(max_digits=5, decimal_places=2)
    ertefa_mahsool = models.DecimalField(max_digits=5, decimal_places=2)
    toole_gostarde = models.DecimalField(max_digits=5, decimal_places=2)
    arze_gostarde = models.DecimalField(max_digits=5, decimal_places=2)
    tedad_dar_ghaleb = models.IntegerField(null=True)
    masahat_taki = models.CharField(max_length=35)
    folder_link = models.CharField(max_length=100)
    Name_mahsool = models.CharField(max_length=150)
    img = models.ImageField

    def __str__(self):
        return self.Formoole_name_mahsool

    def __unicode__(self):
        return u'%s' % (self.Formoole_name_mahsool)     

class WorkStations(models.Model):
    WorkStationName = models.CharField(max_length=150)

    def __str__(self):
        return self.Formoole_name_mahsool

    def __unicode__(self):
        return u'%s' % (self.Formoole_name_mahsool)   


class orders(models.Model):
    Name_Moshtari = models.ForeignKey(
        customers, on_delete=models.CASCADE, default=None, verbose_name="نام مشتری")

    Name_Project = models.CharField(max_length=150, verbose_name="نام پروژه")
    
    Daste_Mahsool = models.ForeignKey(
        DasteMahsool, on_delete=models.CASCADE, default=None, verbose_name="دسته محصول")

    NoeFactore_Choice = (
        ('R', 'رسمی'),
        ('G', 'غیر رسمی'),
    )
    NoeFactor = models.CharField(max_length=12, choices=NoeFactore_Choice, verbose_name="نوع فاکتور")

    Tirazh = models.IntegerField(null=False, verbose_name="تیراژ")
    MavadAvaliye1 = models.ForeignKey(
        Material, on_delete=models.CASCADE, default=None, verbose_name="مواد اولیه")
    SharheMavadAvaliye1 = models.CharField(max_length=300, verbose_name="شرح مواد اولیه")

    IsBehdashti_Choice = (
        ('B', 'بهداشتی'),
        ('G', 'غیر بهداشتی'),
    )
    IsBehdashti = models.CharField(max_length=12, choices=IsBehdashti_Choice, verbose_name="بهداشتی یا غیر بهداشتی؟")
    
    CodeGhaleb = models.ForeignKey(
        Templates, on_delete=models.CASCADE, default=None, verbose_name="کد قالب")

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.Name_Project

    def __unicode__(self):
        return u'%s' % (self.Name_Project)


class OrderAttachments(models.Model):
    AttachmentFile = models.FileField(upload_to='media/% Y/% m/% d/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    order = models.ForeignKey(
        orders, on_delete=models.CASCADE, default=None, related_name='Attachs2Order')
    ws = models.ForeignKey(
        WorkStations, on_delete=models.CASCADE, default=None)

class UserProject(models.Model):
    LastWork = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    order = models.ForeignKey(orders, on_delete=models.CASCADE, default=None)


class Comment(models.Model):
    Message = models.TextField(null=False)
    order = models.ForeignKey(orders, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.Message

    def __unicode__(self):
        return u'%s' % (self.Message)       


class Notifications(models.Model):
    Message = models.TextField(null=False)
    R_S_CHOICES = (
        ('S', 'Send'),
        ('R', 'Receive'),
    )
    R_S = models.CharField(max_length=10, choices=R_S_CHOICES)
    R_S = models.CharField(max_length=10, choices=R_S_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.Message

    def __unicode__(self):
        return u'%s' % (self.Message)       


