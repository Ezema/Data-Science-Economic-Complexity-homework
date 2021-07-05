# %% [markdown]
# # CM2015 Programming with Data Coursework
# 
# ----------------------------------------------------
# ## <i> Research on the relationship between economic complexity, income-inequality and recession-recovery performance across OECD member countries</i>
# ----------------------------------------------------
# 
# ### Introduction
# 
# The economic complexity index (ECI) is a measure that describes the ability and know-how of a given economy to successfully produce and export technically complex products to other countries by outcompeting them.
# 
# As defined in the economic complexity index author's website:
# >"A measure of the knowledge in a society as expressed in the products it makes...Countries that are able to sustain a diverse range of productive know-how, including sophisticated, unique know-how, are found to be able to produce a wide diversity of goods, including complex products that few other countries can make."
# ><cite>https://atlas.cid.harvard.edu/glossary</cite>
# 
# Given that we are currently experiencing the so-called <a href="https://en.wikipedia.org/wiki/Fourth_Industrial_Revolution">"Fourth Industrial Revolution"</a> in which the main drivers of economic productivity increases are given by the ability to develop high-technology advancements and implement those advancements in goods, and also, considering that global trade as a percentage of global GDP <a href="https://data.worldbank.org/indicator/NE.TRD.GNFS.ZS"> is at all-time-highs</a>, the countries that adapt more quickly to this high-technology environment are expected (all else being equal) to outperform in terms of economic growth.
# 
# ### Objective
# 
# In this research, we will try to find out if there is a correlation between a country's high economic-complexity score, a low-income inequality level (due to a higher level of the country's workforce in high-paying industries), and a faster recovery in the country's GDP per capita (in <a href="https://en.wikipedia.org/wiki/Real_versus_nominal_value_(economics)"> real </a> purchasing power parity terms) after the global <a href="https://en.wikipedia.org/wiki/Great_Recession">2007-2009 great recession</a>.
# 
# ### Hypotheses to test
# 
# 1. Given that a high ECI score denotes a country whose exports are highly technically complex, one would expect a higher proportion of the country's population with higher education levels with above-average income which would lead to less <a href="https://en.wikipedia.org/wiki/Poverty#Relative_poverty">relative poverty</a> among its citizens and therefore less income inequality.<br/><br/>
# 2. A high ECI score shows a greater diversification and greater added value in the exports of a given country so this should reflect in greater resilience to handle global recessions. <br/>Having that said, right after the 2008 global recession, commodities prices rallied sharply on financial markets fears of inflation<sup><a href="https://www.reuters.com/article/markets-global/global-markets-oil-near-130-inflation-fears-drag-down-stocks-idUSN2033411520080520">[1]</a></sup> and, for the purpose of this research, this rally leads to statistical noise which means that the correlation will test ECI score and recession resilience <b>adjusting for the great differences between OECD countries when it comes to the availability of natural resources.</b> <br>Examples of these great disparities in natural resources are Japan (few natural resources) vs Australia (great natural resources) or Germany (few natural resources) vs Norway (great natural resources) 
# 
# ### Considerations about the data provenance 
# 
# 1. Regarding the Economic Complexity Index (ECI), it can be said that the data is reliable and trustworthy as it is first obtained from the United Nations Statistical Division and the International Monetary Fund and then all inconsistencies are cleaned by the team of experts that work in Harvard's Growth Lab to ensure the integrity of the report.
# The details of the data cleaning process carried out by the team of experts can be checked in the following entry: https://atlas.cid.harvard.edu/about-data
# <br/><br/>
# 2. The poverty by country data that will be used as the basis to express the income inequality in a given country will be obtained from the Organisation for Economic Co-operation and Development (OECD).
# The OECD is an intergovernmental economic organisation with 38 member countries.
# Even though the majority of the countries publish some kind of statistics regarding poverty, I have chosen to use the OECD's statistics because I understand that they are the most reliable and transparent given that the OECD statistic's collection methodology is country-independent and also because the organization sets a harmonized standard on how to account poverty across different economies.
# The details on the OECD's statistics methodology can be found in the following website: https://www.oecd.org/development/stats/methodology.htm
# <br/><br/>
# 3. The GDP per capita in terms of purchasing power parity data is published by both the World Bank (WB) and the International Monetary Fund (IMF). 
# Both the IMF and the World Bank are institutions part of the United Nations system and recognized by all the <a href="https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations">193 sovereign state<a> governments of the World.
#     
# ### Datasets used in this research
# 
# Three datasets will be used in this research:
# 
# 1. The economic-complexity index is published by the "Atlas of Economic Complexity" which is part of the <a href="https://atlas.cid.harvard.edu/growth-lab">Growth Lab at Harvard University</a>.
# <br/>The index data can be downloaded as <b>a CSV file</b> from the official website: https://atlas.cid.harvard.edu/rankings
# <br/><br/>
# 2. The "average OECD relative poverty rate by country" data is extracted from the OECD's "society at a glance 2019 report". This research will use <b>one CSV file</b> that contains the total percentage of people in relative poverty by country. The CSV file was downloaded from the official website: https://www.oecd-ilibrary.org/sites/8483c82f-en/index.html?itemId=/content/component/8483c82f-en
# <br/><br/>
# 3. Given that the GDP per capita in purchasing power parity (PPP) terms data is provided by both the IMF and the World Bank, this work will consider both sources, compare them and then choose one of them to test the hypotheses.<br/>The World Bank data is included in <b>a CSV file</b> downloaded from the official website: https://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.PP.CD?downloadformat=csv
# <br/>The IMF data will be <b>web scraped</b> from the official website using the Python package "Beautiful Soup"
# <br/>
#     
# ### Use permission and licitness of the data considered in this research
# 
# 1. The Economic Complexity Index is free and meant for public use<sup>[1]</sup> and is developed by The Growth Lab at Harvard University.
#     
# 2. All the data extracted from the OECD is free and meant for public use<sup>[2]</sup>. In this research, one CSV file downloaded from the official website is used.
#     
# 3. All the data extracted from the World Bank is free and meant for public use<sup>[3]</sup>. In this research, one CSV file downloaded from the official website is used.
#     
# 4. Given that we are web-scraping data from the IMF's official website, the terms of the website state<sup>[4]</sup>:
# 
# > <i>"Users may not use the Sites or Content in a manner that i) disrupts, disables or overburdens the IMF’s administration and management of the Sites; or ii) interferes with another User’s ability to access the Sites, as determined by the IMF at its sole discretion."</i>
# 
# There are no explicit prohibitions for web-scraping techniques. In other words, as long as we are not sending a lot of requests per second in order to disturb the normal functioning of the website, we are free to use it.
#     
# 5. Wikipedia does not explicitly forbid web-scraping and under the terms of use page it is stated that as long as the automated action is not performed in an "abusive or disruptive manner" the user of the site is free to disseminate the information on the site<sup>[5]</sup>. 
# 
# <sup>[1]</sup> Source: https://atlas.cid.harvard.edu/data-use-permissions
# <sup>[2]</sup> Source: https://www.oecd.org/termsandconditions/
# <sup>[3]</sup> Source: https://data.worldbank.org/summary-terms-of-use
# <sup>[4]</sup> Source: https://www.imf.org/external/terms.htm
# <sup>[5]</sup> Source: https://foundation.wikimedia.org/wiki/Terms_of_Use/en
#     
# ### Some scope and data cleaning considerations before starting the research
#     
# Before starting working on the datasets to test the hypotheses, it should be noted that even though the Economic Complexity Index includes data for 133 countries and the IMF and World Bank data includes GDP (PPP) per capita data for over 200 countries, this research will only focus on the 38 countries that are members of OECD because, as previously stated, <u>making fair comparisons of relative poverty between countries is impossible if each country has a different standard for measuring relative poverty.</u><br/>Working with OECD's poverty data ensures that we are making a fair "apples-to-apples" comparison between countries. This is the reason why this research will limit itself to OECD countries.

