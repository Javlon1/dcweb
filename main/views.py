from ast import Return
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import status
from django.http import Http404
from main.form import InfoForm
from main.models import *
from main.serializer import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login,logout




class InfoView(APIView): 
    def get(self, request):
        info = Info.objects.last()
        ser = InfoSerializer(info)

        return Response(ser.data)


class SliderView(APIView):

    def get(self, request):
        slider = Slider.objects.all().order_by('-id')[0:5]
        ser = SliderSerializer(slider, many=True)

        return Response(ser.data)


class ProjectsView(APIView):
    def get(self, request):
        projects = Projects.objects.all()
        ser = ProjectsSerializer(projects, many=True)

        return Response(ser.data)


class TechnoparkView(APIView):
    def get(self, request):
        technopark = Technopark.objects.all()[0:6]
        ser = TechnoparkSerializer(technopark, many=True)

        return Response(ser.data)


class SectionView(RetrieveAPIView):

    def retrieve(self, request, pk):
        section = Section.objects.get(id=pk)
        sec = SectionSerializer(section)
        return Response(sec.data)


class Postalservicesview(APIView):

    def get(self, request):
        pochta = Postalservices.objects.all().order_by('-id')
        ser = PostalservicesSerializer(pochta, many=True)

        return Response(ser.data)


class BoglanishView(APIView):
    def post(self, request):
        fullname = request.data['fullname']
        phone = request.data['phone']
        text = request.data['text']
        Boglanish.objects.create(fullname=fullname,phone=phone,text=text)

        return Response('отправлено ваша смс')


class MobileoperatorsView(APIView):

    def get(self, request):
        operator = Mobileoperators.objects.all().order_by('-id')
        ser = MobileoperatorsSerializer(operator, many=True)

        return Response(ser.data)


class InternetprovidersView(APIView):

    def get(self, request):
        providers = Internetproviders.objects.all().order_by('-id')
        ser = InternetprovidersSerializer(providers, many=True)

        return Response(ser.data)


class OurAudienceView(APIView):

    def get(self, request):
        audience = OurAudience.objects.all().order_by('-id')[0:5]
        ser = OurAudienceSerializer(audience, many=True)

        return Response(ser.data)


class PercentageView(APIView):

    def get(self, request):
        percentage = Percentage.objects.all().order_by('-id')[0:4]
        ser = PercentageSerializer(percentage, many=True)

        return Response(ser.data)


class ResidentsView(APIView):

    def get(self, request):
        residents = Residents.objects.all().order_by('-id')[0:5]
        ser = ResidentsSerializer(residents, many=True)

        return Response(ser.data)


class TeamView(APIView):

    def get(self, request):
        team = Team.objects.last()
        ser = TeamSerializer(team)

        return Response(ser.data)


class CoworkingView(APIView):
    def get(self, request):
        coworking = Coworking.objects.all().order_by('-id')[0:2]
        ser = CoworkingSerializer(coworking, many=True)

        return Response(ser.data)


class InfrastructureSliderView(APIView):
    def get(self, request):
        infrastructure = InfrastructureSlider.objects.all().order_by('-id')[0:6]
        ser = InfrastructureSliderSerializer(infrastructure, many=True)

        return Response(ser.data)


class StudyDirectionsView(APIView):

    def get(self, request):
        study = StudyDirections.objects.all().order_by('-id')[0:5]
        ser = StudyDirectionsSerializer(study, many=True)

        return Response(ser.data)

class ItAcademyView(APIView):

    def get(self, request):
        it_academy = ItAcademy.object.all().order_by('-id')[0:5]
        ser = ItAcademySerializer(it_academy, many=True)

        return Response(ser.data)


class StartupDirectionsView(ListAPIView):
    queryset = StartupDirections.objects.all()
    serializer_class = StartupDirectionsSerializer

    def list(self, request):
        incub = StartupDirections.objects.all().order_by("-id")[0:6]
        inc = StartupDirectionsSerializer(incub, many=True)
        return Response(inc.data)


class IncubationCentersView(ListAPIView):
    queryset = IncubationCenters.objects.all()
    serializer_class = IncubationCentersSerializer

    def list(self, request):
        incub = IncubationCenters.objects.all().order_by("-id")[0:4]
        inc = IncubationCentersSerializer(incub, many=True)
        return Response(inc.data)
 

class RaqamlashtirishxizmalariView(ListAPIView):
    queryset = Raqamlashtirishxizmalari.objects.all()
    serializer_class = RaqamlashtirishxizmalariSerializer

    def list(self, request):
        incub = Raqamlashtirishxizmalari.objects.all().order_by("-id")[0:4]
        inc = RaqamlashtirishxizmalariSerializer(incub, many=True)
        return Response(inc.data)


class ContactPost(APIView):

    def post(self, request):
        contact = ContactSerializer(data=request.data)
        if contact.is_valid():
            contact.save()
            return Response(contact.data, status=status.HTTP_201_CREATED)
        return Response(contact.errors, status=status.HTTP_400_BAD_REQUEST)


class XizmatTuriView(ListAPIView):
    queryset = XizmatTuri.objects.all()
    serializer_class = XizmatTuriSerializer

    def list(self, request):
        incub = XizmatTuri.objects.all().order_by("-id")
        inc = XizmatTuriSerializer(incub, many=True)
        return Response(inc.data)


class XizmatlarPost(APIView):

    def get(self, request):
        incub = Xizmatlar.objects.all().order_by("-id")
        inc = XizmatlarSerializer(incub, many=True)
        return Response(inc.data)



    def post(self, request):
        xizmat = XizmatlarSerializer(data=request.data)
        if xizmat.is_valid():
            xizmat.save()
            return Response(xizmat.data, status=status.HTTP_201_CREATED)
        return Response(xizmat.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def XizmatlarGet(request):
    xizmat = Xizmatlar.objects.all()

    a = []
    for i in xizmat:
        dat = {
            "Name": i.name,
            "Name_Ru": i.name_ru,
            "Name_En": i.name_en,
            "Text": i.xizmat.name,
            "Text_Ru": i.xizmat.name_ru,
            "Text_En": i.xizmat.name_en,
        }
        a.append(dat)
    return Response(a)





class ApplicationPost(APIView):

    def post(self, request):
        applicication = ApplicationSerializer(data=request.data)
        if applicication.is_valid():
            applicication.save()
            return Response(applicication.data, status=status.HTTP_201_CREATED)
        return Response(applicication.errors, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth.decorators import login_required


@login_required
def Home(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    contact = Contact.objects.all().order_by("-id")
    persentages = Percentage.objects.all().order_by("-id")
    img = Info.objects.last()
    context = {
        'contact':contact,
        'persentages':persentages,
        'img':img,
    }
    return render(request, 'home.html', context)
    

@login_required
def InfoTemplate(request):
    if request.user.is_authenticated:
        info = Info.objects.all().order_by('-id')
        img = Info.objects.last()
        context = {
        'info':info,
        'img':img,
        }
        return render(request, 'info.html', context)
    else:
        return redirect('login')

@login_required        
def InfoCreate(request):
    info = Info.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "info":info,
    }
    if request.method == "POST" and request.FILES:
        data = request.POST
        Info.objects.create(
            logo = request.FILES['logo'],
            short_phone = data.get('short_phone'),
            phone = data.get('phone'),
            email = data.get('email'),
            address = data.get('address'),
            address_ru = data.get('address_ru'),
            address_en = data.get('address_en'),
            lat = data.get('lat'),
            lng = data.get('lng')
        )
        return redirect('info')
    return render(request, 'infocreate.html', context)


@login_required
def InfoEdit(request, pk):
    img = Info.objects.last()
    info = Info.objects.get(id=pk)
    if request.method == "POST":
        info = Info.objects.get(id=pk)
        if 'logo' in request.FILES:
            info.logo = request.FILES['logo']
        
        info.short_phone = request.POST.get('short_phone')
        info.phone = request.POST.get('phone')
        info.email = request.POST.get('email')
        info.address = request.POST.get('address')
        info.address_ru = request.POST.get('address_ru')
        info.address_en = request.POST.get('address_en')
        info.lat = request.POST.get('lat')
        info.lng = request.POST.get('lng')
        info.save()
        return redirect('info')
    context = {
        'img':img,
        "info": info
    }
    return render(request, 'infoedit.html', context)

@login_required
def DeleteInfo(request, pk):
    info = Info.objects.get(id=pk)
    info.delete()
    return redirect('info')

@login_required
def SliderTemp(request):
    slider = Slider.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        'slider':slider,
    }
    return render(request, 'slider.html', context)

@login_required
def SliderCreate(request):
    slider = Slider.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "slider":slider,
    }
    if request.method == "POST":
        data = request.POST
        Slider.objects.create(
            video = request.FILES['video'],
            title = data.get('title'),
            title_ru = data.get('title_ru'),
            title_en = data.get('title_en'),
        )
        return redirect('slider')
    return render(request, 'slidercreate.html', context)


@login_required
def SliderEdit(request, pk):
    img = Info.objects.last()
    slider = Slider.objects.get(id=pk)
    if request.method == "POST":
        slider = Slider.objects.get(id=pk)
        if 'logo' in request.FILES:
            slider.video = request.FILES['logo']
        else:
            slider.video = request.POST.get('video')
        slider.title = request.POST.get('title')
        slider.title_ru = request.POST.get('title_ru')
        slider.title_en = request.POST.get('title_en')
        slider.save()
        return redirect('slider')
    context = {
        'img':img,
        "slider": slider
    }
    return render(request, 'slideredit.html', context)

@login_required
def DeleteSlider(request, pk):
    slider = Slider.objects.get(id=pk)
    slider.delete()
    return redirect('slider')

@login_required
def ProjectsTemp(request):
    projects = Projects.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "projects":projects
    }
    return render(request, "projects.html", context)

