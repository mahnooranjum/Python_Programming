# -*- coding: utf-8 -*-
# import findspark
# findspark.init('/opt/spark/spark-3.1.2-bin-hadoop3.2')

import pyspark
import pandas as pd
import numpy as np
import time
import numpy as np
import os
import collections
import glob
from pyspark.sql import functions as sf

from pyspark.sql import SparkSession
from pyspark.sql.functions import struct, udf, col, lit, countDistinct, explode, expr, when, floor, row_number
from pyspark.sql.window import Window
from pyspark.sql.types import ArrayType, FloatType, StringType, IntegerType, DoubleType
from pyspark.sql.functions import monotonically_increasing_id 
from pyspark.sql.functions import rand

duplicate_dict = {}
only_columnname_dict = {}

from numpy.random import default_rng
rng = default_rng()

#####################################################
# Getter Code
# These are helper functions and are not to be parallelized along with the other code
##############################################################################################

spark = SparkSession.builder.appName('Basic').\
                    config("spark.driver.extraClassPath", "/usr/share/java/mysql-connector-java-8.0.30.jar").\
                    getOrCreate()

temp_df_coltypes = []

import time 
tic_mega = time.perf_counter()

def decode_ap_e(temp):
    temp = temp[1:len(temp)-1]
    temp = temp.split('][')
    list_anon = temp[0].split(',')
    list_pseudo = temp[1].split(',')
    list_anon = [x.replace("'","").strip() for x in list_anon]
    list_pseudo = [x.replace("'","").strip() for x in list_pseudo]
    list_anon_type = ','.join(list_anon[int((len(list_anon)/2)):])
    list_anon = ','.join(list_anon[:int((len(list_anon)/2))])
    ref = list_pseudo[-2].split(':')[1]
    count = int(list_pseudo[-1].replace('COUNT:', ''))
    list_pseudo = ','.join(list_pseudo[:-2])
    
    return (list_anon, list_anon_type, list_pseudo, ref, count)


import math

##############################################################################################
def get_cuts(mini, maxi, cuts):
    import decimal
    '''
        Get cuts array for numerical binning
        
        inputs:
            maximum value 
            minimum value
            number of bins
        outputs: 
            cuts array
    '''
#     helper_bincuts = np.array([])
    helper_bincuts = []
    for i in range(cuts+1):
#         helper_bincuts.append(np.round(i*((maxi-mini)/cuts) + (mini),prec) )
        divide_res = (decimal.Decimal(maxi) - decimal.Decimal(mini))/decimal.Decimal(cuts)
#         print('divide',str(divide_res))
        multiply_res = decimal.Decimal(i)* divide_res
#         print('mul',str(multiply_res))
        add_res = multiply_res+ decimal.Decimal(mini)
#         print(add_res)
        helper_bincuts.append(float(add_res))
#         helper_bincuts.append(i*(np.divide((maxi-mini),cuts)) + (mini))
#     print(helper_bincuts)
    return helper_bincuts


#############################################################################################

from numpy import random
import os

# i = 0
# df_pseudo_sampling = []


# # This function is used to get samples from a pseudo column
# # The valriable "i" is a global variable necessary for this purpose

# def get_sample_by_col(list_pseudo_e, placeholder_pseudo_e, count_pseudo_e):
#     global i
#     if i == 0:
#         f_lst = os.listdir(placeholder_pseudo_e)
#         f_lst = [x for x in f_lst if x[-4:] == '.csv']
#         global df_pseudo_sampling
#         df_pseudo_sampling = pd.read_csv(placeholder_pseudo_e + '/' + random.choice(f_lst), encoding = "ISO-8859-1")
#         df_pseudo_sampling = df_pseudo_sampling[list_pseudo_e.split(',')]
        
#     lst = list(df_pseudo_sampling.iloc[i])
#     lst = [str(x) for x in lst]
#     lst = ','.join(lst)
#     if i == len(df_pseudo_sampling)-1:
#         i = 0
#     else:
#         i += 1
#     return lst

def get_sample_by_col2(list_pseudo_e, placeholder_pseudo_e, count_pseudo_e, pseudo_df, sample):
    
    # Get Columns only in list_pseudo_e 
    df_pseudo_sampling = pseudo_df[list_pseudo_e.split(',')]

    # Get a random sample from DF
    df_pseudo_sampling = df_pseudo_sampling.sample(n=sample, replace=True)
        
    # Convert the Random DF Rows to Comma Separated String
    df_pseudo_sampling = df_pseudo_sampling.to_csv(header=None, index=False).strip('\n').split('\n')

    return df_pseudo_sampling


#for manipulating correct datatypes in sql
def sqlconnect_datatype(var_host,var_user,var_pass,var_db):


    mydb1 = mysql.connector.connect(
    host= var_host,
    user= var_user,
    password= var_pass,
    database= var_db)

    mycursor1 = mydb1.cursor()
   
    query = ("SELECT table_name FROM information_schema.tables WHERE table_schema = %s")
    mycursor1.execute(query,[var_db])

    #change the execute statemenet for different databases and tables
    # mycursor.execute("SELECT column_name, data_type, character_maximum_length from INFORMATION_SCHEMA.COLUMNS where table_schema = 'employees' and table_name = 'employees' ORDER BY ORDINAL_POSITION ")

    tables_list1 = mycursor1.fetchall()

    
    # printing info1 gives in the form of [('alj_1',), ('alj_2',), ('alj_3',)]
    #following lines changes info to a simple list like: ['alj_1', 'alj_2', 'alj_3']
    tables_list = []
    for i in range(len(tables_list1)):
        tables_list.append(tables_list1[i][0])

    
    all_datatypes = []
    for i in range(len(tables_list)):
        
        query1 = ("SELECT column_name, data_type, character_maximum_length, numeric_precision, numeric_scale from INFORMATION_SCHEMA.COLUMNS where table_schema = %s and table_name = %s ORDER BY ORDINAL_POSITION ")
        mycursor1.execute(query1,(var_db,tables_list[i]))
        # print(tables_list[i])
        datatype_onetable = mycursor1.fetchall()
        all_datatypes.append(datatype_onetable)


    data_type = [[((i[1].decode()) + "(" + str(i[2]) + ")" ) if (i[2] != None) else (((i[1].decode()) + "(" + str(i[3]) + "," + str(i[4]) + ")" )) for i in tables] for tables in all_datatypes]

    #replacing enum with char
    for i in data_type:
        for j in range(len(i)):
            if i[j] == 'enum(1)':
                i[j] = 'char(1)'
        
    column_datatypes_dict= {}

    for index,table in enumerate(all_datatypes):
        column_type = ""
        for i in range(len(table)):
        
            column_type += table[i][0] + " " + data_type[index][i]+ ", "
    
        column_type = column_type[:-2]
        column_datatypes_dict[tables_list[index]] = column_type    

    return column_datatypes_dict
#####################################################
# Helper Code
        
        
##############################################################################################
def check_for_nulls(row):    
    '''
        check if the row has any null values
        
        inputs: 
            spark row
        outputs: 
            boolean 1 if null, 0 otherwise
        
    '''
    for i in row[0]:
        if i != i:
            return True
    return False

##############################################################################################
def get_sample(df,num):
    '''
        get random row of the dataset 
        without any null values
        
        inputs: 
            spark dataframe 
        outputs: 
            sliced row
        note:
            O(n!) in worst cases when we 
            only have one row without nulls
        
    '''
    
    while(True):
        data_row = df.rdd.takeSample(False, num)
        if check_for_nulls(data_row) == False:
            return data_row


#########################################################################
#######################################
# field testing

import sys
import re
import datetime as dt
from random import choice, sample, choices
import numpy
from numpy import random

def generateUSPhNo():
    '''
    Output:
         Phone_number : Generated Phone number
    '''
    
    USCountryCode="+1"
    areaCodes=list(map(str,numpy.arange(201,990))) # Since USA area codes range from 201 - 989
    areaCode=sample(areaCodes,1)[0]
    
    Ph_no=str(random.randint(1000000,9999999,))
    Phone_number=USCountryCode + "(" + areaCode + ")" + Ph_no
    
    return Phone_number



def generateUserEmails(Namesdf):
    '''
    Input: 
         Namesdf : Dataframe containing sample First and Last Names
     
    Output:
         userEmail : Generated Email Address
    '''

    firstNames=Namesdf['FIRSTNAME'].dropna()
    lastNames=Namesdf['LASTNAME'].dropna()
    
    emailProviders=['gmail','gmail','gmail','hotmail','yahoo','yahoo','outlook','outlook','icloud','icloud','protonmail','protonmail','aol','inbox','mail','zohomail','zohomail','gmx','yandex']
    emailProviders=["@" + email + '.com' for email in emailProviders]
    userEmail= sample(emailProviders,1)
    

    FN=sample(list(firstNames),1) 
    LN=sample(list(lastNames),1)

    userName= numpy.core.defchararray.add(FN, LN)[0]
    userName=userName.replace(' ','.')
    
    UserEmail = numpy.core.defchararray.add(userName,userEmail)[0]
    
    return UserEmail

def dataset_loader():
    #print('HELLO')
    # BOTTLENECK 
    database = pd.read_csv("data.csv", low_memory=False)
    # database = pd.read_csv("s3://eks-ascend/input/data.csv", low_memory=False)
    # database = pd.read_csv("/dbfs/mnt/s3system/input/data.csv", low_memory=False)
    final = {}
    for i in database.columns:
        final[i] = database[i].dropna().reset_index(drop = True)
    del(database)
    # BOTTLENECK 
    # USdata=pd.read_csv('database/uscities.csv',usecols=['city','state_id','state_name'])
    return final


database =  dataset_loader()

ph = re.compile("[0-9]{3}[^0-9][0-9]{3}[^0-9][0-9]{4}")
zp = re.compile("^\d{5}(?:[-\s]\d{4})?$")
em = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
fmts = ('%Y',
        '%b %d, %Y',
        '%b %d, %Y',
        '%B %d, %Y',
        '%B %d %Y',
        '%m/%d/%Y',
        '%m/%d/%y',
        '%B-%d-%Y',
        '%m-%d-%y',
        '%d-%m-%Y',
        '%d/%m/%Y',
        '%Y-%m-%d',
        '%Y/%m/%d',
        '%b %Y',
        '%Y %M',
        '%b-%Y',
        '%Y-%M',
        '%B%Y',
        '%b %d,%Y',
        'yyyy MMMM')


def isPhone(num):
    try:
        if len(ph.match(num).string) > 0:
            return True
    except:
        return False


def isEmail(num):
    try:
        if len(em.match(num).string) > 0:
            return True
    except:
        return False


