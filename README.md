# Covid-19 End to End Data Engineering Project Based On Azure Data Factory
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

  ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/0b5cee77-3a26-40be-8586-41f7352cfa95)


# Project Steps 
  1.I manually uploaded the zipped file "population_by_age.tsv.gz" to Azure Blob Storage. Following that, I set up Azure Data Factory, where I established a Linked Service to connect to the Blob Storage and created a DataSet referencing the specific file. In addition to this, I designed a Pipeline that includes a Validation to Check the existing of file and make if condition to check that column count if matches and if it matches make Copy Activity responsible for transferring the Population Data from Blob Storage to ADLS Gen2.
  
![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/9da364d4-56b9-482f-9132-02aa8730454e)



  2.Now I have rest 3 datasets i.e cases_and_deaths, hospial_admissions, testing_data from https://github.com/cloudboxacademy/covid19/tree/main/ecdc_data Now I have to connect these files to the ADF through https: Linked Service and gave my base url name to it.and ingest all these 3 datasets into ADLS gen2 at a time, I created a json file with 3 files and created parameterized dataset and with the help of Lookup acivity and ForEach activity I was able to successfully ingest the data into the ADLS gen2 
  
![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/54be98e8-d744-4f4b-b87c-89759462a5ee)


  3.After the required data ingested into the ADLS gen2 storage, I have created the dataFlows for 2  files {cases deaths data , hospital admission } and  Using DataFlow to make transformation and the other two file i make trasnformation using pyspark by using databricks activity and using hive by using HDInsghts . then, I created the pipelines for all of those 4 datasets which redirects to the processed Container in  ADLS gen2 rephrase it 
  # Hospital Transformation 
  
  ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/790f6d20-a48c-4544-8855-bb0815adbd2c)

 
  # Cases and Deaths Transformation
  
   ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/89e88290-c385-41a6-8260-65695f2f9c0b)

   
  # Population Transformation
  
   ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/c4808175-c9e2-4a66-bad1-1b641ecf2643)


  4.Load All data to azure sql Database By using Copy activity 
  
   ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/bc50d647-b3bf-4336-a0b9-4735a9e45640)

  5.Making Pipeline executions are full automated Using Event triggers and tumbling window triggers
  
   ![1](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/e55e37b6-fbb8-42ed-84f8-f575cb2a63bf)


  6.Monitor Dashboards
  
   ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/00d0f02b-2dd3-4e6f-bac6-bc8178419d83)
   
  7.Creating DashBoards By connecting PowerBi with azure sql database
   # Page 1 
   
   ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/da2d5718-ff17-4536-9544-ee86c5387920)

   # page 2(tooltip)
   
   ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/34bceded-9812-44f5-b82b-2ac7c2ead0c4)

   
   # Page 3
   
   ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/ae25954b-ef01-4db6-a5b5-e06f1bb3ed92)

   
   # Page 4 

   ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/499cfb20-07f2-4672-8560-1718809efebb)

      
   # page 5
   
   ![image](https://github.com/Mustafamegahed20/Covid-19-Project-adf/assets/61358936/1dd7aace-cf5c-4130-8e1f-4b5747eb50e8)


  * Dashboards link :https://www.novypro.com/project/covid-19-dashboard-power-bi

    
       
     
      

    
     


  
  

  

    
  