# %%


# %% [markdown]
# 

# %% [markdown]
# -------------------------------------
# ### First part: obtaining datasets and data cleaning

# %% [markdown]
# Importing the libraries that will be used in the project: pandas, requests, BeautifulSoup, NumPy, matplotlib, and seaborn:

# %%
import seaborn
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Turning off pandas suggestions for chained assignments
pd.options.mode.chained_assignment = None

# %% [markdown]
# Load the OECD's population in relative poverty by country data from the excel file:

# %%
#Load the OECD provided excel file
FilePopulationInPovertyByCountry = pd.ExcelFile('OECD_populationInPovertyByCountry.xlsx')

#Select sheet "data6-4" from the excel file
DataFramePopulationInPovertyByCountry = pd.read_excel(FilePopulationInPovertyByCountry, 'data6-4')

#Print result
DataFramePopulationInPovertyByCountry

# %% [markdown]
# ---------------------
# Cleaning the raw dataframe:

# %%
#Only need the columns for the country name and the column for total relative poverty rate
DataFramePopulationInPovertyByCountry = DataFramePopulationInPovertyByCountry.drop(DataFramePopulationInPovertyByCountry.columns[3:], axis=1)

DataFramePopulationInPovertyByCountry

#Dropping the column that shows the country ISO codes
DataFramePopulationInPovertyByCountry = DataFramePopulationInPovertyByCountry.drop(DataFramePopulationInPovertyByCountry.columns[1], axis=1)

#Remove unnecesary first rows
DataFramePopulationInPovertyByCountry = DataFramePopulationInPovertyByCountry.drop(DataFramePopulationInPovertyByCountry.index[0:9])

#Remove unnecesary last rows
DataFramePopulationInPovertyByCountry = DataFramePopulationInPovertyByCountry.drop(DataFramePopulationInPovertyByCountry.index[46:])

#Drop rows with not a number (NaN) values
DataFramePopulationInPovertyByCountry = DataFramePopulationInPovertyByCountry.dropna()

#Convert relative poverty rate column value types to float
DataFramePopulationInPovertyByCountry["Unnamed: 2"] = DataFramePopulationInPovertyByCountry["Unnamed: 2"].astype(float)

#Convert country names column value types to string
DataFramePopulationInPovertyByCountry["Society at a Glance 2019 - © OECD 2019"] = DataFramePopulationInPovertyByCountry["Society at a Glance 2019 - © OECD 2019"].astype("string")

#Renaming columns to "Country" and "Relative Poverty Rate"
DataFramePopulationInPovertyByCountry.columns = ['Country', 'Relative Poverty Rate (%)']

#Resetting the dataframe index now that the dataframe is cleaned
DataFramePopulationInPovertyByCountry.reset_index(drop=True, inplace=True)

#Print result
DataFramePopulationInPovertyByCountry

# %% [markdown]
# It should be noted that the excel file provided by the OECD allows us to analyse 43 countries (one row of the 'Country' column includes 'OECD' which means the average for the OECD member countries)

# %%
#Saving OECD members average relative-porverty
OECDMembersRelativePovertyAverage = DataFramePopulationInPovertyByCountry.iloc[20,1:2]

#Drop the OECD members average-poverty entry from the dataframe
DataFramePopulationInPovertyByCountry = DataFramePopulationInPovertyByCountry.drop(DataFramePopulationInPovertyByCountry.index[20])

#Sort dataframe by country relative-poverty value
DataFramePopulationInPovertyByCountry = DataFramePopulationInPovertyByCountry.sort_values('Relative Poverty Rate (%)')

# %%
#Setting the graph size on Matplotlib
plt.figure(figsize=(15,8))

#Creating the graph with seaborn
graphRelativePoverty = seaborn.barplot(x=DataFramePopulationInPovertyByCountry['Country'],y=DataFramePopulationInPovertyByCountry['Relative Poverty Rate (%)'], palette=["blue"])

