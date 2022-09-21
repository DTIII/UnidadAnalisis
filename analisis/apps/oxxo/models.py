# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CArmas(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    arma = models.CharField(db_column='Arma', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'C_Armas'


class CIndicios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'C_Indicios'


class CModus(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'C_Modus'


class CObjetos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'C_Objetos'


class COxxos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sucursal = models.TextField(db_column='Sucursal', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    latitud = models.CharField(db_column='Latitud', max_length=50, blank=True, null=True)  # Field name made lowercase.
    longitud = models.CharField(db_column='Longitud', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechaalta = models.DateField(db_column='FechaAlta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'C_Oxxos'


class CPermisos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    permisos = models.CharField(db_column='Permisos', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'C_Permisos'


class CSexo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'C_Sexo'


class Perfilvictimario(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idcaptura = models.IntegerField(db_column='IdCaptura')  # Field name made lowercase.
    numresponsable = models.IntegerField(db_column='NumResponsable', blank=True, null=True)  # Field name made lowercase.
    alias = models.TextField(db_column='Alias', blank=True, null=True)  # Field name made lowercase.
    mediaafiliacion = models.TextField(db_column='MediaAfiliacion', blank=True, null=True)  # Field name made lowercase.
    vestimenta = models.TextField(db_column='Vestimenta', blank=True, null=True)  # Field name made lowercase.
    edadaproximada = models.CharField(db_column='EdadAproximada', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tatuajes = models.TextField(db_column='Tatuajes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerfilVictimario'
        unique_together = (('id', 'idcaptura'),)


class TDenunciaVarios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ru = models.CharField(db_column='RU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdi = models.CharField(db_column='Cdi', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fechadeuncia = models.DateTimeField(db_column='FechaDeuncia', blank=True, null=True)  # Field name made lowercase.
    delito = models.TextField(db_column='Delito', blank=True, null=True)  # Field name made lowercase.
    afectado = models.TextField(db_column='Afectado', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sintesis = models.TextField(db_column='Sintesis', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_Denuncia_Varios'


class TLugarhechos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    iddenuncia = models.IntegerField(db_column='IdDenuncia', blank=True, null=True)  # Field name made lowercase.
    colonia = models.TextField(db_column='Colonia', blank=True, null=True)  # Field name made lowercase.
    calle = models.TextField(db_column='Calle', blank=True, null=True)  # Field name made lowercase.
    no = models.CharField(db_column='No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modulo = models.CharField(db_column='Modulo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    girocomercial = models.CharField(db_column='GiroComercial', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cuadrante = models.CharField(db_column='Cuadrante', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitud = models.CharField(db_column='Latitud', max_length=400, blank=True, null=True)  # Field name made lowercase.
    longitud = models.CharField(db_column='Longitud', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_LugarHechos'


class TOxxoGenerales(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ru = models.CharField(db_column='Ru', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cdi = models.CharField(db_column='Cdi', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fechahechos = models.DateTimeField(db_column='FechaHechos', blank=True, null=True)  # Field name made lowercase.
    delito = models.CharField(db_column='Delito', max_length=100, blank=True, null=True)  # Field name made lowercase.
    afectado = models.TextField(db_column='Afectado', blank=True, null=True)  # Field name made lowercase.
    colonia = models.TextField(db_column='Colonia', blank=True, null=True)  # Field name made lowercase.
    calle = models.TextField(db_column='Calle', blank=True, null=True)  # Field name made lowercase.
    sucursal = models.CharField(db_column='Sucursal', max_length=400, blank=True, null=True)  # Field name made lowercase.
    giroempresarial = models.CharField(db_column='GiroEmpresarial', max_length=400, blank=True, null=True)  # Field name made lowercase.
    latitud = models.CharField(db_column='Latitud', max_length=400, blank=True, null=True)  # Field name made lowercase.
    longitud = models.CharField(db_column='Longitud', max_length=400, blank=True, null=True)  # Field name made lowercase.
    numerodia = models.IntegerField(db_column='NumeroDia', blank=True, null=True)  # Field name made lowercase.
    dia = models.CharField(db_column='Dia', max_length=10, blank=True, null=True)  # Field name made lowercase.
    numagresores = models.IntegerField(db_column='NumAgresores', blank=True, null=True)  # Field name made lowercase.
    sintesis = models.TextField(db_column='Sintesis', blank=True, null=True)  # Field name made lowercase.
    fechacaptura = models.DateTimeField(db_column='FechaCaptura', blank=True, null=True)  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_Oxxo_Generales'


class TPadrondelictivo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    id_captura = models.IntegerField(db_column='Id_Captura', blank=True, null=True)  # Field name made lowercase.
    modus = models.CharField(db_column='Modus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sintesisoperandi = models.TextField(db_column='SintesisOperandi', blank=True, null=True)  # Field name made lowercase.
    vehiculos = models.TextField(db_column='Vehiculos', blank=True, null=True)  # Field name made lowercase.
    caracteristicasvehiculo = models.TextField(db_column='CaracteristicasVehiculo', blank=True, null=True)  # Field name made lowercase.
    armas = models.CharField(db_column='Armas', max_length=400, blank=True, null=True)  # Field name made lowercase.
    indicios = models.CharField(db_column='Indicios', max_length=400, blank=True, null=True)  # Field name made lowercase.
    objetossustraidos = models.CharField(db_column='ObjetosSustraidos', max_length=50, blank=True, null=True)  # Field name made lowercase.
    montorobado = models.FloatField(db_column='MontoRobado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_PadronDelictivo'


class TPadrondelictivoVariosdelitos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idcaptura = models.IntegerField(db_column='IdCaptura', blank=True, null=True)  # Field name made lowercase.
    modus = models.CharField(db_column='Modus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sinteismodus = models.TextField(db_column='SinteisModus', blank=True, null=True)  # Field name made lowercase.
    vehiculo = models.TextField(db_column='Vehiculo', blank=True, null=True)  # Field name made lowercase.
    caracteristicasvehiculo = models.TextField(db_column='CaracteristicasVehiculo', blank=True, null=True)  # Field name made lowercase.
    elementocomision = models.TextField(db_column='ElementoComision', blank=True, null=True)  # Field name made lowercase.
    indicios = models.TextField(db_column='Indicios', blank=True, null=True)  # Field name made lowercase.
    montorobado = models.FloatField(db_column='MontoRobado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_PadronDelictivo_VariosDelitos'


class TPerfinvictimariosDelitosvarios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idcaptura = models.IntegerField(db_column='IdCaptura', blank=True, null=True)  # Field name made lowercase.
    noresponsable = models.IntegerField(db_column='NoResponsable', blank=True, null=True)  # Field name made lowercase.
    alias = models.TextField(db_column='Alias', blank=True, null=True)  # Field name made lowercase.
    mediafiliacion = models.TextField(db_column='MediaFiliacion', blank=True, null=True)  # Field name made lowercase.
    vestimenta = models.TextField(db_column='Vestimenta', blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
    tatuajes = models.TextField(db_column='Tatuajes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_PerfinVictimarios_DelitosVarios'


class TTiempodenuncia(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    iddenuncia = models.IntegerField(db_column='IdDenuncia', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    horanum = models.CharField(db_column='HoraNum', max_length=15, blank=True, null=True)  # Field name made lowercase.
    numdia = models.IntegerField(db_column='NumDia', blank=True, null=True)  # Field name made lowercase.
    dia = models.CharField(db_column='Dia', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_TiempoDenuncia'


class TUsuarios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contrasena = models.TextField(db_column='Contrase�a', blank=True, null=True)  # Field name made lowercase.
    permisos = models.CharField(db_column='Permisos', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_Usuarios'


class TVictima(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idcaptura = models.IntegerField(db_column='IdCaptura')  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_Victima'
        unique_together = (('id', 'idcaptura'),)


class TVictimaDelitosvarios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idcaptura = models.IntegerField(db_column='IdCaptura', blank=True, null=True)  # Field name made lowercase.
    idvictima = models.IntegerField(db_column='IdVictima', blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_Victima_DelitosVarios'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
