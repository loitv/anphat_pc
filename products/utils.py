import requests
import re
import os
import html
from bs4 import BeautifulSoup
from datetime import datetime

from .models import Laptop, VGAInfo, CPUInfo
from logs.my_log import AnphatLogger
from anphat_pc.settings import BASE_DIR

utils_log = AnphatLogger('AP_UTILS')
error_urls_path = os.path.join(BASE_DIR, 'products', 'error_url.txt')
if not os.path.exists(error_urls_path):
    f = open(error_urls_path, 'w+')
    f.close()
error_urls_file = open(error_urls_path, 'a')


def test():
    # get_gpu_url_list()
    crawl_cpu_spec()


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
            error_urls_file.write(url + '\n')
            continue
    utils_log.info('-----------------LIST OF ERROR URL-----------------')
    if error_url_list:
        for url in error_url_list:
            utils_log.info(url)


def crawl_gpu_spec(url):
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, 'lxml')

    spec_divs = soup.find(id="content").find_all('div')
    count = 0
    for div in spec_divs:
        try:
            name = div.find('div', {'class': 'tx-nbc2fe-pi1'}).h1.string
            vga = VGAInfo.objects.filter(name=name)
            if not vga:
                gpu_specs = div.find('div', {'class': 'tx-nbc2fe-pi1'}). \
                    find('table', {'class': 'gputable'}).find_all('tr')
                manufacturer, architecture, pipelines, core_speed, memory_speed, memory_bus_width, memory_type, \
                    max_memory_size, shared_memory, direct_x, technology, features, release_date,\
                    link_to_manufacture =  '', '', '', '', '', '', '', '', '', '', '', '', '', ''
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
            count += 1
            utils_log.error(ae)
            continue
    if count == len(spec_divs):
        error_urls_file.write(url + '\n')


def get_gpu_use_for(lower_name):
    for t in ['laptop', 'desktop']:
        if t in lower_name:
            return t
    return 'unknown'


# ----------------CRAWL CPU SPECIFICATIONS-------------------

def crawl_cpu_spec():
    base_url = 'https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html'

    soup = BeautifulSoup(requests.get(base_url).text, 'lxml')
    cpu_tags = soup.find(id="sortierbare_tabelle").find_all('tr', {'class': ['odd', 'even', 'desk_odd', 'desk_even',
                                                                             'smartphone_odd', 'smartphone_even']})
    html_file = open(os.path.join(BASE_DIR, 'products', 'cpu_table.html'), 'w+', encoding='utf-8')
    url_list_file = open(os.path.join(BASE_DIR, 'products', 'url_list.txt'), 'w+', encoding='utf-8')
    i = 0
    count = 0
    # get_spec = False

    for tag in cpu_tags:
        i += 1
        count += 1
        index_tag = tag.find(lambda t: t.name == 'td' and t['class'] == ['specs', 'poslabel'])
        index = int(''.join(c for c in index_tag.label.get_text() if c.isdigit()))
        try:
            html_file.write('<br>{0} ({1}).<br>\n'.format(count, index))
            name_tag = index_tag.findNext('td')
            url_tag = name_tag.a
            if url_tag:
                html_file.write(str(url_tag) + '<br>\n')
                url_list_file.write(url_tag['href'].strip() + '\n')
                # if url_tag['href'].strip() \
                #         == 'https://www.notebookcheck.net/Apple-A8-SoC.127992.0.html':
                #     get_spec = True
                # if get_spec:
                get_cpu_spec_from_url(url_tag['href'].strip())
            else:
                html_file.write(name_tag.get_text() + '<br>\n')
                pass
            if i < index:
                print(list(k for k in range(i, index)))
            i = index
        except UnicodeEncodeError or AttributeError as error:
            print(error)
            break

    # html_file.close()


def get_cpu_spec_from_url(url):
    print(url)
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    content_div = soup.find(id="content").find_all('div')
    count = 0
    for div in content_div:
        info_div = div.find('div', {'class': 'tx-nbc2fe-pi1'})
        if info_div:
            if info_div.h1:
                name = info_div.h1.get_text().strip()
                cpu = CPUInfo.objects.filter(name=name)
                if not cpu:
                    manufacture = name.split(' ')[0]
                    reference_link = url

                    series, code_name, clock_rate, l1_cache, l2_cache, l3_cache, power_consumption, transistor_count, \
                        die_size, technology, max_temp, socket, features, gpu, sixty_four_bit = \
                        '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
                    core, threads, announce_date = None, None, None

                    spec_div = info_div.find('table', {'class': 'gputable'})
                    for tr in spec_div.find_all('tr'):
                        tds = tr.find_all('td')
                        if tds[0].text.strip().lower() == 'Series'.lower():
                            series = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'Codename'.lower():
                            code_name = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'Clock Rate'.lower():
                            clock_rate = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'Level 1 Cache'.lower():
                            l1_cache = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'Level 2 Cache'.lower():
                            l2_cache = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'Level 3 Cache'.lower():
                            l3_cache = tds[1].text.strip()
                        elif 'Power Consumption'.lower() in tds[0].text.strip().lower():
                            power_consumption = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'Transistor Count'.lower():
                            transistor_count = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'Die Size'.lower():
                            die_size = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'Manufacturing Technology'.lower():
                            technology = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'Max. Temperature'.lower():
                            max_temp = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'Socket'.lower():
                            socket = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'Features'.lower():
                            features = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'GPU'.lower():
                            gpu = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == '64 Bit'.lower():
                            sixty_four_bit = tds[1].text.strip()
                        elif tds[0].text.strip().lower() == 'Number of Cores / Threads'.lower():
                            core_threads = tds[1].text.strip().split('/')
                            core = int(core_threads[0])
                            if len(core_threads) > 1:
                                threads = int(core_threads[1])
                        elif tds[0].text.strip().lower() == 'Announcement Date'.lower():
                            a = re.findall(r'\d\d/\d\d/\d\d\d\d', tds[1].text)[0]
                            announce_date = datetime.strptime(a, '%m/%d/%Y')

                    print(name)
                    cpu = CPUInfo(
                        name=name,
                        manufacture=manufacture,
                        series=series,
                        code_name=code_name,
                        clock_rate=clock_rate,
                        l1_cache=l1_cache,
                        l2_cache=l2_cache,
                        l3_cache=l3_cache,
                        core=core,
                        threads=threads,
                        power_consumption=power_consumption,
                        transistor_count=transistor_count,
                        die_size=die_size,
                        technology=technology,
                        max_temp=max_temp,
                        socket=socket,
                        features=features,
                        gpu=gpu,
                        sixty_four_bit=sixty_four_bit,
                        announce_date=announce_date,
                        reference_link=reference_link
                    )
                    cpu.save()
            else:
                count += 1
                continue
        else:
            count += 1
            continue
    if count == len(content_div):
        error_urls_file.write('CASE 2: {0}\n'.format(url))
