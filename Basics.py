
# coding: utf-8

# In[9]:


#imports our data into "data" list
import csv
f = open("guns.csv")
moreguns = csv.reader(f)
data = list(moreguns)


# In[10]:


#deletes headers from data and assigns it to "headers" list
headers = data[0]
del data[0]


# In[31]:


#creates the list "years" which displays each gun death in its own list
year = []
years = []
for row in data:
    year = row[1]
    years.append(year)

    #creates dictionary that lists how many fatalities in each year
year_counts = {}
for i in years:
    if i not in year_counts:
        year_counts[i] = 1
    else:
        year_counts[i] += 1
        
print(year_counts)


# In[40]:


#creates a "dates" list with the fatality date
import datetime
dates = []
for row in data:
    row_year = int(row[1])
    row_month = int(row[2])
    row_day = 1
    row_date = datetime.datetime(year = row_year, month = row_month, day = row_day)
    dates.append(row_date)
                  
print(dates[:5])


# In[41]:


#finds the number of times each date appears for a fatality
date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date]+=1
    else:
        date_counts[date]=1

print(date_counts)


# In[43]:


#counts frequency of a sex or a race coming up in fatalities
sex_counts = {}
race_counts = {}
for row in data:
    gender = row[5]
    race = row[7]
    if gender in sex_counts:
        sex_counts[gender]+=1
    else:
        sex_counts[gender]=1
    if race in race_counts:
        race_counts[race] +=1
    else:
        race_counts[race] = 1

print(sex_counts)
print(race_counts)


# In[44]:


#imports census data
census_open = open("census.csv")
census_read = csv.reader(census_open)
census = list(census_read)


# In[48]:


#sums the population for each race from the census data
mapping = {}
mapping["Asian/Pacific Islander"] = int(census[1][14])+int(census[1][15])
mapping["Black"] = int(census[1][12])
mapping["Native American/Native Alaskan"] = int(census[1][13])
mapping["Hispanic"] = int(census[1][11])
mapping["White"]=int(census[1][10])

#finds the fatalities per 100,000 population
race_per_hundredk = {}
for race in race_counts:
    race_per_hundredk[race] = race_counts[race] / mapping[race] * 100000
    

    print(race_per_hundredk)


# In[52]:


#creates a filtered data set of ONLY homicides called "intents"
intents = []
for i in data:
    intent = i[3]
    if intent == "Homicide":
        intents.append(i)
#counts how many times each race appears in "intents" list, which is a list of homicides only
homicide_race_counts = {}
for i in intents:
    race = i[7]
    if race in homicide_race_counts:
        homicide_race_counts[race]+=1
    else:
        homicide_race_counts[race]=1
        
#finds these homicide rate counts per 100,000 individuals
homicide_race_per_hundredk = {}
for race in homicide_race_counts:
    homicide_race_per_hundredk[race] = homicide_race_counts[race] / mapping[race] * 100000

print(homicide_race_per_hundredk)

