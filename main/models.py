from django.db import models

class Info(models.Model):
    logo = models.ImageField(upload_to="Logo/")
    short_phone = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    address_ru = models.CharField(max_length=255)
    address_en = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return str(self.short_phone)
   
   
class Slider(models.Model):
    title = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    video = models.FileField(upload_to="Videos/")
 
 
class Projects(models.Model):
    image = models.ImageField(upload_to="Projects/")
    text = models.TextField()
    text_en = models.TextField()
    text_ru = models.TextField()
       
   
class Technopark(models.Model):
    icon = models.ImageField(upload_to="Texnopark/")
    text = models.CharField(max_length=100)
    text_ru = models.CharField(max_length=100)
    text_en = models.CharField(max_length=100)
    number = models.IntegerField()
 
 
 
class Section(models.Model):
    name = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)
    text_en = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Sections/")


class Postalservices(models.Model):
    logo = models.ImageField(upload_to="Pochta xizmatlari/")


class Boglanish(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.IntegerField()
    text = models.CharField(max_length=255)


class Mobileoperators(models.Model):
    logo = models.ImageField(upload_to="Mobile operators/")


class Internetproviders(models.Model):
    logo = models.ImageField(upload_to="Internet providers/")


class OurAudience(models.Model):
    image = models.ImageField(upload_to="OurAudience/")
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)
    text_en = models.CharField(max_length=255)


class Percentage(models.Model):
    percent = models.FloatField()
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)


class Residents(models.Model):
    image = models.ImageField(upload_to="Residents/")
    name = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)
    text_en = models.CharField(max_length=255)


class Team(models.Model):
    text = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()
    image = models.ImageField(upload_to="Team/")


class Coimages(models.Model):
    image = models.ImageField(upload_to="Coworking images/")

    def __str__(self):
        return str(self.image)

class Coworking(models.Model):
    text = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()
    image = models.ManyToManyField(Coimages)


class InfrastructureSlider(models.Model):
    image = models.ImageField(upload_to="InfrastructureSlider")
    text = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()



class StudyDirections(models.Model):
    image = models.ImageField(upload_to="StudyDirections/")
    text = models.CharField(max_length=100)
    text_ru = models.TextField()
    text_en = models.TextField()



class ItAcademy(models.Model):
    name = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    texnologies_eng = models.TextField()
    duration = models.CharField(max_length=50)
    duration_ru = models.CharField(max_length=50)
    duration_en = models.CharField(max_length=50)
    start = models.DateField()
    image = models.ImageField(upload_to="It Academy/")

    def __str__(self):
        return self.name


class StartupDirections(models.Model):
    name = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="StartupDirections/")

    def __str__(self):
        return self.name


class IncubationCenters(models.Model):
    icon = models.ImageField(upload_to="IncubationCenters")
    text = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)
    text_en = models.CharField(max_length=255)


class Raqamlashtirishxizmalari(models.Model):
    name = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Raqamlashtirishchizmalari")
    text = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)
    text_en = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    text = models.TextField()


class XizmatTuri(models.Model):
    name = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Xizmatlar(models.Model):
    xizmat = models.ForeignKey(XizmatTuri, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Application(models.Model):
    xizmat = models.ForeignKey(XizmatTuri, on_delete=models.PROTECT)
    fullname = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    text = models.TextField()
