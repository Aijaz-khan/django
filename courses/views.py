
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render

from .models import Course, Step
from .forms import CourseForm


def course_create(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save
    context = {
        "form": form,
    }
    return render(request, "courses/course_form.html", context)

def course_update(request, pk):
    instance = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "description": instance.description,
        "form": form,
    }
    return render(request, "courses/course_form.html", context)

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})
