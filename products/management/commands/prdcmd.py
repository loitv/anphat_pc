from django.core.management.base import BaseCommand, CommandError
from products.utils import crawl_gpu_spec, get_gpu_url_list, test


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'opt', nargs='+', type=str
        )

    def handle(self, *args, **options):
        if len(options['opt']) == 1:
            if 'getgpu' in options['opt']:
                crawl_gpu_spec()
            elif 'geturl' in options['opt']:
                get_gpu_url_list()
            elif 'test' in options['opt']:
                test()
            else:
                raise CommandError('Command not found!')
            self.stdout.write(self.style.SUCCESS('Successful'))
        else:
            raise CommandError('Please give one argument only!')
