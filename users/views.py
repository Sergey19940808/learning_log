# imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.core import signing
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from . forms import EmailForm, FirstNameLastNameForm




# views for show page user
@login_required
def user(request, user_id):
    title = 'Страница пользователя'
    user = get_object_or_404(User, id=user_id)
    context = {'title': title, 'user': user}
    return render(request, 'users/user.html', context)




# views for resend email with confirmation account
def resend_activation_email(request):

    email_body_template = 'registration/activation_email.txt'
    email_subject_template = 'registration/activation_email_subject.txt'

    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    context = {}

    form = None
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            users = User.objects.filter(email=email, is_active=0)

            if not users.count():
                form._errors['email'] = ["Пользователь с таким адресом уже существует, придумайте другой."]

            REGISTRATION_SALT = getattr(settings, 'REGISTRATION_SALT', 'registration')
            for user in users:
                activation_key = signing.dumps(
                    obj=getattr(user, user.USERNAME_FIELD),
                    salt=REGISTRATION_SALT,
                    )
                context = {}
                context['activation_key'] = activation_key
                context['expiration_days'] = settings.ACCOUNT_ACTIVATION_DAYS
                context['site'] = get_current_site(request)

                subject = render_to_string(email_subject_template,
                                   context)
                # Force subject to a single line to avoid header-injection
                # issues.
                subject = ''.join(subject.splitlines())
                message = render_to_string(email_body_template,
                                           context)
                user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
                return render(request, 'registration/resend_activation_complete.html')

    if not form:
        form = EmailForm()

    context.update({'form' : form})
    return render(request, 'registration/resend_activation_email_form.html', context)


# views for change email
@login_required()
def email_change(request, user_id):
    title = 'Смена электронного адреса'
    user = get_object_or_404(User, id=user_id)

    if request.method != 'POST':
        form = EmailForm()

    else:
        form = EmailForm(data=request.POST)

        if form.is_valid():
            user.email = form.cleaned_data['email']
            user.save()
            return HttpResponseRedirect(reverse('users:user',
                                                args=[user.id]))

    context = {'title': title, 'user': user, 'form': form}
    return render(request, 'users/email_change_form.html', context)



# views for add first_name and last_name
@login_required()
def add_first_last_name(request, user_id):
    title = 'Добавлении имени и фамилии'
    user = get_object_or_404(User, id=user_id)

    if request.method != 'POST':
        form = FirstNameLastNameForm()

    else:
        form = FirstNameLastNameForm(data=request.POST)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return HttpResponseRedirect(reverse('users:user',
                                                args=[user.id]))

    context = {'title': title, 'form': form, 'user': user}
    return render(request, 'users/add_first_last_name.html', context)



# views for edit firstname and last_name
@login_required()
def edit_first_last_name(request, user_id):
    title = 'Редактирование имени и фамилии'
    user = get_object_or_404(User, id=user_id)

    if request.method != 'POST':
        form = FirstNameLastNameForm(instance=user)

    else:
        form = FirstNameLastNameForm(data=request.POST, instance=user)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return HttpResponseRedirect(reverse('users:user',
                                                args=[user.id]))

    context = {'title': title, 'form': form, 'user': user}
    return render(request, 'users/edit_first_last_name.html', context)



# delete_user
@login_required()
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect(reverse('learning_logs:index'))









