from django.shortcuts import render
from .forms import String,Contact,Emprecords,Scform
from .models import Empreco

# Create your views here.
def sc(request):
    if request.method=='POST':
        form=Scform(request.POST)
        if form.is_valid():
            charstring=form.cleaned_data['char_string']
            intstring=form.cleaned_data['int_string']
            context={
                'charstring':charstring,
                'intstring':intstring
            }
        return render(request,'app/index.html',context)
    else:
        form=Scform()
    return render(request,'app/form.html',{'form':form})

def contact(request):
    if request.method=='POST':
        form=String(request.POST)
        if form.is_valid():
            string1=form.cleaned_data['string1']
            string2=form.cleaned_data['string2']
            fstring=string1+ " " +string2
            lstring=" ".join([string1,string2])
            operator=("%s %s" %(string1,string2))
            frmt="{} {}".format(string1,string2)
            return render(request,'app/index.html',{'fstring':fstring,'lstring':lstring,'operator':operator,'frmt':frmt})
    else:
        form=String()
    return render(request,'app/form.html',{'form':form})

def contactstring(request):
    if request.method=='POST':
        form=Contact(request.POST)
        if form.is_valid():
            charstring=form.cleaned_data['char_string']
            intstring=form.cleaned_data['int_string']
            fullstring="{} {}".format(charstring,intstring)
            return render(request,'app/index.html',{'fullstring':fullstring})
    else:
        form=String()
    return render(request,'app/form.html',{'form':form})

def empreco(request):
    if request.method=='POST':
        form=Emprecords(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            data=Empreco(first_name=first_name,last_name=last_name,email=email)
            data.save()
            fullname=first_name+ " " +last_name
            return render(request,'app/index.html',{'fullname':fullname})
    else:
        form=Emprecords()
    return render(request,'app/form.html',{'form':form})