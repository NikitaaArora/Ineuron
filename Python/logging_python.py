import logging
import os

#create logger string

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


#this is the path where we want to save the log file. 
log_path = "logs/running_log.log"

os.makedirs(log_path, exist_ok =True) #dont again create the folder if it already exists. 





















# def add_number(a,b):
#     output = a+b
#     print("Successfully executed")

#     return output


# num = add_number(3,4)

# print(num)



