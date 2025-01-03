import logging
import os

#create logger string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


#this is the path where we want to save the log file. 
log_folder = "logs"
log_file = "logs/running_log.log"

os.makedirs(log_folder, exist_ok=True) #dont again create the folder if it already exists. 

logging.basicConfig(
    level= logging.INFO,
    format = logging_str,
    handlers= [
        logging.FileHandler(log_file) #save the log in a file. #This would automatically create the log of the file and save the logs there. 
              
    ]
)

logger = logging.getLogger("mylog") #creating an object of the log so that we can use it anytime. 



def add_number(a,b):
    output = a+b
    logger.info("Successfully executed")
    return output


num = add_number(3,4)

print(num)

logger.info("Code successfully executed")



