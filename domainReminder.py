from win10toast_click import ToastNotifier
from datetime import date
from urllib.request import urlopen
import os
import json
from src.settings import settings as settings


def format_expiration_date(expiration_date):
    return expiration_date[0:10]

def get_formated_expiration_date(domain_data):
    for event in domain_data['events']:
        if (event['eventAction'] == 'expiration'):
            return format_expiration_date(event['eventDate'])
    
    return ''

def get_date_object_from_str(string_date):
    renovation_date = string_date.split('-')
    renovation_date = date(int(renovation_date[0]), int(renovation_date[1]), int(renovation_date[2]))
    
    return renovation_date

def update_renovation_dates():
    domain_list = json.load(open(settings.DOMAINS))

    renovation_dates_file = open(settings.DOMAIN_RENOVATION_DATES, 'w')
    domains_data = {}
    for domain in domain_list.values():
        domain_data = json.load(urlopen(f"{settings.API_URL}/domain/{domain}"))
        
        domains_data[domain_data['ldhName']] = {
            'name': domain_data['ldhName'],
            'expiration_date': get_formated_expiration_date(domain_data)
        }

    json.dump({
        'data': domains_data,
        'created_date': f"{date.today()}"
        }, renovation_dates_file, indent = 4
    )
    
    renovation_dates_file.close()
    
def toast_click():
    os.system(f"notepad.exe {settings.DELAYED_DOMAINS}")

if (not os.path.exists(settings.DOMAIN_RENOVATION_DATES)):
    domain_renovation_dates_file = open(settings.DOMAIN_RENOVATION_DATES, 'w')
    domain_renovation_dates_file.close()
        
if (os.stat(settings.DOMAIN_RENOVATION_DATES).st_size == 0):
    update_renovation_dates()

domain_renovation_dates_file = open(settings.DOMAIN_RENOVATION_DATES)
domain_renovation_dates = json.load(domain_renovation_dates_file)

today_date = str(date.today())

if (domain_renovation_dates['created_date'] < today_date):
    update_renovation_dates()
    domain_renovation_dates_file = open(settings.DOMAIN_RENOVATION_DATES)
    domain_renovation_dates = json.load(domain_renovation_dates_file)

delayed_renovation_domains = []
delayed_domains_file = open(settings.DELAYED_DOMAINS, 'w')
delayed_domains_file.write("Domínios Expirando/Expirados: \n\n")

for domain in domain_renovation_dates['data'].values():
    if (str(domain['expiration_date']) <= today_date):
        delayed_domains_file.write(f"{domain['name']} - {domain['expiration_date']}\n")
        delayed_renovation_domains.append(domain['name'])
    
delayed_domains_file.close()

if len(delayed_renovation_domains) > 0:
    delayed_renovation_domains_resumed = delayed_renovation_domains[0:3]
    toaster = ToastNotifier()
    toaster.show_toast(
        "Existem domínios com renovação pendente/próxima:",
        "\n".join(delayed_renovation_domains_resumed) + "\nClique para ver Todos...",
        icon_path=settings.TOAST_ICON,
        duration=None,
        threaded=True,
        callback_on_click=toast_click
    )
    