def whatIs(data):
    threshold = 50

    # c_phone = 0
    c_email = 0
    

    for i in data:

        # if isPhone(i):
        #     c_phone = c_phone + 1
        #     ctemp = 100 * (c_phone / len(data))
        #     if ctemp > threshold:
        #         return 'PHONE';

        if isEmail(i):
            c_email = c_email + 1
            etemp = 100 * (c_email / len(data))
            if etemp > threshold:
                return 'EMAIL';

    for i in database.keys():
        df = set(database[i])
        commons = df.intersection(data)
        percent = 100 * len(commons) / len(data.unique())

        if i == "COUNTRYCODE" and percent > 10:
            return i
        elif i == "STATECODE" and percent > 50:
            return i;
        elif i == "GENDER" and percent > 50:
            return i;
        elif i == "GENDERCODE" and percent > 50:
            return i;
        elif i == "COUNTRY" and percent > 10:
            return i;
        elif i == "STATE" and percent > 50:
            return i;
        elif i == "CITY" and percent > 50:
            return i
        elif i == "FIRSTNAME" and percent > 50:
            return i
        elif i == "LASTNAME" and percent > 50:
            return i

    return "OTHERS"



def add_email(df):

    df_fake = spark.read.format("csv").option("header","true").load('data.csv')

    L_names_in_actual_dataset = False
    F_names_in_actual_dataset = False

    for col in df.columns:
        if (col == "LASTNAME"):
            L_names_in_actual_dataset = True
        if ( col == "FIRSTNAME"):
            F_names_in_actual_dataset = True

    ###########
    if not (L_names_in_actual_dataset and F_names_in_actual_dataset):
        # F_count = df_fake.count()
        R_count = df.count()
        df_fake_F = df_fake.select(sf.col("FIRSTNAME"))
        df_fake_L = df_fake.select(sf.col("LASTNAME"))

        print("[PARTITIONS][df_fake_F] " + str(df_fake_F.rdd.getNumPartitions()))
        print("[PARTITIONS][df_fake_L] " + str(df_fake_L.rdd.getNumPartitions()))

        if not(F_names_in_actual_dataset):
            df_fake_F = df_fake_F.dropna()
            F_count = df_fake_F.count() 
            df_fake_F = df_fake_F.sample(True,((R_count)/F_count) +0.01, 101)
            print("[PARTITIONS][df_fake_F]sample " + str(df_fake_F.rdd.getNumPartitions())) 
            # df_fake_F = df_fake_F.limit(R_count)
            print("[PARTITIONS][df_fake_F]limit " + str(df_fake_F.rdd.getNumPartitions()))   
            df_fake_F = df_fake_F.withColumn('rand', rand(seed=35)).orderBy('rand')
            print("[PARTITIONS][df_fake_F]orderby " + str(df_fake_F.rdd.getNumPartitions()))   
            df_fake_F = df_fake_F.drop("rand")
            print("[COUNT][df_fake_F]sample " + str(df_fake_F.count()))
            print("[PARTITIONS][df_fake_F]drop " + str(df_fake_F.rdd.getNumPartitions()))   

            print("[PARTITIONS][df_fake_F]2 " + str(df_fake_F.rdd.getNumPartitions()))

        if not(L_names_in_actual_dataset):
            df_fake_L = df_fake_L.dropna()
            F_count = df_fake_L.count()
            df_fake_L = df_fake_L.sample(True,((R_count)/F_count)+0.01, 101)        
            # df_fake_L = df_fake_L.limit(R_count)
            df_fake_L = df_fake_L.withColumn('rand', rand(seed=50)).orderBy('rand')
            df_fake_L = df_fake_L.drop("rand")       
            print("[COUNT][df_fake_F]sample " + str(df_fake_F.count()))

            print("[PARTITIONS][df_fake_L]2 " + str(df_fake_L.rdd.getNumPartitions()))
        
        if (not(L_names_in_actual_dataset) and not(F_names_in_actual_dataset)):
            df_fake_F = df_fake_F.repartition(df.rdd.getNumPartitions())
            df_fake_L = df_fake_L.repartition(df.rdd.getNumPartitions())
            col_1_with_row_num = df_fake_F.withColumn("row_num", monotonically_increasing_id())
            col_2_with_row_num = df_fake_L.withColumn("row_num", monotonically_increasing_id())

            print("[PARTITIONS][col_1_with_row_num]2 " + str(col_1_with_row_num.rdd.getNumPartitions()))
            print("[PARTITIONS][col_2_with_row_num]2 " + str(col_2_with_row_num.rdd.getNumPartitions()))
            '''
            window = Window().orderBy(lit('A'))
            col_1_with_row_num = df_fake_F.withColumn("row_num", row_number().over(window))
            col_2_with_row_num = df_fake_L.withColumn("row_num", row_number().over(window))
            '''

            df_fake = col_1_with_row_num.join(col_2_with_row_num, on=['row_num']).select('FIRSTNAME', 'LASTNAME')
        elif (not(L_names_in_actual_dataset)):
            df_fake = df_fake_L
        elif (not(F_names_in_actual_dataset)):
            df_fake = df_fake_F
        else:
            pass

        '''
        window = Window().orderBy(lit('A'))
            
        col_1_with_row_num = df_fake.withColumn("row_num", row_number().over(window))
        col_2_with_row_num = df.withColumn("row_num", row_number().over(window))
        '''

        
        df_fake = df_fake.repartition(df.rdd.getNumPartitions())
        df_fake = df_fake.withColumn("row_num", monotonically_increasing_id())
        df = df.withColumn("row_num", monotonically_increasing_id())
        print("[PARTITIONS][df_fake] " + str(df_fake.rdd.getNumPartitions()))
        df = df.join(df_fake, on=['row_num']).select('*')
        df = df.drop("row_num")

    df = df.withColumn('isVal', floor(rand()*100000))
    df = df.withColumn('dot', lit('.'))
    df = df.withColumn('tail', lit('@gmail.com'))
    df = df.withColumn("Email", sf.concat(sf.col('LASTNAME'),sf.col('dot'),sf.col('FIRSTNAME'),sf.col('isVal'),sf.col('tail')))

    print("[PARTITIONS][df]" + str(df.rdd.getNumPartitions()))

    df = df.drop("isVal")
    df = df.drop("dot")
    df = df.drop("tail")
    if not (L_names_in_actual_dataset):
        df = df.drop("LASTNAME")
    if not (F_names_in_actual_dataset):
        df =df.drop("FIRSTNAME")

    return df

###############################################################################

def get_anon_sample(key_lst, factor=None):
    fnl = []
    key_lst = key_lst.split(',')
    for i in key_lst:
        if i == 'PHONE':
            fnl.append(generateUSPhNo())
        elif i == 'EMAIL':
            fnl.append(generateUserEmails(database))
        else:
            fnl.append(choice(database[i]))
    return ",".join(fnl)

def get_anon_sample2(key_lst, factor=None):
    fnl = []
    #key_lst = key_lst.split(',')
    i = key_lst
    if i == 'PHONE':
        fnl.append(generateUSPhNo())
    elif i == 'EMAIL':
        fnl.append(generateUserEmails(database))
    else:
        fnl = choices(database[i],k=factor)
    return fnl

#######################################

tostats_fnameg = ""

