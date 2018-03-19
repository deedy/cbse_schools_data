from collections import namedtuple
import pickle
import time

# http://cbseaff.nic.in/cbse_aff/schdir_Report/AppViewdir.aspx?affno=1930772
CbseSchoolFields = [
        'name', # Name of institution
        'aff_no', # Affiliation number
        'state', # State
        'district', # District
        'address', # Postal Address
        'pincode', # Pincode
        'ph_no', # Phone number with STD code
        'off_ph_no', # Office Phone number [ to remove comma and clean]
        'res_ph_no', # Residence Phone number
        'fax_no', # Fax number
        'email', # Email
        'website', # Website
        'year_found', # Year founded (bad data: 0000, 0046, 0392, 0910, 1193, 2066, 2078, 3201, 3889, 4198, 5981, june)
        'date_opened', # Date opened
        'princi_name', # Principal name
        'sex', # Sex (of school, or principal?)
        'princi_qual', # Principal qualifications
        'princi_exp_adm', # Principal experience administrative [can standardize]
        'princi_exp_teach', # Principal experience teaching [can standardize]
        'status', # Status of school (e.g. Middle school, Secondary School, Senior Secondary)
        'aff_type', # Affiliation type (e.g. Provisional, Permanent)
        'aff_start', # Affiliation start date
        'aff_end', # Affiliation end date
        'soc_name', # Name of Trust/Society/Managing Committee (overseeing company)
]
CbseSchool = namedtuple('CbseSchool', CbseSchoolFields)


RES_FILE_P = 'schools.p'
print('Reading {0}...'.format(RES_FILE_P))
start = time.time()
with open(RES_FILE_P, 'rb') as f:
  data = pickle.load(f)
print('Loaded {0} rows in {1:0.2f} seconds.'.format(len(data), time.time() - start))