#Changing country label visualization parameters so they don't overlap each other
graphRelativePoverty.set_xticklabels(graphRelativePoverty.get_xticklabels(), rotation=40, ha="right", fontsize=11)

#Show graph
graphRelativePoverty

# %% [markdown]
# --------------------------------------------------------------------
# Load the Economic complexity index data from the CSV file:

# %%
# Load economic complexity CSV file
DataFrameEconomicComplexity = pd.read_csv("Harvard_GLab_CountryComplexityRankings1995to2018.csv")

# Print dataframe
DataFrameEconomicComplexity

# %% [markdown]
# Cleaning the dataframe:

# %%
# Given that the file includes the "complexity outlook index" (COI) that is not considered in this research, the dataframe gets cleaned so only the "economic complexity index" (ECI) data is kept.
DataFrameWithECIStatsOnly = DataFrameEconomicComplexity.loc[:, (DataFrameEconomicComplexity.columns.str.contains("Country") + DataFrameEconomicComplexity.columns.str.contains("ECI"))]

#Create a new dataframe that will keep each country's ECI score over the years
DataFrameECIScoreByCountry = DataFrameWithECIStatsOnly[DataFrameWithECIStatsOnly.columns.drop(list(DataFrameWithECIStatsOnly.filter(regex="Rank")))]

#Create a new dataframe that will keep each country's position in the global ECI ranking over the years
DataFrameECIRankingByCountry = DataFrameWithECIStatsOnly.loc[:, (DataFrameWithECIStatsOnly.columns.str.contains("Country") + DataFrameWithECIStatsOnly.columns.str.contains("ECI Rank"))]

#Create a new dataframe that will store only the latest year ECI rankings
DataFrameECIRankingByCountryLatestDataOnly = DataFrameECIRankingByCountry.iloc[:,0:2]

#Print latest ECI rankings
DataFrameECIRankingByCountryLatestDataOnly

# %%
#Sorting the dataframe by ECI rankign position
DataFrameECIRankingByCountryLatestDataOnly = DataFrameECIRankingByCountryLatestDataOnly.sort_values('ECI Rank 2018')

#Resetting the index values
DataFrameECIRankingByCountryLatestDataOnly.reset_index(drop=True, inplace=True)

#Print first 15 positions
DataFrameECIRankingByCountryLatestDataOnly.head(15)

# %% [markdown]
# ----------------------------------------
# Load the GDP per capita (PPP) data from the World-Bank's excel file:

# %%
#Loading excel file
DataFrameGDPPerCapitaByCountryPPP = pd.read_excel("WorldBank_GDPPPPPerCapitaByCountry.xlsx")

#Print dataframe
DataFrameGDPPerCapitaByCountryPPP

# %% [markdown]
# Performing the dataframe cleaning:

# %%
#Convert "Data source" column values to be of type string
DataFrameGDPPerCapitaByCountryPPP["Data Source"] = DataFrameGDPPerCapitaByCountryPPP["Data Source"].astype("string")

#Create new dataframe that just contains the country names column
countriesNamesColumn = DataFrameGDPPerCapitaByCountryPPP.iloc[:,0:1]

#Create new dataframe that contains the columns ranging from year 1990 to year 2019
GDPPerCapitaFrom1990to2019 = DataFrameGDPPerCapitaByCountryPPP.iloc[:,34:-1]

#Concatenate the previously created columns
DataFrameGDPPerCapitaByCountryPPP = pd.concat([countriesNamesColumn, GDPPerCapitaFrom1990to2019], axis=1)

#Remove first 3 empty rows
DataFrameGDPPerCapitaByCountryPPP = DataFrameGDPPerCapitaByCountryPPP[3:]

#Print resulting dataframe
DataFrameGDPPerCapitaByCountryPPP

# %% [markdown]
# Dataframe cleaning continues:

# %%
#Remove rows that contain not a number values (NaN)
DataFrameGDPPerCapitaByCountryPPP = DataFrameGDPPerCapitaByCountryPPP.dropna()

#Change first column name from 'Data Source' to 'Country'
DataFrameGDPPerCapitaByCountryPPP.rename(columns={'Data Source': 'Country'}, inplace=True)

# Create a for loop that will rename the columns with successive years from 1990 to 2019
currentYear = 1990
for column in DataFrameGDPPerCapitaByCountryPPP:    
    if column != "Country":        
        DataFrameGDPPerCapitaByCountryPPP = DataFrameGDPPerCapitaByCountryPPP.rename(columns={column: currentYear})
        currentYear +=1
        
#Print resulting dataframe
DataFrameGDPPerCapitaByCountryPPP

# %% [markdown]
# -----------------------------------
# Last few steps for a clean dataframe

# %%
#Remove first row that was previously acting as an auxiliary header
DataFrameGDPPerCapitaByCountryPPP = DataFrameGDPPerCapitaByCountryPPP.iloc[1:]

#Resetting the dataframe index now that the dataframe is cleaned
DataFrameGDPPerCapitaByCountryPPP.reset_index(drop=True, inplace=True)

#Print resulting dataframe
DataFrameGDPPerCapitaByCountryPPP

# %% [markdown]
# -------------------------------------------------
# The previous GDP per capita (PPP) dataframe was build from the CSV downloaded from the World Banks's website. Now, this data will be obtained from an alternative source, the International Monetary Fund (IMF) website by web-scraping the data with the "BeautifulSoup" and "requests" python packages.

# %%
#Setting the HTTP headers for the upcoming request
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

