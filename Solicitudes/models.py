from django.db import models
from WF.models import ModeloBaseRegistro
from Base.models import TipoGiro, GiroCIIU, FechaBalance, TipoContribuyente, Pais, Departamento, Localidad, Ministerios, Categoria_Inversiones, SubCategoria_Inversiones
from Contribuyentes.models import Contribuyente
# Create your models here.
'''
    1 - Datos básicos
    2 - Ministerio evaluador e indicadores
    3 - Inversiones
    4 - Datos de indicadores
    5 - Beneficios tributarios solicitados
    6 - Contacto
    7 - Documentos
    8 - Evaluación
   ''' 
class Solicitud143_Step1(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	estado_solicitud = models.CharField(max_length=50, help_text='Es el Estado de la Solicitud', verbose_name='Estado de la Solicitud', null=True, blank=True)
	asignado_solicitud = models.CharField(max_length=50, help_text='A quien esta Asignada la Solicitud', verbose_name='Solicitud: Asignado a:', null=True, blank=True)
	observacion_solicitud = models.CharField(max_length=50, help_text='Observacion de la Solicitud', verbose_name='Observacion de la Solicitud', null=True, blank=True)
	tipo_giro_datoseconomicos = models.ForeignKey('Base.TipoGiro', on_delete=models.CASCADE, verbose_name='Tipo de Giro', null=True, blank=True)
	fecha_balance_datoseconomicos = models.ForeignKey('Base.FechaBalance', on_delete=models.CASCADE, verbose_name='Fecha de Balance', null=True, blank=True)
	tipo_contribuyente_datoseconomicos = models.ForeignKey('Base.TipoContribuyente', on_delete=models.CASCADE, verbose_name='Tipo de Contribuyente', null=True, blank=True)
	actividad_agropecuaria_datoseconomicos = models.BooleanField(default=False, help_text='¿La Empresa tiene Actividad Agropecuaria?', verbose_name='¿La Empresa tiene Actividad Agropecuaria?')
	proyectos_previos_datoseconomicos = models.BooleanField(default=False, help_text='Ya cuenta con proyectos de inversión presentados ante la COMAP', verbose_name='Ya cuenta con proyectos de inversión presentados ante la COMAP')

	empresa_nueva_empresanueva = models.BooleanField(default=False, help_text='¿Es empresa nueva?', verbose_name='¿Es empresa nueva?')
	sin_facturacion_ult3ej_empresanueva = models.BooleanField(default=False, help_text='¿Sin facturación ultimos 3 ejercicios?', verbose_name='¿Sin facturación ultimos 3 ejercicios?')
	empresa_vinculada_empresanueva = models.BooleanField(default=False, help_text='¿Se encuentra vinculada con otras empresas?', verbose_name='¿Se encuentra vinculada con otras empresas?')
	empresa_vinculada_sin_factult3ej_empresanueva = models.BooleanField(default=False, help_text='¿Empresas vinculadas sin facturación en los últimos 3 ejercicios?', verbose_name='¿Empresas vinculadas sin facturación en los últimos 3 ejercicios?')

	pyme_mype = models.BooleanField(default=False, help_text='¿Es PYME?', verbose_name='¿Es PYME?')
	cantidad_empleados_mype = models.DecimalField(max_digits=20, decimal_places=6, help_text='Cantidad de Empleados', verbose_name='Cantidad de Empleados')
	ventas_netas_UI_mype = models.DecimalField(max_digits=20, decimal_places=6, help_text='Ventas Netas en UI', verbose_name='Ventas Netas en UI')
	ventas_netas_pesos_mype = models.DecimalField(max_digits=20, decimal_places=6, help_text='Ventas Netas en $', verbose_name='Ventas Netas en $')
	controlada_mype = models.BooleanField(default=False, help_text='¿Esta Controlada?', verbose_name='¿Esta Controlada?')
	controlada_superamyoe_mype = models.BooleanField(default=False, help_text='¿Empresa Controlante Supera los limites de MYPE?', verbose_name='¿Empresa Controlante Supera los limites de MYPE?')
	grupo_economico_mype = models.BooleanField(default=False, help_text='¿Pertenece a un Grupo Económico?', verbose_name='¿Pertenece a un Grupo Económico?')
	grupo_economico_supera_mype = models.BooleanField(default=False, help_text='¿El Grupo Económico supera los limites de MYPE?', verbose_name='¿El Grupo Económico supera los limites de MYPE?')
	proyeccion_cantidad_empleados_mype = models.DecimalField(max_digits=20, decimal_places=6, help_text='Proyección de Cantidad de empleos ejercicio siguiente a inicio de actividad', verbose_name='Proyección de Cantidad de empleos ejercicio siguiente a inicio de actividad')
	proyeccion_ventas_netas_UI_mype = models.DecimalField(max_digits=20, decimal_places=6, help_text='Proyección de Ventas netas en UI ejercicio siguiente inicio de actividad', verbose_name='Proyección de Ventas netas en UI ejercicio siguiente inicio de actividad')
	credito_fiscal_aportes_patronales_mype = models.BooleanField(default=False, help_text='¿Aplica crédito fiscal por aportes patronales de artículo 28º?', verbose_name='¿Aplica crédito fiscal por aportes patronales de artículo 28º?')
	usuario_parque_industrial_mype = models.BooleanField(default=False, help_text='¿Usuario de Parque Industrial?', verbose_name='¿Usuario de Parque Industrial?')

	objetivo_proyecto = models.CharField(max_length=50, help_text='Objetivo del Proyecto', verbose_name='Objetivo del Proyecto', null=True, blank=True)
	informacion_ampliada_proyecto = models.TextField(max_length=50, help_text='Informacion ampliada del Proyecto', verbose_name='Informacion ampliada del Proyecto', null=True, blank=True)
	extension_plazo_proyecto = models.BooleanField(default=False, help_text='¿Solicita extensión de plazo por lit a) artículo 4º?', verbose_name='¿Solicita extensión de plazo por lit a) artículo 4º?')
	anos_ejecucion_inversion_proyecto = models.IntegerField(help_text='Años de ejecución de inversión', verbose_name='Años de ejecución de inversión')

	class Meta:
		verbose_name = 'Solicitud143_Step1'
		verbose_name_plural = 'Solicitud143_Step1'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step1b(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	direccion = models.CharField(max_length=50, help_text='Direccion de la Localizacion', verbose_name='Direccion', null=True, blank=True)
	numero_padron = models.CharField(max_length=50, help_text='Numero de Padron', verbose_name='Numero de Padron', null=True, blank=True)
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, help_text='Departamento', verbose_name='Departamento')
	localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, help_text='Localidad', verbose_name='Localidad')
	localidad_ya_operaciones = models.BooleanField(default=False, help_text='¿Localidad donde ya se realizaban operaciones?', verbose_name='¿Localidad donde ya se realizaban operaciones?')
	mejoras_fijas = models.BooleanField(default=False, help_text='¿Tiene mejoras fijas?', verbose_name='¿Tiene mejoras fijas?')
	plazo_remanente_proyecto = models.IntegerField(help_text='Plazo remanente del contrato', verbose_name='Plazo remanente del contrato')
	vinculacion_juridica_proyecto = models.CharField(max_length=50, help_text='Vinculacion Juridica', verbose_name='Vinculacion Juridica', null=True, blank=True)

	class Meta:
		verbose_name = 'Solicitud143_Step1b'
		verbose_name_plural = 'Solicitud143_Step1b'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ministerio_evaluador = models.ForeignKey(Ministerios, on_delete=models.CASCADE, help_text='Ministerio Evaluador', verbose_name='Ministerio Evaluador', null=True, blank=True)
	
	class Meta:
		verbose_name = 'Solicitud143_Step2'
		verbose_name_plural = 'Solicitud143_Step2'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ministerio_evaluador = models.ForeignKey(Ministerios, on_delete=models.CASCADE, help_text='Ministerio Evaluador', verbose_name='Ministerio Evaluador', null=True, blank=True)
	
	class Meta:
		verbose_name = 'Solicitud143_Step2'
		verbose_name_plural = 'Solicitud143_Step2'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2b(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_gral_empleo = models.BooleanField(default=False, help_text='Generación de empleo', verbose_name='Generación de empleo')
	ind_gral_exportaciones = models.BooleanField(default=False, help_text='Aumento de exportaciones (en US$)', verbose_name='Aumento de exportaciones (en US$)')
	ind_gral_descentralizacion = models.BooleanField(default=False, help_text='Descentralización', verbose_name='Descentralización')
	ind_gral_TL = models.BooleanField(default=False, help_text='Utilización de tecnologías limpias', verbose_name='Utilización de tecnologías limpias')
	ind_gral_IDi = models.BooleanField(default=False, help_text='Incremento de investigación, desarrollo e innovación (I+D+i)', verbose_name='Incremento de investigación, desarrollo e innovación (I+D+i)')
	
	class Meta:
		verbose_name = 'Solicitud143_Step2b'
		verbose_name_plural = 'Solicitud143_Step2b'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2c(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_sect_FCC = models.BooleanField(default=False, help_text='Formación continua y capacitación', verbose_name='Formación continua y capacitación')
	ind_sect_DPP = models.BooleanField(default=False, help_text='Diferenciación de productos y procesos', verbose_name='Diferenciación de productos y procesos')
	ind_sect_ERV = models.BooleanField(default=False, help_text='Energías renovables de vanguardia', verbose_name='Energías renovables de vanguardia')
	ind_sect_DMC = models.BooleanField(default=False, help_text='Desarrollo de mercado de capitales', verbose_name='Desarrollo de mercado de capitales')
	
	class Meta:
		verbose_name = 'Solicitud143_Step2c'
		verbose_name_plural = 'Solicitud143_Step2c'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2d(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_sect_NTPE = models.BooleanField(default=False, help_text='Nivel Tecnológico del producto elaborado', verbose_name='Nivel Tecnológico del producto elaborado')
	ind_sect_STE = models.BooleanField(default=False, help_text='Sectores y tecnologías estrategicos', verbose_name='Sectores y tecnologías estrategicos')
	ind_sect_SIN = models.BooleanField(default=False, help_text='Sello de la Industria Nacional', verbose_name='Sello de la Industria Nacional')
	ind_sect_FCC = models.BooleanField(default=False, help_text='Formación continua y capacitación', verbose_name='Formación continua y capacitación')
	ind_sect_ERV = models.BooleanField(default=False, help_text='Energías renovables de vanguardia', verbose_name='Energías renovables de vanguardia')
	ind_sect_DMC = models.BooleanField(default=False, help_text='Desarrollo de mercado de capitales', verbose_name='Desarrollo de mercado de capitales')
	
	class Meta:
		verbose_name = 'Solicitud143_Step2d'
		verbose_name_plural = 'Solicitud143_Step2d'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2e(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_sect_SI = models.BooleanField(default=False, help_text='Servicios e Infraestructura', verbose_name='Servicios e Infraestructura')
	ind_sect_CES = models.BooleanField(default=False, help_text='Certificación de edificios sostenibles', verbose_name='Certificación de edificios sostenibles')
	ind_sect_FCC = models.BooleanField(default=False, help_text='Formación continua y capacitación', verbose_name='Formación continua y capacitación')
	ind_sect_ERV = models.BooleanField(default=False, help_text='Energías renovables de vanguardia', verbose_name='Energías renovables de vanguardia')
	ind_sect_DMC = models.BooleanField(default=False, help_text='Desarrollo de mercado de capitales', verbose_name='Desarrollo de mercado de capitales')
	
	class Meta:
		verbose_name = 'Solicitud143_Step2e'
		verbose_name_plural = 'Solicitud143_Step2e'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2f(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_sect_ACC = models.BooleanField(default=False, help_text='Inversiones en adaptación al cambio climático', verbose_name='Inversiones en adaptación al cambio climático')
	ind_sect_DPP = models.BooleanField(default=False, help_text='Diferenciación de productos y procesos', verbose_name='Diferenciación de productos y procesos')
	ind_sect_FCC = models.BooleanField(default=False, help_text='Formación continua y capacitación', verbose_name='Formación continua y capacitación')
	ind_sect_ERV = models.BooleanField(default=False, help_text='Energías renovables de vanguardia', verbose_name='Energías renovables de vanguardia')
	ind_sect_DMC = models.BooleanField(default=False, help_text='Desarrollo de mercado de capitales', verbose_name='Desarrollo de mercado de capitales')
	
	class Meta:
		verbose_name = 'Solicitud143_Step2f'
		verbose_name_plural = 'Solicitud143_Step2f'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente