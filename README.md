# CBSE Schools Data

[CBSE](https://en.wikipedia.org/wiki/Central_Board_of_Secondary_Education) is one of the two national level boards of education in India (alongwith [CISCE](https://en.wikipedia.org/wiki/Central_Board_of_Secondary_Education)).
While CISCE is a private board, CBSE is public, central government run board.
Every year, over **1 million** students take the CBSE Class XII (12) board examination as a high school leaving examination in India (and several schools abroad).

As of **2018**, there are **20,367** schools affiliated with the CBSE (out of which only 220 are outside India).
The details of each of these schools can be fetched from the [CBSE School Directory](http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx).
[Here](http://cbseaff.nic.in/cbse_aff/schdir_Report/AppViewdir.aspx?affno=2730017) is an example URL endpoint of the school DPS RK Puram (aff_no = 2730017).
You can replace the `affno` parameter with any Affiliation number to see the original raw data.

## Instructions

The main contribution of this project is to scrape, parse, clean, document, dump and open the data for all of these schools. 
The scraping, parsing and cleaning code is not in this repository.

 - `README_DATA_BASIC` contains a protocol buffer like documentation for the **basic** data (in the `basic/` folder). Lists each of the fields, including which ones are required and optional, the degree to which the optional ones are present, as well as the type and enum definitions of each field.
 - `README_DATA_DETAILED` contains a protocol buffer like documentation for the **detailed** data (in the `detailed/` folder). Lists each of the fields, including which ones are required and optional, the degree to which the optional ones are present, as well as the type and enum definitions of each field.
 - `README_DISTRICTS` contains details of the district (alongwith state enums)
 - `basic/` The basic data containing the primary 24 fields.
   - `analyze_csv.py` reads the `csv` file in Python and prepares it for analysis.
   - `schools.csv` the csv file - 6.1MB.
   - `analyze_pickle.py` reads the `pickle` file in Python and prepares it for analysis.
   - `schools.p` the pickle file - 9.8MB.
 - `detailed/` The detailed data containing the primary 24 fields and the 119 detailed fields for a total of 143 fields.
   - `analyze_csv.py` reads the `csv` file in Python and prepares it for analysis.
   - `schools_detailed.csv` the detailed csv file - 12MB.
   - `analyze_pickle.py` reads the `pickle` file in Python and prepares it for analysis.
   - `schools_detailed.p` the detailed pickle file - 26.7MB.
 
## Short Documentation (Basic)

There are 24 total fields per school, a total of 488k data points. For full documentation, see `README_DATA_BASIC`. 

 - `required string name` School name in upper case
 - `required int32 aff_no` Affiliation number, unique
 - `required State state` Indian State/Union Territory or "Foreign Schools"
 - `optional District district` Indian District (or Country if state == FOREIGN SCHOOlS)
 - `required string address` Postal Address
 - `optional int32 pincode` Indian pincode
 - `optional string ph_no` Phone number (with STD Code). ';' Separated phone-numbers.
 - `optional string off_ph_no` Office phone number. ';' Separated phone-numbers.
 - `optional string res_ph_no` Residential phone number. ';' Separated phone-numbers.
 - `optional string fax_no` Fax number. ';' Separated numbers.
 - `optional string email` Email address
 - `optional string website` Website
 - `optional int32 year_found` Year that the school was founded (between 1800 and 2018)
 - `optional Date date_opened` Date that the school was opened (in form "Sep 9, 2010")
 - `optional string princi_name` Name of the principal, upper case
 - `optional Sex sex` Gender/sex of the school.
 - `optional int32 princi_qual` Qualifications of the principal
 - `optional int32 princi_exp_adm` Number of years of administrative experience of the principal
 - `optional int32 princi_exp_teach` Number of years of teaching experience of the principal
 - `required Status status` Status of the school - e.g. Middle Class, Secondary or Senior Secondary
 - `optional AffiliationType aff_type` Affiliation Type e.g. Provisional, Permanent
 - `optional Date aff_start` Affiliation start date (in form "Sep 9, 2010")
 - `optional Date aff_end` Affiliation end date (in form "Sep 19, 2011")
 - `optional string soc_name` Name of Trust, Society or Managing Committee, upper case

## Short Documentation (Detailed)

There are 143 total fields per school - the 24 basic ones above, and 119 more, for a total of 2.9m data points.

 - **School Location Details** (6 fields)
   - `optional string l_nearest_railway` Name of nearest railway station
   - `optional float l_nearest_railway_dist` Distance (in km) to nearest railway station
   - `optional string l_nearest_police` Name of nearest polic station
   - `optional float l_nearest_police_dist` Distance (in km) to nearest police station
   - `optional string l_nearest_bank` Name of nearest nationalized bank
   - `optional float l_nearest_bank_dist` Distance (in km) to nearest nationalized bank
 - **School Nature Details** (3 fields)
   - `optional Category n_category` The gender category of the school (e.g. Co-educational, Boys, Girls)
   - `optional Medium n_medium` The medium of instruction (e.g. English, Hindi)
   - `optional Type n_school_type` The type of the school (e.g. Independent, Govt, KVS, JNV, Govt Aided, etc)
 - **School Enrollment Details** (34 fields)
   - -`sections` and -`students` of each the different classes:
   - `e_nursery_`- (Nursery/KG/LKG), `e_i_v_`- (Class I-V Elementary), `e_vi_viii_`- (Class VI-VIII Middle), `e_ix_x_`- (Class IX-X Secondary), `e_xi_xii_`- (Class XI-XII Senior Secondary) and 
   - `e_i_`-, `e_ii_`-, `e_iii_`-, `e_iv_`-, `e_v_`-, `e_vi_`-, `e_vii_`-, `e_viii_`-, `e_ix_`-, `e_x_`-, `e_xi_`-, `e_xii_`- (Class I through XII)
 - **School Infrastructure Details** (33 fields)
   - Each of -`_no` (number), `_length` (length in m), `_breadth` (breadth in m) of
   - `i_classrooms`-, `i_composite_lab`-, `i_phy_lab`-, `i_chem_lab`-, `i_bio_lab`-, `i_biotech_lab`-, `i_math_lab`-, `i_cs_lab`-, `i_home_lab`-, `i_library`-, `i_other_lab`-
 - **School Teacher Details** (21 fields)
   - Each of -`_no` (number), `_trained` (trained), `_untrained` (untrained) of
   - `t_ntts`- NTTs: Nursery Teacher Training
   - `t_prts`- PRTs: PRimary Teacher (1-5th, diploma in education)
   - `t_tgts`- TGTs: Trained Graduate Teacher (6-10th, grad in subject, B.Ed)
   - `t_librarians`- Librarians
   - `t_ptis`- PTIs: Physical Training Instructor
   - `t_pgts`- PGTs: Post Graduate Teacher (11-12th, post grad in subject, B.Ed)
   - `t_execs`- Executive (Vice Principal/Supervisor/Head Master/Head Mistress) Teacher
 - **School Physical Infrastructure Details** (10 fields)
   - `optional float p_area_meter` Area of school (in m^2)
   - `optional float p_area_acre` Area of school (in acre)
   - `optional float p_area_builtup_meter` Built-up area of school (in m^2)
   - `optional Sites p_num_sites` Number of sites this school is at (e.g. ONE, TWO)
   - `optional float p_area_playground` Area of playground (in m^2)
   - `optional UrinalType p_urinal_type` Type of urinals (e.g. flush, dry)
   - `optional int p_boys_urinal` Number of boys urinals
   - `optional int p_girls_urinal` Number of girls urinals
   - `optional bool p_potable_water` Whether the water is drinkable
   - `optional bool p_health_cert` Whether the school has an Oficial Health and Sanitary certificate
 - **School Facilities Details** (12 fields) 
   - `optional int f_total_books` Number of total books
   - `optional int f_periodicals` Number of periodicals
   - `optional int f_dailies` Number of dailies
   - `optional int f_reference_books` Number of reference books
   - `optional int f_magazine` Number of magazines
   - `optional bool f_swimming_pool` Swimming Pool? (yes/no)
   - `optional bool f_indoor_games` Indoor games? (yes/no)
   - `optional bool f_dance_rooms` Dance rooms? (yes/no)
   - `optional bool f_gym` Gym? (yes/no)
   - `optional bool f_music_rooms` Music rooms? (yes/no)
   - `optional bool f_hostel` Hostel? (yes/no)
   - `optional bool f_health_checkup` Health checkup? (yes/no)
 
 # License 
 This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
