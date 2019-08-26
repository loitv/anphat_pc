from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CPUInfo(BaseModel):
    TYPE_CHOICES = (
        ('mobile', 'Mobile'),
        ('laptop', 'Laptop'),
        ('desktop', 'Desktop')
    )
    name = models.CharField("Tên CPU", max_length=255)
    brand = models.CharField("Hãng", max_length=255)
    type = models.CharField("Dùng cho", max_length=32, choices=TYPE_CHOICES)
    core = models.SmallIntegerField("Số lõi", )
    thread = models.SmallIntegerField("Số luồng", )
    base_freq = models.FloatField("Tần số cơ bản (GHz)", )
    max_freq = models.FloatField("Tần số boost (GHz)", )
    cache = models.SmallIntegerField("Kích thước bộ nhớ đệm (MB)", )

    class Meta:
        verbose_name_plural = "CPU Spec."

    def __str__(self):
        return self.name


class RAMInfo(BaseModel):
    RAM_TYPES = (
        ('ddr4', 'DDR4'),
        ('ddr3', 'DDR3'),
        ('ddr3l', 'DDR3L')
    )
    USE_FOR_CHOICES = (
        ('laptop', 'RAM Laptop'),
        ('desktop', 'RAM DESKTOP')
    )
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=16, choices=RAM_TYPES)
    use_type = models.CharField(max_length=16, choices=USE_FOR_CHOICES)
    memory_size = models.SmallIntegerField(null=True)
    bus = models.CharField(max_length=16, null=True)
    timing = models.SmallIntegerField(null=True)

    class Meta:
        verbose_name_plural = "RAM Spec."

    def __str__(self):
        return self.name


class VGAInfo(BaseModel):
    USE_FOR_CHOICES = (
        ('laptop', 'Laptop'),
        ('desktop', 'Desktop'),
        ('unknown', 'Unknown')
    )
    name = models.CharField(max_length=255, verbose_name="Tên card")
    use_type = models.CharField(max_length=16, choices=USE_FOR_CHOICES, verbose_name="Dùng cho")

    manufacturer = models.CharField(verbose_name="Nhà sản xuất", max_length=128, null=True)
    architecture = models.CharField(verbose_name="Kiến trúc", max_length=128, null=True)
    pipelines = models.CharField(verbose_name="Nhân CUDA", max_length=128, null=True)
    core_speed = models.CharField(verbose_name="Xung nhịp lõi (MHz)", max_length=128, null=True)
    memory_speed = models.CharField(verbose_name="Xung nhịp bộ nhớ (MHz)", max_length=128, null=True)
    memory_bus_width = models.CharField(verbose_name="Bus", max_length=128, null=True)
    memory_type = models.CharField(verbose_name="Loại bộ nhớ", max_length=128, null=True)
    max_memory_size = models.CharField(verbose_name="Dung lượng tối đa", max_length=32, null=True)
    shared_memory = models.CharField(verbose_name="Chia sẻ bộ nhớ", max_length=32, null=True)
    direct_x = models.CharField(verbose_name="DirectX", max_length=32, null=True)
    technology = models.CharField(verbose_name="Công nghệ", max_length=32, null=True)
    features = models.TextField(verbose_name="Tính năng", null=True)
    release_date = models.DateField(verbose_name="Ngày ra mắt", null=True)
    link_to_manufacture = models.CharField(verbose_name="Link tham khảo", null=True, max_length=255)

    class Meta:
        verbose_name_plural = "VGA Spec."

    def __str__(self):
        return self.name


class Laptop(BaseModel):
    SCREEN_RESOLUTION_CHOICES = (
        ('hd', 'HD (1280x720)'),
        ('hd+', 'HD+ (1600x900)'),
        ('full_hd', 'Full HD (1920x1080)'),
        ('2k', '2K (2560x1440)'),
        ('4k', 'UHD 4K (3840x2160)')
    )
    SCREEN_PANEL_TYPES = (
        ('ips', 'IPS'),
        ('va', 'VA'),
        ('tn', 'TN'),
    )
    RAM_TYPES = (
        ('ddr2', 'DDR2'),
        ('ddr3', 'DDR3'),
        ('ddr3l', 'DDR3L'),
        ('ddr4', 'DDR4'),
    )
    MEMORY_SIZES = (
        (2, '2 GB'), (4, '4 GB'), (8, '8 GB'), (16, '16 GB'), (32, '32 GB'), (64, '64 GB'), (128, '128 GB'),
    )
    BRAND_CHOICES = (
        ('acer', 'Acer'),
        ('asus', 'Asus'),
        ('dell', 'Dell'),
        ('msi', 'MSI'),
    )
    SUB_BRAND_CHOICES = [
        ('Acer', (
            ('aspire', 'Aspire'),
            ('switch', 'Switch')
        )),
        ('Dell', (
            ('inspiron', 'Inspiron'),
            ('xps', 'XPS'),
            ('vostro', 'Vostro')
        )),
        ('MSI', (
            ('gl', 'GL'),
            ('gv', 'GV'),
            ('gs', 'GS'),
            ('gt', 'GT'),
            ('ge', 'GE'),
            ('px', 'PX'),
        ))
    ]
    name = models.CharField(max_length=255, verbose_name="Tên máy")
    brand = models.CharField(max_length=255, choices=BRAND_CHOICES, verbose_name='Hãng')
    sub_brand = models.CharField(max_length=255, null=True, choices= SUB_BRAND_CHOICES, verbose_name='Dòng máy')
    serial_number = models.CharField(max_length=16, blank=True, verbose_name = "Số Seri")
    service_tag = models.CharField(max_length=16, blank=True)
    cpu = models.ForeignKey(CPUInfo, on_delete=models.CASCADE, related_name='laptops', verbose_name="CPU")
    vga = models.ForeignKey(VGAInfo, on_delete=models.CASCADE, related_name='laptops', verbose_name="VGA")
    memory_type = models.CharField(max_length=16, choices=RAM_TYPES, null=True, verbose_name="Loại RAM")
    memory_size = models.SmallIntegerField(choices=MEMORY_SIZES, null=True, verbose_name="Dung lượng RAM")
    screen_size = models.FloatField(verbose_name="Kích thước màn hình (inches)")
    screen_panel_type = models.CharField(max_length=16, choices=SCREEN_PANEL_TYPES, null=True, verbose_name="Tấm nền")
    screen_resolution = models.CharField(max_length=16, choices=SCREEN_RESOLUTION_CHOICES, null=True, verbose_name="Độ phân giải")
    os = models.CharField(max_length=255, verbose_name="Hệ điều hành")
    pin = models.CharField(max_length=16, verbose_name="Pin (cell)")
    weight = models.CharField(max_length=16, verbose_name="Khối lượng (kg)")
    cover = models.ImageField(null=True, verbose_name="Ảnh sản phẩm")

    class Meta:
        verbose_name_plural = 'LAPTOP'

    def __str__(self):
        return self.name