# Function To Generate Data if Signature Provided
def do_gen_prq_signature(params):
    adder                       \
    ,boolit                      \
    ,placeholder_filename_output \
    ,sig_ap_e                    \
    ,l_anon                      \
    ,l_pseudo                    \
    ,header                      \
    ,trav_counts                 \
    ,traverser                   \
    ,exporter                    \
    ,column_names                \
    ,info_precision_e            \
    ,list_pseudo_e               \
    ,placeholder_pseudo_e        \
    ,type_anon_e                 \
    ,counts                      \
    ,scale_factor                \
    ,placeholder_local_sig       \
    ,list_anon_e                 \
    ,input_t                     \
    ,out_params                  = params

    params_broadcast = spark.sparkContext.broadcast(params)



    # The do_gen function is the function that needs to be spread over 
    # different nodes for distributed processing


    # Spark UDF -- IMPORTANT: Using Broadcast Variable
    def do_gen2(line_sig):
        
        #Extract Broadcast Params
        params = params_broadcast.value
        adder                       \
        ,boolit                      \
        ,placeholder_filename_output \
        ,sig_ap_e                    \
        ,l_anon                      \
        ,l_pseudo                    \
        ,header                      \
        ,trav_counts                 \
        ,traverser                   \
        ,exporter                    \
        ,column_names                \
        ,info_precision_e            \
        ,list_pseudo_e               \
        ,placeholder_pseudo_e        \
        ,type_anon_e                 \
        ,counts                      \
        ,scale_factor                \
        ,placeholder_local_sig       \
        ,list_anon_e                 \
        ,input_t                     \
        ,out_params                  = params


        # Return List to Replace Print Statments
        value_input = []
        pseudo_lst = []

        ### Removed 
        #with open(placeholder_filename_output[:-4] + str(file_dunder) + '.csv', 'w') as optr:
            #print(header, file=optr)

        if trav_counts == 1:
            ### Removed 
            # tmp = pa.Table.from_batches([ipa]).drop_null().to_pydict()
            # tmp = [x for y,x in tmp.items() ]
            # tmp = list(zip(*tmp))

            ### Removed
            #for line_sig in tmp:  
            
            group = line_sig[:-1]
            temp = line_sig[-1]*scale_factor

            tuple_temp = math.modf(temp)
            temp = tuple_temp[1]
            adder = adder + tuple_temp[0]
            
            if adder >= 1.0:
                temp = temp + 1.0
                adder = adder - 1.0

            temp = int(temp)
            if temp != 0:
            #         continue
            # else:
                
                for k in range(traverser):
                    #saver_line = ""
                    if (column_names[k] in exporter) and (len(exporter[column_names[k]]) > 0):
                        value_input.append(rng.uniform(float(exporter[column_names[k]][str(group[k])][0]),
                                                            float(exporter[column_names[k]][str(group[k])][1]),size=(1,temp)).round( int(info_precision_e[column_names[k]]))[0])
                        
                    else:
                        value_input.append(np.full((1, temp), group[k])[0])


        #List to Array: For Transpose
        value_input = np.array(value_input) 
        value_input = value_input.T.tolist()

        #Convert Array to String
        for i in range(temp):
            value_input[i] = ','.join(map(str, value_input[i]))
               

        return value_input

    
    # Initialzie Spark UDF: dogen_udf
    dogen_udf = udf(do_gen2, ArrayType(StringType()))        

    # Read the Parquet Input files in Spark
    spark_df = spark.read.option("header","true").option("recursiveFileLookup","true").parquet(placeholder_local_sig)
    print("Partitions Before :" + str(spark_df.rdd.getNumPartitions()))
    #spark_df = spark_df.repartition(6)
    print("Partitions After :" + str(spark_df.rdd.getNumPartitions()))

    # Cap Counts
    max_count = 100
    cap_count_to_list = udf(lambda integer: ([max_count] * int (int(integer)/max_count)) + [int(integer) % max_count] if (int(integer) % max_count) > 0 else ([max_count] * int (int(integer)/max_count))
                            , ArrayType(IntegerType()))
        
    spark_df = spark_df.withColumn('counts_list', cap_count_to_list('count'))
    spark_df = spark_df.drop('count')       

    # Explode Cap Counts: Convert List to Rows
    spark_df = spark_df.withColumn('count', explode('counts_list'))
    spark_df = spark_df.drop('counts_list') 

    # spark_df.show(n=10)

    test_count = spark_df.where(spark_df['count'] > 100).count()
    print("[TEST] The number of rows with counts > 100: " + str(test_count))

    # Run UDF on the Input DF
    spark_df = spark_df.select(dogen_udf(struct([spark_df[col] for col in spark_df.columns])
                    ).alias('result'))

    # Write Results to CSV using Pandas
    #spark_df.select(explode('result')).toPandas().to_csv(placeholder_filename_output,header=[header], index=False)

    # Explode: Convert List to Rows
    spark_df = spark_df.select(explode('result').alias('result'))

    # Split Strings to Columns
    split_col = pyspark.sql.functions.split(spark_df['result'], ',')
    
    i=0
    for h in header.split(","):
        spark_df = spark_df.withColumn(h, split_col.getItem(i))
        i+=1
    
    # Drop String Column
    spark_df = spark_df.drop('result')
    

    print(spark_df.columns)
    
    ########################
    # Changes @Abdullah for Pseudo and Linked
    ########################

    merged_spark_df = None
    temp_spark_df = None
    
    if sig_ap_e != None:
        if list_pseudo_e != '':
            counts = int(counts)
            pseudo_spark_df = spark.read.option("header","true").option("recursiveFileLookup","true").csv(placeholder_pseudo_e)
            pseudo_cols = list_pseudo_e.split(',')
            pseudo_spark_df = pseudo_spark_df[pseudo_cols]
            
            print("Got Pseudo Cols: " + str(pseudo_cols))
            
            pseudo_spark_df_count = pseudo_spark_df.count()
            pseudo_scaling_factor = (counts/pseudo_spark_df_count) + 0.01 
            print("Pseudo Rows    :" + str(pseudo_spark_df_count))
            print("Output Rows    :" + str(counts))
            print("Scaling Factor :" + str(pseudo_scaling_factor))
            
            pseudo_spark_df = pseudo_spark_df.sample(True, pseudo_scaling_factor)
            # pseudo_spark_df = pseudo_spark_df.limit(counts)
            
            merged_spark_df = pseudo_spark_df.select("*").withColumn("id", monotonically_increasing_id())
            
        if len(type_anon_e) > 0:
            counts = int(counts)
            anon_spark_df = spark.read.format("csv").option("header","true").load('data.csv')
            
            anon_list = list_anon_e.split(",")
            anon_cols = type_anon_e.split(',')

            email_var = False
            if 'EMAIL' in anon_cols:
                print("[Email Integration] : Email has been detected")
                anon_cols.remove('EMAIL')
                email_var = True

            anon_spark_df = anon_spark_df[anon_cols]   
            
            for col in range(len(anon_cols)):
                
                # Get Col with no nulls
                temp_spark_df = anon_spark_df.select(anon_cols[col])
                temp_spark_df = temp_spark_df.na.drop()

                # Get Anon Scaling Factor
                temp_spark_df_count = temp_spark_df.count()
                temp_scaling_factor = (counts/temp_spark_df_count) + 0.01
                print("temp Rows    :" + str(temp_spark_df_count))
                print("Output Rows    :" + str(counts))
                print("Scaling Factor :" + str(temp_scaling_factor))

                # Scaling Pseudo DF
                temp_spark_df = temp_spark_df.sample(True, temp_scaling_factor)
                # temp_spark_df = temp_spark_df.limit(counts)
                # print("counts made    : " + str(temp_spark_df.count()))
                temp_spark_df = temp_spark_df.withColumn('rand', rand()).orderBy('rand')

                
                
                if (merged_spark_df != None):
                    # Add Index
                    temp_spark_df = temp_spark_df.repartition(merged_spark_df.rdd.getNumPartitions())
                    temp_spark_df = temp_spark_df.select("*").withColumn("id", monotonically_increasing_id())
                    temp_spark_df = temp_spark_df.withColumnRenamed(anon_cols[col], anon_list[col])
                    merged_spark_df = merged_spark_df.join(temp_spark_df,['id'])
                    merged_spark_df = merged_spark_df.drop('rand')
                    
                else:
                    
                    merged_spark_df = temp_spark_df
                    merged_spark_df = merged_spark_df.drop('rand')

            if email_var:
                print("[SAAD] Calling Function")
                merged_spark_df = add_email(merged_spark_df)

    
    
    if merged_spark_df != None:
        # print("Merged length: " + str(merged_spark_df.count()))
        merged_spark_df = merged_spark_df.drop('id')
        merged_spark_df = merged_spark_df.repartition(spark_df.rdd.getNumPartitions())
        merged_spark_df = merged_spark_df.select("*").withColumn("id", monotonically_increasing_id())
        spark_df = spark_df.select("*").withColumn("id", monotonically_increasing_id())
        # print("SparkDF length: " + str(spark_df.count()))
        spark_df = merged_spark_df.join(spark_df,['id'])
        
    
    spark_df = spark_df.drop('id')
    # print("SparkDF after drop length: " + str(spark_df.count()))

    #####################
    # End of Changes
    #####################

    # Write Results to CSV using Spark
    # outputfile = os.path.dirname(os.path.abspath(__file__)) + '/' + placeholder_filename_output.replace('.csv','')

    if input_t == "csv":    
        spark_df.write.mode("overwrite").option("header", "true")\
                .csv(placeholder_filename_output)  
                # .option("compression", "snappy")\
                # .parquet(outputfile)  

    elif input_t == "mysql":

        global temp_df_coltypes

        print(temp_df_coltypes)

        from pyspark.sql.functions import col
        for i in temp_df_coltypes:
            spark_df = spark_df.withColumn(i[0],col(i[0]).cast(i[1]))

        print("[SUB] post processed ")
        print(list(spark_df.dtypes))        

#        out_params = out_params.split(",")
#        spark_df.write.format("jdbc").\
#                option("url", out_params[0]).\
#                option("driver", "com.mysql.jdbc.Driver").\
#                option("dbtable", out_params[1]).\
#                option("user", out_params[2]).\
#                option("password", out_params[3]).save()

    global tostats_fnameg

    if boolit:
        if input_t == "csv":
            fsizepath = placeholder_filename_output
            tostats_fnameg = fsizepath
            fsize = 0
            if os.path.isfile(fsizepath):
                fsize = os.path.getsize(fsizepath)
            elif os.path.isdir(fsizepath):
                fsize = sum(d.stat().st_size for d in os.scandir(fsizepath) if d.is_file())
            else:
                print("[SUB] [1] Invalid Path for Get Size")
    
            print(fsize)
    
            if fsize > 5000000000:
                gensample_fraction = 5000000000 / fsize  

                tic =time.time()
                spark_df.sample(fraction=gensample_fraction).write.mode("overwrite").option("header", "true")\
                        .csv(placeholder_filename_output + ".sample")  
                print("[SUB] [1] time taken to sample spark df is " + str(time.time() - tic) + " seconds")
                print("[SUB] [1] file size is  " + str(fsize / 1000000 ) + " Mbytes")
                tostats_fnameg = placeholder_filename_output + ".sample"
            else:
                print("[SUB] [1] file size is  " + str(fsize / 1000000 ) + " Mbytes")
                
    return spark_df

#######################################

#######################################
# SIGNATURE FUNCTIONS
    
def get_stratum(df, n_rows):
    '''
        get random stratum of the dataframe
        
        inputs: 
            spark dataframe 
            (integer) number of rows 
        outputs: 
            sliced dataframe
        
    '''
    n_total = df.count()
    if n_total<= n_rows:
        return df
    else:
        n_percentage = n_rows/n_total
        if (n_percentage > 0 and n_percentage <= 1):
            return df.sample(fraction = n_percentage, withReplacement = True)
        else:
            return {'message': 'invalid input percentage'}
        

def get_fields(slice_fields)->dict:
    '''
        get fields for anonymization 
        
        inputs: 
            pandas slice 
        outputs: 
             dictionary of detected natives 
    '''
    cols = [i for i in slice_fields.columns]
    natives = {}
    for i in cols:
        natives[i] = whatIs(slice_fields[i])
    return natives


def get_categoricals(col_array, type_array):
    '''
        get the statistical nature of columns based on the data types
        
        inputs: 
            col_array containing columns  
            type array containing data types in tuples 
        outputs: 
            info_categoricals dictionary
            

    '''
    info_categoricals = {}
    type_array = dict(type_array)
    # for testing, make them all numerical
    for i in range(len(col_array)):
        if type_array[col_array[i]] == 'string':
            info_categoricals[col_array[i]] = 1
        else:
            info_categoricals[col_array[i]] = 0
            
    return info_categoricals


def get_precision(df,info_categoricals):
    '''
        get the number of digits to the right of the decimal
        
        inputs: 
            df 
            info_categoricals 
        outputs: 
            info_precision dictionary
            
        note: 
            must have numerical data in the columns with 
            info_categoricals[col] == 0 
    '''
    data_num = [key for key,value in info_categoricals.items() if value == 0]
    data_row = get_sample(df,5)
    info_precision = {}
    max_prec = 0
    for i in data_num:
        for j in data_row:
            if len(str(j[i]).split('.')) == 1:
                max_prec = 0
            else:
                if len(str(j[i]).split('.')[1]) > max_prec:
                    max_prec = len(str(j[i]).split('.')[1])
        info_precision[i] = max_prec
    return info_precision


def get_minmax(df, info_categoricals):
    '''
        Get minimum and maximum values of the dataframe
        
        inputs: 
            spark dataframe 
        outputs: 
            min max summary of the dataframe
    '''
    # df.summary('min', 'max').select('summary').take(1)[0][0]
    
    data_num = [key for key,value in info_categoricals.items() if value == 0]
    df_numerical = df.select(data_num)
    return df_numerical.summary('min', 'max').toPandas().set_index('summary')


def get_bincount(df, num_cats,op):
    from pyspark.sql import functions as f
    '''
        get bin cut numbers 
        
        inputs: 
            df
        outputs: 
            number of bins
            skewness of dataset
            no_of_rows
    '''
    n_rows = df.count()
    count  = math.ceil(1 + 3.3*math.log10(n_rows))
#     print(count)
    bcounts = {}
    skew_dict = {}
    data_num = [key for key,value in num_cats.items() if value == 0]
    for i in data_num:
        if (op):
            temp = math.sqrt((6*(n_rows-6))/((n_rows+1)*(n_rows+3)))
            skew = df.agg(f.skewness(i)).collect()[0][0]
            if pd.isna(skew):
                skew = 0
            print("[SKEW] Gor skew value: " + str(skew))
            skew_dict[i] = skew
            skew_fact = 3.3*math.log10(1 + abs(skew)/temp)
