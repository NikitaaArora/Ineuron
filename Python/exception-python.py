
#Exception Handling 
import logging
import os

#Using logging for exception handling #copying the same logging code from before. 
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

def division(a,b):
    try:

        output = a/b
        return output
    except Exception as e:
        logger.info(e)
        adds = a+b
        logger.info(adds)
        
    
out = division(3,89)


print(out)

