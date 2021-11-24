import pandas as pd
import seaborn as sns
import numpy as np


def main():

    raw_data = excel_csv_conversion()

    cleaned_data = csv_file_cleaner(raw_data)

    renamed_data = column_name_selection(cleaned_data)

    iso_data = column_extraction(renamed_data)

    northeast, div1, div2 = northeast_organizer(iso_data)

    midwest, div3, div4 = midwest_organizer(iso_data)

    south, div5, div6, div7 = south_organizer(iso_data)

    west, div8, div9 = west_organizer(iso_data)

    #Division 1-9

    #Nested in some iterative operation through regional/divisional data
    year_classes = year('some regional/divisional data')

    #Nested in some iterative operation through regional/divsional data --> iterative operation through year data
    benefit_classes = benefit('some regional/divisional data --> year data')

    #Below 2 nested in region --> year --> benfit
    percentage_classes = 

    count_classes = 

    #Need a variable (or multiple) that will store info yielded from the above triple nest

    #Conditional - percentage figures or total figures?

    #EDA 

    #Visual display

    #Interpretation



    #Need a loop such that it iteratively calls region_organizer to obtain separated data by region

    #Idea - create functions for each region, such that respective regional data, along with the according divisional data,
    #is returned

    #Then need a loop such that it iteratively calls payment_class to obtain data specific to payment class

    #Next, pass through to EDA and obtain some interpretation of the data

    #Once we have made various interpretations (by division and by region), pass to visual_display

    #This is where we will use Seaborn to show data on a visual basis 



def excel_csv_conversion():
   
    Yr06 = pd.read_excel('../data/raw/group36_MedicareData.xlsx', sheet_name='PUF_2006', header=1)
    Yr07 = pd.read_excel('../data/raw/group36_MedicareData.xlsx', sheet_name='PUF_2007', header=1)
    Yr08 = pd.read_excel('../data/raw/group36_MedicareData.xlsx', sheet_name='PUF_2008', header=1)
    Yr09 = pd.read_excel('../data/raw/group36_MedicareData.xlsx', sheet_name='PUF_2009', header=1)
    Yr10 = pd.read_excel('../data/raw/group36_MedicareData.xlsx', sheet_name='PUF_2010', header=1)
    Yr11 = pd.read_excel('../data/raw/group36_MedicareData.xlsx', sheet_name='PUF_2011', header=1)
    Yr12 = pd.read_excel('../data/raw/group36_MedicareData.xlsx', sheet_name='PUF_2012', header=1)

    Yrlist = [Yr06, Yr07, Yr08, Yr09, Yr10, Yr11, Yr12]

    Numlist = [2006, 2007, 2008, 2009, 2010, 2011, 2012]

    for i in range(len(Yrlist)):
        Yrlist[i]['Year'] = Numlist[i]

    Yrtable = pd.concat(Yrlist)

    Yrtable.to_csv('../data/raw/concatenated_data.csv', sep=',', index=False)

    return Yrtable

def csv_file_cleaner(raw_csv):

    cleandata = pd.read('../data/processed/concatenated_data.csv', sep=',', index=False)

    return cleandata