#             print(skew_fact)
            count1 = math.ceil(count + skew_fact)
            bcounts[i] = str(count1)
        else:
            bcounts[i] = str(count)
#     print("bcounts: ",bcounts)
    return bcounts,skew_dict,n_rows


def AdaptiveBinning(data,bins,len_data):
    '''
    Input:
        data: Col data to be binned
        bins: Total No. of bins
        len_data: length of column
    Output:
        final_adaptive_bins: Adaptive Bin cuts for the given col 
    '''

    
    HDR_k=round(0.55*bins)
    MDR_k=round(0.25*bins)
    LDR_k=round(0.2*bins)
    
    if (MDR_k%2):
        MDR_k=MDR_k+1
    if (LDR_k%2):
        LDR_k=LDR_k+1

    bins=HDR_k+MDR_k+LDR_k
    print(data.dtypes)
    hist_data = data.select(data.columns[0]).rdd.flatMap(lambda x: x).map(float).histogram(bins)
    normalized_freq=np.array(hist_data[1])/len_data
#     normalized_freq=(np.histogram(data,bins=bins)[0])/len_data

    #Finding Regions
    tempHDR=np.where(normalized_freq> 0.55*max(normalized_freq))
    tempMDR=np.where((normalized_freq < 0.55*max(normalized_freq))  & (normalized_freq> 0.15*max(normalized_freq)))
    tempLDR=np.where(normalized_freq < 0.15*max(normalized_freq))
    mybins=np.array(hist_data[0])
#     mybins=(np.histogram(data,bins=bins))[1]
    tempRegions=[tempHDR[0],tempMDR[0],tempLDR[0]]

    if(len(tempLDR[0])==0):
        if(len(tempMDR[0])==0):
            MDR_k=MDR_k+LDR_k
            HDR_k=HDR_k+MDR_k
            TotalRegionBins=[HDR_k,0,0]
        else:
            MDR_k=MDR_k+np.round(0.4*LDR_k)
            HDR_k=HDR_k+np.round(0.6*LDR_k)
            TotalRegionBins=[HDR_k,MDR_k,0]
    else:
        if(len(tempMDR[0])==0):
            LDR_k=LDR_k+np.round(0.35*MDR_k)
            HDR_k=HDR_k+np.round(0.65*MDR_k)
            TotalRegionBins=[HDR_k,0,LDR_k]
        else:
            TotalRegionBins=[HDR_k,MDR_k,LDR_k]
        
    local_no_regions=[]
    Discon_idx=[]
    LocalRegionCuts=[]
    RegionBins=[]
    for idx,reg in enumerate(tempRegions):
        if(len(reg))>0:
            no_regions=len(np.where(np.diff(reg)>1)[0])+1
            local_no_regions.append(no_regions)
            discon_idx=np.where(np.diff(reg)>1)[0]+1
            Discon_idx.append(discon_idx)

            #Finding equal width bins of each region HDR,MDR,LDR
            TempBins=[]
            for i in np.split(reg,discon_idx): #For each discontinuity, append the right edge
                tempBins=mybins[i]
                tempBins=np.append(tempBins,mybins[(i+1)[-1]]) # APPENDING THE RIGHT EDGE
                TempBins=np.append(TempBins,tempBins) #Concatenate all bins of a region

            localregionscuts=[]
            min_cut=min(TempBins)
            for i in range(no_regions):
                if(i<no_regions-1):
                    max_cut=TempBins[discon_idx[i]] # THE CUT BEFORE DISCONTINUITY
                    localregionscuts.append([min_cut,max_cut])
                    min_cut=TempBins[discon_idx[i]+1] # Cut at the discontinuity
                else:
                    max_cut=max(TempBins)
                    localregionscuts.append([min_cut,max_cut])
            LocalRegionCuts.append(localregionscuts)
    #         print(LocalRegionCuts)

            #Allocaitng bins to local regions

            regionsWidth=[region[1]-region[0] for region in localregionscuts]
            totalRegionWidth=sum(regionsWidth)
            totalRegionBins=TotalRegionBins[idx]


            regionBins=[]
            for i in range(no_regions):
                local_no_bins=(int(np.ceil( (totalRegionBins * regionsWidth[i]) / totalRegionWidth)))
                regionBins.append(np.linspace(start=localregionscuts[i][0],stop=localregionscuts[i][1],num=local_no_bins+1))
        else:
            regionBins=[]
        RegionBins.append((regionBins))

    
    FinalHDRBins=np.concatenate([RegionBins[0][i] for i in range(len(RegionBins[0]))]) if((len(RegionBins[0]))>0) else []
    FinalMDRBins=np.concatenate([RegionBins[1][i] for i in range(len(RegionBins[1]))]) if((len(RegionBins[1]))>0) else []
    FinalLDRBins=np.concatenate([RegionBins[2][i] for i in range(len(RegionBins[2]))]) if((len(RegionBins[2]))>0) else []
    final_adap_bins=np.sort(list(set(np.concatenate([FinalHDRBins,FinalMDRBins,FinalLDRBins]))))
        
    return list(final_adap_bins)


# spark = SparkSession.builder.appName('Basic').getOrCreate()

spark = SparkSession.builder.appName('Basic').config("spark.driver.extraClassPath", "/usr/share/java/mysql-connector-java-8.0.30.jar").getOrCreate()

# spark = SparkSession.builder \
#     .appName("Basic") \
#     .master("local[6]") \
#     .getOrCreate()

# The generate function initializes and calculates the exact variables to be 
# passed to each process


def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())


def get_stats(filename_r, filename_g, bins_count):
    mastertic = time.time()
    
    # path = '/'.join(filename_g.split("/")[:-1])
    
    path = filename_g

    if '.sample' not in path:
        path = path + '.sample'
    
    if not os.path.exists(path):
        os.mkdir(path)


    '''
    df = dd.read_csv('s3://bucket/myfiles.*.csv')  
    
    df = dd.read_csv('hdfs:///myfiles.*.csv')  
    
    '''
    tic = time.time()
    df_r = spark.read.csv(filename_r, header=True, inferSchema=True)
    df_r = df_r.repartition(200)
    print("[SUB] Time to read reference file: " + str(time.time() - tic))

    tic = time.time()
    cols = {}
    cols_s = {}
    for i in df_r.dtypes:
        if 'string' not in i[1]: 
            cols[i[0]] = i[1]
        else:
            cols_s[i[0]] = i[1]

    cols = list(cols.keys())
    cols_s = list(cols_s.keys())
    print("[SUB] Time to segregate cols and cols_s: " + str(time.time() - tic))

    tic = time.time()
    result_r = df_r.describe(*cols) 
    print("[SUB] Time to get ref stats: " + str(time.time() - tic))
    # if not os.path.exists(path + '/stats_r'):
    #     os.mkdir(path + '/stats_r')    
    tic = time.time()
    result_r.write.format("csv").option('header', 'true').save(path + '/stats_r')  
    print("[SUB] Time to write ref stats: " + str(time.time() - tic))
    
    tic = time.time()
    df_g = spark.read.csv(filename_g,  header=True, inferSchema=True)
    df_g = df_g.repartition(200)
    print("[SUB] Time to read generated file: " + str(time.time() - tic))

    tic = time.time()
    result_g = df_g.describe(*cols) 
    print("[SUB] Time to get gen stats: " + str(time.time() - tic))

    tic = time.time()
    result_g.write.format("csv").option('header', 'true').save(path + '/stats_g')  
    print("[SUB] Time to write gen stats: " + str(time.time() - tic))
 
    print( "[SUB] All stats done in " + str(time.time()-mastertic) + " seconds")    

    tic = time.time()
    # print(toc-tic)
    saver_r = {}
    saver_g = {}
    mserr = {}
    # print(cols)



    tic = time.time()
    for i in cols:
        _, temp = df_r.select(i).rdd.flatMap(lambda x: x).histogram(bins_count) 
        divider = sum(temp) 
        saver_r[i] = [x/divider for x in temp]
        _, temp = df_g.select(col(i).cast(DoubleType())).rdd.flatMap(lambda x: x).histogram(bins_count)
        divider = sum(temp) 
        saver_g[i] = [x/divider for x in temp]
        mserr[i] = rmse(np.array(saver_r[i]), np.array(saver_g[i]))


   
    
    print("[SUB] Time to get numerical distributions: " + str(len(cols)) + " cols: " + str(time.time() - tic))    

    # tic = time.time()
    # for i in cols_s:
    #     temp = list(df_r.select(i).rdd.countByValue().values())
    #     divider = sum(temp) 
    #     saver_r[i] = [x/divider for x in temp]
    #     temp = list(df_g.select(i).rdd.countByValue().values())
    #     divider = sum(temp) 
    #     saver_g[i] = [x/divider for x in temp]
    #     mserr[i] = rmse(np.array(saver_r[i]), np.array(saver_g[i]))

    # print("[SUB] Time to get string distributions of " + str(len(cols_s)) + " cols: " + str(time.time() - tic))        




    if not os.path.exists(path + '/bincuts/'):
        os.mkdir(path + '/bincuts/')
    
    
    import csv

    tic = time.time()
    with open(path + '/bincuts/rmse.csv', 'w') as f:
        for key in mserr.keys():
            f.write("%s, %s\n" % (key, str(mserr[key])))
    print("[SUB] Time to write RMSE bins: " + str(time.time() - tic))

    tic = time.time()
    with open(path + '/bincuts/ref.csv', 'w') as f:
        for key in saver_r.keys():
            f.write("%s, %s\n" % (key, ",".join([str(x) for x in saver_r[key]])))
    print("[SUB] Time to write ref bins: " + str(time.time() - tic))
    
    tic = time.time()
    with open(path + '/bincuts/gen.csv', 'w') as f:
        for key in saver_g.keys():
            f.write("%s, %s\n" % (key, ",".join([str(x) for x in saver_g[key]])))
    print("[SUB] Time to write ref bins: " + str(time.time() - tic))
    # pd.DataFrame(saver_r).to_csv(path + '/bincuts/ref.csv', index=None)  
    # pd.DataFrame(saver_g).to_csv(path + '/bincuts/gen.csv', index=None)
    
    print("[SUB] Time to get stats + bins : " + str(time.time() - mastertic))
    return {"message" : "done" }
 

tostats_fnamer = ""

