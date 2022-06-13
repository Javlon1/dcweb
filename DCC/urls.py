from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *


urlpatterns = [ 

    ###
    path('admin/', admin.site.urls),
    path('api/info/', InfoView.as_view()),
    path('api/slider/', SliderView.as_view()),
    path('api/porjects/', ProjectsView.as_view()),
    path('api/technopark/', TechnoparkView.as_view()),
    path('api/section/<int:pk>/', SectionView.as_view()),
    path('api/postalservice/', Postalservicesview.as_view()),
    path('api/boglanish/', BoglanishView.as_view()),
    path('api/mobileoperator/', MobileoperatorsView.as_view()),
    path('api/internetproviders/', InternetprovidersView.as_view()),
    path('api/audince/', OurAudienceView.as_view()),
    path('api/percentage/', PercentageView.as_view()),
    path('api/residents/', ResidentsView.as_view()),
    path('api/team/', TeamView.as_view()),
    path('api/coworking/', CoworkingView.as_view()),
    path('api/infrastructure/', InfrastructureSliderView.as_view()),
    path('api/studydirection/', StudyDirectionsView.as_view()),
    path('api/itacademy/', ItAcademyView.as_view()),
    path('api/startupdirections/', StartupDirectionsView.as_view()),
    path('api/incubationcenters/', IncubationCentersView.as_view()),
    path('api/raqamlashtirishxizmalari/', RaqamlashtirishxizmalariView.as_view()),
    path('api/contact/', ContactPost.as_view()),
    path('api/xizmatturi/', XizmatTuriView.as_view()),
    path('api/xizmatlar/', XizmatlarPost.as_view()),
    path("api/xizmatlarget/", XizmatlarGet, name="xizmatget"),
    path('api/application/', ApplicationPost.as_view()),


    ####
        #Templates
    path('home/', Home, name='home'),
    path('info/', InfoTemplate, name='info'),
    path('infoedit/<int:pk>/', InfoEdit, name='infoedit'),
    path('deleteinfo/<int:pk>/', DeleteInfo, name='deleteinfo'),
    path('infocreate/', InfoCreate, name='infocreate'),

    path('slider/', SliderTemp, name='slider'),
    path('slideredit/<int:pk>/', SliderEdit, name='slideredit'),
    path('deleteslider/<int:pk>/', DeleteSlider, name='deleteslider'),
    path('slidercreate/', SliderCreate, name='slidercreate'),
 
    path('projects/', ProjectsTemp, name='projects'),
    path('projectscreate/', ProjectsCreate, name='projectscreate'),
    path('projectsedit/<int:pk>/', ProjectsEdit, name='projectsedit'),
    path('deleteprojects/<int:pk>/', DeleteProjects, name='deleteprojects'),

    path('technopark/', TechnoparkTemp, name='technopark'),
    path('technoparkcreate/', TechnoparkCreate, name='technoparkcreate'),
    path('technoparkedit/<int:pk>/', TechnoparkEdit, name='technoparkedit'),
    path('deletetechnopark/<int:pk>/', DeleteTechnopark, name='deletetechnopark'),

    path('section/', SectionTemp, name='section'),
    path('deletesection/<int:pk>/', DeleteSection, name='deletesection'),
    path('editsection/<int:pk>/', SectionEdit, name='editsection'),
    path('createsection/', SectionCreate, name='sectioncreate'),

    path('postalservices/', PostalservicesTemp, name='postalservices'),
    path('deletepostalservices/<int:pk>/', DeletePostal, name='deletepostalservices'),
    path('postalservices-edit/<int:pk>/', PostalservicesEdit, name='postalservicesedit'),
    path('postalservices-create/', PostalservicesCreate, name='postalservicescreate'),


    path('boglanish/', BoglanishTemp, name='boglanish'),
    path('deleteboglanish/<int:pk>/', DeleteBoglanish, name='deleteboglanish'),

    path('mobileoperator/', MobileoperatorTemp, name='mobileoperator'),
    path("mobileoperatorsedit/<int:pk>/",MobileoperatorsEdit,name="mobileoperatorsedit"),
    path('mobileoperatorcreate/', MobileoperatorCreate, name='mobileoperatorcreate'),
    path('deletemobileoperator/<int:pk>/', DeleteMobiloperator, name='deletemobileoperator'),

    path('internetproviders/', InternetprovidersTemp, name='internetproviders'),
    path('internetprovidersedit/<int:pk>/',InternetprovidersEdit,name='internetprovidersedit'),
    path('deletemobileinternetproviders/<int:pk>/', DeleteInternetproviders, name='deleteinternetproviders'),
    path('createinternetproviders/', CreateInternetproviders, name='createinternetproviders'),

    path('ouraudience/', OurAudienceTemp, name='ouraudience'),
    path('ouraudienceed/<int:pk>/', OurAudienceEdit, name='ouraudienceedit'),
    path("ouraudiencecreate/",OuraudienCereate,name="ouraudiencecreate"),
    path('deletemobileouraudience/<int:pk>/', DeleteOurAudience, name='deleteouraudience'),

    path('percentage/', PercentageTemp, name='percentage'),
    path('percentageedit/<int:pk>/',  PercentageEdit, name='percentageedit'),
    path("percentagecreate/", PercentageCreate,name="percentagecreate"),
    path('deletemobilepercentage/<int:pk>/', DeletePercentage, name='deletepercentage'),

    path('residents/', ResidentsTemp, name='residents'),
    path('residentsedit/<int:pk>/',  ResidentsEdit, name='residentsedit'),
    path("residentscreate/", ResidentsCreate,name="residentscreate"),
    path('deleteresidents/<int:pk>/', DeleteResidents, name='deleteresidents'),

    path('team/', TeamTemp, name='team'),
    path('teamedit/<int:pk>/',  TeamEdit, name='teamedit'),
    path("teamcreate/", TeamCreate,name="teamcreate"),
    path('deleteteam/<int:pk>/', DeleteTeam, name='deleteteam'),

    path('coworking/', CoworkingTemp, name='coworking'),
    path('coworkingedit/<int:pk>/',  CoworkingEdit, name='coworkingedit'),
    path("coworkingcreate/", CoworkingCreate,name="coworkingcreate"),
    path('deletecoworking/<int:pk>/', DeleteCoworking, name='deletecoworking'),

    path("coimagescreate/", CoimagesCreate,name="coimagescreate"),
    path('CoimagesEditedit/<int:pk>/',  CoimagesEdit, name='coimagesedit'),
    path('deletecoimage/<int:pk>/', DeleteCoimage, name='deletecoimage'),

    path('infrastructureslider/',  InfrastructureSliderTemp, name='infrastructureslider'),
    path('infrastructureslidercreate/',  InfrastructureCreate, name='infrastructureslidercreate'),
    path('infrastructureslideredit/<int:pk>/',  InfrastructureEdit, name='infrastructureslideredit'),
    path('infrastructuresliderdelete/<int:pk>/',  InfrastructureDelete, name='infrastructuresliderdelete'),

    path('studydirection/',  StudyDirectionsTemp, name='studydirection'),
    path('studydirectiondelete/<int:pk>/',  StudyDirectionsDelete, name='studydirectiondelete'),
    path('studydirectionedit/<int:pk>/',  StudyDirectionsEdit, name='studydirectionedit'),
    path('studyDirectionscreate/',  StudyDirectionsCreate, name='studyDirectionscreate'),
    
    path('itacademy/',  ItAcademyTemp, name='itacademy'),
    path('itacademycreate/',  ItAcademyTempCreate, name='itacademycreate'),
    path('itacademydelete/<int:pk>/',  ItAcademyDelete, name='itacademydelete'),
    path("itacademyedit/<int:pk>/",ItAcademyEdit,name="itacademyedit"),

    path('startupdirection/',  StartupDirectionsTemp, name='startupdirection'),
    path('startupdirectioncreate/',  StartupDirectionsCreate, name='startupdirectioncreate'),
    path('startupdirectionsdelete/<int:pk>/',  StartupDirectionsDelete, name='startupdirectionsdelete'),
    path('startupdirectionsedit/<int:pk>/',  StartupDirectionsEdit, name='startupdirectionedit'),

    path('incubationcenters/',  IncubationCentersTemp, name='incubationcenters'),
    path('incubationcentersdelete/<int:pk>/',  IncubationCentersDelete, name='incubationcentersdelete'),
    path('incubationcenterscreate/',  IncubationCentersCreate, name='incubationcenterscreate'),
    path('incubationcentersedit/<int:pk>/',  IncubationCentersEdit, name='incubationcentersedit'),

    path('raqamlashtirishxizmatlari/', RaqamlashtirishXizmatlariTemp, name='raqamlashtirishxizmatlari'),
    path('raqamlashtirishxizmatlaricreate/', RaqamlashtirishXizmatlariCreate, name='raqamlashtirishxizmatlaricreate'),
    path('raqamlashtirishxizmatlaridelete/<int:pk>/',  RaqamlashtirishXizmatlariDelete, name='raqamlashtirishxizmatlaridelete'),
    path('raqamlashtirishxizmatlariedit/<int:pk>/',  RaqamlashtirishXizmatlariEdit, name='raqamlashtirishxizmatlariedit'),

    path('contact', ContactTemp, name='contact'),
    path('contactdelete/<int:pk>', ContactDelete, name='contactdelete'),

    path('xizmatlari', XizmatlariTemp, name='xizmatlari'),
    path('xizmmatturicreate', XizmatturiCreate, name='xizmmatturicreate'),
    path('xizmmatlarcreate', XizmatlarCreate, name='xizmmatlarcreate'),
    path('xizmatlaredit/<int:pk>/', XizmatlarEdit, name='xizmatlaredit'),

    path('xizmatturiedit/<int:pk>/', XizmatturiEdit, name='xizmatturiedit'),
    path('xizmatlaridelete/<int:pk>/', XizmatlariDelete, name='xizmatlaridelete'),
    path('xizmmatturidelete/<int:pk>/', XizmatturiDelete, name='xizmmatturidelete'),


    path('application', ApplicationTemp, name='application'),
    path('applicationdelete/<int:pk>/', ApplicationDelete, name='applicationdelete'),

    path('', Login, name='login')

    ####

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

