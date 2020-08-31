from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from .models import Lesson
from .forms import LessonForm

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class LessonListView(ListView):
    model = Lesson
    def video(self, request):
            obj=Lesson.object.id()
            return render(request, 'lesson_list.html',{'obj':obj})

class LessonDetailView(DetailView):
    model = Lesson
    def video(self, request):
            obj=Lesson.object.id()
            return render(request, 'lesson_detail.html',{'obj':obj})

@method_decorator(staff_member_required, name='dispatch')
class LessonCreate(CreateView):
    model = Lesson
    form_class = LessonForm
    success_url = reverse_lazy('lessons:lessons')

@method_decorator(staff_member_required, name='dispatch')
class LessonUpdate(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('lessons:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class LessonDelete(DeleteView):
    model = Lesson
    success_url = reverse_lazy('lessons:lessons')