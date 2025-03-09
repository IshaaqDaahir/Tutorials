from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm

# Create your views here.

class CourseObjectMixin(object):
    model = Course

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj

class CourseDeleteView(CourseObjectMixin, View):
    template_name = 'courses/course_delete.html'
    
    def get(self, request, id=None):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['obj'] = obj
        return render(request, self.template_name, context)
    
    def post(self, request, id=None):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['obj'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)

class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'
    
    def get(self, request, id=None):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['obj'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
    
    def post(self, request, id=None):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['obj'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    def get(self, request):
        form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    qs = Course.objects.all()

    def get_queryset(self):
        return self.qs
    
    def get(self, request):
        context = {'obj_list': self.get_queryset()}
        return render(request, self.template_name, context)

class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None):
        context = {'obj': self.get_object()}
        return render(request, self.template_name, context)

def my_fbv(request):
    print(request.method)
    return render(request, 'courses/about.html', {})
