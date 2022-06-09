from django.shortcuts import render, redirect
from django.views import View


class CustomAddForm(View):
    model = None
    form_to_post = None
    redirect_to = None

    def get(self, request):
        context = {
            'form': self.model
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_to_post(request.POST)

        if form.is_valid():
            form.save()
            return redirect(self.redirect_to)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