def column_extraction(data):

    #Goal - choose your desired columns that fit the research question(s); create new dataframes 
    #fitting the scope
    #Transition - pass to region organizer, which will isolate data per state

    #population totals
    total_df = data[['total']]
    gender_df = data[['female', 'male']]
    age_df = data[['<40, %', '40-64, %', '65-84, %', '>84, %']]
    ethnicity_df = data[['non-hi wh, %', 'af am, %', 'hi, %', 'as or pi, %', 'fn, %', 'unknown, %']]
    
    #option 1 - substance use, mental health, related physiological ailments, poverty relation
    pr_df = data[['poverty relation, %']]
    substance_use_df = data[['tobacco, %', 'alcohol, %', 'drug use, %', 'opioid use, %']]
    mental_health_df = data[['depression, %', 'clincal depression, %', 'adhd, %', 'anxiety, %',
    'bpd, %', 'personality disorders, %', 'ptsd, %', 'schizophrenia, %', 'schizophrenia or other, %']]
    substance_complication_df = data[['opioid complicaton, %']]
    
    #option 2 - population, FFS population(s), services used via FFS classification, revenue generated by FFS
    #specific focus - mental health services and hospital services
    mental_health_df2 = data[['res mental health, %', 'com mental health, %', 'com mental health, ffs',
    'medicaid mental health, ffs']]
    hospital_df = data[['acute ip hosp days, m and m', 'acute ip hosp admis, m and m',
    'acute ip hosp readmis, m and m', 'readmis rate, %', 'ed visits, m and m', 'ed visits per 1k',
    'medicare ip hosp, ffs', 'medicare other ip hosp, ffs', 'medicaid ip hosp, ffs', ]]
    ffs_df = data[['total, ffs', 'female, ffs', 'male, ffs']]
    ffs_vs_partd_df = data[['ffs medicaid year-round, %', 'ffs medicare year-round, %', 'part d coverage year-round, %']]
    revenues_df = data[['medicare ffs, $', 'ip hosp admis, m and m $', 'medicare ip hosp, ffs $',
     'medicare other ip hosp, ffs $', 'medicare com mental health, ffs $', 'medicaid, ffs $', 'medicaid ip hosp, ffs $',
     'medicaid mental health, ffs $']]

    #development_df = data[['autism, %', 'intellectual, %', 'learning, %']]
    #ms_df = data[['ms, %']]

    return 'data of some kind (TBD)'

def state_organizer(data):

    #yr = int(input('Yr: '))
    #state = str(input('State: '))

    National = data.loc[(data['State'] == 'National')]
    StateAK = data.loc[(data['State'] == 'AK')]
    StateAL = data.loc[(data['State'] == 'AL')]
    StateAR = data.loc[(data['State'] == 'AR')]
    StateAZ = data.loc[(data['State'] == 'AZ')]
    StateCA = data.loc[(data['State'] == 'CA')]
    StateCO = data.loc[(data['State'] == 'CO')]
    StateCT = data.loc[(data['State'] == 'CT')]
    StateDC = data.loc[(data['State'] == 'DC')]
    StateDE = data.loc[(data['State'] == 'DE')]
    StateFL = data.loc[(data['State'] == 'FL')]
    StateGA = data.loc[(data['State'] == 'GA')]
    StateHI = data.loc[(data['State'] == 'HI')]
    StateIA = data.loc[(data['State'] == 'IA')]
    StateID = data.loc[(data['State'] == 'ID')]
    StateIL = data.loc[(data['State'] == 'IL')]
    StateIN = data.loc[(data['State'] == 'IN')]
    StateKS = data.loc[(data['State'] == 'KS')]
    StateKY = data.loc[(data['State'] == 'KY')]
    StateLA = data.loc[(data['State'] == 'LA')]
    StateMA = data.loc[(data['State'] == 'MA')]
    StateMD = data.loc[(data['State'] == 'MD')]
    StateME = data.loc[(data['State'] == 'ME')]
    StateMI = data.loc[(data['State'] == 'MI')]
    StateMN = data.loc[(data['State'] == 'MN')]
    StateMO = data.loc[(data['State'] == 'MO')]
    StateMS = data.loc[(data['State'] == 'MS')]
    StateMT = data.loc[(data['State'] == 'MT')]
    StateNC = data.loc[(data['State'] == 'NC')]
    StateND = data.loc[(data['State'] == 'ND')]
    StateNE = data.loc[(data['State'] == 'NE')]
    StateNH = data.loc[(data['State'] == 'NH')]
    StateNJ = data.loc[(data['State'] == 'NJ')]
    StateNM = data.loc[(data['State'] == 'NM')]
    StateNV = data.loc[(data['State'] == 'NV')]
    StateNY = data.loc[(data['State'] == 'NY')]
    StateOH = data.loc[(data['State'] == 'OH')]
    StateOK = data.loc[(data['State'] == 'OK')]
    StateOR = data.loc[(data['State'] == 'OR')]
    StatePA = data.loc[(data['State'] == 'PA')]
    StateRI = data.loc[(data['State'] == 'RI')]
    StateSC = data.loc[(data['State'] == 'SC')]
    StateSD = data.loc[(data['State'] == 'SD')]
    StateTN = data.loc[(data['State'] == 'TN')]
    StateTX = data.loc[(data['State'] == 'TX')]
    StateUT = data.loc[(data['State'] == 'UT')]
    StateVA = data.loc[(data['State'] == 'VA')]
    StateVT = data.loc[(data['State'] == 'VT')]
    StateWA = data.loc[(data['State'] == 'WA')]
    StateWI = data.loc[(data['State'] == 'WI')]
    StateWV = data.loc[(data['State'] == 'WV')]
    StateWY = data.loc[(data['State'] == 'WY')]

    Statelist = [National, StateAK, StateAL, StateAR, StateAZ, StateCA, StateCO, StateCT,
    StateDC, StateDE, StateFL, StateGA, StateHI, StateIA, StateID, StateIL, StateIN, StateKS, StateKY,
    StateLA, StateMA, StateMD, StateME, StateMI, StateMN, StateMO, StateMS, StateMT, StateNC, StateND, 
    StateNE, StateNH, StateNJ, StateNM, StateNV, StateNY, StateOH, StateOK, StateOR, StatePA, StateRI,
    StateSC, StateSD, StateTN, StateTX, StateUT, StateVA, StateVT, StateWA, StateWI, StateWV, StateWY]

    return Statelist