def get_signature(boolit, input_file_path, placeholder_local, sparkconf_location, placeholder_pseudo, binFunc, input_t, df):

    global tostats_fnamer

    if input_file_path != None:
        fsizepath = input_file_path
        tostats_fnamer = fsizepath
        fsize = 0
        if os.path.isfile(fsizepath):
            fsize = os.path.getsize(fsizepath)
        elif os.path.isdir(fsizepath):
            fsize = sum(d.stat().st_size for d in os.scandir(fsizepath) if d.is_file())
        else:
            print("[SUB] [5] Invalid Path for Ref Get Size")


        print("[SUB] [5] The ref file path is : " + tostats_fnamer)

        
        if tostats_fnamer != None:
            print("[SUB] The value is not null")
            
        print("[SUB] Printing for confirmation")


    sig_tic = time.time()

    # if os.path.isdir(input_file_path):
    #     files = os.listdir(input_file_path)
    #     for file in files:
    #         file = input_file_path + "/" + file
    #         print(file)
    #         with open(file, 'r', errors='ignore') as f:
    #             temp = f.readline()
            
    #         temp = temp[:-1]
    #         temp = temp.split(",")
            
    #         ic = "[ ,;{}()\n\t=]+*"
    #         illegal_chars = []
    #         for i in range(len(ic)):
    #             illegal_chars.append(ic[i]) 
            
    #         for i in range(len(temp)):
    #             for j in illegal_chars:
    #                 if j in temp[i]:
    #                     temp[i] = temp[i].replace(j, "_")
                        
    #         temp = ",".join(temp)
            
    #         print(temp)
            
    #         col_change = os.popen("sed -i \"1s/.*/" + temp + "/\" " + file)
    #         col_change.read()
            
        
    # elif os.path.isfile(input_file_path):
    #     with open(input_file_path, 'r', errors='ignore') as f:
    #         temp = f.readline()
        
    #     temp = temp[:-1]
    #     temp = temp.split(",")
        
    #     ic = "[ ,;{}()\n\t=]+*"
    #     illegal_chars = []
    #     for i in range(len(ic)):
    #         illegal_chars.append(ic[i]) 
        
    #     for i in range(len(temp)):
    #         for j in illegal_chars:
    #             if j in temp[i]:
    #                 temp[i] = temp[i].replace(j, "_")
                    
    #     temp = ",".join(temp)
        
    #     col_change = os.popen("sed -i \"1s/.*/" + temp + "/\" " + input_file_path)
    #     col_change.read()
               
    from pyspark.sql.functions import col
    from pyspark.sql.types import StringType
    global temp_df_coltypes
    temp_df_coltypes = list(df.dtypes)

    coltypes_to_string = []
    coltypes_to_float = []
    for i in temp_df_coltypes:
         if ('date' in i[1]) or ('bool' in i[1]):
             coltypes_to_string.append(i)
         if ('int' in i[1]):
             coltypes_to_float.append(i)

    for i in coltypes_to_string:
        df = df.withColumn(i[0],col(i[0]).cast(StringType()))
    print("[SUB] changed to string")
    print(coltypes_to_string)
    print("[SUB] all datatypes of the dataframe")
    print(df.dtypes)


    # print("[REF COUNT]" + str(df.count()))

    list_linked = df.columns
    try:
        list_linked = list_linked.split(",")
    except:
        list_linked = list_linked

    list_anon = []
    list_pseudo = []

    if boolit:
        if input_file_path != None:
            fsizepath = input_file_path

            fsize = 0
            if os.path.isfile(fsizepath):
                fsize = os.path.getsize(fsizepath)
            elif os.path.isdir(fsizepath):
                fsize = sum(d.stat().st_size for d in os.scandir(fsizepath) if d.is_file())
            else:
                print("[SUB] [0] Invalid Path for Ref Get Size")
        
        
            if fsize > 5000000000:
                refsample_fraction = 5000000000 / fsize  

                tic =time.time()
                df.sample(fraction=refsample_fraction).write.mode("overwrite").option("header", "true")\
                        .csv(input_file_path + ".sample")  
                print("[SUB] [0] time taken to sample ref df is " + str(time.time() - tic) + " seconds")
                print("[SUB] [0] ref file size is  " + str(fsize / 1000000 ) + " Mbytes")
                tostats_fnamer = input_file_path + ".sample"
            else:
                print("[SUB] [0] ref file size is  " + str(fsize / 1000000 ) + " Mbytes")




    df = df.drop('index')

    slice_for_fields = 500
    if df.count() > slice_for_fields:
        slice_fields = get_stratum(df.select(*list_anon), slice_for_fields).toPandas()
    else:
        slice_fields = df.select(*list_anon).toPandas()
    
    dict_anon = get_fields(slice_fields)
    
    for i, k in dict_anon.items():
        if k == 'OTHERS':
            list_anon.remove(i)
            list_pseudo.append(i)
        else:
            pass
    
    slice_anon = df.select(*list_anon)
    
    slice_pseudo = df.select(*list_pseudo)
    
    import math
    
    
    
    if len(list_pseudo) != 0:    
        slice_pseudo.repartition(200).write\
                    .format('csv')\
                    .option('header',True)\
                    .mode('overwrite')\
                    .option('sep',',')\
                    .save(placeholder_pseudo)
    
    df = df.select(*list_linked)
    
    # info_categoricals
    col_array = df.columns
    type_array = df.dtypes
    info_categoricals = get_categoricals(col_array, type_array)
    
    
    if ((len(col_array) != 0) and ((len(list_anon) == 0) and (len(list_pseudo) == 0))):
        trailer = pd.DataFrame({col_array[0]: "trailer_n"}, index = ['trail'])
    elif ((len(col_array) == 0) and ((len(list_anon) != 0) or (len(list_pseudo) != 0))):
        trailer = pd.DataFrame({1:"trailer_ap"}, index = ['trail'])
    elif ((len(col_array) != 0) and ((len(list_anon) != 0) or (len(list_pseudo) != 0))):
        trailer = pd.DataFrame({col_array[0]: "trailer"}, index = ['trail'])
    
    
    if trailer.iloc[0,0] == 'trailer_n':
        list_pseudo = None
    elif (len(slice_pseudo.columns) != 0) and (trailer.iloc[0,0] != 'trailer_n'):
        list_pseudo.append("LOC:" + placeholder_pseudo)
    else:
        list_pseudo.append("LOC:None")
    
    
    if (list_pseudo != None):
        list_pseudo.append("COUNT:" + str(df.count()))
    
    
    temp = {'my_anons': list_anon, 'my_pseudos': list_pseudo}
    
    print(dict_anon)
    
    for i in list_anon.copy():
        list_anon.append(dict_anon[i])
        
    
    
    if trailer.iloc[0,0] == 'trailer_n':
        sig_ap = None
    elif len(col_array) != 0:
        sig_ap = pd.DataFrame({col_array[0]: str(list_anon) + str(list_pseudo)}, index = ['ap'])
    else:
        sig_ap = pd.DataFrame({1: str(list_anon) + str(list_pseudo)}, index = ['ap'])
    
    
    info_precision = get_precision(df,info_categoricals)
    
    
    info_minmax = get_minmax(df, info_categoricals)
    
    
    no_bins,skew_dict,len_of_data = get_bincount(df, info_categoricals,binFunc)
    
    for item, value in skew_dict.items():
        if value == 0:
            info_categoricals[item] = 1
            del(no_bins[item])
    
#     no_bins = get_bincount(df, info_categoricals)
    
    
    from pyspark.ml.feature import Bucketizer
    info_ctypes = dict(type_array)
    
    
    data_num = [key for key,value in info_categoricals.items() if value == 0]
    input_cols_array = []
    output_cols_array = []
    info_bincuts = {}
    
    old_columns = df.columns

    for i in data_num:
        if binFunc == 2:
            unique_val = df.select(countDistinct(i)).collect()[0][0]
            if (unique_val > int(0.1*len_of_data)):
                info_bincuts[i] = AdaptiveBinning(df.select(i),int(no_bins[i]),len_of_data)
            else:
                info_bincuts[i] = get_cuts(float(info_minmax.loc['min', i]), float(info_minmax.loc['max', i]),int(no_bins[i]))
        else:
            info_bincuts[i] = get_cuts(float(info_minmax.loc['min', i]), float(info_minmax.loc['max', i]),int(no_bins[i]))

        input_cols_array.append(i)

        output_cols_array.append(i+'_binned')
        info_categoricals[i+'_binned'] = 1
    
    obj = Bucketizer()
    obj.setSplitsArray(list(info_bincuts.values()))
    obj.setInputCols(input_cols_array)
    obj.setOutputCols(output_cols_array)
    df = obj.setHandleInvalid("keep").transform(df)
    
    cols_drop = [x for x in df.columns if x+'_binned' in df.columns]
    
    df = df.drop(*cols_drop)
    
    for i in range(len(output_cols_array)):
        df = df.withColumnRenamed(output_cols_array[i], input_cols_array[i])
    
    if len(col_array) != 0:
        from pyspark.sql.functions import desc
        signature = df.groupby(*df.columns).count().sort(desc('count'))
    else:
        signature = None
    
    
    
    no_bins = pd.DataFrame([no_bins])
    
    
    
    no_bins.index = ['bcount']
    
    for i in info_bincuts.keys():
        info_bincuts[i] = str(info_bincuts[i])
    info_bincuts = pd.DataFrame(info_bincuts,index = ['bincuts'])
    
    
    info_minmax = info_minmax.append(no_bins)
    
    info_precision = pd.DataFrame(info_precision, index = ['precision'])
    
    info_minmax = pd.concat([info_minmax,info_precision,info_bincuts])
    
    
    import numpy as np
    
    
    
    if trailer.iloc[0,0] != 'trailer_n':
        try: 
            sig_ap = spark.createDataFrame(sig_ap) 
        except:
            sig_ap[col_array] = np.nan
            sig_ap = spark.createDataFrame(sig_ap) 
    
    
    
    
    try: 
        info_minmax = spark.createDataFrame(info_minmax.astype(str))
    except:
        if len(col_array) != 0:
            info_minmax[col_array] = np.nan
            info_minmax = spark.createDataFrame(info_minmax)
    
    if len(col_array) != 0:
        trailer = trailer.rename(columns = {trailer.columns[0]:signature.columns[0]})
    
    esc = 0
    if trailer.iloc[0,0] == 'trailer_n':
        esc = 1
    
    trailer = spark.createDataFrame(trailer) 
    
    if esc == 0:
        if len(col_array) != 0:
            sig_ap = sig_ap.withColumnRenamed(sig_ap.columns[0],info_minmax.columns[0])
    
    
    if len(col_array) != 0:
        if esc == 0:
            info_minmax = info_minmax.unionByName(sig_ap, allowMissingColumns=True)
        info_minmax = info_minmax.unionByName(trailer, allowMissingColumns=True)
    else:
        sig_ap = sig_ap.unionByName(trailer, allowMissingColumns=True)
        
        
    placeholder_local_minmax = placeholder_local.split('/')
    placeholder_local_minmax.append("min_max_" + placeholder_local_minmax[-1])
    placeholder_local_minmax = "/".join(placeholder_local_minmax)
    
    placeholder_local_sig = placeholder_local.split('/')
    placeholder_local_sig.append("sig_" + placeholder_local_sig[-1])
    placeholder_local_sig = "/".join(placeholder_local_sig)
    
    if len(col_array) != 0:
        info_minmax.coalesce(1)\
        .write\
        .format('parquet')\
        .option('header', True)\
        .mode('overwrite')\
        .save(placeholder_local_minmax)
    else:
        sig_ap.coalesce(1)\
        .write\
        .format('parquet')\
        .option('header', True)\
        .mode('overwrite')\
        .save(placeholder_local_minmax)
    
    if signature != None:
        signature\
            .repartition(200)\
            .write\
            .format('parquet')\
            .option('header',True)\
            .mode('overwrite')\
            .save(placeholder_local_sig)

    sig_toc = time.time()

    print("[TIME] The signature was extracted in " + str(sig_toc - sig_tic) + " secs")
    
    return {'Message': 'extracted'}
                