#Set the target URL 
url = "https://www.imf.org/en/Publications/WEO/weo-database/2019/October/weo-report?c=512,914,612,614,311,213,911,314,193,122,912,313,419,513,316,913,124,339,638,514,218,963,616,223,516,918,748,618,624,522,622,156,626,628,228,924,233,632,636,634,238,662,960,423,935,128,611,321,243,248,469,253,642,643,939,734,644,819,172,132,646,648,915,134,652,174,328,258,656,654,336,263,268,532,944,176,534,536,429,433,178,436,136,343,158,439,916,664,826,542,967,443,917,544,941,446,666,668,672,946,137,546,674,676,548,556,678,181,867,682,684,273,868,921,948,943,686,688,518,728,836,558,138,196,278,692,694,962,142,449,564,565,283,853,288,293,566,964,182,359,453,968,922,714,862,135,716,456,722,942,718,724,576,936,961,813,726,199,733,184,524,361,362,364,732,366,144,146,463,528,923,738,578,537,742,866,369,744,186,925,869,746,926,466,112,111,298,927,846,299,582,474,754,698,&s=PPPPC,&sy=2006&ey=2019&ssm=0&scsm=1&scc=0&ssd=1&ssc=0&sic=0&sort=country&ds=.&br=1"

#Using the requests package to made the "get" HTTP request to the target website using the passed headers
req = requests.get(url, headers)

#Pass the HTTP request response to BeautifulSoup
soup = BeautifulSoup(req.content, 'html.parser')

#Find the "table" HTML tags and store the results on the variable table
scrappedTable = soup.find_all("table")

#Show first table stored in the variable
scrappedTable[0]

# %% [markdown]
# Seeing that the data we are after is indeed in the HTML table, we can pass it to the pandas' HTML reader to create a new pandas dataframe

# %%
#Create new dataframe from the HTML table scrapped from the IMF's website
DataFrameScrapedIMFGDPPerCapitaPPP = pd.read_html(str(scrappedTable))[0]

#Print resulting dataframe
DataFrameScrapedIMFGDPPerCapitaPPP

# %%
#Convert countries name column values into strings
DataFrameScrapedIMFGDPPerCapitaPPP["Country"] = DataFrameScrapedIMFGDPPerCapitaPPP["Country"].astype("string")

#Create a new "historical" dataframe that will contain the GDP per capita data over the years
DataFrameScrapedIMFHistoricalGDPPerCapitaPPP = pd.concat([DataFrameScrapedIMFGDPPerCapitaPPP["Country"], DataFrameScrapedIMFGDPPerCapitaPPP.iloc[:,5:]], axis=1)

#Create a new dataframe that will only contain the GDP per capita data for year 2019
DataFrameScrapedIMF2019GDPPerCapitaPPP = pd.concat([DataFrameScrapedIMFGDPPerCapitaPPP["Country"], DataFrameScrapedIMFGDPPerCapitaPPP["2019"]], axis=1)

#Covert both dataframes column names into strings

DataFrameScrapedIMFHistoricalGDPPerCapitaPPP.columns = DataFrameScrapedIMFHistoricalGDPPerCapitaPPP.columns.astype("string")
DataFrameScrapedIMF2019GDPPerCapitaPPP.columns = DataFrameScrapedIMF2019GDPPerCapitaPPP.columns.astype("string")

#Drop rows with not a number (NaN) values
DataFrameScrapedIMFHistoricalGDPPerCapitaPPP = DataFrameScrapedIMFHistoricalGDPPerCapitaPPP.dropna()

#Resetting dataframe index
DataFrameScrapedIMFHistoricalGDPPerCapitaPPP.reset_index(drop=True, inplace=True)

#Print resulting "historical" dataframe
DataFrameScrapedIMFHistoricalGDPPerCapitaPPP

# %% [markdown]
# Now that the GDP per capita (PPP) data is available from both the IMF and the World Bank, we will calculate the GDP values discrepancy between both sources for each country:

# %%
#Sort world bank GDP data by country name
DataFrameGDPPerCapitaByCountryPPP = DataFrameGDPPerCapitaByCountryPPP.sort_values('Country')

#Create a new dataframe that will store the world bank data only if the country name is also in the IMF's dataframe
DataFrameWorldBankHistoricalGDPPerCapitaByCountryPPP = DataFrameGDPPerCapitaByCountryPPP[DataFrameGDPPerCapitaByCountryPPP.iloc[:,0].isin(DataFrameScrapedIMFHistoricalGDPPerCapitaPPP.iloc[:,0])]

#Remove the GDP data for the years prior to 2006 from the dataframe
DataFrameWorldBankHistoricalGDPPerCapitaByCountryPPP = pd.concat([DataFrameWorldBankHistoricalGDPPerCapitaByCountryPPP.iloc[:,0:1],DataFrameWorldBankHistoricalGDPPerCapitaByCountryPPP.iloc[:,17:]],axis=1)

#Reset the index
DataFrameWorldBankHistoricalGDPPerCapitaByCountryPPP.reset_index(drop=True, inplace=True)

#Create a list that will be populated by the following for-loop and will be later used as the basis for the dataframe that will contain the GDP discrepancy data
IMFvsWorldBankGDPDiscrepancyByCountryAndYear = []

#This for loop will first get each Country's index in the two different dataframes (IMF and World Bank), save them and later compare the discrepancy between the GDP data for that country for each year (2006 to 2019). The resulting percentage variation in the data will be saved in a list.
#After the for loop finishes creating the list for each of the countries, the result is appended to the python array that holds the aggregated results for all of the countries 
for country in DataFrameWorldBankHistoricalGDPPerCapitaByCountryPPP.iloc[:,0]:
    saveIndexOfWorldBankDataFrame = DataFrameWorldBankHistoricalGDPPerCapitaByCountryPPP.index[DataFrameWorldBankHistoricalGDPPerCapitaByCountryPPP['Country'] == country]    
    saveIndexOfIMFDataFrame = DataFrameScrapedIMFHistoricalGDPPerCapitaPPP.index[DataFrameScrapedIMFHistoricalGDPPerCapitaPPP['Country'] == country]        
    #create list containing country name as first value
    countryAndPercentageDifferenceByYear = [country]
    for year in DataFrameWorldBankHistoricalGDPPerCapitaByCountryPPP.iloc[saveIndexOfWorldBankDataFrame,1:]:
        countryAndPercentageDifferenceByYear.append((int(DataFrameScrapedIMFHistoricalGDPPerCapitaPPP.loc[saveIndexOfIMFDataFrame,str(year)])/int(DataFrameWorldBankHistoricalGDPPerCapitaByCountryPPP.loc[saveIndexOfWorldBankDataFrame,year]))*100-100)    
    
    #append country data to the list that contains the data for all of the countries
    IMFvsWorldBankGDPDiscrepancyByCountryAndYear.append(countryAndPercentageDifferenceByYear)
    
