from django.http import HttpResponse
from django.views.generic import FormView
from .render import render_request
from .forms import RequestForm

class RequestView(FormView):
    template_name = 'request.html'
    form_class = RequestForm
        
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            pdf = render_request(form)
            filename = 'Auskunftsbegehren_{0}.pdf'.format(form.full_name.replace(' ', '_'))

            response = HttpResponse(pdf,
                status=200,
                content_type='application/pdf',
            )
            response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
            return response
        else:
            return self.form_invalid(form)
            