@login_required
def ProjectsCreate(request):
    projects = Projects.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "projects":projects,
    }
    if request.method == "POST":
        data = request.POST
        Projects.objects.create(
            image = request.FILES['image'],
            text = data.get('text'),
            text_en = data.get('text_en'),
            text_ru = data.get('text_ru'),
        )
        return redirect('projects')
    return render(request, 'projectscreate.html', context)

@login_required
def ProjectsEdit(request, pk):
    img = Info.objects.last()
    if request.method == "POST":
        projects = Projects.objects.get(id=pk)
        if 'logo' in request.FILES:
            projects.image = request.FILES['logo']
        else:
            projects.image = request.POST.get('image')
        projects.text = request.POST.get('text')
        projects.text_en = request.POST.get('text_en')
        projects.text_ru = request.POST.get('text_ru')
        projects.save()
        return redirect('projects')
    projects = Projects.objects.get(id=pk)
    context = {
        'img':img,
        "projects": projects
    }
    return render(request, 'projectsedit.html', context)

@login_required
def DeleteProjects(request, pk):
    projects = Projects.objects.get(id=pk)
    projects.delete()
    return redirect('projects') 
  

@login_required
def TechnoparkTemp(request):
    technopark = Technopark.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "technopark":technopark
    }
    return render(request, "technopark.html", context)

@login_required
def TechnoparkCreate(request):
    technopark = Technopark.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "technopark":technopark,
    } 
    if request.method == "POST":
        data = request.POST
        Technopark.objects.create(
            icon = request.FILES['icon'],
            text = data.get('text'),
            text_en = data.get('text_en'),
            text_ru = data.get('text_ru'),
            number = data.get('number'),
        )
        return redirect('technopark')
    return render(request, 'technoparkcreate.html', context)

@login_required
def TechnoparkEdit(request, pk):
    img = Info.objects.last()
    if request.method == "POST":
        technopark = Technopark.objects.get(id=pk)
        if 'icon' in request.FILES:
            technopark.icon = request.FILES['icon']
        technopark.text = request.POST.get('text')
        technopark.text_en = request.POST.get('text_en')
        technopark.text_ru = request.POST.get('text_ru')
        technopark.number = request.POST.get('number')
        technopark.save()
        return redirect('technopark')
    technopark = Technopark.objects.get(id=pk)
    context = {
        'img':img,
        "technopark": technopark
    }
    return render(request, 'technoparkedit.html', context)

@login_required
def DeleteTechnopark(request, pk):
    technopark = Technopark.objects.get(id=pk)
    technopark.delete()
    return redirect('technopark')


@login_required
def SectionTemp(request):
    section = Section.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "section":section
    }
    return render(request, "section.html", context)

@login_required
def DeleteSection(request, pk):
    section = Section.objects.get(id=pk)
    section.delete()
    return redirect("section")

@login_required
def SectionCreate(request):
    if request.method == "POST":
        data = request.POST
        Section.objects.create(
            image = request.FILES['image'],
            text = data.get('text'),
            text_en = data.get('text_en'),
            text_ru = data.get('text_ru'),
            name = data.get('name'),
            name_en = data.get('name_en'),
            name_ru = data.get('name_ru')
        )
        return redirect('section')

    return render(request, 'sectioncreate.html')


@login_required
def SectionEdit(request, pk):
    img = Info.objects.last()
    section = Section.objects.get(id=pk)
    if request.method == "POST":
        section = Section.objects.get(id=pk)
        if 'logo' in request.FILES:
            section.image = request.FILES['logo']
        else:
            section.image = request.POST.get('image')
        section.name = request.POST.get('name')
        section.name_ru = request.POST.get('name_ru')
        section.name_en = request.POST.get('name_en')

        section.text = request.POST.get('text')
        section.text_ru = request.POST.get('text_ru')
        section.text_en = request.POST.get('text_en')
        section.save()
        return redirect('section')
    context = {
        'img':img,
        "section": section
    }
    return render(request, 'sectionedit.html', context)

@login_required
def PostalservicesEdit(request,pk):
    img = Info.objects.last()
    postalservices = Postalservices.objects.get(id=pk)
    if request.method == "POST":
        postalservices = Postalservices.objects.get(id=pk)
        if 'logo' in request.FILES:
            postalservices.logo = request.FILES['logo']
        else:
            postalservices.logo = request.POST.get('image')
        postalservices.save()
        return redirect('postalservices')
    context = {
        'img':img,
        "postalservices": postalservices
    }
    return render(request, 'postalservicesedit.html', context)


@login_required
def PostalservicesCreate(request):
    if request.method == "POST":
        data = request.POST
        Postalservices.objects.create(
            logo = request.FILES['image'],
        )
        return redirect('postalservices')

    return render(request, 'postalservicescreate.html')

@login_required
def PostalservicesTemp(request):
    postalservices = Postalservices.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "postalservices":postalservices
    }

    return render(request, 'postalservices.html', context)


@login_required
def DeletePostal(request, pk):
    postal = Postalservices.objects.get(id=pk)
    postal.delete()
    return redirect("postalservices")


@login_required
def BoglanishTemp(request):
    boglanish = Boglanish.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "boglanish":boglanish
    }

    return render(request, 'boglanish.html', context)