#Create a new pandas dataframe from the previous list
DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears = pd.DataFrame(IMFvsWorldBankGDPDiscrepancyByCountryAndYear)

#Remove rows that contain not a number values (NaN)
DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears = DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears.dropna()

#Change first column name from 0 to 'Country'
DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears.rename(columns={0: 'Country'}, inplace=True)

# Create a for loop that will rename the columns with successive years from 2006 to 2019
currentYear = 2006
for column in DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears:    
    if column != "Country":        
        DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears = DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears.rename(columns={column: currentYear})
        currentYear +=1
        
#Show resulting GDP-discrepancy dataframe
DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears

# %% [markdown]
# Graph the mean GDP IMF-World Bank data discrepancy

# %%
#Create a new column that stores the average discrepancy (years 2006-2019)
DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears['Mean GDP data discrepancy (IMF/World Bank)'] = DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears.mean(axis=1)

#Drop rows with not a number (NaN) values
DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears = DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears.dropna()

#Setting the graph size on Matplotlib
plt.figure(figsize=(20,10))

GDPDiscrepancyGraphDataFrame = pd.concat([DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears['Country'],DataFrameWithGDPDataDiscrepancyBetweenIMFandWorldBankOverTheYears['Mean GDP data discrepancy (IMF/World Bank)']],axis=1)

#Create seaborn graph
graphGDPDiscrepancy = seaborn.barplot(x=GDPDiscrepancyGraphDataFrame['Country'],y=GDPDiscrepancyGraphDataFrame['Mean GDP data discrepancy (IMF/World Bank)'], palette=["blue"])

#Edit countries labels styling
graphGDPDiscrepancy.set_xticklabels(graphGDPDiscrepancy.get_xticklabels(), rotation=90, ha="right", fontsize=8)

#Show a grid in the graph
graphGDPDiscrepancy.grid(True)

#Show the result in a graph
graphGDPDiscrepancy


# %% [markdown]
# Graphing discrepancies for OECD member countries

# %%
#load web-scraped OECD members CSV file
OECDMembersDataframeFromCSV = pd.read_csv("webScraped_OECDMembers.csv")

OECDMembersListFromCSV = OECDMembersDataframeFromCSV.Country.to_list()

#Create OECD exclusive dataframe
GDPDiscrepancyGraphDataFrameOECD = GDPDiscrepancyGraphDataFrame[GDPDiscrepancyGraphDataFrame["Country"].isin(OECDMembersListFromCSV)]

#Drop rows with not a number (NaN) values
GDPDiscrepancyGraphDataFrameOECD = GDPDiscrepancyGraphDataFrameOECD.dropna()

#Setting the graph size on Matplotlib
plt.figure(figsize=(15,7))

#Create seaborn graph
graphGDPDiscrepancy = seaborn.barplot(x=GDPDiscrepancyGraphDataFrameOECD['Country'],y=GDPDiscrepancyGraphDataFrameOECD['Mean GDP data discrepancy (IMF/World Bank)'], data=GDPDiscrepancyGraphDataFrameOECD, palette=["blue"])

#Edit countries labels styling
graphGDPDiscrepancy.set_xticklabels(graphGDPDiscrepancy.get_xticklabels(), rotation=40, ha="right", fontsize=8)

#Show a grid in the graph
graphGDPDiscrepancy.grid(True)

#Show the result in a graph
graphGDPDiscrepancy

# %% [markdown]
# The reason why the IMF and the World Bank GDP data differ is that <b>both institutions take a different approach when taking into account inflation and exchange rates.</b> The world bank takes the GDP in the local currency and converts it to US dollars by the official exchange rate that is usually quoted by the national bank of the country. The IMF on the other hand measures the country's GDP in purchasing parity terms (PPP).<br/>Wikipedia<sup>[1]</sup> defines PPP as: 
# 
# >"Purchasing power parity (PPP) is a measurement of prices in different countries that uses the prices of specific goods to compare the absolute purchasing power of the countries' currencies..."
# 
# For the specifics of how the IMF calculates their figures, they provide an extensive (very technical) FAQ page that explains all of it in detail: https://www.imf.org/external/pubs/ft/weo/faq.htm
# 
# For the purpose of this research, I'm inclined to believe the IMF's figures over the figures from the World Bank so, going forward, <b>all the GDP per capita information will be taken from the IMF data</b>.
# 
# [1] Source: https://en.wikipedia.org/wiki/Purchasing_power_parity

# %% [markdown]
# -------------------------------------
# 
# ### Second part: testing first hypothesis, ECI and relative poverty correlation
# -------------------------------------
# 

# %%
#Create a new dataframe by merging the ECI dataframe and the population in realtive-poverty by country dataframe
DataFrameECIAndRelativePoverty = pd.merge(DataFrameECIRankingByCountryLatestDataOnly, DataFramePopulationInPovertyByCountry, on="Country")

#Setting the graph size on Matplotlib
plt.figure(figsize=(15,8))

#Show graph
seaborn.regplot(y=DataFrameECIAndRelativePoverty["Relative Poverty Rate (%)"], x=DataFrameECIAndRelativePoverty["ECI Rank 2018"], data=DataFrameECIAndRelativePoverty)

# %% [markdown]
# From the above graph, it can already be seen that there's some correlation between high economic-complexity and lower relative poverty rates.
# Still, as discussed in the introduction, for a more reliable comparison, <b>the test should only be made between OECD countries since the statistical method is harmonised between member countries.</b>
# 
# A list of the OECD member countries can be web-scrapped from the official OECD website:

# %%
#Setting the HTTP headers for the upcoming request
HTTPHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