def generate(boolit, placeholder_local, scale_factor, placeholder_filename_output,binFunc, input_t, out_params):

    tic_gen = time.time()

    placeholder_local_sig = placeholder_local.split('/')
    placeholder_local_sig.append("sig_" + placeholder_local_sig[-1])
    placeholder_local_sig = "/".join(placeholder_local_sig)

    tic = time.time()
    
    if placeholder_local_sig.split("/")[-1] in os.listdir(placeholder_local):
        sig_schema = spark.read.format("parquet").load(placeholder_local_sig).schema
        prq_signature = spark.read.schema(sig_schema).format("parquet").load(placeholder_local_sig)
    else:
        prq_signature = None
    
    toc = time.time()
    print("[SUB] Time of getting signature if present: " + str(toc-tic) + " sec")
    
    tic = time.time()
    
    placeholder_local_minmax = placeholder_local.split('/')
    placeholder_local_minmax.append("min_max_" + placeholder_local_minmax[-1])
    placeholder_local_minmax = "/".join(placeholder_local_minmax)
    
    info_minmax_e = spark.read.format("parquet").load(placeholder_local_minmax)
    
    info_minmax_e = info_minmax_e.toPandas()
    
    toc = time.time()
    print("[SUB] Time to get min-max signature: " + str(toc-tic) + " sec")
    
    #print(info_minmax_e)

    
    if 'trailer' in info_minmax_e.tail(1).values:
        info_minmax_e.index = ['min', 'max', 'bincount', 'precision','bincuts','sig_ap', 'trailer']
    elif 'trailer_ap' in info_minmax_e.tail(1).values:
        info_minmax_e.index = ['sig_ap', 'trailer']
    elif 'trailer_n' in info_minmax_e.tail(1).values:
        if len(info_minmax_e) != 1:
            info_minmax_e.index = ['min', 'max', 'bincount', 'precision','bincuts','trailer']
        else:
            info_minmax_e.index = ['trailer']

        
    if 'precision' in info_minmax_e.index:
        temp_precision_e = info_minmax_e.loc['precision']
    
    if 'bincuts' in info_minmax_e.index:
        temp_bincuts_e = info_minmax_e.loc['bincuts']
    
    if 'sig_ap' in list(info_minmax_e.index):
        sig_ap_e = str(info_minmax_e.loc[['sig_ap'], info_minmax_e.columns[0]].values[0])
    else:
        sig_ap_e = None
    
    tic = time.time()

    print("The sig_ap_e var is " + str(sig_ap_e))

    count_pseudo_e = None
    
    if sig_ap_e != None:
        (list_anon_e, type_anon_e, list_pseudo_e, placeholder_pseudo_e, count_pseudo_e) = decode_ap_e(sig_ap_e)
        #placeholder_pseudo_e='pseudo_basketball'

    toc = time.time()
    print("[SUB] Time taken to decode information: " + str(toc-tic) + " sec")
    
    if 'min' in list(info_minmax_e.index):
        info_minmax_e = info_minmax_e.loc[['min', 'max', 'bincount'], :]
    
    if prq_signature != None:
        prq_signature = prq_signature.na.drop()

    
    if prq_signature != None:
        traverser = len(prq_signature.head()) - 1
    
    if prq_signature != None:
        column_names = prq_signature.columns[:-1]
    
    if prq_signature != None:
        if count_pseudo_e != None:
            counts = count_pseudo_e * scale_factor
        # counts = list(prq_signature.select('count').collect())
        # counts = count_pseudo_e * scale_factor
        trav_counts = 1
    else:
        counts = count_pseudo_e * scale_factor
        trav_counts = 0
    
    
    if prq_signature != None:
        save_signature = prq_signature.drop('count')
    
    tic = time.time()
    
    exporter = {}
    info_precision_e = {}
    if (info_minmax_e.size > 2) and (temp_precision_e.replace("NaN", np.nan).isna().sum() != len(temp_precision_e)):
        for i in column_names:
            if i in list(info_minmax_e):
                if str(info_minmax_e.loc['min', i]) != 'None'\
                    and str(info_minmax_e.loc['min', i]) != 'NaN':
    
                    if (binFunc == 2):
                        cuts = temp_bincuts_e[i].strip('][').split(', ')
                        cuts = [float(cut) for cut in cuts]
                    else:  
                        cuts = get_cuts(float(info_minmax_e.loc['min', i]),\
                                     float(info_minmax_e.loc['max', i]),\
                                     int(info_minmax_e.loc['bincount', i]))
                    exporter[i] = {}
                    info_precision_e[i] = temp_precision_e.loc[i]
                    indexer = 0
                    for j in range(len(cuts)-1): 
            #             print(float(indexer), cuts[indexer], cuts[indexer+1]) 
                        exporter[i][str(float(j))] = (cuts[j], cuts[j+1])
    
    toc = time.time()
    print("[SUB] Time to set up min-max dictionary: " + str(toc-tic) + " sec")
    
    header = ''
    if prq_signature != None:
        header += ",".join(save_signature.columns) + ','
    # if sig_ap_e != None:
    #     if (len(list_anon_e) != 0):
    #         header += list_anon_e + ','
    #     if len(list_pseudo_e) != 0:
    #         header += list_pseudo_e + ','
    
    # Removed Extra comma from header
    header = header[:-1]
    
    tic = time.time()
    
    # pseudo_df = pd.DataFrame()
    # if sig_ap_e != None:
    #     if len(list_pseudo_e) != 0:
    #         # Get Pseudo Spark DF
    #         pseudo_e = spark.read.format("csv").load(placeholder_pseudo_e, header = True)
            
    #         # Get Pseudo Pandas DF
    #         all_files = glob.glob(os.path.join(placeholder_pseudo_e , "*.csv"))
    #         all_df = []
    #         for filename in all_files:
    #             df = pd.read_csv(filename, index_col=None, header=0)
    #             all_df.append(df)
    #         pseudo_df = pd.concat(all_df, axis=0, ignore_index=True)
    


    toc = time.time()
    print("[SUB] Time to import pseudo: " + str(toc-tic) + " sec")
    
    if sig_ap_e != None:
        l_anon = len(list_anon_e.split(","))
        l_pseudo = len(list_pseudo_e.split(","))
    
    tic = time.time()
    
    # from pyarrow.parquet import ParquetFile
    #import pyarrow as pa
#    import s3fs
#    import os
#    fs = s3fs.S3FileSystem(key=ACCESS_KEY, secret=SECRET_KEY)
    
#    if sig_ap_e != None:
#        f_lst_e = fs.ls(placeholder_pseudo_e)
#        f_lst_e = [x for x in f_lst_e if x[-4:] == '.csv']
    
    toc = time.time()
    print("[SUB] Time to get pseudo file list: " + str(toc-tic) + " sec")

    tic = time.time()
    
    
    # if prq_signature != None:
    #     file_location = [x for x in os.listdir(placeholder_local_sig) if x[-8:] == '.parquet']
    #     pf_arr = []
    #     for i in file_location:
    #         pf_arr.append(ParquetFile(placeholder_local_sig + "/" + i))
    #     # pf = ParquetFile(bucket_location + file_location[0])
    
    toc = time.time()
    print("[SUB] Time to get locations of parque files: " + str(toc-tic) + " sec")    
    
    tic= time.time()
    
    adder = 0
    # i = 0
    # bidx = 0
    # lines = ""
    # BATCH_SIZE = 10000

    if prq_signature != None:
        counts_sig = spark.read.format("parquet").load(placeholder_local_sig).count()
    else:
        counts_sig = counts
        
    # n_cores = 2
    # n_processes = n_cores
    # ipa_array = []
    # for pf in pf_arr:
    #     for ipa in pf.iter_batches(batch_size = math.ceil(counts_sig/n_processes)):
    #         ipa_array.append(ipa)
    
    try:
        print(list_pseudo_e)
    except:
        list_pseudo_e = None
    
    try:
        print(placeholder_pseudo_e)
    except:
        placeholder_pseudo_e = None
        
    try:
        print(count_pseudo_e)
    except:
        count_pseudo_e = None
    
    # try:
    #     print(f_lst_e)
    # except:
    #     f_lst_e = None
    
    try:
        print(type_anon_e)
    except:
        type_anon_e = None
        
    try:
        print(counts)
    except:
        counts = None

    if sig_ap_e == None:
        l_anon = None
        l_pseudo = None
        list_anon_e = None

    ### Removed
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     inputs_togen = []
    #     for i in range(len(ipa_array)):
    #         inputs_togen.append([i, 0, ipa_array[i], placeholder_filename_output,sig_ap_e, l_anon, l_pseudo, header,\
    #                                 trav_counts, traverser, exporter, column_names,\
    #                                 info_precision_e, list_pseudo_e, placeholder_pseudo_e, count_pseudo_e, type_anon_e, counts, scale_factor])
    #     results = executor.map(do_gen, inputs_togen)
             

    #Run Different Streams Depending on Signature Files Provided
    if prq_signature != None: 
        #Run Using Spark UDF
        params = [0
            ,boolit
            ,placeholder_filename_output
            ,sig_ap_e
            ,l_anon
            ,l_pseudo
            ,header
            ,trav_counts
            ,traverser
            ,exporter
            ,column_names
            ,info_precision_e
            ,list_pseudo_e
            ,placeholder_pseudo_e
            ,type_anon_e
            ,counts
            ,scale_factor
            ,placeholder_local_sig,
            list_anon_e
            ,input_t
            ,out_params]
        final_df = do_gen_prq_signature(params)
                         
    toc = time.time()
    print("[SUB] Time of generate function: " + str(toc-tic) + " sec")
    
    toc_gen = time.time()
    print("[TOTAL] Total time for data generation: " + str(toc_gen-tic_gen) + " sec")
    

    global tostats_fnameg
    global tostats_fnamer

    print("[BOOLIT] :" + str(boolit))
    print("[PATH] : " + str(tostats_fnameg))
    print("[PATH] :" + str(tostats_fnamer))
    
    #if boolit:
        # print(tostats_fnameg)
        # get_stats(tostats_fnamer, tostats_fnameg, 10)
    
    
    return final_df