@login_required
def DeleteBoglanish(request, pk):
    boglanish = Boglanish.objects.get(id=pk)
    boglanish.delete()
    return redirect("boglanish")


@login_required
def MobileoperatorTemp(request):
    mobileoperator = Mobileoperators.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "mobileoperator":mobileoperator
    }

    return render(request, 'mobileoperator.html', context)

@login_required
def MobileoperatorsEdit(request,pk):
    mobileoperator = Mobileoperators.objects.get(id=pk)
    if request.method == "POST":
        mobileoperator = Mobileoperators.objects.get(id=pk)
        if 'logo' in request.FILES:
            mobileoperator.logo = request.FILES['logo']
        else:
            mobileoperator.logo = request.POST.get('image')
        mobileoperator.save()
        return redirect('mobileoperator')
    context = {
        "mobileoperators": mobileoperator
    }
    return render(request, 'mobileoperatoredit.html', context)

@login_required
def MobileoperatorCreate(request):
    if request.method == "POST":
        Mobileoperators.objects.create(
            logo = request.FILES['image'],
        )
        return redirect('mobileoperator')

    return render(request, 'mobileoperatorcreate.html')

@login_required
def DeleteMobiloperator(request, pk):
    mobileoperator = Mobileoperators.objects.get(id=pk)
    mobileoperator.delete()
    return redirect("mobileoperator")


@login_required
def InternetprovidersTemp(request):
    internetproviders = Internetproviders.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "internetproviders":internetproviders
    }

    return render(request, 'internetproviders.html', context)

@login_required
def InternetprovidersEdit(request,pk):
    img = Info.objects.last()
    internetproviders = Internetproviders.objects.get(id=pk)
    if request.method == "POST":
        internetproviders = Internetproviders.objects.get(id=pk)
        if 'logo' in request.FILES:
            internetproviders.logo = request.FILES['logo']
        else:
            internetproviders.logo = request.POST.get('image')
        internetproviders.save()
        return redirect('internetproviders')
    context = {
        'img':img,
        "internetproviders": internetproviders
    }
    return render(request, 'internetprovidersedit.html', context)

@login_required
def DeleteInternetproviders(request, pk):
    internetproviders = Internetproviders.objects.get(id=pk)
    internetproviders.delete()
    return redirect("internetproviders")

@login_required
def CreateInternetproviders(request):
    if request.method == "POST":
        Internetproviders.objects.create(
            logo = request.FILES['image'],
        )
        return redirect('internetproviders')

    return render(request, 'createinternetproviders.html')

@login_required
def OurAudienceEdit(request, pk):
    img = Info.objects.last()
    ouraudience = OurAudience.objects.get(id=pk)
    if request.method == "POST":
        ouraudience = OurAudience.objects.get(id=pk)
        if 'logo' in request.FILES:
            ouraudience.image = request.FILES['logo']
        else:
            ouraudience.image = request.POST.get('image')
        ouraudience.name = request.POST.get('name')
        ouraudience.name_ru = request.POST.get('name_ru')
        ouraudience.name_en = request.POST.get('name_en')
        
        ouraudience.text = request.POST.get('text')
        ouraudience.text_ru = request.POST.get('text_ru')
        ouraudience.text_en = request.POST.get('text_en')
        ouraudience.save()
        return redirect('ouraudience')
    context = {
        'img':img,
        "ouraudience": ouraudience
    }
    return render(request, 'ouraudienceedit.html', context)

@login_required
def OuraudienCereate(request):
    ouraudience = OurAudience.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "ouraudience":ouraudience,
    }
    if request.method == "POST":
        data = request.POST
        OurAudience.objects.create(
            image = request.FILES['image'],
            name = data.get('name'),
            name_ru = data.get('name_ru'),
            name_en = data.get('name_en'),

            text = data.get('text'),
            text_ru = data.get('text_ru'),
            text_en = data.get('text_en'),
            
        )
        return redirect('ouraudience')
    return render(request, 'ouraudiencecreate.html', context)

@login_required
def OurAudienceTemp(request):
    ouraudience = OurAudience.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "ouraudience":ouraudience
    }

    return render(request, 'ouraudience.html', context)


@login_required
def DeleteOurAudience(request, pk):
    ouraudience = OurAudience.objects.get(id=pk)
    ouraudience.delete()
    return redirect("ouraudience")


@login_required
def PercentageTemp(request):
    percentage = Percentage.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "percentage": percentage
    }
    return render(request, 'percentage.html', context)

@login_required
def PercentageCreate(request):
    percentage = Percentage.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "percentage":percentage,
    } 
    if request.method == "POST":
        data = request.POST
        Percentage.objects.create(
            percent = data.get('percent'),
            name = data.get('name'),
            name_ru = data.get('name_ru'),
            name_en = data.get('name_en'),
        )
        return redirect('percentage')
    return render(request, 'percentagecreate.html', context)