#Set the target URL 
OECDMembersUrl = "https://www.oecd.org/about/document/ratification-oecd-convention.htm"

#Using the requests package to made the "get" HTTP request to the target website using the passed headers
HTTPrequest = requests.get(OECDMembersUrl, HTTPHeaders)

#Pass the HTTP request response to BeautifulSoup
soup = BeautifulSoup(HTTPrequest.content, 'html.parser')

#Find the "table" HTML tags and store the results on the variable table
OECDMembersScrappedTable = soup.find_all("table")

#Show second table stored in the variable that is the one that contains the OECD member countries
OECDMembersScrappedTable[1]

# %%
#Create new dataframe from the HTML table scrapped from the OECD's website
DataFrameScrapedOECDMemberCountries = pd.read_html(str(OECDMembersScrappedTable))[1]

#Print first 10 results from the new dataframe
DataFrameScrapedOECDMemberCountries.head(10)

# %% [markdown]
# Data claning the OECD's members dataframe:

# %%
#Removing unnecesary columns and rows
DataFrameScrapedOECDMemberCountries =DataFrameScrapedOECDMemberCountries.iloc[1:-1,1:2]

#Setting dataframe column name
DataFrameScrapedOECDMemberCountries.columns = ["Country"]

#Change country names casing for consistency among different dataframes
DataFrameScrapedOECDMemberCountries.Country = DataFrameScrapedOECDMemberCountries.Country.str.title()

#Resetting dataframe index
DataFrameScrapedOECDMemberCountries.reset_index(drop=True, inplace=True)

#Save dataframe as a CSV file. Enable overwriting
DataFrameScrapedOECDMemberCountries.to_csv("webScraped_OECDMembers.csv", mode='w+', index = False)

#print first 10 results of the dataframe
DataFrameScrapedOECDMemberCountries.head(10)

# %% [markdown]
# Create a new dataframe that will contain relative-poverty rate and ECI ranking <b>only if the country is an OECD member</b>:

# %%
#Create a list with the names of the OECD members countries
OECDMembersList = list(DataFrameScrapedOECDMemberCountries["Country"])

#Crate a new dataframe that will contain the countries relative-poverty rate and the position in the ECI index ranking only if they are members of the OECD
DataFrameOECDMembersExlusiveECIAndRelativePoverty = DataFrameECIAndRelativePoverty[DataFrameECIAndRelativePoverty["Country"].isin(OECDMembersList)]

#Reset index after cleaning
DataFrameOECDMembersExlusiveECIAndRelativePoverty.reset_index(drop=True, inplace=True)

#Print resulting "OECD members exclusive" dataframe
DataFrameOECDMembersExlusiveECIAndRelativePoverty

# %% [markdown]
# Note that the resulting dataframe has 35 countries while there are 38 OECD countries. <br/>This is because the economic-complexity index <b>does not include data</b> for two OECD member countries: <b>Iceland and Luxembourg</b>, and because <b>Costa Rica</b> joined the OECD on the 25th of May 2021 so there are no statistics yet available for Costa Rica. 

# %%
#Setting the graph size on Matplotlib
plt.figure(figsize=(15,8))
#Show graph
seaborn.regplot(y=DataFrameOECDMembersExlusiveECIAndRelativePoverty["Relative Poverty Rate (%)"], x=DataFrameOECDMembersExlusiveECIAndRelativePoverty["ECI Rank 2018"], data=DataFrameOECDMembersExlusiveECIAndRelativePoverty)

# %% [markdown]
# ### Conclusion and confirmation of the first hypothesis
# It is also observed that a higher economic-complex economy is related to lower relative-povery rates in OECD countries.

# %% [markdown]
# -------------------------------------
# ### Third part: testing second hypothesis, ECI and recession recovery performance across the OECD member countries
# -------------------------------------

# %% [markdown]
# To calculate the number of years it took for a country to recover the GDP-per-capita pre-crisis-level <a href="https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%932008">(2007-2008 economic crisis)</a> the following functions will be used:

# %%
# The following function will take a country name as a parameter and will find out how many year it took for that country to recover the pre-crisis GDP per capita (PPP) level. If the result is 0 it means the country didn't experience a recession at all. An example of a country that didn't experience a recession was Australia.

def calculatePassedCountryYearsToRecoverFrom2008Crisis(countryToSearch):
    foundFlag = False
    for country in DataFrameScrapedIMFHistoricalGDPPerCapitaPPP["Country"] :
        
        if country == countryToSearch:
            foundFlag = True
            saveCountryIndex = DataFrameScrapedIMFHistoricalGDPPerCapitaPPP.index[DataFrameScrapedIMFHistoricalGDPPerCapitaPPP['Country'] == countryToSearch]
            DataFrameForCountrySelected = DataFrameScrapedIMFHistoricalGDPPerCapitaPPP.iloc[saveCountryIndex]
            preCrisisGDPPerCapita, yearOfHighestPreCrisisGDP = calculateHighestGDPBetween2007and2009(DataFrameForCountrySelected)
            countYear = 0
            
            for year in DataFrameForCountrySelected.iloc[:,1:]:
                if (int(year)>yearOfHighestPreCrisisGDP):
                    if (int(DataFrameForCountrySelected[year])<preCrisisGDPPerCapita):
                        countYear += 1                    
            return countYear

#Different countries GDP peaked in different years (2006,2007,2008), this function determines that year 
def calculateHighestGDPBetween2007and2009(countryDataframe):    
    highest = int(countryDataframe["2006"])
    yearOfHighestGDP = 2006
    
    if int(countryDataframe["2007"]) > highest:
        highest = int(countryDataframe["2007"])
        yearOfHighestGDP = 2007
    
    if int(countryDataframe["2008"]) > highest:
        highest = int(countryDataframe["2008"])
        yearOfHighestGDP = 2008
    
    return highest,yearOfHighestGDP

