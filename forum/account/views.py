from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


# @login_required
# def edit(request):
#     user_edit_form = UserEditForm()
#     profile_form = ProfileEditForm()
#     if request.method == 'POST':
#         user_edit_form = UserEditForm(instance=request.user,
#                                  data=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile,
#                                        data=request.POST,
#                                        files=request.FILES)
#         if user_edit_form.is_valid() and profile_form.is_valid():
#             user_edit_form.save()
#             profile_form.save()
#         else:
#             user_edit_form = UserEditForm(instance=request.user)
#             profile_form = profile_form(instance=request.user.profile)
#     return render(request, 
#                   'account/edit.html',
#                   {'user_edit_form': user_edit_form,
#                    'profile_form': profile_form})