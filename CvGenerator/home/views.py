from django.shortcuts import render,redirect
from . models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.
def indexPage(request):
    return render(request,'index.html')

def acceptPage(request):
    request.session.flush()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        address=request.POST.get("personal_address")
        summary=request.POST.get("summary")
        degree=request.POST.get("degree")
        pg=request.POST.get("pg")
        school=request.POST.get("school")
        language=request.POST.get("language")
        skills=request.POST.get("skills")
        experience=request.POST.get("experience")
        request.session['name']=name
        
        form=Profile(
            name=name,
            email=email,
            phone=phone,
            address=address,
            summary=summary,
            degree=degree,
            pg=pg,
            school=school,
            language=language,
            skills=skills,
            experience=experience
        )
        form.save()
        return redirect(resumePage)
    return render(request,'accept.html')

def resumePage(request):
    uname = request.session.get('name')
    if uname:
        user_profile = Profile.objects.filter(name=uname)
    
        if user_profile.exists():  # Check if the profile exists
            template = loader.get_template('resume.html')
            html = template.render({'user_profile': user_profile})
            
            options = {
                'page-size': 'Letter',
                'encoding': 'UTF-8',
            }
            
            pdf = pdfkit.from_string(html, False, options)
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "resume.pdf"
            
            # Ensure the filename is included in the Content-Disposition header
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            return response
        else:
            return HttpResponse("No profile found", status=404)
    else:
        return HttpResponse("User not logged in", status=403)
