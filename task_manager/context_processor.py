from statuses.forms import StatusForm
from tasks.forms import TaskForm
from labels.forms import LabelForm

def get_form_status(request):
    context = {
        'add_s': StatusForm
    }
    return context


def get_form_tasks(request):
    context = {
        'add_t': TaskForm
    }
    return context

def get_form_labels(request):
    context = {
        'add_l': LabelForm
    }
    return context