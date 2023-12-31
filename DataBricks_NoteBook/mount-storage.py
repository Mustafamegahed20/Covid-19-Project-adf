# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers
# MAGIC 1. raw
# MAGIC 2. processed
# MAGIC 3. lookup

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "7b1976f3-9f2b-4e01-be76-647506e43b30",
           "fs.azure.account.oauth2.client.secret": "m1x8Q~j.OAhQWScJ4aAY9M9WWUuyW7nXg2SBWamI",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/32c3449d-4d78-4a63-8360-0e35fc6ac39c/oauth2/token"}
# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://row@covids19reportdl.dfs.core.windows.net/",
  mount_point = "/mnt/covids19reportdl/row",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the processed container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://processed@covids19reportdl.dfs.core.windows.net/",
  mount_point = "/mnt/covids19reportdl/processed",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the lookup container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://lookup@covids19reportdl.dfs.core.windows.net/",
  mount_point = "/mnt/covids19reportdl/lookup",
  extra_configs = configs)
