# Covid-19 End to End Data Engineering Project Based On Europe Data 
This project focus on the Europe covid-19 data . This data taken from ECDC Website for Covid-19 Data https://www.ecdc.europa.eu/en/covid-19/data and Euro Stat Website for Population Data  https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tps00010.tsv.gz


* The main objective of this project is to use raw data to perform **ETL** (Extract, Transform and Load) using  **Azure Data Factory**.

### Types of files and data used in the project are listed below:

File Name | Description of File
-------- | ---------
1.population_by_age.tsv.gz (EuroStat/Blob) | This is a zipped file that contains the population data of countries.
2.cases_deaths.csv (ECDC) | This csv contains the number emerging Covid Cases and Deaths followed by the each day.
3.hospital_admissions.csv (ECDC) | This csv file contains the Daily Hospital Admissions, Daily ICU admissions, Weekly Hospital Admissions per 100k, Weekly ICU Admissions per 100k.
4.testing.csv (ECDC) | This csv file contains the emerging covid cases, tests being done, testing_rate and covid postive_rate on the weekly basis.
5.lookups (Blob) | Other miscellaneous  files like Calendar Lookup/dim and Country lookup/dim files used.

# Tools Used :
  * Python
  * Pyspark
  * sql
  * Azure Data Factory
  * Microsoft Azure Srorage Explorer
  * Azure Blob Storage
  * Azure Databricks
  * Azure Data Lake Storage Gen2
  * Azure sql Database
  * PowerBi

# Project Workflow
  ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/7aa4eb6c-c2a5-47e9-afc0-f7b288866c9c)


# Project Steps 
  1.I manually uploaded the zipped file "population_by_age.tsv.gz" to Azure Blob Storage. Following that, I set up Azure Data Factory, where I established a Linked Service to connect to the Blob Storage and created a DataSet referencing the specific file. In addition to this, I designed a Pipeline that includes a Validation to Check the existing of file and make if condition to check that column count if matches and if it matches make Copy Activity responsible for transferring the Population Data from Blob Storage to ADLS Gen2.
  
![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/febc2b2d-0d60-4596-ab5e-2ba99f86bd7d)


  2.Now I have rest 3 datasets i.e cases_and_deaths, hospial_admissions, testing_data from https://github.com/cloudboxacademy/covid19/tree/main/ecdc_data Now I have to connect these files to the ADF through https: Linked Service and gave my base url name to it.and ingest all these 3 datasets into ADLS gen2 at a time, I created a json file with 3 files and created parameterized dataset and with the help of Lookup acivity and ForEach activity I was able to successfully ingest the data into the ADLS gen2 
![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/c3882f01-1a80-4db4-aa1d-f44a928eab0f)

  3.After the required data ingested into the ADLS gen2 storage, I have created the dataFlows for 2  files {cases deaths data , hospital admission } and  Using DataFlow to make transformation and the other two file i make trasnformation using pyspark by using databricks activity and using hive by using HDInsghts . then, I created the pipelines for all of those 4 datasets which redirects to the processed Container in  ADLS gen2 rephrase it 
  # Hospital Transformation 
  ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/347367ef-306e-46c2-96e3-07c0d17d17f1)
  # Cases and Deaths Transformation
   ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/b1a5bc3f-8339-443f-9fdf-ff63c75eae01)
  # Population Transformation
  ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/dfef0289-1210-4099-9062-bb20fbaa66f9)

  4.Load All data to azure sql Database By using Copy activity 
    ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/52270c83-d1d2-4e51-b8bc-b6dae7db5b4b)
  
  5.Making Pipeline executions are full automated Using tumbling window triggers
![1](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/69efbcc5-1d0c-4b42-b22a-636af3fbd46c)

  6.Monitor Dashboards
     ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/a04b1049-e580-46c3-b00a-0681a2f9831f)

  7.Creating DashBoards By connecting PowerBi with azure sql database
    # Page 1 
    ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/fe53e703-8c5b-42ce-b99b-1ea47ce72650)
    # page 2(tooltip)
      ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/06c77ff3-8036-48b8-8d63-3dd9633158c5)
    # Page 3
      ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/3de46c6c-5aef-4074-a26c-74aef6b6ac59)
    # Page 4 
      ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/724c3176-0518-44af-8614-6fb2331275e6)
    # page 5
      ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/cdcd1cf0-9894-405e-a677-9214a2d8bdab)

  * Dashboards From this link :https://www.novypro.com/project/covid-19-dashboard-power-bi

    
       
     
      

    
     


  
  

  

    
  
