from django.shortcuts import render, redirect

from retake.common.forms import ProfileCreateForm, EventCreateForm, ProfileEditForm, ProfileDeleteForm
from retake.common.models import ProfileModel, EventModel


def get_profile():
    try:
        return ProfileModel.objects.first()
    except ProfileModel.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'shared/home-page.html', context)


def dashboard(request):
    profile = get_profile()
    events = EventModel.objects.all()
    context = {
        'profile': profile,
        'events': events,
    }
    return render(request, 'events/dashboard.html', context)


def profile_create(request):
    profile = get_profile()

    if not profile:
        form = ProfileCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'profile': profile,
            'form': form,
        }
        return render(request, 'profiles/profile-create.html', context)


def profile_edit(request):
    profile = get_profile()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile_details')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profiles/profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    event = EventModel.objects.all()
    form = ProfileDeleteForm(request.POST or None, instance=profile)
    if request.method == 'POST':
        profile.delete()
        event.delete()
        return redirect('index')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profiles/profile-delete.html', context)


def profile_details(request):
    profile = get_profile()
    evens_count = EventModel.objects.all().count()
    context = {
        'profile': profile,
        'evens_count': evens_count,
    }
    return render(request, 'profiles/profile-details.html', context)


def create_event(request):
    profile = get_profile()
    form = EventCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'events/event-create.html', context)


def edit_event(request, pk):
    profile = get_profile()
    event = EventModel.objects.get(pk=pk)
    form = EventCreateForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form,
        'profile': profile,
        'event': event,
    }
    return render(request, 'events/event-edit.html', context)


def details_event(request, pk):
    profile = get_profile()
    event = EventModel.objects.get(pk=pk)
    context = {
        'profile': profile,
        'event': event,
    }
    return render(request, 'events/events-details.html', context)


def delete_event(request, pk):
    profile = get_profile()
    event = EventModel.objects.get(pk=pk)
    form = EventCreateForm(request.POST or None, instance=event)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True
    if request.method == 'POST':
        event.delete()
        return redirect('dashboard')
    context = {
        'form': form,
        'profile': profile,
        'event': event,
    }
    return render(request, 'events/events-delete.html', context)
