import requests
import re
import os
from bs4 import BeautifulSoup
from datetime import datetime

from .models import Laptop, VGAInfo
from logs.my_log import AnphatLogger

utils_log = AnphatLogger('AP_UTILS')


def count_laptops():
    return Laptop.objects.count()


def get_gpu_url_list():
    url_list = []
    base_url = 'https://www.notebookcheck.net/NVIDIA-GeForce-RTX-2080-Ti-Desktop-Graphics-Card.386296.0.html'
    r = requests.get(url=base_url)
    soup = BeautifulSoup(r.text, 'lxml')
    classes = soup.find(id="c5498226").div.div.find_all('span')
    for cls in classes:
        divs = cls.find_all('div')
        for div in divs:
            try:
                url_list.append(div.a['href'])
            except TypeError as e:
                utils_log.info(e)
                continue
    error_url_list = []
    for url in url_list:
        try:
            crawl_gpu_spec(url)
        except Exception as e:
            utils_log.error(e)
            error_url_list.append(url)
            continue
    utils_log.info('-----------------LIST OF ERROR URL-----------------')
    if error_url_list:
        for url in error_url_list:
            utils_log.info(url)


def crawl_gpu_spec(url):
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, 'lxml')

    spec_divs = soup.find(id="content").find_all('div')
    for div in spec_divs:
        try:
            name = div.find('div', {'class': 'tx-nbc2fe-pi1'}).h1.string
            gpu_specs = div.find('div', {'class': 'tx-nbc2fe-pi1'}). \
                find('table', {'class': 'gputable'}).find_all('tr')
            manufacturer, architecture, pipelines, core_speed, memory_speed, memory_bus_width, memory_type, \
                max_memory_size, shared_memory, direct_x, technology, features, release_date, link_to_manufacture = \
                '', '', '', '', '', '', '', '', '', '', '', '', '', ''
            for tr in gpu_specs:
                tds = tr.find_all('td')
                if tds[0].string == 'Manufacturer':
                    manufacturer = tds[1].string
                elif tds[0].string == 'Architecture':
                    architecture = tds[1].string
                elif tds[0].string == 'Pipelines':
                    pipelines = tds[1].string
                elif tds[0].string == 'Core Speed':
                    core_speed = tds[1].string
                elif tds[0].string == 'Memory Speed':
                    memory_speed = tds[1].string
                elif tds[0].string == 'Memory Bus Width':
                    memory_bus_width = tds[1].string
                elif tds[0].string == 'Memory Type':
                    memory_type = tds[1].string
                elif tds[0].string == 'Max. Amount of Memory':
                    max_memory_size = tds[1].string
                elif tds[0].string == 'Shared Memory':
                    shared_memory = tds[1].string
                elif tds[0].string == 'DirectX':
                    direct_x = tds[1].string
                elif tds[0].string == 'technology':
                    technology = tds[1].string
                elif tds[0].string == 'Features':
                    features = tds[1].string
                elif tds[0].string == 'Date of Announcement':
                    a = re.findall(r'\d\d.\d\d.\d\d\d\d', str(tds[1]))[0]
                    release_date = datetime.strptime(a.split(' ')[0], '%d.%m.%Y')
                elif tds[0].string == 'Link to Manufacturer Page':
                    link_to_manufacture = tds[1].string

            vga = VGAInfo.objects.filter(name=name)
            if not vga:
                vga = VGAInfo(
                    name=name,
                    use_type=get_gpu_use_for(lower_name=name.lower()),
                    manufacturer=manufacturer,
                    architecture=architecture,
                    pipelines=pipelines,
                    core_speed=core_speed,
                    memory_speed=memory_speed,
                    memory_bus_width=memory_bus_width,
                    memory_type=memory_type,
                    max_memory_size=max_memory_size,
                    shared_memory=shared_memory,
                    direct_x=direct_x,
                    technology=technology,
                    features=features,
                    release_date=release_date,
                    link_to_manufacture=link_to_manufacture,
                )
                vga.save()
            break
        except AttributeError as ae:
            utils_log.error(ae)
            continue


def get_gpu_use_for(lower_name):
    for t in ['laptop', 'desktop']:
        if t in lower_name:
            return t
    return 'unknown'


def crawl_again():
    file = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'url_list.txt'))
    lines = file.readlines()
    for line in lines:
        url = line.split('INFO - ')[1]
        print(repr(url))
        try:
            crawl_gpu_spec(url.strip())
        except AttributeError as e:
            print(e)
            raise
            # continue


def test():
    crawl_again()
