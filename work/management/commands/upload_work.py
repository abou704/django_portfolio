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
from experience.models import Employment, Education
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
        #save employement
        d = {
            'name': 
            [
                'Aboubakiri DIAW',         
                'Banque Centrale Populaire',
                'SNCF reseau',
                'Maghreb accessoires',
                'SmartProf',
                'Centrale Coding'

            ],
            'position':
            [
                'Quantitative Analyst', 
                'Internship PFE',
                'Chef de projet',
                'Assistant ing??nieur',
                'Tuteur',
                'President'


            ],

            'time_period': 
            [
                'Nov 2021 - current',
                'Apr 2021 - Oct 2021',
                'Dec 2020 - Fev 2021',
                'Juil 2020 - Sept 2020',
                'Sept 2020 - Oct 2021',
                'janv. 2021 - sept. 2021'
             
            ],
            'description': 
            [
            'Mod??lisation du loss given default (LGD) dans le cadre de la mise oeuvre de la norme IFRS9',
            'Construction d???un outil de pricing multiproduits en simultan?? permettant d???arbitrer entre les prix des produits bancaires.',
            'D??veloppement d???un syst??me de detection de pantographes d??fectueux, l??ger, fiable et peu couteux adapt?? au r??seau ??tendus.',
            'D??veloppement d???un mod??le de machine learning pour la recommandation de produits',
            'Tuteur acad??mique des mati??res scientifiques',
            'Centrale Coding: Club ayant pour but de d??mocratiser le codage informatique ?? l???ECC.'
            ],
            'town': 
            [
                'Casablanca',
                'Casablanca',
                'Casablanca',
                'Casablanca',
                'Casablanca',
                'Bouskoura'

            ],

            'url':
            [
                0,
            ] * 6,
            'date':
            [
                date,
            ] * 6

             }
        df = pd.DataFrame(data=d)
        dd = df[df.duplicated(['date'], keep=False)].groupby(['date']).last()
        for d, _ in dd.iterrows():
            #d = str(d)
            d = d.date()
            print('dddddddd', d)
            if not dry and not insert:
                make_date_ready(Employment, d)

        if not dry:
            now = datetime.datetime.now()
            df['created'] = now
            df['modified'] = now
            dataframe_to_table(df, dry, 'experience_employment', disable_trigger = True)
        
        d = {
            'status': [True],
            'completed': [True],
            'client_name': ['Aboubakiri DIAW'],
            'type': ['Website'],
            'date': [date],
            'skills': [,
            'software': [date] *3,
            'description':,
            'url':,
            'photo': 'upload'      
             }
        df = pd.DataFrame(data=d)
        dd = df[df.duplicated(['date'], keep=False)].groupby(['date']).last()
        for d, _ in dd.iterrows():
            #d = str(d)
            d = d.date()
            print('dddddddd', d)
            if not dry and not insert:
                make_date_ready(Education, d)

        if not dry:
            now = datetime.datetime.now()
            df['created'] = now
            df['modified'] = now
            dataframe_to_table(df, dry, 'experience_education', disable_trigger = True)
