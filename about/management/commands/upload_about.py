from datetime import date
import re
from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
import datetime
import math
import re

import datetime
import time
from about.models import Interest, Profile
import logging
from aboubakiri.model_tools import get_connection, dataframe_to_table, make_date_ready


xl_origin = datetime.datetime(1899,12,30)
def iso_to_datetime(iso_date):

    return datetime.datetime(int(iso_date[:4]),int(iso_date[4:6]),int(iso_date[6:8]),)


class Command(BaseCommand):
    help = "Insert datas from CSV"

    def add_arguments(self, parser):
        super().add_arguments(parser)
        
        parser.add_argument(
                    '--dry',
                    action='store_true',
                    dest='dry',
                    default=False,
                    help='Dry run, do not alter database..',
                )
        
        parser.add_argument(
                    '--insert',
                    action='store_true',
                    dest='insert',
                    default=False,
                    help='insert without delete previous table..',
                )

        parser.add_argument(
                    '--force',
                    action='store_true',
                    dest='force',
                    default=False,
                    help='forcer la maj de la table..',)

        #parser.add_argument('csv_in', type=str)
        parser.add_argument('dateiso', type=str)
        #parser.add_argument('outfolder')


    def handle(self, *args, **options):
        dateiso = options['dateiso']
        dry = options['dry']
        insert = options['insert']
        force = options['force']
        date = iso_to_datetime(dateiso)
        d = {
            'name': 'Aboubakiri',
            'photo': 'upload',
            'town': 'Casablanca',
            'nationality': 'Senegalese',
            'phone': '+2120603392868',
            'latitude': 0,
            'longitude': 0,
            'email': 'aboubacar198@gmail.com',
            'website': 'inconnue',
            'facebook': 'inconnue',
            'instagram': 'inconnue',
            'twitter': 'inconnue',
            'skype': 'inconnue',
            'linkedin': 'https://www.linkedin.com/in/aboubakiri-diaw-8a9a35173/',
            'spoken_lang': 'FR/EN',
            'years_exp': 5,
            'date': date      
             }
        df = pd.DataFrame(data=d, index=[0])
        dd = df[df.duplicated(['date'], keep=False)].groupby(['date']).last()
        for d, _ in dd.iterrows():
            #d = str(d)
            d = d.date()
            print('dddddddd', d)
            if not dry and not insert:
                make_date_ready(Profile, d)

        if not dry:
            now = datetime.datetime.now()
            df['created'] = now
            df['modified'] = now
            dataframe_to_table(df, dry, 'about_profile', disable_trigger = True)