@login_required
def PercentageEdit(request, pk):
    img = Info.objects.last()
    if request.method == "POST":
        percentage = Percentage.objects.get(id=pk)
        percentage.percent = request.POST.get('percent')
        percentage.name = request.POST.get('name')
        percentage.name_ru = request.POST.get('name_ru')
        percentage.name_en = request.POST.get('name_en')
        percentage.save()
        return redirect('percentage')
    percentage = Percentage.objects.get(id=pk)
    context = {
        'img':img,
        "percentage": percentage
    }
    return render(request, 'percentageedit.html', context)

@login_required
def DeletePercentage(request, pk):
    percentage = Percentage.objects.get(id=pk)
    percentage.delete()
    return redirect("percentage")


@login_required
def ResidentsTemp(request):
    residents = Residents.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "residents": residents
    }
    return render(request, 'residents.html', context)

@login_required
def ResidentsCreate(request):
    residents = Percentage.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "residents":residents,
    } 
    if request.method == "POST":
        data = request.POST
        Residents.objects.create(
            image = request.FILES['image'],
            name = data.get('name'),
            name_ru = data.get('name_ru'),
            name_en = data.get('name_en'),
            text = data.get('text'),
            text_ru = data.get('text_ru'),
            text_en = data.get('text_en'),
        )
        return redirect('residents')
    return render(request, 'residentscreate.html', context)

@login_required
def ResidentsEdit(request, pk):
    img = Info.objects.last()
    residents = Residents.objects.get(id=pk)
    if request.method == "POST":
        residents = Residents.objects.get(id=pk)
        if 'logo' in request.FILES:
            residents.image = request.FILES['logo']
        else:
            residents.image = request.POST.get('image')
        residents.text = request.POST.get('text')
        residents.text_ru = request.POST.get('text_ru')
        residents.text_en = request.POST.get('text_en')
        residents.save()
        return redirect('residents')
    context = {
        'img':img,
        "residents": residents
    }
    return render(request, 'residentsedit.html', context)

@login_required
def DeleteResidents(request, pk):
    residents = Residents.objects.get(id=pk)
    residents.delete()
    return redirect("residents")


@login_required
def TeamTemp(request):
    team = Team.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "team": team
    }
    return render(request, 'team.html', context)


@login_required
def TeamCreate(request):
    team = Team.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "team":team,
    } 
    if request.method == "POST":
        data = request.POST
        Team.objects.create(
            image = request.FILES['image'],
            text = data.get('text'),
            text_ru = data.get('text_ru'),
            text_en = data.get('text_en'),
        )
        return redirect('team')
    return render(request, 'teamcreate.html', context)

@login_required
def TeamEdit(request, pk):
    img = Info.objects.last()
    team = Team.objects.get(id=pk)
    if request.method == "POST":
        team = Team.objects.get(id=pk)
        if 'image' in request.FILES:
            team.image = request.FILES['image']
        team.text = request.POST.get('text')
        team.text_ru = request.POST.get('text_ru')
        team.text_en = request.POST.get('text_en')
        team.save()
        return redirect('team')
    context = {
        'img':img,
        "team": team
    }
    return render(request, 'teamedit.html', context)

@login_required
def DeleteTeam(request, pk):
    team = Team.objects.get(id=pk)
    team.delete()
    return redirect("team")


@login_required
def CoworkingTemp(request):
    coworking = Coworking.objects.all().order_by('-id')
    coimages = Coimages.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "coimages": coimages,
        "coworking": coworking
    }
    return render(request, 'coworking.html', context)

@login_required
def CoworkingCreate(request):
    coworking = Coworking.objects.all().order_by('-id')
    coimages = Coimages.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "coworking":coworking,
        "coimages":coimages,
    } 
    if request.method == "POST":
        data = request.POST
        list = data.getlist('images')
        images = []
        for i in list:
            images.append(Coimages.objects.get(id=i))
        obj = Coworking.objects.create(text=request.POST.get('text'),
        text_ru=request.POST.get('text_ru'),
        text_en=request.POST.get('text_en')
        )
        obj.image.set(images)
        obj.save()
        return redirect('coworking')
    return render(request, 'coworkingcreate.html', context)

@login_required
def CoworkingEdit(request, pk):
    img = Info.objects.last()
    coworking = Coworking.objects.get(id=pk)
    if request.method == "POST":
        coworking = Coworking.objects.get(id=pk)
        images = []
        for selected in request.POST.getlist('images'):
            images.append(Coimages.objects.get(id=selected))
        coworking.image.set(images)
        coworking.text = request.POST.get('text')
        coworking.text_ru = request.POST.get('text_ru')
        coworking.text_en = request.POST.get('text_en')
        coworking.save()
        return redirect('coworking')
    context = {
        'img':img,
        "coworking": coworking,
        "coimages":Coimages.objects.all(),
    }
    return render(request, 'coworkingedit.html', context)

@login_required
def CoimagesCreate(request):
    coimages = Coimages.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "coimages":coimages,
    } 
    if request.method == "POST":
        Coimages.objects.create(
            image = request.FILES['image'],
        )
        return redirect('coworking')
    return render(request, 'coimagescreate.html', context)

