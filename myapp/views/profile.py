# views.py

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from myapp.forms import UserUpdateForm, ProfileUpdateForm
from myapp.models import Profile, Transaction

@login_required
def profile(request):
    try:
        profile_instance = request.user.profile
    except ObjectDoesNotExist:
        profile_instance = None

    if request.method == 'POST':
        if 'update_profile' in request.POST:
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_instance)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                if profile_instance:
                    profile_form.save()
                else:
                    profile_form.instance.user = request.user
                    profile_form.save()
                return redirect('profile')
        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile_instance)
        password_form = PasswordChangeForm(user=request.user)

    transactions = Transaction.objects.filter(user=request.user)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form,
        'email': request.user.email,
        'transactions': transactions,
    }
    return render(request, 'myapp/profile.html', context)
