import os
from django.template import loader, Context
from django.conf import settings
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from sass_processor.processor import sass_processor

font_config = FontConfiguration()
css_path = settings.RUN_DIR + sass_processor('scss/pdf.scss')
css = CSS(filename=css_path, font_config=font_config)

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
    return doc.write_pdf(stylesheets=[css], font_config=font_config)