def northeast_organizer(data):
    #Northeast
    div1 = [StateCT, StateME, StateMA, StateNH, StateRI, StateVT]
    df_newengland = pd.concat(div1)
    df_newengland['Division'] = 'New England'
    div2 = [StateNJ, StateNY, StatePA]
    df_midatlantic = pd.concat(div2)
    df_midatlantic['Division'] = 'Mid-Atlantic'
    northeast = [div1, div2]
    df_northeast = pd.concat(div1 + div2)
    df_northeast['Region'] = 'Northeast'

    return df_northeast, df_newengland, df_midatlantic

def midwest_organizer(data):
    #Midwest
    div3 = [StateIL, StateIN, StateMI, StateOH, StateWI]
    df_eastnorthcentral = pd.concat(div3)
    df_eastnorthcentral['Division'] = 'East North Central'
    div4 = [StateNE, StateMO, StateND, StateSD, StateIA, StateKS, StateMN] 
    df_westnorthcentral = pd.concat(div4)
    df_westnorthcentral['Division'] = 'West North Central'
    midwest = [div3, div4]
    df_midwest = pd.concat(midwest)
    df_midwest['Region'] = 'Midwest'

    return df_midwest, df_eastnorthcentral, df_westnorthcentral

def south_organizer(data):
    #South
    div5 = [StateDE, StateFL, StateGA, StateMD, StateNC, StateSC, StateVA, StateWV]
    df_southatlantic = pd.concat(div5)
    df_southatlantic['Division'] = 'South Atlantic'
    div6 = [StateAL, StateKY, StateMS, StateTN]
    df_eastsouthcentral = pd.concat(div6)
    df_eastsouthcentral['Division'] = 'East South Central'
    div7 = [StateAR, StateLA, StateOK, StateTX]
    df_westsouthcentral = pd.concat(div7)
    df_westsouthcentral['Division'] = 'West South Central'
    south = [div5, div6, div7]
    df_south = pd.concat(south)
    df_south['Region'] = 'South'

    return df_south, df_southatlantic, df_eastsouthcentral, df_westsouthcentral

def west_organizer(data):
    #West
    div8 = [StateID, StateAZ, StateCO, StateMT, StateNM, StateNV, StateUT, StateWY]
    df_mountain = pd.concat(div8)
    df_mountain['Division'] = 'Mountain'
    div9 = [StateAK, StateCA, StateHI, StateOR, StateWA]
    df_pacific = pd.concat(div9)
    df_pacific['Division'] = 'Pacific'
    west = [div8, div9]
    df_west = pd.concat(west)
    df_west['Region'] = 'West'

    return df_west, df_mountain, df_pacific