############################################################################
    
def get_rels(database, host="localhost", user="root", password="password"):

    ret_list = []

    mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)

    mycursor = mydb.cursor()

    mycursor.execute("SELECT `TABLE_NAME`,`REFERENCED_TABLE_NAME`,`COLUMN_NAME`,`REFERENCED_COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`KEY_COLUMN_USAGE` WHERE `TABLE_SCHEMA` = SCHEMA() AND `REFERENCED_TABLE_NAME` IS NOT NULL;")
    myresult = mycursor.fetchall()

    for x in myresult:
        ret_list.append([(x[0], x[1]), (x[2], x[3])])
    
    return ret_list

def get_dict_cols(table_list, database, host="localhost", user="root", password="password"):
    mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)

    final_dict = {}

    for table in table_list:
        mycursor = mydb.cursor()
        comm_str = "SHOW COLUMNS FROM " + str(table) + ";"
        mycursor.execute(comm_str)
        myresult = mycursor.fetchall()

        ret_list = []

        for x in myresult:
            ret_list.append(x[0])
        
        final_dict[table] = ret_list
    

    for table in table_list:
        if table in duplicate_dict:
            i = 0
            for col in final_dict[table]:
                if col in duplicate_dict[table]:
                    print("Column tested: ", col)
                    print("Column Replacement: ", duplicate_dict[table][col])
                    final_dict[table][i] = duplicate_dict[table][col]
                i += 1

    return final_dict






def join_tables(reader, t1, t2, k1, k2, duplicate_handling = True):
    df1_i = reader.table(t1)
    df2_i = reader.table(t2)
    if duplicate_handling:
        df2 = handle_duplicates(df2_i, t2, df1_i, k2)
        df1 = handle_duplicates(df1_i, t1, df2_i, k1)
    if k1 == k2:
        d_df = df1.join(df2, [k2], "fullouter")
    else:
        d_df = df1.join(df2, df1[k1] == df2[k2], "fullouter")
    
    return d_df

def handle_timestamps(d_df):
    
    spark_df = d_df
    for tup in d_df.dtypes:
        col = tup[0]
        col_dtype = tup[1]

        if col_dtype == 'timestamp':
            spark_df = spark_df.withColumn(col, f.to_timestamp(f.col(col)))
    print("\nSuccessfully handled timestamps\n")
    return spark_df

def handle_duplicates(o_df, t_name, d_df, key_list):
    o_list = o_df.columns
    d_list = d_df.columns
    r_name = []
    s_df = o_df

    dict_loc = {}

    for col in o_list:
        if col in d_list:
            if col in key_list:
                print("pass")
            else:
                r_name.append(col)
                namer = t_name + "_" + col
                s_df = s_df.withColumnRenamed(col,namer)
                dict_loc[col] = namer
                only_columnname_dict[namer] = t_name

    print("Table Name: ", t_name)
    print("Local Dict: ", dict_loc)
    if t_name in duplicate_dict:
        dict_loc == dict_loc.update(duplicate_dict[t_name])
    duplicate_dict[t_name] = dict_loc
    
    return s_df


def handle_duplicates_after(o_df):
    s_df = o_df

    for col in s_df.columns:
        check = 0
        for col2 in s_df.columns:
            if col == col2:
                check += 1
                if check > 1:
                    s_df = s_df.withColumnRenamed(col, col + "_" + str(check - 1))
    
    return s_df


def split_composites_pairs(keypairs):

    p_traversed = []
    comp_list = []
    
    for tup in keypairs:
        a, b = tup
        check = 0
        inner_list = []
        inner_list.append(b)
        for tup2 in keypairs:
            c, d = tup2
            if (((a[0] == c[0]) and (a[1] == c[1])) and ((b[0] != d[0]) or (b[1] != d[1]))):

                check += 1
                already_bool = False
                for tup3 in comp_list:
                    e = tup3[0]

                    if a == e:
                        already_bool = True
                if already_bool ==  False:

                    inner_list.append(d)

        if check == 0:
            p_traversed.append(tup)
        elif len(inner_list) > 1:

            comp_list.append([a, inner_list])
    
    return p_traversed, comp_list



def get_from_mysql(var_url, var_db, var_table, var_user, var_password):
    
    var_dbtable = var_db + "." + var_table
    
    x_df = spark.read.format("jdbc", ).\
                option("url", var_url).\
                option("driver", "com.mysql.jdbc.Driver").\
                option("dbtable", var_dbtable).\
                option("user", var_user).\
                option("password", var_password).\
                load()
    return x_df



def send_to_mysql(x_df, var_url, var_db, var_table_out, var_user, var_password,datatype):

    
    var_dbtable_out = var_db + "." + var_table_out
    
    
    x_df.write.format("jdbc").\
                option("url", var_url).\
                option("driver", "com.mysql.jdbc.Driver").\
                option("dbtable", var_dbtable_out).\
                option("user", var_user).\
                option("password", var_password).\
                option("createTableColumnTypes", datatype).save()


def join_database(var_user, var_password,var_db, var_url="jdbc:mysql://localhost:3306", write_out = False, var_table_out = None, duplicate_handling = True, var_host = "mysql-service.staging"):
#    findspark.init()
    

    #list of the tables in the server
    table_names_list = spark.read.format('jdbc'). \
        options(
            url=var_url, # database url (local, remote)
            dbtable='information_schema.tables',
            user=var_user,
            password=var_password,
            driver="com.mysql.jdbc.Driver"). \
        load().\
        filter("table_schema = '" + var_db +"'").toPandas()
        #filter("table_schema = '" + var_db +"'").select("table_type").toPandas()
        

    #print(table_names_list)     
    table_names_list = list(table_names_list['TABLE_NAME'])
        
    url = var_url + "/" + var_db
    # url = "jdbc:mysql://localhost:3306/" + var_db
    reader = (
        spark.read.format("jdbc")
        .option("url", url)
        .option("user", var_user)
        .option("password", var_password)
    )
    for tablename in table_names_list:
        reader.option("dbtable", tablename).load().createTempView(tablename)


    keypairs = get_rels(database=var_db, host = var_host, user=var_user, password=var_password)

    # [MARKER:SORTED] keypairs sorting 
    keypairs_sorted = []
    for i in keypairs: 
        
        if i[0][0] < i[0][1]:
            keypairs_sorted.append(i)
        else:
            i_0 = (i[0][1],i[0][0])
            i_1 = (i[1][1],i[1][0])
            keypairs_sorted.append([i_0, i_1])
            
    keypairs = keypairs_sorted
    # [MARKER:SORTED] keypairs sorting 



    p_traversed, comp_list = split_composites_pairs(keypairs)

    print("P Traversed: ", p_traversed)
    print("Comp List: ", comp_list, "\n\n")

    t_traversed = []
    k_traversed = 0
    k = 0
    kin = 0

    cur = p_traversed[0][0]
    # JOIN
    ##print("cur: ", cur)
    t_traversed.append(cur[0])
    t_traversed.append(cur[1])
    #print(t_traversed)
    kin = kin + 1

    #print(len(keypairs))

    rel_lists = p_traversed[0]

    #print("KeyPairs: ", keypairs)

    a_1, b_1 = rel_lists
    t_1, t_2 = a_1
    k_1, k_2 = b_1
    d_df = join_tables(reader, t_1, t_2, k_1, k_2, duplicate_handling = duplicate_handling)
    #print("rel_list:", rel_lists)
    #print("cols: ", d_df.columns)

    
    #print(d_df.columns)
    # masterbreak = False
    iteroo = 0
    total_additions = 0
    #brk_loop = False
    for i in range(len(p_traversed)):
        additions = 0
        #print("Iteration: ", i)
        #print("traversed: ", t_traversed)
        for rel_lists in p_traversed:
            iteroo = iteroo +1
            #print("iteroo: ", iteroo)
            a, b = rel_lists
            t1, t2 = a
            k1, k2 = b
            #print("t1, t2: ", t1, ", ", t2)
            print("loop rel_list: ", rel_lists)
            if ((t1 in t_traversed) and (t2 in t_traversed)):
                print("First condition")
            elif ((t1 in t_traversed) or (t2 in t_traversed)):
                if t1 in t_traversed:
                    df2_i = reader.table(t2)
                    if duplicate_handling:
                        df2 = handle_duplicates(df2_i, t2, d_df, [k2])
                        #d_df = handle_duplicates(d_df, t1, df2_i, k1)
                    #print("Adding cols: ", df2.columns, "\n")
                    print("DF2 Columns: ", df2.columns)
                    print("D_DF Columns: ", d_df.columns)
                    if k1 == k2:
                        d_df = d_df.join(df2, k2, "fullouter")
                    else:
                        d_df = d_df.join(df2, d_df[k1] == df2[k2], "fullouter")
                    t_traversed.append(t2)
                else:
                    df1_i = reader.table(t1)
                    if duplicate_handling:
                        df1 = handle_duplicates(df1_i, t1, d_df, [k1])
                        #d_df = handle_duplicates(d_df, t2, df1_i, k2)

                    #print("Adding cols: ", df1.columns, "\n")
                    print("DF1 Columns: ", df1.columns)
                    print("D_DF Columns: ", d_df.columns)
                    if k1 == k2:
                        d_df = df1.join(d_df, k1, "fullouter")
                    else:
                        d_df = df1.join(d_df, df1[k1] == d_df[k2], "fullouter")
                    t_traversed.append(t1)
                #print("Second condition")
                #print("Updated traversed: ", t_traversed)
                #print(t_traversed)
                additions += 1
            else:
                """
                df1 = reader.table(t1)
                df2 = reader.table(t2)

                if k1 == k2:
                    d_df = d_df.join(df1, k1, "fullouter")
                    d_df = d_df.join(df2, k2, "fullouter")
                else:
                    d_df = d_df.join(df1, df1[k1] == d_df[k2], "fullouter")
                    d_df = d_df.join(df2, d_df[k1] == df2[k2], "fullouter")
                """
                print("Third condition")
        total_additions += additions
        #print("Additions in iteration: ", additions, "\n\n")
        if additions == 0:
            print("\n\nBreaking on iteration number: ", i)
            break
    
    if len(comp_list) > 0:
        for i in range(len(comp_list)):
            additions_1 = 0
            #print("Iteration: ", i)
            #print("traversed: ", t_traversed)
            for rel_lists in comp_list:
                iteroo = iteroo +1
                #print("iteroo: ", iteroo)
                a, b = rel_lists
                t1, t2 = a
                print("\n\nrel_list: ", rel_lists, "\n\n")
                print("\n\nb: ", b, "\n\n")
                key_list_0 = []
                key_list_1 = []

                for i in b:
                    key_list_0.append(i[0])
                    key_list_1.append(i[1])
                
                print("\n\nkey_list_0: ", key_list_0, "\n\n")
                print("\n\nkey_list_1: ", key_list_1, "\n\n")

                #k1, k2 = b
                #k3, k4 = c
                #print("t1, t2: ", t1, ", ", t2)
                #print("loop rel_list: ", rel_lists)
                if ((t1 in t_traversed) and (t2 in t_traversed)):
                    print("First condition")
                    pass
                elif ((t1 in t_traversed) or (t2 in t_traversed)):
                    print("Second condition")
                    if t1 in t_traversed:
                        df2_i = reader.table(t2)
                        if duplicate_handling:
                            df2 = handle_duplicates(df2_i, t2, d_df, key_list_1)
                        print("DF2 Columns: ", df2.columns)
                        print("D_DF Columns: ", d_df.columns)
                        if key_list_0 == key_list_1:
                            d_df = d_df.join(df2, key_list_1, "fullouter")
                        else:
                            d_df = d_df.join(df2, [d_df[f] == df2[s] for (f, s) in b], "fullouter")
                        print("D_DF Columns Afterwards: ", d_df.columns)
                        #print("Adding cols: ", df2.columns, "\n")
                        #if k1 == k2:
                        #    d_df = d_df.join(df2, k2, "fullouter")
                        #else:
                        #    d_df = d_df.join(df2, (d_df[k1] == df2[k2]) & (d_df[k3] == df2[k4]), "fullouter")
                        t_traversed.append(t2)
                    else:
                        df1_i = reader.table(t1)
                        if duplicate_handling:
                            df1 = handle_duplicates(df1_i, t1, d_df, key_list_0)
                        print("DF1 Columns: ", df1.columns)
                        print("D_DF Columns: ", d_df.columns)
                        if key_list_0 == key_list_1:
                            d_df = df1.join(d_df, key_list_0, "fullouter")
                        else:
                            d_df = df1.join(d_df, [df1[f] == d_df[s] for (f, s) in b], "fullouter")
                        print("D_DF Columns Afterwards: ", d_df.columns)

                        #print("Adding cols: ", df1.columns, "\n")
                        #if k1 == k2:
                        #    d_df = df1.join(d_df, k1, "fullouter")
                        #else:
                        #    d_df = df1.join(d_df, df1[k1] == d_df[k2], "fullouter")
                        t_traversed.append(t1)
                    #print("Second condition")
                    #print("Updated traversed: ", t_traversed)
                    #print(t_traversed)
                    additions_1 += 1
                else:
                    print("Third condition")
                    pass
            #print("Additions in iteration: ", additions, "\n\n")
            if additions_1 == 0:
                print("\n\nBreaking on iteration number: ", i)
                break

    
    print("\nfinal traversed: ", t_traversed)
    print("\ntable list for ref: ", table_names_list, "\n")
    
    print("Total Additions Made: ", total_additions, "\n\n")

    db_table_list = get_dict_cols(table_list=table_names_list, host=var_host, database=var_db, user=var_user, password=var_password)

    if write_out == False:
        #print("\n\nDataframe: ", d_df, "\n\n")
        #d_df = handle_timestamps(d_df)
        #d_df = d_df.toPandas()
        return d_df, db_table_list
    
    elif var_table_out != None:
        send_to_mysql(d_df, var_url, var_db, var_table_out, var_user, var_password)
        return d_df, db_table_list
    else:
        print("No name sent for output, simply returning pandas dataframe")
        return d_df
    
