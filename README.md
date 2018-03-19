# CBSE Schools Data

[CBSE](https://en.wikipedia.org/wiki/Central_Board_of_Secondary_Education) is one of the two national level boards of education in India (alongwith [CISCE](https://en.wikipedia.org/wiki/Central_Board_of_Secondary_Education)).
While CISCE is a private board, CBSE is public, central government run board.
Every year, over **1 million** students take the CBSE Class XII (12) board examination as a high school leaving examination in India (and several schools abroad).

As of 2018, there are **20,367** schools affiliated with the CBSE (out of which only 220 are outside India).
The details of each of these schools can be fetched from the [CBSE School Directory](http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx).
[Here](http://cbseaff.nic.in/cbse_aff/schdir_Report/AppViewdir.aspx?affno=2730017) is an example URL endpoint of the school DPS RK Puram (aff_no = 2730017).
You can replace the `affno` parameter with any Affiliation number to see the original raw data.

## Instructions

The main contribution of this project is to scrape, parse, clean, document, dump and open the data for all of these schools. 
The scraping, parsing and cleaning code is not in this repository.

 - `README_DATA_DETAILS` contains a protocol buffer like documentation of each of the fields, including which ones are required and optional, the degree to which the optional ones are present, as well as the type and enum definitions of each field.
 - `README_DISTRICTS` contains details of the district (alongwith state enums)
 - `analyze_csv.py` reads the `csv` file in Python and prepares it for analysis.
 - `analyze_pickle.py` reads the `pickle` file in Python and prepares it for analysis.
 
## Short Documentation

There are 24 total fields per school. For full documentation, see `README_DATA_DETAILS`. 

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
 
 
 # License 
 This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
