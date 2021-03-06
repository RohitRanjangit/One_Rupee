from django.db import models
from django.contrib.auth.models import User
from users.models import user
from django.shortcuts import reverse


class Ngo(User, models.Model):
    CATEGORY_CHOICES = (
        ('AGC',
         'Age care (care for the aged/Older persons)'),
        ('AGR', 'Agriculture'),
        ('AW', 'Animal Welfare'),
        ('ANC', 'Art & Craft'),
        ('CE', 'Child Education'),
        ('CUD', 'Cities/Urban Development'),
        ('CD', 'Community Development'),
        ('CNH', ' Culture & Heritage'),
        ('D', 'Disability'),
        ('DM', 'Disaster Management'),
        ('EDU', 'Education'),
        ('ENVI', 'Environmental issues'),
        ('HNH', 'Health & Hygiene'),
        ('HA', ' HIV/AIDS'),
        ('HS', 'Housing & Slums'),
        ('P', 'Population'),
        ('PR', 'Poverty Removal'),
        ('RD', 'Rural Development'),
        ('STD', 'Science & Technology Development'),
        ('TP', 'Tribal people'),
        ('WM', 'Waste Management'),
        ('DW', 'Drinking Water'),
        ('WO', 'Women'),
        ('O', 'others')


    )
    category = models.CharField(
        ("category"), max_length=50, choices=CATEGORY_CHOICES, blank=False)

    class Meta:
        verbose_name = ("Ngo")
        verbose_name_plural = ("Ngos")

    def __str__(self):
        return self.ngo_name

    def get_absolute_url(self):
        return reverse("Ngo_detail", kwargs={"pk": self.pk})
    # later, override the email field as well as username field
    ngo_name = models.CharField(("ngo_name"), max_length=50, blank=False)
    Email = models.EmailField(
        ("email_ngo"), max_length=254, unique=True, blank=False)
    Ngo_certificate = models.URLField(
        default='https://www.google.com', max_length=200)
    Ngo_website = models.URLField(
        default='https://www.google.com', max_length=200)
    users = models.ManyToManyField(user, verbose_name=(
        "users_to_ngo_through_payment"), through="payment.Payment")
    IsNgo = True


class Profile(models.Model):

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})
    image = models.ImageField(default='www.google.com', upload_to='profile_pics',
                              height_field=None, width_field=None, max_length=None)
    amount_collected = models.IntegerField(default=0)
    long_description = models.TextField()
    location = models.TextField()
    goal = models.TextField(max_length=1000)
    contact = models.DecimalField(
        ("contact_number"), max_digits=10, decimal_places=0)
    Ngo = models.OneToOneField(Ngo, on_delete=models.CASCADE)
