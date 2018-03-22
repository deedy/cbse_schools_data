from collections import namedtuple
import pickle
import time

# http://cbseaff.nic.in/cbse_aff/schdir_Report/AppViewdir.aspx?affno=2730017
CbseSchoolDetailedFields = [
        'name', # Name of institution
        'aff_no', # Affiliation number
        'state', # State
        'district', # District
        'region', # CBSE Region
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
        # School Location Details
        'l_nearest_railway', # Nearest Railway (string, upper)
        'l_nearest_railway_dist', # Distance (in km) to nearest railway (float)
        'l_nearest_police', # Nearest Police station (string, upper)
        'l_nearest_police_dist', # Distance (in km) to nearest police station (float)
        'l_nearest_bank', # Nearest Bank (string, upper)
        'l_nearest_bank_dist', # Distance (in km) to nearest bank (float)
        # School Nature details
        'n_category', # Category of school (e.g. Co-educational, Boys, Girls)
        'n_medium', # Medium of instruction (e.g. English, Hindi)
        'n_school_type', # Type of school (e.g. Independent, Govt, KVS, JNV, Govt Aided)
        # School Enrollment details,
        'e_nursery_sections', # Nursery/Kindergarten/Lower Kindergarten Number of Sections  (int)
        'e_nursery_students', # Nursery/Kindergarten/Lower Kindergarten Number of Students (int)
        'e_i_v_sections', # Class I-V (Elementary School) Number of Sections (int)
        'e_i_v_students', # Class I-V (Elementary School) Number of Students (int)
        'e_vi_viii_sections', # Class VI-VIII (Middle School) Number of Sections (int)
        'e_vi_viii_students', # Class VI-VIII (Middle School) Number of Students (int)
        'e_ix_x_sections', # Class IX-X (Secondary School) Number of Sections (int)
        'e_ix_x_students', # Class IX-X (Secondary School) Number of Students (int)
        'e_xi_xii_sections', # Class XI-XII (Senior Secondary School) Number of Sections (int)
        'e_xi_xii_students', # Class XI-XII (Senior Secondary School) Number of Students (int)
        'e_i_sections', # Class I Number of Sections (int)
        'e_i_students', # Class I Number of Students (int)
        'e_ii_sections', # Class II Number of Sections (int)
        'e_ii_students', # Class II Number of Students (int)
        'e_iii_sections', # Class III Number of Sections (int)
        'e_iii_students', # Class III Number of Students (int)
        'e_iv_sections', # Class IV Number of Sections (int)
        'e_iv_students', # Class IV Number of Students (int)
        'e_v_sections', # Class V Number of Sections (int)
        'e_v_students', # Class V Number of Students (int)
        'e_vi_sections', # Class VI Number of Sections (int)
        'e_vi_students', # Class VI Number of Students (int)
        'e_vii_sections', # Class VII Number of Sections (int)
        'e_vii_students', # Class VII Number of Students (int)
        'e_viii_sections', # Class VIII Number of Sections (int)
        'e_viii_students', # Class VIII Number of Students (int)
        'e_ix_sections', # Class IX Number of Sections (int)
        'e_ix_students', # Class IX Number of Students (int)
        'e_x_sections', # Class X Number of Sections (int)
        'e_x_students', # Class X Number of Students (int)
        'e_xi_sections', # Class XI Number of Sections (int)
        'e_xi_students', # Class XI Number of Students (int)
        'e_xii_sections', # Class XII Number of Sections (int)
        'e_xii_students', # Class XII Number of Students (int)
        # School Infrastructure details
        'i_classrooms_no', # Classroom Number (int)
        'i_classrooms_length', # Classroom Length (in ft) (float)
        'i_classrooms_breadth', # Classroom Breadth (in ft) (float)
        'i_composite_lab_no', # Composite Number (int)
        'i_composite_lab_length', # Composite Length (in ft) (float)
        'i_composite_lab_breadth', # Composite Breadth (in ft) (float)
        'i_phy_lab_no', # Physics Lab Number (int)
        'i_phy_lab_length', # Physics Lab Length (in ft) (float)
        'i_phy_lab_breadth', # Physics Lab Breadth (in ft) (float)
        'i_chem_lab_no', # Chemistry Lab Number (int)
        'i_chem_lab_length', # Chemistry Lab Length (in ft) (float)
        'i_chem_lab_breadth', # Chemistry Lab Breadth (in ft) (float)
        'i_bio_lab_no', # Biology Number (int)
        'i_bio_lab_length', # Biology Length (in ft) (float)
        'i_bio_lab_breadth', # Biology Breadth (in ft) (float)
        'i_biotech_lab_no', # Biotechnology Number (int)
        'i_biotech_lab_length', # Biotechnology Length (in ft) (float)
        'i_biotech_lab_breadth', # Biotechnology Breadth (in ft) (float)
        'i_math_lab_no', # Math Labs Number (int)
        'i_math_lab_length', # Math Labs Length (in ft) (float)
        'i_math_lab_breadth', # Math Labs Breadth (in ft) (float)
        'i_cs_lab_no', # Computer Science Lab Number (int)
        'i_cs_lab_length', # Computer Science Lab Length (in ft) (float)
        'i_cs_lab_breadth', # Computer Science Lab Breadth (in ft) (float)
        'i_home_lab_no', # Home Science Lab Number (int)
        'i_home_lab_length', # Home Science Lab Length (in ft) (float)
        'i_home_lab_breadth', # Home Science Lab Breadth (in ft) (float)
        'i_library_no', # Library Number (int)
        'i_library_length', # Library Length (in ft) (float)
        'i_library_breadth', # Library Breadth (in ft) (float)
        'i_other_lab_no', # Other Labs Number (int)
        'i_other_lab_length', # Other Labs Length (in ft) (float)
        'i_other_lab_breadth', # Other Labs Breadth (in ft) (float)
        # School Teacher details
        't_ntts_no', # Nursery Teacher Training Number (int)
        't_ntts_trained', # Nursery Teacher Training Trained number (int)
        't_ntts_untrained', # Nursery Teacher Training Untrained number (int)
        't_prts_no', # PRimary Teacher (1-5th, diploma in education) Number (int)
        't_prts_trained', # PRimary Teacher (1-5th, diploma in education) Trained number (int)
        't_prts_untrained', # PRimary Teacher (1-5th, diploma in education) Untrained number (int)
        't_tgts_no', # Trained Graduate Teacher (6-10th, grad in subject, B.Ed) Number (int)
        't_tgts_trained', # Trained Graduate Teacher (6-10th, grad in subject, B.Ed) Trained number (int)
        't_tgts_untrained', # Trained Graduate Teacher (6-10th, grad in subject, B.Ed) Untrained number (int)
        't_librarians_no', # Librarian Number (int)
        't_librarians_trained', # Librarian Trained number (int)
        't_librarians_untrained', # Librarian Untrained number (int)
        't_ptis_no', # Physical Training Instructor Number (int)
        't_ptis_trained', # Physical Training Instructor Trained number (int)
        't_ptis_untrained', # Physical Training Instructor Untrained number (int)
        't_pgts_no', # Post Graduate Teacher (11-12th, post grad in subject, B.Ed) Number (int)
        't_pgts_trained', # Post Graduate Teacher (11-12th, post grad in subject, B.Ed) Trained number (int)
        't_pgts_untrained', # Post Graduate Teacher (11-12th, post grad in subject, B.Ed) Untrained number (int)
        't_exec_no', # Executive  = Vice Principal/Supervisor/Head Master/ Head Mistress Number (int)
        't_exec_trained', # Executive  = Vice Principal/Supervisor/Head Master/ Head Mistress Trained number (int)
        't_exec_untrained', # Executive  = Vice Principal/Supervisor/Head Master/ Head Mistress Untrained number (int)
        # School Physical Infrastructure details
        'p_area_meter', # Area of Campus (in m^2) (float)
        'p_area_acre', # Area of Campus (in acres) (float)
        'p_area_builtup_meter', # Built-up Area of Campus (in m^2) (float)
        'p_num_sites', # Number of sites (e.g. ONE, TWO, NO)
        'p_area_playground', # Area of Playground (in m^2) (float)
        'p_urinal_type', # Type of urinal (e.g. flush, dry)
        'p_boys_urinal', # Number of boys urinals (int)
        'p_girls_urinal', # Number of girls urinals (int)
        'p_potable_water', # Is there potable water (e.g. yes, no)
        'p_health_cert', # Has it been health certified? (sanitary, drinking water, fire safety)
        # School Facilities details
        'f_total_books', # Library total number of books (int)
        'f_periodicals', # Library number of periodicals (int)
        'f_dailies', # Library number of dailies (int)
        'f_reference_books', # Library number of reference books (int)
        'f_magazine', # Library number of magazines (int)
        'f_swimming_pool', # Is there a swimming pool (e.g. yes, no)
        'f_indoor_games', # Is there an indoors games room (e.g. yes, no) 
        'f_dance_rooms', # Is there a dance room (e.g. yes, no) 
        'f_gym', # Is there a gym (e.g. yes, no) 
        'f_music_rooms', # Is there a music room (e.g. yes, no) 
        'f_hostel', # Is there a hostel (e.g. yes, no) 
        'f_health_checkup', # Is there a health and medical checkup room (e.g. yes, no) 
]
CbseSchool = namedtuple('CbseSchoolDetailed', CbseSchoolDetailedFields)


RES_FILE_P = 'schools_detailed.p'
print('Reading {0}...'.format(RES_FILE_P))
start = time.time()
with open(RES_FILE_P, 'rb') as f:
  data = pickle.load(f)
print('Loaded {0} rows in {1:0.2f} seconds.'.format(len(data), time.time() - start))

