import json
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, UpdateUserForm
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from .models import CustomUser

"""
Contains code for loading data into views
"""


class HomepageView(TemplateView):
    """
    Handles the base URL route to display a map
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["markers"] = json.loads(serialize("geojson",
                                                  CustomUser.objects.all()))
        return context


class RegisterView(View):
    """
    Handles the registration and auth redirection
    """

    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Redirects users after being registered
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        # will redirect to the home page if a user tries to
        # access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """"
        Displays the registration page
        """

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """
        Takes in data for new registrations
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


"""
Class based view that extends from the built in login view
to add a remember me functionality
"""


class CustomLoginView(LoginView):
    """
    Handles authentication
    """

    form_class = LoginForm

    def form_valid(self, form):
        """
        Checks if login form data is valid
        :param form:
        :return:
        """

        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically
            # close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time
        # "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


@login_required
def profile(request):
    """
    Updates and displays user profiles
    :param request:
    :return:
    """
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='user-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'profile.html', {'user_form': user_form})