@login_required
def CoimagesEdit(request, pk):
    coimages = Coimages.objects.get(id=pk)
    img = Info.objects.last()
    context = {
        'img':img,
        "coimages":coimages,
    } 
    if request.method == "POST":
        if 'logo' in request.FILES:
            coimages.image = request.FILES['logo']

        coimages.save()
        return redirect('coworking')
    return render(request, 'coimagesedit.html', context)

@login_required
def DeleteCoimage(request, pk):
    coimage = Coimages.objects.get(id=pk)
    coimage.delete()
    return redirect('coworking') 

@login_required
def DeleteCoworking(request, pk):
    coworking = Coworking.objects.get(id=pk)
    coworking.delete()
    return redirect('coworking')

@login_required
def InfrastructureSliderTemp(request):
    infra = InfrastructureSlider.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        'infra':infra,
    }
    return render(request, 'infrastructureslider.html', context)

@login_required
def InfrastructureCreate(request):
    infra = InfrastructureSlider.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "infra":infra,
    }
    if request.method == "POST":
        data = request.POST
        InfrastructureSlider.objects.create(
            image = request.FILES['image'],
            text = data.get('text'),
            text_ru = data.get('text_ru'),
            text_en = data.get('text_en'),
        )
        return redirect('infrastructureslider')
    return render(request, 'infrastructureslidercreate.html', context)


@login_required
def InfrastructureEdit(request, pk):
    img = Info.objects.last()
    infrastructureslider = InfrastructureSlider.objects.get(id=pk)
    if request.method == "POST":
        infrastructureslider = InfrastructureSlider.objects.get(id=pk)
        if 'image' in request.FILES:
            infrastructureslider.image = request.FILES.get("image")
        infrastructureslider.text = request.POST.get('text')
        infrastructureslider.text_ru = request.POST.get('text_ru')
        infrastructureslider.text_en = request.POST.get('text_en')
        infrastructureslider.save()
        return redirect('infrastructureslider')
    context = {
        'img':img,
        "infrastructureslider": infrastructureslider
    }
    return render(request, 'infrastructureslideredit.html', context)


@login_required
def InfrastructureDelete(request, pk):
    infra = InfrastructureSlider.objects.get(id=pk)
    infra.delete()
    return redirect("infrastructureslider")


@login_required
def StudyDirectionsTemp(request):
    studydirection = StudyDirections.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        'studydirection':studydirection
    }
    return render(request, 'studydirection.html', context)

@login_required
def StudyDirectionsEdit(request, pk):
    img = Info.objects.last()
    studydirection = StudyDirections.objects.get(id=pk)
    if request.method == "POST":
        studydirection = StudyDirections.objects.get(id=pk)
        if 'logo' in request.FILES:
            studydirection.image = request.FILES.get("logo")

        studydirection.text = request.POST.get('text')
        studydirection.text_ru = request.POST.get('text_ru')
        studydirection.text_en = request.POST.get('text_en')
        studydirection.save()
        return redirect('studydirection')
    context = {
        'img':img,
        "studydirection": studydirection
    }
    return render(request, 'studydirectionedit.html', context)

@login_required
def StudyDirectionsCreate(request):
    studydirection = StudyDirections.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "studydirection":studydirection,
    }
    if request.method == "POST":
        data = request.POST
        StudyDirections.objects.create(
            image = request.FILES['image'],
            text = data.get('text'),
            text_ru = data.get('text_ru'),
            text_en = data.get('text_en'),
        )
        return redirect('studydirection')
    return render(request, 'studyDirectionscreate.html', context)


@login_required
def StudyDirectionsDelete(request, pk):
    study = StudyDirections.objects.get(id=pk)
    study.delete()
    return redirect("studydirection")


@login_required
def ItAcademyTemp(request):
    it_academy = ItAcademy.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "it_academy":it_academy,
    }
    return render(request, 'itacademy.html', context)

@login_required
def ItAcademyTempCreate(request):
    it_academy = ItAcademy.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "it_academy":it_academy,
    }
    if request.method == "POST":
        data = request.POST
        ItAcademy.objects.create(
            image = request.FILES['image'],
            duration = data.get('duration'),
            duration_ru = data.get('duration_ru'),
            duration_en = data.get('duration_en'),
            name=data.get('name'),
            name_ru=data.get('name_ru'),
            name_en=data.get('name_en'),
            start= data.get('start'),
            texnologies_eng=data.get("tech")

        )
        return redirect('itacademy')
    return render(request, 'itacademycreate.html', context)

@login_required
def ItAcademyEdit(request, pk):
    img = Info.objects.last()
    itacademy = ItAcademy.objects.get(id=pk)
    if request.method == "POST":
        itacademy = ItAcademy.objects.get(id=pk)
        if 'image' in request.FILES:
            itacademy.image = request.FILES.get("image")
        itacademy.text = request.POST.get('text')
        itacademy.text_ru = request.POST.get('text_ru')
        itacademy.text_en = request.POST.get('text_en')
        itacademy.save()
        return redirect('itacademy')
    date_start = str(itacademy.start)
    context = {
        'img':img,
        "itacademy": itacademy,
        "date_start":date_start,
    }
    return render(request, 'itacademyedit.html', context)


