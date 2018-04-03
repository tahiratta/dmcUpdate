from django.shortcuts import render, redirect
from dmc.models import Menu, Sub_menu, Video_slider, Product, Sub_product, About, Service, Document,Form
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm, DocumentForm
from django.core.files.storage import FileSystemStorage

import os

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders


def index(request):
	mindex = Menu.objects.all()
	smindex = Sub_menu.objects.all()
	vslindex = Video_slider.objects.all()
	pindex = Product.objects.all()
	spindex = Sub_product.objects.all()
	sindex = Service.objects.all()
	findex = Form.objects.all()
	context = {'mindex' : mindex, 'smindex' : smindex,'sindex': sindex, 'vslindex' : vslindex, 'pindex' : pindex, 'spindex' : spindex, 'findex':findex }
	return render(request, 'index.html', context)

def contact(request):
	mindex = Menu.objects.all()
	smindex = Sub_menu.objects.all()
	findex = Form.objects.all()

	title = 'Contact Us'
	form = contactForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		name = form.cleaned_data['name']
		email = form.cleaned_data['email']
		message = form.cleaned_data['message']
		subject = form.cleaned_data['subject']
		comment = '%s %s %s %s' %(email, name, subject, message)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, comment,emailFrom, emailTo, fail_silently=True)
		title = "Thanks!"
		confirm_message = "Thanks for the message, we will right back to you."
		form = None
		
	context = {'mindex' : mindex, 'smindex' : smindex, 'title':title, 'form': form, 'confirm_message': confirm_message, 'findex':findex}
	return render(request, 'contact.html', context)

def about(request):
	mindex = Menu.objects.all()
	smindex = Sub_menu.objects.all()
	abindex = About.objects.all()
	findex = Form.objects.all()
	context = {'mindex' : mindex, 'smindex' : smindex,  'abindex' : abindex, 'findex':findex}
	return render(request, 'about.html', context)

def products(request):
	mindex = Menu.objects.all()
	smindex = Sub_menu.objects.all()
	pindex = Product.objects.all()
	spindex = Sub_product.objects.all()
	findex = Form.objects.all()
	context = {'mindex' : mindex, 'smindex' : smindex, 'pindex' : pindex, 'spindex' : spindex, 'findex':findex }
	return render(request, 'portfolio.html', context)

def services(request):
	mindex = Menu.objects.all()
	smindex = Sub_menu.objects.all()
	sindex = Service.objects.all()
	findex = Form.objects.all()
	context = {'mindex' : mindex, 'smindex' : smindex, 'sindex': sindex, 'findex':findex}
	return render(request, 'services.html', context)			

def certificate(request):
	mindex = Menu.objects.all()
	smindex = Sub_menu.objects.all()
	findex = Form.objects.all()
	context = {'mindex' : mindex, 'smindex' : smindex, 'findex':findex}
	return render(request, 'certificate.html', context)	

def careers(request):
		mindex = Menu.objects.all()
		smindex = Sub_menu.objects.all()
		dindex = Document.objects.all()
		findex = Form.objects.all()
		title = 'Careers'
		form = DocumentForm(request.POST or None, request.FILES or None)
		confirm_message = None

		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			subject = form.cleaned_data['subject']
			document = form.cleaned_data['document']
			myfile = request.FILES['document']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.url(filename)

			comment = '%s %s %s %s %s' %(email,name,subject,(message),document)
			emailFrom = form.cleaned_data['email']
			emailTo = [settings.EMAIL_HOST_USER_NAME]
			send_mail(subject, comment,emailFrom, emailTo, fail_silently=True)
			form.save()
			title = "Thanks!"
			confirm_message = "Thanks for the message, we will right back to you."
			form = None
			context = {'mindex' : mindex, 'smindex' : smindex, 'title':title, 'form': form, 'confirm_message': confirm_message, 'dindex':dindex}
			return render(request, 'careers.html',context)
			
		context = {'mindex' : mindex, 'smindex' : smindex, 'title':title, 'form': form, 'confirm_message': confirm_message, 'dindex':dindex, 'findex':findex}
		return render(request, 'careers.html', context)
		# attachement = open(filename, 'rb')
		# part = MIMEBase('application', 'octet-stream')
		# part.set_payload((attachement).read())
		# encoders.encode_base64(part)
		# part.add_header('Content-Disposition', "attachment; filename =" +filename)
		# msg.attach(part)
		# text = msg.as_string()

def pdfs(request):
	mindex = Menu.objects.all()
	smindex = Sub_menu.objects.all()
	dindex = Document.objects.all()
	findex = Form.objects.all()
	context = {'mindex' : mindex, 'smindex' : smindex,'dindex':dindex, 'findex':findex}
	return render(request, 'pdfs.html', context)			
		

def marketWatch(request):
	mindex = Menu.objects.all()
	smindex = Sub_menu.objects.all()
	findex = Form.objects.all()

	context = {'mindex' : mindex, 'smindex' : smindex, 'findex':findex}
	return render(request, 'marketWatch.html', context)		

# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('careers')
#     else:
#         form = DocumentForm()
#     return render(request, 'model_form_upload.html', {
#         'form': form
#     })	