from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView


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


class CustomDeleteView(SuccessMessageMixin, DeleteView):
    success_message = ''
    unsuccess_message = ''


    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, self.unsuccess_message)
            return redirect(self.success_url)
        else:
            messages.success(self.request, self.success_message)
            return redirect(self.success_url)


class HandleNoPermissionMixin(object):

    def handle_no_permission(self):
        messages.error(self.request, self.restriction_message)
        return redirect(self.redirect_url_while_restricted)