# %% [markdown]
# The previously declared functions will now be used to create a new DataFrame that will contain the number of years taken to recover the pre-crisis levels of GDP per capita (PPP) and the ECI rank by country.<br/>
# Creating the dataframe:

# %%
# The following for loop will call the function that calculates the number of years it took for a given country to recover from the crisis for all the countries included in the "DataFrameScrapedIMFHistoricalGDPPerCapitaPPP" dataframe

countriesResults = []
for country in DataFrameScrapedIMFHistoricalGDPPerCapitaPPP.iloc[:,0]:
    yearsToRecover = calculatePassedCountryYearsToRecoverFrom2008Crisis(country)    
    countryNameAndYearsToRecover = [country, yearsToRecover]
    countriesResults.append(countryNameAndYearsToRecover)

#Create a new dataframe with the results
DataFrameIMFCountriesByYearToRecoverFromTheCrisis = pd.DataFrame(countriesResults)

#Change default headers names
DataFrameIMFCountriesByYearToRecoverFromTheCrisis.rename(columns={0: 'Country', 1: 'Years to recover'}, inplace=True)

#Change column values variable types
DataFrameIMFCountriesByYearToRecoverFromTheCrisis['Years to recover'] = DataFrameIMFCountriesByYearToRecoverFromTheCrisis['Years to recover'].astype(int)
DataFrameIMFCountriesByYearToRecoverFromTheCrisis['Country'] = DataFrameIMFCountriesByYearToRecoverFromTheCrisis['Country'].astype('string')

#Create new dataframe that contains each country's years to recover and its lastest ECI ranking position
DataFrameIMFDataECIRankingAndYearsToRecover = pd.merge(DataFrameECIRankingByCountryLatestDataOnly, DataFrameIMFCountriesByYearToRecoverFromTheCrisis, on="Country")

#Reset dataframe index
DataFrameIMFDataECIRankingAndYearsToRecover.reset_index(drop=True, inplace=True)

#Show graph
seaborn.regplot(x=DataFrameIMFDataECIRankingAndYearsToRecover["ECI Rank 2018"], y=DataFrameIMFDataECIRankingAndYearsToRecover["Years to recover"], data=DataFrameIMFDataECIRankingAndYearsToRecover)

# %% [markdown]
# Interestingly, when considering all the countries in the dataset we see a <b>negative correlation</b> between a high-economic-complex (firsts positions in the ranking) economy and the number of years it took for that economy to recover to pre-crisis levels.<br/>
# Still, the focus is on OECD member countries and after adjusting for the crisis-fueled-commodities-price rally so let's find out if our hypothesis can be proved:

# %%
#Create a new dataframe with only OECD member countries
DataFrameOECDExclusiveIMFDataECIRankingAndYearsToRecover = DataFrameIMFDataECIRankingAndYearsToRecover[DataFrameIMFDataECIRankingAndYearsToRecover["Country"].isin(OECDMembersList)]

# #Reset index after cleaning
DataFrameOECDExclusiveIMFDataECIRankingAndYearsToRecover.reset_index(drop=True, inplace=True)

#Print resulting "OECD members exclusive" dataframe
DataFrameOECDExclusiveIMFDataECIRankingAndYearsToRecover

# %% [markdown]
# Once again, please be noted that there are 3 OECD members countries missing from the previous table: <b>Luxembourg, Iceland and Costa Rica</b>. The ECI index does not include Luxembourg and Iceland in its research and Costa Rica became a member of the OECD on May 2021.

# %%
#Graph the scatter plot
seaborn.regplot(x=DataFrameOECDExclusiveIMFDataECIRankingAndYearsToRecover["ECI Rank 2018"], y=DataFrameOECDExclusiveIMFDataECIRankingAndYearsToRecover["Years to recover"], data=DataFrameOECDExclusiveIMFDataECIRankingAndYearsToRecover)

# %% [markdown]
# Once again, the graph shows <b>no correlation</b> between high-economic-complexity and the years it took for the country to recover across the OECD member countries data.<br/>
# It can be noted that Australia is one extreme case in the scatter plot. It ranks the lowest in the economic-complexity index between OECD countries and still the economy didn't experience a recession. <br/> Paradoxically, during the crisis, Australia was not a rare case in this regard given that raw materials prices exploded to the upside <sup>[1] [2]</sup>, so countries with heavy reliance on commodities exports (high ECI ranking) like Australia outperformed the high economic-complex economies (low ECI ranking) which are also, in the majority of cases net-commodities importers.
# 
# [1] https://en.wikipedia.org/wiki/2000s_commodities_boom [2]https://theconversation.com/national-economy-grows-but-some-non-mining-states-in-recession-12670

# %% [markdown]
# ________________________
# #### Testing the second hypothesis by excluding OECD countries that are rich in natural resources
# 
# As stated in the hypothesis introduction, the last correlation test will be run against a more homogenous set of countries that have relatively poor availability of economic resources to find out if it is the case that a better (lower) ECI ranking leads to better recession resilience (lower amount of years to recover).

# %% [markdown]
# To achieve the test explained above, the following scatter plot <b>will only include European countries which are reasonably poor on natural resources</b>. This is the reason why Norway will not be included in the list of European countries given that it is rich in oil reserves and profited from the 2008 post-crisis oil price run.<br/>
# <u>All these data-cleaning processes and reflective considerations are done with the objective of making the comparison fairer and representative of reality</u>.<br/>
# Wikipedia provides a table that categorizes the OECD member countries by geographical region:

# %%
#Setting the HTTP headers for the upcoming request
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

#Set the target URL 
url = "https://en.wikipedia.org/wiki/OECD"

#Using the requests package to made the "get" HTTP request to the target website using the passed headers
req = requests.get(url, headers)

#Pass the HTTP request response to BeautifulSoup
soup = BeautifulSoup(req.content, 'html.parser')

#Find the "table" HTML tags and store the results on the variable table
scrappedOECDMembers = soup.find_all("table")

#Show tenth table stored in the variable
scrappedOECDMembers[10]


# %%
#save HTML table in a variable
HTMLTableOECDGeoraphic = scrappedOECDMembers[10]

