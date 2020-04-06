import os
from django.template import loader, Context
from django.conf import settings

from weasyprint import HTML, CSS
from sass_processor.processor import sass_processor

def render_request(form):
    tmpl = loader.get_template('request/ams_request.html')
    rendered = tmpl.render({
        'name': form.full_name,
        'address': form.cleaned_data['address'],
        'zipcode': form.cleaned_data['zipcode'],
        'municipality': form.cleaned_data['municipality'],
        'email': form.cleaned_data['email'],
    })

    doc = HTML(string=rendered)
    css_path = settings.RUN_DIR + sass_processor('scss/pdf.scss')
    return doc.write_pdf(stylesheets=[CSS(filename=css_path)])
