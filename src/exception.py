import sys
import logging
import logger
def error_message_detail(error,error_detail:sys)->str:
    _,_,exc_tb = error_detail.exc_info()  #exc_tb on which file which line the exception get occured 
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_num = exc_tb.tb_lineno
    error_message = "Error occured in python script name \
                    [{0}] line number [{1}] error message[{2}]".format(
                        file_name,
                        line_num,str(error)
                    )
    return error_message

class CustomeException(Exception):
    def __init__(self, error_message, error_detail:sys)->None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self)->str:
        return self.error_message



# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by zero error")
#         print(CustomeException(e,sys))


