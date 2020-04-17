import logging

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  # This is the set up for logging in Python, the filename argument make a file in the current working directory. All the messages will be saved in the file.

# logging.disable(logging.CRITICAL)  # This will disable all the logging messages, here it means I want to disable all logging messages, at the critical level or lower.

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of fractorial(%s)'%(n))
    total = 1
    for i in range(n+1):
        total *= i
        logging.debug('i is %s, total is %s'%(i, total))
    
    logging.debug('Return value is %s'%(total))
    return total
print(factorial(5))

logging.debug('End of program')
