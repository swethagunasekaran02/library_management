from django.shortcuts import render, get_object_or_404, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

def member_list(request):
    members = Member.objects.all()
    return render(request, 'customer/member_list.html', {'members': members})

def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'customer/member_detail.html', {'member': member})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member registered successfully!')
            return redirect('customer:member_list') 
    else:
        form = MemberForm()
    return render(request, 'customer/member_form.html', {'form': form, 'title': 'Add Member'})

def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member updated successfully!')
            return redirect('customer:member_detail', pk=member.pk) 
    else:
        form = MemberForm(instance=member)
    return render(request, 'customer/member_form.html', {'form': form, 'title': 'Edit Member'})
