from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CPUInfo(BaseModel):
    TYPE_CHOICES = (
        ('mobile', 'Mobile'),
        ('laptop', 'Laptop'),
        ('desktop', 'Desktop')
    )
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    core = models.SmallIntegerField()
    thread = models.SmallIntegerField()
    base_freq = models.FloatField()
    max_freq = models.FloatField()
    cache = models.SmallIntegerField()

    def __str__(self):
        return self.name


class RAMInfo(BaseModel):
    RAM_TYPES = (
        ('ddr4', 'DDR4'),
        ('ddr3', 'DDR3'),
        ('ddr3l', 'DDR3L')
    )
    USE_TYPES = (
        ('laptop', 'RAM Laptop'),
        ('desktop', 'RAM DESKTOP')
    )
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=16, choices=RAM_TYPES)
    use_type = models.CharField(max_length=16, choices=USE_TYPES)
    memory_size = models.SmallIntegerField(null=True)
    bus = models.CharField(max_length=16, null=True)
    timing = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.name


class VGAInfo(BaseModel):
    USE_TYPES = (
        ('laptop', 'RAM Laptop'),
        ('desktop', 'RAM DESKTOP')
    )
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True)
    use_type = models.CharField(max_length=16, choices=USE_TYPES)
    core = models.SmallIntegerField()
    base_clock = models.SmallIntegerField()
    boost_clock = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Laptop(BaseModel):
    SCREEN_RESOLUTION_CHOICES = (
        ('hd', 'HD (1280x720)'),
        ('full_hd', 'Full HD (1920x1080)'),
        ('hd+', 'HD+ (1600x900)'),
        ('2k', '2K (2560x1440)'),
        ('4k', 'UHD 4K (3840x2160)')
    )
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=16, blank=True)
    service_tag = models.CharField(max_length=16, blank=True)
    cpu = models.ForeignKey(CPUInfo, on_delete=models.CASCADE, related_name='laptops')
    ram = models.ForeignKey(RAMInfo, on_delete=models.CASCADE, related_name='laptops')
    vga = models.ForeignKey(VGAInfo, on_delete=models.CASCADE, related_name='laptops')
    screen_size = models.FloatField()
    screen_type = models.CharField(max_length=16)
    screen_resolution = models.CharField(max_length=16, choices=SCREEN_RESOLUTION_CHOICES)
    os = models.CharField(max_length=255)
    pin = models.CharField(max_length=16)
    weight = models.CharField(max_length=16)
    cover = models.ImageField(null=True)

    def __str__(self):
        return self.name