@login_required
def ItAcademyDelete(request, pk):
    it_academy = ItAcademy.objects.get(id=pk)
    it_academy.delete()
    return redirect("itacademy")


@login_required
def StartupDirectionsTemp(request):
    startupdirection = StartupDirections.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        'startupdirection':startupdirection
    }
    return render(request, 'startupdirections.html', context)


@login_required
def StartupDirectionsCreate(request):
    startupdirection = StartupDirections.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "startupdirection": startupdirection,
    }
    if request.method == "POST":
        data = request.POST
        StartupDirections.objects.create(
            icon=request.FILES['image'],
            name=data.get('name'),
            name_ru=data.get('name_ru'),
            name_en=data.get('name_en'),
        )
        return redirect('startupdirection')
    return render(request, 'startupdirectioncreate.html', context)

@login_required
def StartupDirectionsEdit(request, pk):
    img = Info.objects.last()
    startupdirection = StartupDirections.objects.get(id=pk)
    if request.method == "POST":
        startupdirection = StartupDirections.objects.get(id=pk)
        if 'image' in request.FILES:
            startupdirection.icon = request.FILES.get("image")
        startupdirection.name = request.POST.get('name')
        startupdirection.name_ru = request.POST.get('name_ru')
        startupdirection.name_en = request.POST.get('name_en')
        startupdirection.save()
        return redirect('startupdirection')
    context = {
        'img':img,
        "startupdirection": startupdirection,
    }
    return render(request, 'startupdirectionedit.html', context)



@login_required
def StartupDirectionsDelete(request, pk):
    startupdirections = StartupDirections.objects.get(id=pk)
    startupdirections.delete()
    return redirect("startupdirection")


@login_required
def IncubationCentersTemp(request):
    incubationcenters = IncubationCenters.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        'incubationcenters':incubationcenters
    }
    return render(request, 'incubationcenters.html', context)

@login_required
def IncubationCentersEdit(request, pk):
    img = Info.objects.last()
    incubationcenters = IncubationCenters.objects.get(id=pk)
    if request.method == "POST":
        incubationcenters = IncubationCenters.objects.get(id=pk)
        if 'image' in request.FILES:
            incubationcenters.icon = request.FILES.get("image")
        incubationcenters.text = request.POST.get('text')
        incubationcenters.text_ru = request.POST.get('text_ru')
        incubationcenters.text_en = request.POST.get('text_en')
        incubationcenters.save()
        return redirect('incubationcenters')
    context = {
        'img':img,
        "incubationcenters": incubationcenters,
    }
    return render(request, 'incubationcentersedit.html', context)

@login_required
def IncubationCentersCreate(request):
    incubationcenters = IncubationCenters.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "incubationcenters": incubationcenters,
    }
    if request.method == "POST":
        data = request.POST
        IncubationCenters.objects.create(
            icon=request.FILES['icon'],
            text=data.get('text'),
            text_en=data.get('text_en'),
            text_ru=data.get('text_ru'),
        )
        return redirect('incubationcenters')
    return render(request, 'incubationcenterscreate.html', context)

@login_required
def IncubationCentersDelete(request, pk):
    incubationcenters = IncubationCenters.objects.get(id=pk)
    incubationcenters.delete()
    return redirect("incubationcenters")

@login_required
def RaqamlashtirishXizmatlariTemp(request):
    raqamlashtirishxizmatlari = Raqamlashtirishxizmalari.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        'raqamlashtirishxizmatlari':raqamlashtirishxizmatlari
    }
    return render(request, 'raqamlashtirishxizmatlari.html', context)


@login_required
def RaqamlashtirishXizmatlariEdit(request, pk):
    raqamlashtirishxizmatlari = Raqamlashtirishxizmalari.objects.get(id=pk)
    img = Info.objects.last()
    if request.method == "POST":
        raqamlashtirishxizmatlari = Raqamlashtirishxizmalari.objects.get(id=pk)
        if 'image' in request.FILES:
            raqamlashtirishxizmatlari.image = request.FILES.get("image")
        raqamlashtirishxizmatlari.name = request.POST.get('name')
        raqamlashtirishxizmatlari.name_ru = request.POST.get('name_ru')
        raqamlashtirishxizmatlari.name_en = request.POST.get('name_en')
        raqamlashtirishxizmatlari.text = request.POST.get('text')
        raqamlashtirishxizmatlari.text_ru = request.POST.get('text_ru')
        raqamlashtirishxizmatlari.text_en = request.POST.get('text_en')
        raqamlashtirishxizmatlari.save()
        return redirect('raqamlashtirishxizmatlari')
    context = {
        'img':img,
        "raqamlashtirishxizmatlari": raqamlashtirishxizmatlari,
    }
    return render(request, 'raqamlashtirishxizmatlariedit.html', context)