# create a pandas dataframe from the HTML table
DataFrameOECDGeoraphic = pd.read_html(str(HTMLTableOECDGeoraphic))[0]

#Remove the unnecessary columns
DataFrameOECDGeoraphic = pd.concat([DataFrameOECDGeoraphic.iloc[:,0:1],DataFrameOECDGeoraphic.iloc[:,5:6]],axis=1)

#Show first 10 entries of the dataframe
DataFrameOECDGeoraphic.head(10)

# %%
#Removing non-european countries from the OECD members table 
DataFrameOECDGeoraphic = DataFrameOECDGeoraphic.loc[DataFrameOECDGeoraphic['Geographic location'] == "Europe"]

#Resetting index
DataFrameOECDGeoraphic.reset_index(drop=True, inplace=True)

#Show the dataframe
DataFrameOECDGeoraphic

# %%
#Removing Norway (natural-resource rich country)
DataFrameOECDGeoraphic = DataFrameOECDGeoraphic[DataFrameOECDGeoraphic.Country != "Norway"]

#Create list of european OECD member countries
EuropeanCountries = list(DataFrameOECDGeoraphic["Country"])

#Create dataframe for European OECD member countries
EuropeanOECDMembers = DataFrameIMFDataECIRankingAndYearsToRecover[DataFrameIMFDataECIRankingAndYearsToRecover["Country"].isin(EuropeanCountries)]

#Resetting index
EuropeanOECDMembers.reset_index(drop=True, inplace=True)

#Show the dataframe
EuropeanOECDMembers

# %%
#Setting the graph size on Matplotlib
plt.figure(figsize=(15,8))

#Graph the scatter plot
seaborn.regplot(x=EuropeanOECDMembers["ECI Rank 2018"], y=EuropeanOECDMembers["Years to recover"], data=EuropeanOECDMembers)

# %% [markdown]
# ### Confirmation of the second hypothesis
# It is observed that all things equal, a higher economic-complex economy is correlated to fewer years taken to recover from a global economic recession.

# %% [markdown]
# ----------------
# ### Plotting both hypotheses correlations in 3D 

# %%
#Change display parameter before importingmatplotlib
%matplotlib notebook
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Create new dataframe merging the two dataframes used for the hypotheses
DataframeECIandEconomicRecoveryPerformanceFor3D = pd.merge(DataFrameOECDMembersExlusiveECIAndRelativePoverty, EuropeanOECDMembers, on="Country")

#Clean duplicated column
DataframeECIandEconomicRecoveryPerformanceFor3D.drop('ECI Rank 2018_y', axis=1, inplace=True)
DataframeECIandEconomicRecoveryPerformanceFor3D.rename(columns={'ECI Rank 2018_x': 'ECI Rank 2018'}, inplace=True)

#*** Creating 3D graph. Larned how to make a 3D graph following the follwing video-tutorial: https://www.youtube.com/watch?v=6ljHxJQ47Uk&ab_channel=sentdex ***

seaborn.set(style = "darkgrid")
graphFigure = plt.figure()
graph = graphFigure.add_subplot(111, projection = '3d')

#Set axis information
x = DataframeECIandEconomicRecoveryPerformanceFor3D['ECI Rank 2018']
y = DataframeECIandEconomicRecoveryPerformanceFor3D['Relative Poverty Rate (%)']
z = DataframeECIandEconomicRecoveryPerformanceFor3D['Years to recover']

#Set graph labels
graph.set_xlabel("ECI Rank 2018 (lower is better)")
graph.set_ylabel("Relative Poverty Rate (%)")
graph.set_zlabel("Years taken to recover from 2008 crisis")

#Show graph. *** Larned how to make a 3D graph following the follwing video-tutorial: https://www.youtube.com/watch?v=6ljHxJQ47Uk&ab_channel=sentdex ****
graph.scatter(x, y, z)
plt.show()

# %% [markdown]
# ------------------
# ### Conclusion and final reflection on the research
# 
# * #### Findings of this project
# 
#   It was shown that a high economic-complexity score (lower position in the ECI Ranking) is correlated to lower levels of relative-poverty among the citizens of the country and it is also correlated (<a href="https://en.wikipedia.org/wiki/Ceteris_paribus">all other things being equal</a>) to fewer years being taken to recover from the 2008 economic crisis.
# 
# * #### How the research done provides valuable insights for the readers
#     Being cautious of the fact that correlation does not mean causation, this research shows that a highly educated private sector (companies and individuals) is associated with lower levels of relative poverty which has a direct impact on lowering income inequality. <br/>A conclusion following this study is that investment in higher education and subsequent investments in companies that output high value-added exports must be a priority on a national level to adapt to the modern high-technology era. The goal of this double investment is to bridge the gap in the long term between the high-technology exporting countries and the countries that are lagging that are currently forced to import this technology from third parties.<br/>
#     Another observation of the study is that when a given country has its exports diversified into high value-added goods, it becomes more resilient to global economic recessions since it takes fewer years for the economy to recover from them. This correlation makes sense given that recessions tend to affect some specific sectors of the economy more over the others. An example of this is the construction sector that was one of the hardest hit by the 2008 recession<sup><a href="https://www.cnbc.com/2012/06/01/Industries-Hit-Hardest-by-the-Recession.html">[1]</a></sup>. In conclusion, diversified exports are a great way for countries to be more stable during global economic downturns.
#     
# * #### How can this topic be explored further in the future?
#     Given the positive correlations found for a high economic-complexity score and, also given that one of the necessary conditions to achieve it is by having highly educated citizens, the topic can be explored further by taking into account education statistics by country. One of these questions is how does the OECD's Programme for International Student Assessment (PISA) results for each country relate to economic performance. Another related question is which factor has more of an impact when it comes to lifting the standard of living of a given country. Does a higher coverage of primary health services have more of an impact on future education performance than education expenditure per se?.<br/>
#     All of these education-related questions could be explored further in an extension of this research.