####################### TRANSFER START ###########################################

# Join a test database and get joined_df 
# Get dict_cols which is a dictionary of table names : [columns ]
# E.g 
# {'tab1': ['orderNumber', 'orderDate', 'requiredDate', 'shippedDate'],
# 'tab2': ['status', 'comments', 'customerNumber']}
    
# use the following code to send the joined df to a NEW database , change var_db etc with respect to your setup

def deid_db(joined_df,column_datatypes_dict ,dict_cols, var_url, output_db, var_db, var_user, var_password, host = 'localhost'):
    
    mydb = mysql.connector.connect(host=host, user=var_user, password=var_password)

    mycursor = mydb.cursor()

    mycursor.execute("SHOW databases;")
    myresult = mycursor.fetchall()
    
    curr_dbs = [i[0] for i in myresult]
    
    if output_db not in curr_dbs:
        mycursor.execute("create schema " + output_db + ";")
        myresult = mycursor.fetchall()

    # for key,values in dict_cols.items():
    #     print(values)
    #     for vi in values:
    #         if vi in only_columnname_dict.keys():
    #             t_namecut = only_columnname_dict[vi]
    #             fullname = vi
    #             length = len(t_namecut) + 1
    #             replaced = fullname[length:]
    #             values[values.index(vi)] = replaced


    #     df_slice = joined_df[values].distinct()
    #     df_slice = df_slice.na.drop()
    #     send_to_mysql(df_slice, var_url, output_db, key, var_user, var_password)
    
    

    for (key,values) in (dict_cols.items()):
        # print(values)
        columns_replaced_dict ={}
        df_slice = joined_df[values].distinct()
        df_slice = df_slice.na.drop()
        for vi in values:
            if vi in only_columnname_dict.keys():
                t_namecut = only_columnname_dict[vi]
                fullname = vi
                length = len(t_namecut) + 1
                replaced = fullname[length:]
                columns_replaced_dict[fullname] = replaced
                
        print(columns_replaced_dict)
        for i in columns_replaced_dict:
            df_slice = df_slice.withColumnRenamed(i, columns_replaced_dict[i])
        
        print(df_slice.columns)
        # df_slice = df_slice.rename(columns = columns_replaced_dict)
        # df_slice.toPandas()
        # print(type(df_slice))
        
        
        datatype = column_datatypes_dict[key]
        send_to_mysql(df_slice, var_url, output_db, key, var_user, var_password,datatype)
    


    
    # for i in dict_cols:
    #     print(dict_cols[i])
    #     df_slice = joined_df[dict_cols[i]].distinct()
    #     df_slice = df_slice.na.drop()
        

    #     send_to_mysql(df_slice, var_url, output_db, i, var_user, var_password)
        
# MARKER[COMMENTED]        
# def get_primary(database, user = "root", password = "password", host = "localhost"):
#     mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)

#     mycursor = mydb.cursor()
    
#     get_primary = "SELECT k.TABLE_NAME, k.COLUMN_NAME " + \
#                     "FROM information_schema.table_constraints t " + \
#                     "JOIN information_schema.key_column_usage k " + \
#                     "USING(constraint_name,table_schema,table_name) " + \
#                     "WHERE t.constraint_type='PRIMARY KEY' " + \
#                     "AND t.table_schema='test_rels_comp';"
                    
#     mycursor.execute(get_primary)
#     primary_keys_df = mycursor.fetchall()
    
    # # Got tables and theur associated primary keys
    
    # primary_keys = {}
    # for k in primary_keys_df:
    #     if k[0] in primary_keys.keys():
    #         primary_keys[k[0]].append(k[1])
    #     else:
    #         primary_keys[k[0]] = [k[1]]
            
    # return primary_keys
        
####################### UNDER CONSTRUCTION ##########################################################

def make_rels(primary_keys, rels, database, user = "root", password = "password", host = "localhost"):
    mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)

    mycursor = mydb.cursor()
    
    for i in primary_keys.keys():
        command = "ALTER TABLE " + i + " ADD PRIMARY KEY " + "(" + ",".join(primary_keys[i]) + ");"
        mycursor.execute(command)
    
    for i in rels:
        # ALTER TABLE your_table ADD FOREIGN KEY (your_column) REFERENCES other_table(other_column);
        command = "ALTER TABLE " + str(i[0][1]) + " ADD FOREIGN KEY (" + str(i[1][1]) + ") REFERENCES " + str(i[0][0]) + "(" + str(i[1][0]) + ");"
        mycursor.execute(command)
    
    return 1

##################################################################################################


import argparse

def get_arg(parser, flag, name, text):
    parser.add_argument("-" + flag, "--" + name, dest=name, help=text)
    return parser


if __name__ == '__main__':
    import time
    import json
    import sys
    import mysql.connector

    parser = argparse.ArgumentParser()

    parser = get_arg(parser, 'j', 'jsonFile', 'The json file to be read for the arguments') 

    value  = parser.parse_args()
    
    with open(value.jsonFile, 'r') as jfile:
        value = json.load(jfile)
        
    print("The type of the variable is:" + str(type(value)))
    
    print(value)
    var_host = value["var_url"].split("//")[-1].split(":")[0]

    print("[MARKER] CALLING GET RELS")
    pairs = get_rels(database=value["var_db"], host = var_host, user=value["var_user"], password=value["var_password"])
    print(pairs)
    print("[MARKER] CALLED GET RELS")

    
    joined_df, dict_cols = join_database(value["var_user"], value["var_password"], value["var_db"], value["var_url"],
                            value["write_out"], value["var_table_out"], duplicate_handling = True, var_host = value["host"])
    
    
    
    print("Value of scit_cols: ")
    print(dict_cols)

    column_datatypes_dict = sqlconnect_datatype(var_host,value["var_user"], value["var_password"], value["var_db"])
    
    
    
###########################################################################
# Comments not to be deleted

#    if value.listAnon == None:
#        anon_list = []
#    else:
#        anon_list = value.listAnon.split(',')
#    if value.listPseudo == None:
#        pseudo_list = []
#    else:
#        pseudo_list = value.listPseudo.split(',')
#    if value.listLinked == None:
#        linked_list = []
#    else:
#        linked_list = value.listLinked.split(',')
    
###########################################################################
    
    binFunc = 2
    
    input_t = 'mysql'

###########################################################################
# Comments not to be deleted    

#    print("Anon List: " + str(value.listAnon))
#    print("Pseudo List: " + str(value.listPseudo))
#    print("Linked List: " + str(value.listLinked))

###########################################################################

#    inparams = str(value["var_url"] + "," + value["var_db"] + "," + value["user"] + "," + value["passwd"])
#    outparams = str(value["url"] + "," + value["db"] + "." + value["tname_out"] + "," + value["user"] + "," + value["passwd"])

    # get_signature(boolit, input_file_path, placeholder_local, sparkconf_location, placeholder_pseudo, binFunc, input_t, in_params)
    get_signature(True, None, './sigfile', None, None, binFunc, input_t, joined_df)
    
#    generate(boolit, placeholder_local, scale_factor, placeholder_filename_output,binFunc, input_t, out_params):
    df = generate(True, './sigfile', float(1), None, binFunc, input_t, None)
    
    print(type(df))

    print(column_datatypes_dict)
   
    
    # deid_db(df ,column_datatypes_dict, dict_cols, value["var_url"], value["output_db"], value["var_db"], value["var_user"], value["var_password"], value["host"])
    deid_db(df ,column_datatypes_dict, dict_cols, value["var_url"], value["output_db"], value["var_db"], value["var_user"], value["var_password"], var_host)

    time_mega = time.perf_counter() - tic_mega
    print("MEGA TIME: " + str(time_mega))

    spark.stop()