@login_required
def RaqamlashtirishXizmatlariCreate(request):
    raqamlashtirishxizmatlari = Raqamlashtirishxizmalari.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "raqamlashtirishxizmatlari": raqamlashtirishxizmatlari,
    }
    if request.method == "POST":
        data = request.POST
        Raqamlashtirishxizmalari.objects.create(
            image=request.FILES['image'],
            name=data.get('name'),
            name_en=data.get('name_en'),
            name_ru=data.get('name_ru'),
            text=data.get('text'),
            text_en=data.get('text_en'),
            text_ru=data.get('text_ru'),
        )
        return redirect('raqamlashtirishxizmatlari')
    return render(request, 'raqamlashtirishxizmatlaricreate.html', context)


@login_required
def RaqamlashtirishXizmatlariDelete(request, pk):
    raqamlashtirishxizmatlari = Raqamlashtirishxizmalari.objects.get(id=pk)
    raqamlashtirishxizmatlari.delete()
    return redirect("raqamlashtirishxizmatlari")
#####

@login_required
def ContactTemp(request):
    contact = Contact.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        'contact':contact
    }
    return render(request, 'contact.html', context)

@login_required
def ContactDelete(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return redirect("contact")


@login_required
def XizmatlariTemp(request):
    xizmatlar = Xizmatlar.objects.all().order_by('-id')
    xizmmatturi = XizmatTuri.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        'xizmatlar':xizmatlar,
        'xizmmatturi':xizmmatturi,
    }
    return render(request, 'xizmatlar.html', context)



@login_required
def XizmatlarCreate(request):
    xizmmatturi = XizmatTuri.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "xizmmatturi": xizmmatturi,
    }
    if request.method == "POST":
        data = request.POST
        list = data.get('xizmat')
        xizmat = []
        for i in list:
            xizmat.append(XizmatTuri.objects.get(id=i))
        obj = Xizmatlar.objects.create(name=request.POST.get('name'),
        name_ru=request.POST.get('name_ru'),
        name_en=request.POST.get('name_en'),
        xizmat=xizmat[0],
        )
        obj.save()
        return redirect('xizmatlari')
    return render(request, 'xizmatlarcreate.html', context) 



@login_required
def XizmatlarEdit(request, pk):
    img = Info.objects.last()
    xizmatlari = Xizmatlar.objects.get(id=pk)
    turlari = XizmatTuri.objects.all().order_by("-id")
    if request.method == "POST":
        xizmatlari = Xizmatlar.objects.get(id=pk)
        if 'xizmat' in request.POST:
            xizmatlari.xizmat = XizmatTuri.objects.get(id=request.POST['xizmat'])
        xizmatlari.name = request.POST.get('name')
        xizmatlari.name_ru = request.POST.get('name_ru')
        xizmatlari.name_en = request.POST.get('name_en')
        xizmatlari.save()
        return redirect('xizmatlari')
    context = {
        'img':img,
        "xizmatlari": xizmatlari,
        "turlari":turlari,
    
    }
    return render(request, 'xizmatlaredit.html', context)



@login_required
def XizmatlariDelete(request, pk):
    xizmatlar = Xizmatlar.objects.get(id=pk)
    xizmatlar.delete()
    return redirect("xizmatlari")

@login_required
def XizmatturiCreate(request):
    xizmmatturi = XizmatTuri.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        "xizmmatturi": xizmmatturi,
    }
    if request.method == "POST":
        data = request.POST
        XizmatTuri.objects.create(
            name=data.get('name'),
            name_en=data.get('name_en'),
            name_ru=data.get('name_ru'),
            price=data.get('price'),
        )
        return redirect('xizmatlari')
    return render(request, 'xizmmatturicreate.html', context)


@login_required
def XizmatturiEdit(request, pk):
    img = Info.objects.last()
    xizmatturi = XizmatTuri.objects.get(id=pk)
    if request.method == "POST":
        xizmatturi = XizmatTuri.objects.get(id=pk)
        xizmatturi.name = request.POST.get('name')
        xizmatturi.name_ru = request.POST.get('name_ru')
        xizmatturi.name_en = request.POST.get('name_en')
        xizmatturi.price = request.POST.get('price')
        xizmatturi.save()
        return redirect('xizmatlari')
    context = {
        'img':img,
        "xizmatturi": xizmatturi,
    }
    return render(request, 'xizmatturiedit.html', context)



@login_required
def XizmatturiDelete(request, pk):
    xizmmatturi = XizmatTuri.objects.get(id=pk)
    xizmmatturi.delete()
    return redirect("xizmatlari")




@login_required
def ApplicationTemp(request):
    application = Application.objects.all().order_by('-id')
    img = Info.objects.last()
    context = {
        'img':img,
        'application':application
    }
    return render(request, 'application.html', context)

@login_required
def ApplicationDelete(request, pk):
    application = Application.objects.get(id=pk)
    application.delete()
    return redirect("application")

def Login(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        print('post')
        username =request.POST.get("username")
        password = request.POST.get ('password')
        employe = User.objects.filter(username=username)
        if employe.count() > 0:
            if employe[0].check_password(password):
                login(request,employe[0])
                return redirect("home")
            else:
                return redirect('login')
        else:
            return redirect('login')    
    return render(request, 'login.html')

    