def national_organizer(data):
    #National
    national = northeast + midwest + south + west
    national_df = pd.concat(national)

    return national_df
    
    #for comparing data across states, fixed year
    #fixed_year = data.loc[(data['Year'] == yr)]

    #for comparing data across years, fixed state
    #fixed_state = data.loc[(data['State'] == state)]

  
def column_name_selection(data):

    #shortening column names for ease of extraction
    abbrv_data = data.rename(columns={'Number of People': 'total', 'Number of People with FFS': 'total, ffs',
    'Number of Females with FFS': 'female, ffs', 'Number of Males with FFS': 'male, ffs', 
    'Percent with all 12 months in FFS Medicaid': 'ffs medicaid year-round, %', 
    'Percent with all 12 months in FFS Medicare': 'ffs medicare year-round, %',
    'Percent with all 12 months with Medicare Part D coverage': 'part d coverage year-round, %',
    'Percent under 40 Years': '<40, %', 'Percent between 40-64 Years': '40-64, %',
    'Percent between 65-84 Years': '65-84, %', 'Percent 85+ Years': '>84, %',
    'Percent under 65 Years': '<65, %', 'Percent 65+ Years': '>65, %',
    'Percent Female': 'female, %', 'Percent Male': 'male, %', 'Percent Non-Hispanic White': 'non-hi wh, %',
    'Percent African American': 'af am, %', 'Percent Hispanic': 'hi, %',
    'Percent Asian or Pacific Islander': 'as or pi, %', 
    'Percent American Indian or Alaskan Native': 'fn, %',
    'Percent Other or Unknown Race': 'unknown, %', 
    'Percent of Medicaid enrollees with MAS - Poverty Related': 'poverty relation, %',
    'Percent of people with depression (any instance including bipolar episodes)': 'depression, %',
    'Percent of people with Major Depressive Disorders': 'clinical depression, %',
    'Percent of people with ADHD or other conduct disorders': 'adhd, %':
    'Percent of people with anxiety': 'anxiety, %':
    'Percent of people with bipolar disorder': 'bpd, %',
    'Percent of people with personality disorders': 'personality disorders, %',
    'Percent of people with post-traumatic stress disorder': 'ptsd, %',
    'Percent of people with schizophrenia': 'schizophrenia, %',
    'Percent of people with schizophrenia or other psychotic disorders': 'schizophrenia or other, %',
    'Percent of people with tobacco use disorder': 'tobacco, %',
    'Percent of people with autism': 'autism, %',
    'Percent of people with intellectual disabilities': 'intellectual, %',
    'Percent of people with learning disabilities': 'learning, %',
    'Percent of people with multiple sclerosis and transverse myelitis': 'ms, %',
    'Percent of people with alcohol use disorder': 'alcohol, %',
    'Percent of people with drug use disorder': 'drug use, %',
    'Percent of people with opioid use disorder diagnosis': 'opioid use, %',
    'Percent of people with opioid related hospitalization or ED visit': 'opioid complication, %',
    'Total Medicare FFS payments': 'medicare ffs, $',
    'Percent with at least one Medicare or Medicaid Residential Mental Health service': 'res mental health, %',
    'Percent with at least one Medicare or Medicaid Community Mental Health Service': 'com mental health, %',
    'Number of FFS people who used Medicare Community Mental Health Clinic Services': 'com mental health, ffs',
    'Count of Acute IP Hospital Days - Medicare and Medicaid combined': 'acute ip hosp days, m and m',
    'Count of Acute IP Hospital Admissions - Medicare and Medicaid combined': 'acute ip hosp admis, m and m',
    'Total dollars (Medicare and Medicaid) associated with IP hospital admissions': 'ip hosp admis, m and m $',
    'Count of Acute IP Hospital 30-day Readmissions - Medicare and Medicaid combined': 'acute ip hosp readmis, m and m',
    'Readmission Rate ('%' of admissions that are readmissions)': 'readmis rate, %',
    'Count of ED Visits - Medicare and Medicaid combined': 'ed visits, m and m':
    'ED Visits per 1000 enrollees': 'ed visits per 1k',
    'Number of FFS people who used Medicare IP Hospital services': 'medicare ip hosp, ffs',
    'Number of FFS people who used Medicare Other IP Hospital services': 'medicare other ip hosp, ffs',
    'Total Medicare IP Hospital FFS payments': 'medicare ip hosp, ffs $',
    'Total Medicare Other IP Hospital FFS payments': 'medicare other ip hosp, ffs $',
    'Total Medicare Community Mental Health Clinic FFS Payments': 'medicare com mental health, ffs $',
    'Number of FFS people who used Medicaid Hospital services': 'medicaid ip hosp, ffs',
    'Number of FFS people who used Medicaid mental health services': 'medicaid mental health, ffs',
    'Total Medicaid FFS payments': 'medicaid, ffs $',
    'Total Medicaid IP Hospital FFS Payments': 'medicaid ip hosp, ffs $',
    'Total Medicaid mental health FFS payments': 'medicaid mental health, ffs $'})

    return abbrv_data


