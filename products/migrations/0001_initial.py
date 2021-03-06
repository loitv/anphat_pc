# Generated by Django 2.2.4 on 2019-08-26 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPUInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Tên CPU')),
                ('brand', models.CharField(max_length=255, verbose_name='Hãng')),
                ('type', models.CharField(choices=[('mobile', 'Mobile'), ('laptop', 'Laptop'), ('desktop', 'Desktop')], max_length=32, verbose_name='Dùng cho')),
                ('core', models.SmallIntegerField(verbose_name='Số lõi')),
                ('thread', models.SmallIntegerField(verbose_name='Số luồng')),
                ('base_freq', models.FloatField(verbose_name='Tần số cơ bản (GHz)')),
                ('max_freq', models.FloatField(verbose_name='Tần số boost (GHz)')),
                ('cache', models.SmallIntegerField(verbose_name='Kích thước bộ nhớ đệm (MB)')),
            ],
            options={
                'verbose_name_plural': 'CPU Spec.',
            },
        ),
        migrations.CreateModel(
            name='RAMInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(choices=[('ddr4', 'DDR4'), ('ddr3', 'DDR3'), ('ddr3l', 'DDR3L')], max_length=16)),
                ('use_type', models.CharField(choices=[('laptop', 'RAM Laptop'), ('desktop', 'RAM DESKTOP')], max_length=16)),
                ('memory_size', models.SmallIntegerField(null=True)),
                ('bus', models.CharField(max_length=16, null=True)),
                ('timing', models.SmallIntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'RAM Spec.',
            },
        ),
        migrations.CreateModel(
            name='VGAInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Tên card')),
                ('use_type', models.CharField(choices=[('laptop', 'Laptop'), ('desktop', 'Desktop'), ('unknown', 'Unknown')], max_length=16, verbose_name='Dùng cho')),
                ('manufacturer', models.CharField(max_length=128, null=True, verbose_name='Nhà sản xuất')),
                ('architecture', models.CharField(max_length=128, null=True, verbose_name='Kiến trúc')),
                ('pipelines', models.CharField(max_length=128, null=True, verbose_name='Nhân CUDA')),
                ('core_speed', models.CharField(max_length=128, null=True, verbose_name='Xung nhịp lõi (MHz)')),
                ('memory_speed', models.CharField(max_length=128, null=True, verbose_name='Xung nhịp bộ nhớ (MHz)')),
                ('memory_bus_width', models.CharField(max_length=128, null=True, verbose_name='Bus')),
                ('memory_type', models.CharField(max_length=32, null=True, verbose_name='Loại bộ nhớ')),
                ('max_memory_size', models.CharField(max_length=32, null=True, verbose_name='Dung lượng tối đa')),
                ('shared_memory', models.CharField(max_length=32, null=True, verbose_name='Chia sẻ bộ nhớ')),
                ('direct_x', models.CharField(max_length=32, null=True, verbose_name='DirectX')),
                ('technology', models.CharField(max_length=32, null=True, verbose_name='Công nghệ')),
                ('features', models.CharField(max_length=255, null=True, verbose_name='Tính năng')),
                ('release_date', models.DateField(null=True, verbose_name='Ngày ra mắt')),
                ('link_to_manufacture', models.CharField(max_length=255, null=True, verbose_name='Link tham khảo')),
            ],
            options={
                'verbose_name_plural': 'VGA Spec.',
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Tên máy')),
                ('brand', models.CharField(choices=[('acer', 'Acer'), ('asus', 'Asus'), ('dell', 'Dell'), ('msi', 'MSI')], max_length=255, verbose_name='Hãng')),
                ('sub_brand', models.CharField(choices=[('Acer', (('aspire', 'Aspire'), ('switch', 'Switch'))), ('Dell', (('inspiron', 'Inspiron'), ('xps', 'XPS'), ('vostro', 'Vostro'))), ('MSI', (('gl', 'GL'), ('gv', 'GV'), ('gs', 'GS'), ('gt', 'GT'), ('ge', 'GE'), ('px', 'PX')))], max_length=255, null=True, verbose_name='Dòng máy')),
                ('serial_number', models.CharField(blank=True, max_length=16, verbose_name='Số Seri')),
                ('service_tag', models.CharField(blank=True, max_length=16)),
                ('memory_type', models.CharField(choices=[('ddr2', 'DDR2'), ('ddr3', 'DDR3'), ('ddr3l', 'DDR3L'), ('ddr4', 'DDR4')], max_length=16, null=True, verbose_name='Loại RAM')),
                ('memory_size', models.SmallIntegerField(choices=[(2, '2 GB'), (4, '4 GB'), (8, '8 GB'), (16, '16 GB'), (32, '32 GB'), (64, '64 GB'), (128, '128 GB')], null=True, verbose_name='Dung lượng RAM')),
                ('screen_size', models.FloatField(verbose_name='Kích thước màn hình (inches)')),
                ('screen_panel_type', models.CharField(choices=[('ips', 'IPS'), ('va', 'VA'), ('tn', 'TN')], max_length=16, null=True, verbose_name='Tấm nền')),
                ('screen_resolution', models.CharField(choices=[('hd', 'HD (1280x720)'), ('hd+', 'HD+ (1600x900)'), ('full_hd', 'Full HD (1920x1080)'), ('2k', '2K (2560x1440)'), ('4k', 'UHD 4K (3840x2160)')], max_length=16, null=True, verbose_name='Độ phân giải')),
                ('os', models.CharField(max_length=255, verbose_name='Hệ điều hành')),
                ('pin', models.CharField(max_length=16, verbose_name='Pin (cell)')),
                ('weight', models.CharField(max_length=16, verbose_name='Khối lượng (kg)')),
                ('cover', models.ImageField(null=True, upload_to='', verbose_name='Ảnh sản phẩm')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptops', to='products.CPUInfo', verbose_name='CPU')),
                ('vga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptops', to='products.VGAInfo', verbose_name='VGA')),
            ],
            options={
                'verbose_name_plural': 'LAPTOP',
            },
        ),
    ]
