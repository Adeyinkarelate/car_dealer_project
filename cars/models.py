from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator
# Create your models here.


class Car(models.Model):
    state_choice = (
        ('NI', 'Niger'),
        ('BO', 'Borno '),
        ('TA', 'Taraba'),
        ('KD', 'Kaduna'),
        ('BA', 'Bauchi'),
        ('YO', 'Yobe'),
        ('ZA', 'Zamfara'),
        ('AD', 'Adamawa'),
        ('KW', 'Kwara'),
        ('KE', 'Kebbi'),
        ('BE', 'Benue'),
        ('PL', 'Plateau'),
        ('KO', 'Kogi'),
        ('OY', 'Oyo'),
        ('NA', 'Nasarawa'),
        ('SO', 'Sokoto'),
        ('KT', 'Katsina'),
        ('JI', 'Jigawa'),
        ('CR', 'Cross River'),
        ('KN', 'Kano'),
        ('GO', 'Gombe'),
        ('ED', 'Edo'),
        ('DE', 'Delta'),
        ('OG', 'Ogun'),
        ('ON', 'Ondo'),
        ('RI', 'Rivers'),
        ('BY', 'Bayelsa'),
        ('OS', 'Osun'),
        ('FC', 'Fct'),
        ('EN', 'Enugun'),
        ('AK', 'Akwa Ibom'),
        ('EK', 'Ekit'),
        ('AB', 'Abia'),
        ('EB', 'Ebonyi'),
        ('IM', 'Imo'),
        ('AN', 'Anambra'),
        ('LA', 'Lagos'),
    )
    
    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    
    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))
        
    cart_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10, choices=state_choice)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('Year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    car_photo = models.ImageField(validators=[FileExtensionValidator(['png','jpg','jpeg'])] , upload_to='cars_images' )
    car_photo_1 = models.ImageField(validators=[FileExtensionValidator(['png','jpg','jpeg'])] , upload_to='cars_images',blank=True )
    car_photo_2 = models.ImageField(validators=[FileExtensionValidator(['png','jpg','jpeg'])] , upload_to='cars_images',blank=True )
    car_photo_3 = models.ImageField(validators=[FileExtensionValidator(['png','jpg','jpeg'])] , upload_to='cars_images',blank=True)
    car_photo_4 = models.ImageField(validators=[FileExtensionValidator(['png','jpg','jpeg'])] , upload_to='cars_images',blank=True )
    features = models.CharField(max_length=100, choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.PositiveIntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.PositiveIntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateField(default=datetime.now, blank=True)
