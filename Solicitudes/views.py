from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import FormStepOne, FormStepTwo, SolicitudesStep1_Form, SolicitudesStep1b_Form, SolicitudesStep2_Form, SolicitudesStep2b_Form, SolicitudesStep2c_Form, SolicitudesStep2d_Form, SolicitudesStep2e_Form, SolicitudesStep2f_Form
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.mixins import LoginRequiredMixin


#Para API
from rest_framework import generics
from .models import *
from .serializers import SolicitudesSerializer


# Create your views here.
class FormWizardView(LoginRequiredMixin, SessionWizardView):
	template_name = "solicitudes.html"
	form_list = [SolicitudesStep1_Form, SolicitudesStep1b_Form, SolicitudesStep2_Form, SolicitudesStep2b_Form, SolicitudesStep2c_Form, SolicitudesStep2d_Form, SolicitudesStep2e_Form, SolicitudesStep2f_Form]

	def get_form_initial(self, step):
		initial = {}
		print(self, step)
		return self.initial_dict.get(step, initial)

	def dispatch(self, request, pk, *args, **kwargs):
		try:
			form_1 = Solicitud143_Step1.objects.get(num_expediente=pk)
		except Exception as e:
			form_1 = {}		
		try:
			form_2 = Solicitud143_Step1b.objects.get(num_expediente=pk)
		except Exception as e:
			form_2 = {}
		try:
			form_3 = Solicitud143_Step2.objects.get(num_expediente=pk)
		except Exception as e:
			form_3 = {}
		try:
			form_4 = Solicitud143_Step2b.objects.get(num_expediente=pk)
		except Exception as e:
			form_4 = []
		try:
			form_5 = Solicitud143_Step2c.objects.get(num_expediente=pk)
		except Exception as e:
			form_5 = {}
		try:
			form_6 = Solicitud143_Step2d.objects.get(num_expediente=pk)
		except Exception as e:
			form_6 = {}
		try:
			form_7 = Solicitud143_Step2e.objects.get(num_expediente=pk)
		except Exception as e:
			form_7 = {}
		try:
			form_8 = Solicitud143_Step2f.objects.get(num_expediente=pk)
		except Exception as e:
			form_8 = {}

		self.instance_dict = {
			'0': form_1,
			'1': form_2,
			'2': form_3,
			'3': form_4,
			'4': form_5,
			'5': form_6,
			'6': form_7,
			'7': form_8,
		}
		return super(FormWizardView, self).dispatch(request, *args, **kwargs)
	
	# def get_form_initial(self, step):
	# 	if 'num_expediente' in self.kwargs:
	# 		return {}
	# 	return self.initial_dict.get(step, {})

	# def get_form_instance(self, step):
	# 	if not self.instance:
	# 		if 'num_expediente' in self.kwargs:
	# 			num_expediente = self.kwargs['num_expediente']
	# 			self.instance = form_list.objects.get(id=num_expediente)
	# 		else:
	# 			self.instance = form_list()
	# 	return self.instance 
    
	#def done(self, form_list, **kwargs):
	def done(self, form_list, form_dict, **kwargs):
		#SolicitudesStep1 = SolicitudesStep1_Form.save(commit=False)
		#SolicitudesStep1.save()
		#[form.save(commit=True) for form in form_list]
		for form in form_list:
			form.save(commit=False)
			form.instance.uc = self.request.user
			form.save()
		#SolicitudesStep1b = SolicitudesStep1b_Form.save(commit=False)
		#SolicitudesStep1b.user = self.request.user
		#SolicitudesStep1b.SolicitudesStep1 = SolicitudesStep1
		#SolicitudesStep1b.save()

		return render(self.request, 'solicitud_ok.html', {
			'form_data': [form.cleaned_data for form in form_list],
		})


class SolicitudesList(generics.ListCreateAPIView):
	queryset = Solicitud143_Step1.objects.all()
	serializer_class = SolicitudesSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk = self.kwargs['pk'],
		)
		return obj