def new_columns():

    #Will create new columns for: regional means in a fixed year;
    #regional means across years;
    #state meaans across years;
    #national means in a fixed year;
    #national means across years;
    #ideally, a column for percent changes across each year (regional and national)

    #First, must complete EDA #1

def missing_data_filler(data):
    
    filled_data = data.replace('*', '0')
    filled_data = filled_data.replace('.', '0')
    filled_data = filled_data.replace(' ', '0')
    
    return filled_data

def year(data):

    data06 = data.loc((data['Year'] == 2006))
    data07 = data.loc((data['Year'] == 2007))
    data08 = data.loc((data['Year'] == 2008))
    data09 = data.loc((data['Year'] == 2009))
    data10 = data.loc((data['Year'] == 2010))
    data11 = data.loc((data['Year'] == 2011))
    data12 = data.loc((data['Year'] == 2012))

    year_classes = [data06, data07, data08, data09, data10, data11, data12]

    return year_classes

def benefit(data):
    
    #Separating data by benefit type/payment classification
    full = []
    partial = []
    medicare_only = []
    medicaid_only = []
    #Separating regionak
    for i in data_list:
        full += i.loc('Full Benefit')
        partial += i.loc('Partial Benefit')
        medicare_only += i.loc('Medicare Only')
        medicaid_only += i.loc('Medicaid Only (Disability)')

    benefit_classes = [full, partial, medicare_only, medicaid_only]

    return benefit_classes

def eda_counts(data, count_type = None): 

    #first, obtain means across divsions and regions for each year;
    
    # gender_df = data[['female', 'male']]
    # age_df = data[['<40, %', '40-64, %', '65-84, %', '>84, %']]
    # ethnicity_df = data[['non-hi wh, %', 'af am, %', 'hi, %', 'as or pi, %', 'fn, %', 'unknown, %']]

    #Need data points for each year
    #Will graph these points over time
    #Expressed as means per division and per region
    #Need to create matrices, where rows are the years and columns are the respective states from each div.
    #data_list variable isolates years, so need to iterate through data_list 
    #Assumption - either a region or division is being passed through

    #This data is pulled from ... this data covers ... amount of people nationwide, 
    #... from the ... region (... from {div} and ... from {div})
    # " "
    #Question 1:    
    
    #benefit_classes = ['Full Benefit', 'Partial Benefit', 'Medicare Only', 'Medicaid Only (Disability)'

    #Function for gathering total counts across divsions/regions, per year
    
    #totals_dict = {'Full Benefit': 0, 'Partial Benefit': 0, 'Medicare Only': 0, 'Medicaid Only (Disability)': 0}

    #Obtaining regional/divisional totals, per year
    
    array_init = data.loc(count_type)
    array_counts = np.array(array_init)
    new_total = np.sum(array_counts)
    
    return new_total

    #Above syntax good for counting totals across regions and divisions; 
    #Can also be used for mean values of totals across years, by looping through the dictionary

def eda_total(data, percentage_type = None):
    
    array_init = data.loc(percentage_type)
    divisor = len(array_init)
    percentages_array = np.array(array_init)
    percentages_sum = np.sum(percentages_array)
    percentages_mean = percentages_sum/divisor

    return percentages_mean













