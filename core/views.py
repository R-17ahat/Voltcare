
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomerRegistrationForm, ComplaintForm
from .models import Complaint


# HOMEPAGE
def home(request):
    return render(request, 'core/index.html')


# CUSTOMER REGISTRATION
def register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')

    else:
        form = CustomerRegistrationForm()

    return render(request, 'core/register.html', {
        'form': form
    })


# CUSTOMER LOGIN
def customer_login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')

    else:
        form = AuthenticationForm()

    form.fields['username'].widget.attrs.update({
        'class': 'form-input',
        'placeholder': 'Enter your username'
    })

    form.fields['password'].widget.attrs.update({
        'class': 'form-input',
        'placeholder': 'Enter your password'
    })

    return render(request, 'core/login.html', {
        'form': form
    })


# CUSTOMER DASHBOARD
@login_required(login_url='login')
def customer_dashboard(request):

    complaints = Complaint.objects.filter(
        customer=request.user
    ).order_by('-created_at')

    total_complaints = complaints.count()

    pending_complaints = complaints.exclude(
        status__in=['resolved', 'closed']
    ).count()

    resolved_complaints = complaints.filter(
        status__in=['resolved', 'closed']
    ).count()

    recent_complaints = complaints[:5]

    return render(request, 'core/dashboard.html', {
        'total_complaints': total_complaints,
        'pending_complaints': pending_complaints,
        'resolved_complaints': resolved_complaints,
        'complaints': recent_complaints,
    })


# SUBMIT COMPLAINT
@login_required(login_url='login')
def submit_complaint(request):

    if request.method == 'POST':
        form = ComplaintForm(request.POST)

        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.customer = request.user
            complaint.save()

            messages.success(
                request,
                f'Your complaint was submitted successfully. '
                f'Your Complaint ID is {complaint.complaint_id}.'
            )

            return redirect('dashboard')

    else:
        form = ComplaintForm()

    return render(request, 'core/submit_complaint.html', {
        'form': form
    })


# TRACK COMPLAINT
@login_required(login_url='login')
def track_complaint(request):

    complaint = None
    error = None

    # GET: Read Complaint ID from the Track link
    complaint_id = request.GET.get(
        'complaint_id', ''
    ).strip().upper()

    # POST: Read Complaint ID from the search form
    if request.method == 'POST':
        complaint_id = request.POST.get(
            'complaint_id', ''
        ).strip().upper()

    if complaint_id:

        try:
            complaint = Complaint.objects.get(
                complaint_id__iexact=complaint_id,
                customer=request.user
            )

        except Complaint.DoesNotExist:
            error = 'No complaint was found with this ID.'

    elif request.method == 'POST':
        error = 'Please enter your Complaint ID.'

    return render(request, 'core/track_complaint.html', {
        'complaint': complaint,
        'error': error,
        'complaint_id': complaint_id,
    })


# CUSTOMER COMPLAINT HISTORY
@login_required(login_url='login')
def complaint_history(request):

    complaints = Complaint.objects.filter(
        customer=request.user
    ).order_by('-created_at')

    total_complaints = complaints.count()

    pending_complaints = complaints.exclude(
        status__in=['resolved', 'closed']
    ).count()

    resolved_complaints = complaints.filter(
        status__in=['resolved', 'closed']
    ).count()

    return render(request, 'core/complaint_history.html', {
        'complaints': complaints,
        'total_complaints': total_complaints,
        'pending_complaints': pending_complaints,
        'resolved_complaints': resolved_complaints,
    })


# CUSTOMER LOGOUT
def customer_logout(request):

    if request.method == 'POST':
        logout(request)

    return redirect('home')
