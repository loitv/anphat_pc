from django.db import models
from anphat_pc.settings import P_STATUS_DISCONTINUE, P_STATUS_ON_SALE, P_STATUS_OUT_STOCK

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseProduct(BaseModel):
    STATUS_CHOICES = (
        (P_STATUS_ON_SALE, 'Còn hàng'),
        (P_STATUS_OUT_STOCK, 'Hết hàng'),
        (P_STATUS_DISCONTINUE, 'Ngừng phân phối'),
    )
    price = models.CharField("Giá", max_length=32, null=True)
    old_price = models.CharField("Giá cũ", max_length=32, null=True)
    status = models.SmallIntegerField("Tình trạng", choices=STATUS_CHOICES, default=P_STATUS_ON_SALE)
    quantity = models.SmallIntegerField("Số lượng", default=1)


class CPUInfo(BaseModel):
    name = models.CharField("Tên CPU", max_length=255)
    non_white_space_name = models.CharField(max_length=255, null=True)
    manufacture = models.CharField("Hãng", max_length=255, null=True)
    series = models.CharField("Dòng", max_length=255, null=True)
    code_name = models.CharField("Tên mã", max_length=128, null=True)
    clock_rate = models.CharField("Xung nhịp (MHz)", max_length=128, null=True)
    l1_cache = models.CharField(max_length=64, null=True)
    l2_cache = models.CharField(max_length=64, null=True)
    l3_cache = models.CharField(max_length=64, null=True)
    core = models.SmallIntegerField("Số lõi", null=True)
    threads = models.SmallIntegerField("Số luồng", null=True)
    power_consumption = models.CharField("Công suất tiêu thụ (W)", max_length=128, null=True)
    transistor_count = models.CharField("Số lượng bóng bán dẫn", max_length=128, null=True)
    die_size = models.CharField(max_length=64, null=True)
    technology = models.CharField('Công nghệ', max_length=64, null=True)
    max_temp = models.CharField('Nhiệt độ tối đa', max_length=64, null=True)
    socket = models.CharField(max_length=128, null=True)
    features = models.TextField(null=True)
    gpu = models.CharField("Đồ họa tích hợp", max_length=255, null=True)
    sixty_four_bit = models.CharField("64 Bit", max_length=128, null=True)
    announce_date = models.DateField(null=True)
    reference_link = models.CharField("Link tham khảo", null=True, max_length=512)

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
    non_white_space_name = models.CharField(max_length=255, null=True)
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
    non_white_space_name = models.CharField(max_length=255, null=True)
    brand = models.CharField(max_length=255, verbose_name='Hãng', null=True)
    sub_brand = models.CharField(max_length=255, null=True, verbose_name='Dòng máy')
    serial_number = models.CharField(max_length=16, blank=True, verbose_name = "Số Seri")
    service_tag = models.CharField(max_length=16, blank=True)
    cpu = models.ForeignKey(CPUInfo, on_delete=models.CASCADE, related_name='laptops', verbose_name="CPU", null=True)
    vga = models.ForeignKey(VGAInfo, on_delete=models.CASCADE, related_name='laptops', verbose_name="VGA", null=True)
    ram = models.CharField(max_length=255, null=True, verbose_name="RAM")
    hard_disk = models.CharField(max_length=255, null=True, verbose_name="Ổ cứng")
    screen = models.CharField(max_length=255, null=True, verbose_name="Màn hình")
    os = models.CharField(max_length=255, verbose_name="Hệ điều hành")
    pin = models.CharField(max_length=255, verbose_name="Pin (cell)")
    weight = models.CharField(max_length=255, verbose_name="Khối lượng (kg)")
    cover = models.ImageField(null=True, verbose_name="Ảnh sản phẩm")

    class Meta:
        verbose_name_plural = 'LAPTOP'

    def __str__(self):
        return self.name
