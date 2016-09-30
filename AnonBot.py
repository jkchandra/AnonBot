
#   AnonBot | Suite of tools that facilitates anonymous collection of #
#   responses through Telegram.                                       #
#   Creative Commons (CC) 2016  Kenneth, Christopher, Chandra,        #
#   De Quan, Tai Fong                                                 #
#                                                                     #
#   This work is licensed under the Creative Commons                  #
#   Attribution-NonCommercial 4.0 International License.              #
#   To view a copy of this license, visit                             #
#   http://creativecommons.org/licenses/by-nc/4.0 or send a letter to #
#   Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.      #
#                                                                     #
#   Contact authors of work: tskennethteo@gmail.com                   #

# ▐ ░░█▓▓▓▓ ▄║║║▐▐ ░░█▓▓▓▓ ▄║║║▐▐ ░░█▓▓▓▓ ▄║║║▐▐ ░░█▓▓▓▓ ▄║║║▐▐ ░░█▓▓ #

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ #
#                                                                     #
# Structure:                                                          #
#   [X00] Import : All import statements                              #
#   [X01] Settings : Settings for the bot                             #
#   [X02] Utility Classes : User defined classes for utility purposes #
#   [X03] Modules : Classes to process each function of the bot       #
#   [X04] Handlers : Classes that handles chat for the bot            #
#   [X05] Main Method : Script to run initialisation                  #
#                                                                     #
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ #

# ███████████████████████████████████████████████████████████████████ #
#                                                                     #
# [X00] Import                                                        #
#                                                                     #
# ███████████████████████████████████████████████████████████████████ #

# Import the required native libraries for the program                #
import sys
import asyncio
import pprint
import json
import math
from datetime \
    import datetime
from operator \
    import itemgetter

# Import Python to MySQL Database connector                           #
import pymysql.cursors

# Import Mathematic and Scientific Libraries                          #
import numpy
import scipy

# Import Telegram framework for python
import telepot
from telepot.aio.delegate \
    import pave_event_space, per_chat_id, create_open
from telepot.namedtuple \
    import ReplyKeyboardMarkup, KeyboardButton

# ███████████████████████████████████████████████████████████████████ #
#                                                                     #
# [X01] Settings                                                      #
#                                                                     #
# ███████████████████████████████████████████████████████████████████ #

# Token for the bot. Available by contacting @BotFather via Telegram. #
TOKEN = '286771222:AAH2F4xqooW9BLzZM1F9d8rSDyvrWxen7JM'

# Bot Settings                                                        #

# Time in seconds before the bot terminates itself.                   #
setBotTimeout = 600

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ #
# Bot Responses to commands:                                          #
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ #

# ------------------------------------------------------------------- #
# General commands                                                    #
# ------------------------------------------------------------------- #
setReply_nocommand = 'Type /help for a list of commands to start!'
setReply_help = 'I am a friendly bot that keeps surveys annonymous! I can help you set up '     +\
                'surveys, polls and RSVP forms on telegram and allow people give responses'     +\
                'anonymously.\n\n'                                                              +\
                'Type these commands to start:\n\n'                                             +\
                '/newsession - Create a new session'
                
setReply_Cancel = 'Current operations cancelled!'

# ------------------------------------------------------------------- #
# Commands related to session creator                                 #
# ------------------------------------------------------------------- #

setReply_newsession_ItemsDisplayPrefix = 'Currently your session has the following questions '  +\
                                         'and answers:'

setReply_newsession_ItemsDisplaySuffix = '\n\nType /delete <index> to delete a question '       +\
                                         'from the session'                                     +\
                                         '\nType /cancel to cancel the session creation '       +\
                                         'process'                                              +\
                                         '\nType /next to confirm the items and move on to '    +\
                                         'session settings'                               

setReply_newsession_SessionDisplayPrefix = 'Session has been created! Check the contents:\n'

setReply_newsession_SessionDisplaySuffix = '\n\nType /done to confirm and save the session!'    +\
                                           '\n\nOr, type the following options to:\n'           +\
                                           '\n"Change Items" to change the questions and '      +\
                                           'options'                                            +\
                                           '\n"Change Type" to change the session type'         +\
                                           '\n"Change Password" to change password (Session '   +\
                                           'type must be private!) '                            +\
                                           '\n"Change Anonymity" to set session '               +\
                                           'anonymity status'                                   +\
                                           '\n"/cancel" to cancel the session creation process'      
                                       
setReply_newsession_WhenNotPrivate = 'Private message this command to AnonBot '                 +\
                                     'to create a new session!'

setReply_newsession_WhenPrivate = 'New Session Created!\n'                                      +\
                                  'Follow the the format to create questions and the options:'  +\
                                  '\nSeperate Question from Options using dash (-) and '        +\
                                  'seperate options from each other using pipe (|)'             +\
                                  '\n\nExample:\n'                                              +\
                                  'Question - Option 1|Option 2|Option 3|Option 4\n'            +\
                                  'Favourite Fruit? - Apple|Banana|Chandra|Durian'              +\
                                  setReply_newsession_ItemsDisplaySuffix
                                    
setReply_newsession_WrongCommand = 'Unrecognised Command!\n'                                    +\
                                   'Follow the the format to create questions and the options:' +\
                                   '\nSeperate Question from Options using dash (-) and '       +\
                                   'seperate options from each other using pipe (|)'            +\
                                   '\n\nExample:\n'                                             +\
                                   'Question - Option 1|Option 2|Option 3|Option 4\n'           +\
                                   'Favourite Fruit? - Apple|Banana|Chandra|Durian'         
                                    
setReply_newsession_WrongFormat = 'Invalid format!\n'                                           +\
                                   'Follow the the format to create questions and the options:' +\
                                   '\nSeperate Question from Options using dash (-) and '       +\
                                   'seperate options from each other using pipe (|)'            +\
                                   '\n\nExample:\n'                                             +\
                                   'Question - Option 1|Option 2|Option 3|Option 4\n'           +\
                                   'Favourite Fruit? - Apple|Banana|Chandra|Durian\n\n'
                         
setReply_newsession_EmptyItems = 'There are no questions in the session!'

setReply_newsession_ConfirmItems = 'Items saved!'

setReply_newsession_SessionType = 'Choose the appropriate type for your session:\n\n'           +\
                                  'Public: Anyone with the session id can respond to it\n'      +\
                                  'Private: Responders require a password to respond\n'         +\
                                  'Commercial: The session is created for commercial purposes'  +\
                                  ' (Marketing, customer feedback, etc)'

setReply_newsession_PasswordInput = 'Type in your desired password that responders will '       +\
                                    'require to access your created session\n'                  +\
                                    '(Minimum 4 Maximum 8 characters, alphanumeric characters ' +\
                                    'only!)'
                                    
setReply_newsession_PasswordError = 'Check your input!\n'                                       +\
                                    '(Minimum 4 Maximum 8 characters, alphanumeric characters ' +\
                                    'only!)'
                                    
setReply_newsession_AnonymityType = 'Does your session maintain anonymity?\n'                   +\
                                    '(Responders can see this setting!):\n\n'                   +\
                                    'Yes: You will not see the responder name or id, usually '  +\
                                    'for public sessions or sessions that deals with '          +\
                                    'sensitive topics\n'                                        +\
                                    'No: You will see the names and id of the responders\n' 

setReply_newsession_CommitMessage = 'Session has been saved!'

# ------------------------------------------------------------------- #
# Commands related to Response creator                                #
# ------------------------------------------------------------------- #

setReply_response_WhenNotPrivate = 'Private message this command and the session id to '        +\
                                   'AnonBot to respond to the session!'

setReply_response_WhenPrivate = 'Session Found! Type /proceed to continue!'

setReply_response_IDValidationError = 'Error! Either the session does not exist or your input ' +\
                                      'is invalid! Please follow the format:\n\n'               +\
                                      '"/respond <session_id>"\n'                               +\
                                      'Example: "/respond 1"' 

setReply_response_notifyPublic = 'This session is of public nature. Your identity is kept secret'
setReply_response_notifyPrivateAnon = 'This session is of private nature. Your identity is '    +\
                                      'kept secret.\n\n'                                        +\
                                      'Type in the password for the session to continue'         

setReply_response_notifyPrivateNotAnon = 'This session is of private nature. However, your '    +\
                                         'identity is NOT kept secret!\n\n'                     +\
                                         'Type in the password for the session to continue'         

setReply_response_notifyCommercial = 'This session is of commercial nature. Your identity is '  +\
                                     'kept secret'

setReply_response_WrongPassword = 'Wrong password, try again!'

setReply_response_responseDisplayPrefix = 'All questions has been answered, check your responses:\n'

setReply_response_responseDisplaySuffix = 'Type /done to confirm and save your response!'       +\
                                           '\n\nOr, type the following options to:\n'           +\
                                           '\n"/change <Question Number>" to change the answer '+\
                                           'to a particular question.'                          +\
                                           '\n"/cancel" to cancel the response creation process'

setReply_response_ChangeAnswerWrongFormat = 'Check your format! Type "/change '                 +\
                                            '<Question Number>". Example:\n\n'                  +\
                                            '/change 1 \n\n to change your answer to the first '+\
                                            'question.'

# ------------------------------------------------------------------- #
# Commands related to view creator                                    #
# ------------------------------------------------------------------- #                                            
                                            
setReply_view_IDValidationError =    'Error! Either:'                                           +\
                                      '\n  The session does not exist'                          +\
                                      '\n  Your input is invalid!'                              +\
                                      '\n  You do not have access to view the results'          +\
                                      '\n\nPlease follow the following format:\n\n'             +\
                                      '"/respond <session_id>"\n'                               +\
                                      'Example: "/respond 1" to respond to session 1'

setReply_view_WhenNotPrivate = 'Private message this command and the session id to'             +\
                               ' AnonBot to view the results for the session!'

setReply_view_WhenPrivate = 'Session Found! Type /proceed to continue!'

setReply_view_resultDisplaySuffix = 'Session Found! Type /proceed to continue!'

# SQL Settings and credentials
setSQLHost_Str = 'localhost'
setSQLUser_Str = 'root'
setSQLPassword_Str = ''
setSQLStr = 'anondb'

# ███████████████████████████████████████████████████████████████████ #
#                                                                     #
# [X02] Utility Classes                                               #
#   [X02-0] SQLDatabase:                                              #
#       Contains all the functions that commit data to MySQL Database #
#   [X02-1] MiscellaneousFunc:                                        #
#       Contains all the user defined Miscellaneous functions         # 
#                                                                     #
# ███████████████████████████████████████████████████████████████████ #

# ------------------------------------------------------------------- #
# [X02-0] SQLDatabase:                                          #
#    Contains all the functions that commit data to MySQL Database    #
# ------------------------------------------------------------------- #
class SQLDatabase(object):
    #Initialisation                                                   #
    def __init__(self):
        # Check to see if connection to MySQL database can be         #
        #   established                                               #
        self.SQLstatus_Bool = self.check_database_status()
    
    def check_database_status(self):
    
    # Function check_database_status:                                 #
    #   to check to see if connection to MySQL database can be        #
    #   established                                                   #
    #                                                                 #
    # Returns: True if online, False if offline                       #
    
        sqlStatus_Bool = True
        
        # Attempt to establish connection to the database             #
        try:
            sqlConnection_Obj = pymysql.connect(
                host=setSQLHost_Str,
                user=setSQLUser_Str,
                password=setSQLPassword_Str,
                db=setSQLStr,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
        
        # Catch error and notify MySQL database offline               #
        except Exception as e:
            sqlStatus_Bool = False
        
        else:
            sqlConnection_Obj.close()
            
        # If able to establish connection, notify MySQL is online     #      
        return sqlStatus_Bool
    
    def commit_data_to_SQL(self,tableName_Str, data_Dict, existConnection_Obj = False):
    
    # Function commit_data_to_SQL:                                    #
    #   Commit a a list of data to their columns respectively         #
    #   in the MySQL Database                                         #
    #                                                                 #
    # Parameters:                                                     #
    #   tableName_Str:                                                #
    #       Name of table in the database to store the data in        #
    #   data_Dict:                                                    #
    #       List of data to store with the keys to identify which     #
    #       column to store the data in                               #
    #       database                                                  #
    #   existConnection_Obj (Optional,default=False):                 #
    #       Existing connection to MySQL, will not be closed at the   #
    #       end if there is such a connection                         #
    #                                                                 #
    # Returns: ID of last inserted row, False if failed               #
    
        # Check if MySQL is notified to be offline                    #
        if (self.SQLstatus_Bool == False):
            return False
        
        # Initialise Variables                                        #
        sqlExecStmt_Str = "INSERT INTO `" + tableName_Str + "` ("     
        sqlExecStmtValues_Str = "VALUES ("
        sqlCommitStmt_Str = "cursor.execute(sqlExecStmt_Str, ("
        
        # Append list of column names and data to execution statement #
        for columnName_Str, data in data_Dict.items():
            sqlExecStmt_Str += "`" + columnName_Str + "`,"
            sqlExecStmtValues_Str += "%s,"
            
            if isinstance(data, list):
                data = json.dumps(data)
            
            data = str(data)
            
            sqlCommitStmt_Str += "'" + data + "',"
        
        # Get rid of the last comma created from the loop             #
        sqlExecStmt_Str = sqlExecStmt_Str[:-1] + ") "
        sqlExecStmtValues_Str = sqlExecStmtValues_Str[:-1] + ");"
        sqlExecStmt_Str += sqlExecStmtValues_Str +\
                           'SELECT LAST_INSERT_ID();'
        
        sqlCommitStmt_Str = sqlCommitStmt_Str[:-1] + "))"
        
        # Establish Connection to MySQL                               #
        if existConnection_Obj == False:
            sqlConnection_Obj = pymysql.connect(
                host=setSQLHost_Str,
                user=setSQLUser_Str,
                password=setSQLPassword_Str,
                db=setSQLStr,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
        else:
            sqlConnection_Obj = existConnection_Obj
        
        try:
            with sqlConnection_Obj.cursor() as cursor:
                exec(sqlCommitStmt_Str)
            sqlConnection_Obj.commit()
            lastID_Str = cursor.fetchone()
        
        except Exception as e:
            return False
        
        finally:
            if existConnection_Obj == False:
                sqlConnection_Obj.close()
            
        return lastID_Str
    
    def check_response_exist(self,responderID_Str,sessionID_Str, existConnection_Obj = False):
        # Check if MySQL is notified to be offline                    #
        if (self.SQLstatus_Bool == False):
            return False
            
        # Initialise Variables                                        #
        sqlExecStmt_Str = "SELECT `response_ID` FROM `chatresponses` "+\
                          "WHERE `Responder_ID` = %s  AND `Session_ID` = %s"
                          
        if existConnection_Obj == False:
            sqlConnection_Obj = pymysql.connect(
                host=setSQLHost_Str,
                user=setSQLUser_Str,
                password=setSQLPassword_Str,
                db=setSQLStr,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
        else:
            sqlConnection_Obj = existConnection_Obj
        
        try:
            with sqlConnection_Obj.cursor() as cursor:
                cursor.execute(sqlExecStmt_Str, responderID_Str,sessionID_Str)
            sqlConnection_Obj.commit()
            responseExist_Bool = cursor.fetchone()
        
        except Exception as e:
            return False
         
        finally:
            if existConnection_Obj == False:
                sqlConnection_Obj.close()
            
        if responseExist_Bool:
            return True
        else:
            return False
    
    def update_response_to_SQL(self, responseContent_List,responderID_Str, sessionID_Str, existConnection_Obj = False):
        # Check if MySQL is notified to be offline                    #
        if (self.SQLstatus_Bool == False):
            return False
            
        # Initialise Variables                                        #
        sqlExecStmt_Str = "UPDATE `CHATRESPONSES` SET "         +\
                          "`Response_Content` = %s WHERE "      +\
                          "`Responder_ID` = %s AND "            +\
                          "`Session_ID = %s"
        
        responseContent_Str = json.dumps(responseContent_List)
        
        if existConnection_Obj == False:
            sqlConnection_Obj = pymysql.connect(
                host=setSQLHost_Str,
                user=setSQLUser_Str,
                password=setSQLPassword_Str,
                db=setSQLStr,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
        else:
            sqlConnection_Obj = existConnection_Obj

        try:
            with sqlConnection_Obj.cursor() as cursor:
                cursor.execute(sqlExecStmt_Str, responseContent_Str, responderID_Str, sessionID_Str)
            sqlConnection_Obj.commit()

        except Exception as e:
            return False
        
        finally:
            if existConnection_Obj == False:
                sqlConnection_Obj.close()
            
    
    def fetch_data_from_SQL(self,tableName_Str, columnName_Str, identifier_Str, existConnection_Obj = False):
    
    # Function fetch_data_from_SQL:                                   #
    #   Fetch data from the database based on specification           #
    #                                                                 #
    # Parameters:                                                     #
    #   tableName_Str:                                                #
    #       Name of table in the database to fetch the data from      #
    #   columnName_Str:                                               #
    #       Name of column in the table to delete the data from       #
    #   identifier_Str:                                               #
    #       ID to identify which data to fetch                        #
    #   existConnection_Obj (Optional,default=False):                 #
    #       Existing connection to MySQL, will not be closed at the   #
    #       end if there is such a connection                         #
    #                                                                 #
    # Returns: True if succeeded, False if failed                     #
    
        # Check if MySQL is notified to be offline                    #
        if (self.SQLstatus_Bool == False):
            return False    

        sqlExecStmt_Str = "SELECT * FROM `" + tableName_Str     +\
                          "` WHERE `" + columnName_Str          +\
                          "` = %s ;"

        # Establish Connection to MySQL                               #
        if existConnection_Obj == False:
            sqlConnection_Obj = pymysql.connect(
                host=setSQLHost_Str,
                user=setSQLUser_Str,
                password=setSQLPassword_Str,
                db=setSQLStr,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
        else:
            sqlConnection_Obj = existConnection_Obj

        try:
            with sqlConnection_Obj.cursor() as cursor:
                cursor.execute(sqlExecStmt_Str, identifier_Str)
            sqlConnection_Obj.commit()
            sqlResult_Dict = cursor.fetchone()

        except Exception as e:
            return False
        
        finally:
            if existConnection_Obj == False:
                sqlConnection_Obj.close()
                
        return sqlResult_Dict
    
    def fetch_multiple_data_from_SQL(self,tableName_Str, columnName_Str, identifier_Str, existConnection_Obj = False):

    # Function fetch_result_from_SQL:                                 #
    #   Fetch multiple data from the database based on specification  #
    #                                                                 #
    # Parameters:                                                     #
    #   tableName_Str:                                                #
    #       Name of table in the database to fetch the data from      #
    #   columnName_Str:                                               #
    #       Name of column in the table to delete the data from       #
    #   identifier_Str:                                               #
    #       ID to identify which data to fetch                        #
    #   existConnection_Obj (Optional,default=False):                 #
    #       Existing connection to MySQL, will not be closed at the   #
    #       end if there is such a connection                         #
    #                                                                 #
    # Returns: True if succeeded, False if failed                     #
        
        if (self.SQLstatus_Bool == False):
            return False    

        sqlExecStmt_Str = "SELECT * FROM `" + tableName_Str     +\
                          "` WHERE `" + columnName_Str          +\
                          "` = %s ;"
        
        sqlResults_List = []
        
        # Establish Connection to MySQL                               #
        if existConnection_Obj == False:
            sqlConnection_Obj = pymysql.connect(
                host=setSQLHost_Str,
                user=setSQLUser_Str,
                password=setSQLPassword_Str,
                db=setSQLStr,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
        else:
            sqlConnection_Obj = existConnection_Obj
        
        try:
            with sqlConnection_Obj.cursor() as cursor:
                cursor.execute(sqlExecStmt_Str, identifier_Str)
                sqlConnection_Obj.commit()
                
                # Fetch data while there is more data to be fetched   # 
                while(True):
                    sqlResult_Dict = cursor.fetchone()
                    
                    # If no more data, break out of the fetch loop    # 
                    if not sqlResult_Dict:
                        break;
                    else:
                        sqlResults_List.append(sqlResult_Dict)
        
        except Exception as e:
            return false
        
        finally:
            if existConnection_Obj == False:
                sqlConnection_Obj.close()
        
        return sqlResults_List
    
    
    def delete_data(self,tableName_Str, columnName_Str, identifier_Str, existConnection_Obj = False):
    
    # Function delete_data:                                           #
    #   Delete data from the database based on specification          #
    #                                                                 #
    # Parameters:                                                     #
    #   tableName_Str:                                                #
    #       Name of table in the database to delete the data from     #
    #   columnName_Str:                                               #
    #       Name of column in the table to delete the data from       #
    #   identifier_Str:                                               #
    #       ID to identify which data to delete                       #
    #   existConnection_Obj (Optional,default=False):                 #
    #       Existing connection to MySQL, will not be closed at the   #
    #       end if there is such a connection                         #
    #                                                                 #
    # Returns: True if succeeded, False if failed                     #
    
        # Check if MySQL is notified to be offline                    #
        if (self.SQLstatus_Bool == False):
            return False    
        
        sqlExecStmt_Str = "DELETE FROM `" + tableName_Str + "` WHERE `" + columnName_Str +\
                          "` = %s ;"
                          
        # Establish Connection to MySQL                               #
        if existConnection_Obj == False:
            sqlConnection_Obj = pymysql.connect(
                host=setSQLHost_Str,
                user=setSQLUser_Str,
                password=setSQLPassword_Str,
                db=setSQLStr,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
        else:
            sqlConnection_Obj = existConnection_Obj
        
        try:
            with sqlConnection_Obj.cursor() as cursor:
                cursor.execute(sqlExecStmt_Str, identifier_Str)
            
            sqlConnection_Obj.commit()
        except Exception as e:
            return False
            
        finally:
            if existConnection_Obj == False:
                sqlConnection_Obj.close()

# ███████████████████████████████████████████████████████████████████ #
#                                                                     #
# [X03] Modules                                                       #
#   [X03-0] SessionModule:                                            #
#       Module that handles creation of new sessions                  # 
#                                                                     #
# ███████████████████████████████████████████████████████████████████ #

class SessionModule(object):
    # --------------------------------------------------------------- #
    # [X03-0] SessionModule:                                          #
    #    Module that handles creation of new sessions                 # 
    # --------------------------------------------------------------- #
    def __init__(self):
        self.session_List = []
        self.session_Dict = {}
        self.sessionCreationStage = 0    
    
    def validate_input_line(self,inputLine_Str):
    
    # Function validate_input_line:                                   #
    #   Validate if input line is in the correct format to be         #
    #     translated into an item in the session                      #
    #                                                                 #
    # Parameters:                                                     #
    #   inputLine_Str:                                                #
    #       The string to validate                                    #
    #                                                                 #
    # Returns: True if format is correct, False if format is wrong    #
    
        # String can only have one '-' to seperate question from      #
        #  options and cannot start or end with '-'                   #
        if inputLine_Str.count('-') != 1     \
            or inputLine_Str.startswith('-') \
            or inputLine_Str.endswith('-'):
            return False

        else:
            inputs_List = inputLine_Str.split('-')
            question_Str = inputs_List[0]
            
            # Question cannot have '|' in it                          #
            if "|" in question_Str:
                return False
            
            options_Str = inputs_List[1].strip()
            
            # Options cannot start or end with '|'                    #
            #   nor can have 2 consecutive '|'                        #
            if '||' in options_Str              \
                or options_Str.startswith('|')  \
                or options_Str.endswith('|'):
                
                return False

            else:
                return True

    def validate_deletion(self,messageInput_List):
    
    # Function validate_deletion:                                     #
    #   Validate if message is in the correct format to delete one or #
    #   more items from the current session                           #
    #                                                                 #
    # Parameters:                                                     #
    #   messageInput_List:                                            #
    #       The input, in the integrity of the original 'message'     #
    #       structure                                                 #
    #                                                                 #
    # Returns:                                                        #
    #   List of Valid Identifiers                                     #
    #   List of Invalid Identifiers                                   #
    #   Error Flag, if any                                            #
    #     True if no numbers are valid                                # 
    #     False if all numbers or some numbers are valid              #
        
        # Initialise the variables                                    #
        deletionLine_Str = messageInput_List['text'].strip()
        deletions_List = deletionLine_Str.split(' ')
        
        validDeletions = []
        invalidDeletions = []
        deletionErrorFlag = True
        
        # If no arguments are specified, return error message         #
        if len(deletions_List) <= 1:
            deletionResults_Dict = {'validDeletions':validDeletions,    \
                                    'invalidDeletions':invalidDeletions,\
                                    'errorFlag':deletionErrorFlag}
            invalidDeletions.append('(Empty String)')
            return deletionResults_Dict
            
        for listCounter_Int in range(1,len(deletions_List)):
            itemIndex = deletions_List[listCounter_Int]
            
            if not itemIndex.isdigit():
                invalidDeletions.append(itemIndex)
                continue
            
            if 0 < int(itemIndex) <= len(self.session_List)                \
            and itemIndex not in validDeletions:
                validDeletions.append(itemIndex)
                deletionErrorFlag = False
                
            else:
                invalidDeletions.append(itemIndex)
        
        deletionResults_Dict = {'validDeletions':validDeletions,      \
                                'invalidDeletions':invalidDeletions,  \
                                'errorFlag':deletionErrorFlag}
        
        return deletionResults_Dict
                
    def validate_creation(self,messageInput_List):
    
    # Function validate_creation:                                     #
    #   Validate if items can be appended to the session              #
    #                                                                 #
    # Parameters:                                                     #
    #   messageInput_List:                                            #
    #       The input, in the integrity of the original 'message'     #
    #         structure                                               #
    #                                                                 #
    # Returns: A dictionary that contains -                           #
    #   an error flag                                                 #
    #   any error message                                             #
    #   and a list that consist of valid items (question and options) #
    
        # Initialise Variables                                        #
        itemLineCounter_Int = 0
        itemCreationErrorMsg_Str = ""
        itemCreationErrorFlag_Bool = False
        
        itemContent_List = []
        inputContent_Str = messageInput_List['text']
        
        # Check if there is atleast '-' and '|' in the input content  #
        if ('-' not in inputContent_Str or '|' not in inputContent_Str):
            itemCreationErrorMsg_Str = setReply_newsession_WrongFormat
            itemCreationErrorFlag_Bool = True
            
            # Construct results to return prematurely
            itemCreationResult = {'itemsArray':itemContent_List, \
                                'errorFlag':itemCreationErrorFlag_Bool, \
                                'errorMessage':itemCreationErrorMsg_Str} \
            
            return itemCreationResult
            
        else:
            itemCreationErrorMsg_Str = "No Error!"
            inputContent_List = inputContent_Str.split('\n')
            
            # Loop through every line in the input content
            for inputLine_Str in inputContent_List:
                inputLine_Str = inputLine_Str.strip()
                itemLineCounter_Int += 1        
                
                # If input is invalid, append error source to error   #
                #  message                                            #
                if self.validate_input_line(inputLine_Str) == False:
                    
                    # If this is the first error, append heading first#
                    #   to error message                              #
                    if itemCreationErrorFlag_Bool == False:
                        itemCreationErrorFlag_Bool = True
                        itemCreationErrorMsg_Str = '\n\nYou have error with format at:'
                    
                    itemCreationErrorMsg_Str += '\nLine ' + str(itemLineCounter_Int) +\
                                                ': '  + inputLine_Str
                    continue
                    
                else:
                    # Split item into the question and options and    #
                    # Strip both parts of redundant white spaces      #
                    inputItem_List = inputLine_Str.split('-')
                    inputQuestion = inputItem_List[0].strip()
                    
                    inputOptions_List = inputItem_List[1].split('|')
                    
                    for option_Str in inputOptions_List:
                        option_Str = option_Str.strip()      
                    
                    # Append the cleaned items to a list
                    itemContent_List.append([inputQuestion,inputOptions_List])
            
            # Construct results to return
            itemCreationResult = {'itemsArray':itemContent_List, \
                                'errorFlag':itemCreationErrorFlag_Bool, \
                                'errorMessage':itemCreationErrorMsg_Str} \
            
            return itemCreationResult

    def append_items(self,item_List):
    
    # Function append_item:                                           #
    #   Appends a list of items to the session                        #
    #                                                                 #
    # Parameters:                                                     #
    #   item_List:                                                    #
    #       List of items to append                                   #
    #                                                                 #
    # Returns: True if successfully appended the item, False if       #
    #          one or more of the item is not successfully appended   #
    
        errorFlag_Bool = True
        # Loop through items in the item list                         #
        for item in item_List:
            # Attempt to append                                       #
            try:
                self.session_List.append(item)
                
            # Return False if unable to append                        #
            except (KeyError,ValueError) as e:
                errorFlag_Bool = False
                continue
                
        return errorFlag_Bool
    
    def remove_item(self,itemIdentifier_Int):
    
    # Function remove_item:                                           #
    #   Remove an item from the session item list                     #
    #                                                                 #
    # Parameters:                                                     #
    #   itemIdentifier_Int:                                           #
    #       Identifies which item to remove using index of            #
    #          item in the session                                    #
    #                                                                 #
    # Returns: True if successfully removed the item                  #
        
        # Attempt to remove item
        try:
            del self.session_List[itemIdentifier_Int-1]
        
        # Return False if unable to remove
        except Exception as e:
            return False
        
        else:
            return True
    
    def translate_items_to_text(self):

    # Function translate_items_to_text:                               #
    #   Translate items in the session and its contents to text so as #
    #     to show the user                                            #
    #                                                                 #
    # Returns: a formatted string that shows the contents of          #
    #          the session                                            #

    # Initialise Variables                                        #
        translatedItems_Str = ''
        itemCounter_Int = 0
        
        # Return if session is empty
        if not self.session_List:
            translatedItems_Str += '\n\nEmpty!'
            return translatedItems_Str
            
        # Loop through each item in the session                       #
        for items_List in self.session_List:
            itemCounter_Int += 1
            translatedItems_Str += '\n\nQ' + str(itemCounter_Int) +\
                                     ' ' + items_List[0] + ':'
            optionCounter_Int = 1
            
            # Loop through each option in the item                    #
            for sessionCreatedOption in items_List[1]:
                translatedItems_Str += '\n' + str(optionCounter_Int) +\
                                         ' :' + sessionCreatedOption
                optionCounter_Int += 1
            translatedItems_Str += ""

        return translatedItems_Str

    
    
    def translate_session_to_text(self):
    
    # Function translate_session_to_text:                             #
    #   Translate the current session and its contents to text so as  #
    #     to show the user                                            #
    #                                                                 #
    # Returns: a formatted string that shows the contents of          #
    #          the session                                            #
    
        translatedSession_Str = 'Session Type: ' + self.session_Dict['Session_Type']            +\
                                '\nPassword: ' + self.session_Dict['Password']                  +\
                                '\nAnonymity: ' + self.session_Dict['Anonymity_Type']           +\
                                '\nNumber of Questions: '                                       +\
                                str(self.session_Dict['Number_Of_Questions'])                   +\
                                '\nCreator: ' + self.session_Dict['Creator_User_Name']          +\
                                self.translate_items_to_text()
       
        return translatedSession_Str


    def clear_session(self):
    # Function clear_session:                                         #
    #   Clear the contents of the session, usually after when session #
    #   creation process is cancelled or completed                    #
    
        self.session_List =[]
        self.session_Dict ={}

class ResponseModule(object):
    # --------------------------------------------------------------- #
    # [X03-0] ResponseModule:                                         #
    #    Module that handles process of responding to a session       # 
    # --------------------------------------------------------------- #
    def __init__(self):
        self.response_List = []
        self.response_Dict = {}
        self.responseCounter_Int = 0
        
        self.session_Dict = {}
        self.session_List = []
        
        self.translatedSession_List = []
        self.SQL_Obj = SQLDatabase()
        self.responseCreationStage = 0

    def validate_session_id(self,messageInput_List):
    
    # Function validate_session_id:                                   #
    #   Check if input is valid and if the session exists             #
    #                                                                 #
    # Parameters:                                                     #
    #   messageInput_List:                                            #
    #       The input, in the integrity of the original 'message'     #
    #       structure                                                 #
    #                                                                 #
    # Returns: True if session exists,                                #
    #           False if session doesn't exist                        #
    #                 or if input is invalid                          #
    #                                                                 #
    # Additionally, if session exists, its contents are stored in     #
    # this object.                                                    #
    
        # Clean the input                                             #
        inputContent_Str = messageInput_List['text']
        inputContent_Str = inputContent_Str.strip()
        inputContent_List = inputContent_Str.split(' ')
        
        # Check if there are 2 components only                        #
        if 1 < len(inputContent_List) <= 2:
            # Seperate the input into their respective components     #
            inputCommand_Str = inputContent_List[0]
            sessionID_Str = inputContent_List[1]

            if inputCommand_Str == '/respond' and sessionID_Str.isdigit():    
                # If input is valid, attempt to find the session      #
                # in the database                                     #
                result_Dict = self.SQL_Obj.fetch_data_from_SQL(       \
                    'SESSIONSLIST',                                   \
                    'Session_ID',                                     \
                    sessionID_Str)                                    \

                # If session can be found, store the contents         #
                # and return True                                     #
                if result_Dict:
                    self.session_Dict = result_Dict
                    self.session_List = json.loads(self.session_Dict['Session_Content'])
                    return True

            else:
                return False
        else:
            return False
    
    def translate_session_item(self):
    
    # Function translate_session_item:                                #
    #   Check if message is valid and if the session exists           #
    #                                                                 #
    # Parameters:                                                     #
    # Returns: True if successfully translated, False if not          #
    
        # Initialise Variables                                        #
        itemOptions_List = []
        itemOptionsButtons_List = []
        itemOptionsButtonsWrapper_List = []
        itemOptionsKeyboard = ''
        
        itemCounter_Int = 0
        
        # Loop through each item in session list                      #
        for sessionItems_List in self.session_List:

            itemText_Str = ''
            optionCounter_Int = 1
            
            itemOptionsButtons_List = []
            itemOptionsButtonsWrapper_List = []
            itemResult_Dict = {}
            
            itemCounter_Int += 1

            itemQuestion_Str = sessionItems_List[0]
            itemOptions_List = sessionItems_List[1]
            
            itemText_Str += 'Question '             +\
                str(itemCounter_Int)       +\
                ':\n' + itemQuestion_Str + '\n'
            
            # Split the number of options evenly across the rows      #
            optionSplitter_Int = 0
            itemNumberOfOptions_Int = len(itemOptions_List)
            if itemNumberOfOptions_Int >= 4:
                optionsPerRow = math.ceil(itemNumberOfOptions_Int/2)
            else:
                optionsPerRow = False
                
            # Create keyboard buttons for each of the option          #
            for option_Str in itemOptions_List:
                
                itemText_Str += '\n' + str(optionCounter_Int) + '- ' + option_Str.strip()
                itemOptionsButtons_List.append( \
                    KeyboardButton(text=str(optionCounter_Int) + '- ' + option_Str.strip()))
                optionCounter_Int += 1
                optionSplitter_Int += 1
                
                # If the number of options in the current row reaches #
                # threshold, form new row for the next options        #   
                if optionsPerRow and optionSplitter_Int == optionsPerRow:
                    itemOptionsButtonsWrapper_List.append(itemOptionsButtons_List)
                    optionSplitter_Int = 0
                    itemOptionsButtons_List = []
            
            # If there is only one row of optionsPerRow               #
            if not optionsPerRow or optionSplitter_Int != 0:
                itemOptionsButtonsWrapper_List.append(itemOptionsButtons_List)
            
            # Append all buttons onto a keyboard to display to user   #
            itemOptionsKeyboard = ReplyKeyboardMarkup(keyboard=itemOptionsButtonsWrapper_List, \
                                                        one_time_keyboard = True,              \
                                                        resize_keyboard = True)
            
            # Store the translated item (display text and keyboard)   #
            # in a dictionary object                                  #
            itemResult_Dict['text'] = itemText_Str + '\n\n'
            itemResult_Dict['keyboard'] = itemOptionsKeyboard
            
            # Store the translated item
            self.translatedSession_List.append(itemResult_Dict)
    
    def translate_responses(self):
    
    # Function translate_responses:                                   #
    #   Translates the users responses and display it into a          #
    #   formatted text                                                #
    #                                                                 #
    # Returns: The translated responses if successfully translated    # 
    #          False if not                                           #
    
        translatedText_Str = ''
        translatedText_Str += setReply_response_responseDisplayPrefix
        
        iterationCounter_Int = 0
        
        for answerIdentifier_Str in self.response_List:
            sessionItem_List = self.session_List[iterationCounter_Int]
            sessionQuestion_Str = sessionItem_List[0]
            sessionOptions_List = sessionItem_List[1]
            translatedText_Str += 'Question ' + str(iterationCounter_Int+1)         +\
                                  ': '                                              +\
                                  sessionQuestion_Str + '\n'                        +\
                                  sessionOptions_List[int(answerIdentifier_Str)-1]  +\
                                  '\n\n'
            
            iterationCounter_Int += 1
                                  
        translatedText_Str += setReply_response_responseDisplaySuffix
        
        return translatedText_Str
        
    
    def validate_change_line(self,messageInput_List):
    
    # Function validate_change_line:                                  #
    #   Check if input is valid and if such a question exist          #
    #                                                                 #
    # Parameters:                                                     #
    #   messageInput_List:                                            #
    #       The input, in the integrity of the original 'message'     #
    #       structure                                                 #
    #                                                                 #
    # Returns: The question identifier if question exists,            #
    #           False if question doesn't exist                       #
    #                 or if input is invalid                          #
    #                                                                 #
    
        changeAnswerLine_Str = messageInput_List['text'].strip()
        changeAnswer_List = changeAnswerLine_Str.split(' ')
        if 1 < len(changeAnswer_List) <= 2:
            commandToChange_Str = changeAnswer_List[0]
            questionToChange_Str = changeAnswer_List[1]
            
            if commandToChange_Str == '/change'                       \
                and questionToChange_Str.isdigit()                    \
                and int(questionToChange_Str) <= len(self.response_List):
                
                return questionToChange_Str
            
            else:
                return False
        else:
            return False
        
    
    def validate_response(self,messageInput_List,questionNumber_Int):
    
    # Function validate_response:                                     #
    #   Check if input is valid and if such a question exist          #
    #                                                                 #
    # Parameters:                                                     #
    #   messageInput_List:                                            #
    #       The input, in the integrity of the original 'message'     #
    #       structure                                                 #
    #   questionNumber_Int:                                           #
    #       The identifier that identifies the question that the      #
    #       response is answering                                     #
    #                                                                 #
    # Returns: True if the question exist,                            #
    #           False if question doesn't exist                       #
    #                 or if input is invalid                          #
    #                                                                 #
    # Additionally, append the response to the response list if True  #

        inputContent_Str = messageInput_List['text'].strip()
        inputContent_List = inputContent_Str.split('-')
        
        item_List = self.session_List[questionNumber_Int]
        maxOptions_Int = len(item_List[1])
        
        if 1 <= len(inputContent_List) <= 2:
            answerIdentifier_Str = inputContent_List[0].strip()
            if answerIdentifier_Str.isdigit() and (int(answerIdentifier_Str) <= maxOptions_Int):
                if questionNumber_Int < len(self.response_List):
                    self.response_List[questionNumber_Int] = answerIdentifier_Str
                else:
                    self.response_List.append(answerIdentifier_Str)
                
                return True
            else:
                return False
        else:
            return False
    
    def clear_responses(self):
    
    # Function clear_response:                                        #
    #   Clear the contents of the response, usually after when        #
    #   response creation process is cancelled or completed           #
    
        self.response_List =[]
        self.response_Dict ={}
        self.translatedSession_List = []
        
        self.session_Dict = {}
        self.session_List = []

class ViewModule(object):
    def __init__(self):
        self.SQL_Obj = SQLDatabase()
        self.session_Dict = {}
        self.session_List = []
        
        self.result_List = []
        self.tabulatedResults_List = []
        self.translatedResult_Str = ''
    
    def validate_session_id(self,messageInput_List):

    # Function validate_session_id:                                   #
    #   Checks if message is valid and if the session exists.         #
    #   Also checks if user is a creator and only allow access if     #
    #   he/she is                                                     #
    #                                                                 #
    # Parameters:                                                     #
    #   messageInput_List:                                            #
    #       The input, in the integrity of the original 'message'     #
    #       structure                                                 #
    #                                                                 #
    # Returns: True if session exists and user is the creator,        #
    #           False if session doesn't exist                        #
    #                 or if validation failed                         #
    #                 or if input is invalid                          #
    #                 or if user is not creator                       #
    #                                                                 #
    # Additionally, if session exists, its contents are stored in     #
    # this object.                                                    #

        # Clean the input                                             #
        inputCreator_Str = str(messageInput_List['from']['id']).strip()
        inputContent_Str = messageInput_List['text'].strip()
        inputContent_List = inputContent_Str.split(' ')
        
        # Check if there are 2 components only                        #
        if 1 < len(inputContent_List) <= 2:
            # Seperate the input into their respective components     #
            inputCommand_Str = inputContent_List[0]
            sessionID_Str = inputContent_List[1]
            
            if inputCommand_Str == '/view' and sessionID_Str.isdigit():    
                # If input is valid, attempt to find the session      #
                # in the database                                     #
                result_Dict = self.SQL_Obj.fetch_data_from_SQL(       \
                    'SESSIONSLIST',                                   \
                    'Session_ID',                                     \
                    sessionID_Str)                                    \
                
                # If the session exist, store the session into        #
                # the object only if the user is the creator          #
                if result_Dict                                        \
                and str(result_Dict['Creator_ID']) == inputCreator_Str:
                    self.session_Dict = result_Dict
                    self.session_List = json.loads(result_Dict['Session_Content'])
                    
                    sessionID_Str = self.session_Dict['Session_ID']
                    self.result_List = self.SQL_Obj.fetch_multiple_data_from_SQL('CHATRESPONSES', 'Session_ID', sessionID_Str)
                    return True

            else:
                return False
        else:
            return False
    
    def tabulate_results(self):
    
        self.tabulatedResults_List = []
        
        # Create the empty list first                                 #
        for itemContent_List in self.session_List:
            itemOptions_List = itemContent_List[1]
            optionScores_List = []
            for option_Str in itemOptions_List:
                optionScores_List.append(0)
            self.tabulatedResults_List.append(optionScores_List)
            
        for responses_Dict in  self.result_List:
            responses_List = json.loads(responses_Dict['Response_Content'])
            questionCounter_Int = 0
            for response_Str in responses_List:
                self.tabulatedResults_List[questionCounter_Int][int(response_Str)-1] += 1
                questionCounter_Int += 1
        
        print(self.tabulatedResults_List)
    
    def translate_result_to_text(self):

    # Function translate_result_to_text:                              #
    #   Obtain and translate the results of the session to text       #
    #                                                                 #
    # Returns: Formatted results in the form of text                  #

        itemCounter_Int = 0
        sessionID_Str = str(self.session_Dict['Session_ID'])
        
        totalResponses_Int = sum(self.tabulatedResults_List[0])
        self.translatedResult_Str = 'The results for session ' + sessionID_Str + ':\n' +\
                                    '(Total Responses: ' + str(totalResponses_Int) + ')\n\n'
        for itemContent_List in self.session_List:
            itemQuestion_Str = itemContent_List[0]
            itemOptions_List = itemContent_List[1]
            
            self.translatedResult_Str += 'Question ' + str((itemCounter_Int +1)) + ' - \n'+\
                                         itemQuestion_Str + '\n'
            
            itemOptionCounter_Int = 0

            for itemOption_Str in itemOptions_List:
                responseScore_Int = self.tabulatedResults_List[itemCounter_Int][itemOptionCounter_Int]
                percentageCount_Float = round(((responseScore_Int / totalResponses_Int) * 100))
                percentageIllustration_Int = int(math.floor(percentageCount_Float/10))
                self.translatedResult_Str += str((itemOptionCounter_Int + 1 )) + ' - ' + itemOption_Str +\
                                              '\n' + str(responseScore_Int) + ' (' + str(percentageCount_Float) + '%)'
                
                self.translatedResult_Str += '\n\n'
                    
                    
                itemOptionCounter_Int += 1
            self.translatedResult_Str += '\n'    
            itemCounter_Int += 1
            
        return self.translatedResult_Str
            
    def scan_message(self,messageInput_List):
    
    # Function scan_message:                                          #
    #   Summarise the message                                         #
    #                                                                 #
    # Parameters:                                                     #
    #   messageInput_List:                                            #
    #       The input, in the integrity of the original 'message'     #
    #       structure                                                 #
    #                                                                 #
    # Returns: The summarised message in the form of a list,          #
    #           False if session doesn't exist                        #
    #                 or if validation failed                         #
    #                 or if input is invalid                          #
    #                 or if user is not creator                       #
    #                                                                 #
    
        messageOutline_Dict = {}
        inputContent_Str = messageInput_List['text']

        contentType_Str, chatType_Str, chatId_Str = telepot.glance(messageInput_List)
        
        # Store                                                       #
        messageOutline_Dict['contentType'] = contentType_Str
        messageOutline_Dict['chatType'] = chatType_Str
        messageOutline_Dict['chatId'] = chatId_Str

        # Check if the input is a command                             #
        try:
            commandCheck = messageInput_List['entities']
        except KeyError:
            pass

        else:
            # Check if there is more than 1 command                   #
            if inputContent_Str.count('/') > 1:
                pass
            else:
                messageOutline_Dict['contentType'] = 'command'

        return messageOutline_Dict
        
    def clear_view(self):
    
    # Function clear_view:                                            #
    #   Clear the contents of the view, usually after when            #
    #   response creation process is cancelled or completed           #
    
        self.session_Dict = {}
        self.session_List = []
        
        self.result_List = []
        self.translatedResult_Str = ''
        self.tabulatedResults_List = []

# ███████████████████████████████████████████████████████████████████ #
#                                                                     #
# [X04] Handlers                                                      #
#   [X04-0] Chat Handler:                                             #
#       Class that handles reading replies and sending messages       #
#                                                                     #
# ███████████████████████████████████████████████████████████████████ #
        
class anonChatHandler(telepot.aio.helper.ChatHandler):
    # --------------------------------------------------------------- #
    # [X04-0] Chat Handler:                                           #
    #    Class that handles reading replies and sending messages      # 
    # --------------------------------------------------------------- #
    def __init__(self, *args, **kwargs):
        super(anonChatHandler, self).__init__(*args, **kwargs)

        self.chatMode_Str = 'chat'
        self.stageCounter_Int = 0
        self.sessionEditMode = False
        self.responseEditMode = False
        
        self.session_Obj = SessionModule()
        self.response_Obj = ResponseModule()
        self.view_Obj = ViewModule()
        
        self.questionCounter = 0
        self.SQL_Obj = SQLDatabase()
        
        
        
        self.sessionTypeKeyboard =  ReplyKeyboardMarkup(                            \
                                        keyboard=[                                  \
                                            [KeyboardButton(text="Public"),         \
                                            KeyboardButton(text="Private")],        \
                                            [KeyboardButton(text="Commercial"),     \
                                            KeyboardButton(text="/cancel")]         \
                                        ],                                          \
                                        one_time_keyboard = True,                   \
                                        resize_keyboard = True                      \
                                    )                                               \
                                    
        self.anonymityTypeKeyboard =  ReplyKeyboardMarkup(                          \
                                        keyboard=[                                  \
                                            [KeyboardButton(text="Yes"),            \
                                            KeyboardButton(text="No"),              \
                                            KeyboardButton(text="/cancel")]         \
                                        ],                                          \
                                        one_time_keyboard = True,                   \
                                        resize_keyboard = True                      \
                                    )                                               \
                                    
        self.confirmationEditKeyBoard =  ReplyKeyboardMarkup(                       \
                                        keyboard=[                                  \
                                            [KeyboardButton(text="Change Items"),   \
                                            KeyboardButton(text="Change Type"),     \
                                            KeyboardButton(text="Change Password")],\
                                            [KeyboardButton(text="Change Anonymity"),\
                                            KeyboardButton(text="/done"),           \
                                            KeyboardButton(text="/cancel")]         \
                                        ],                                          \
                                        one_time_keyboard = True,                   \
                                        resize_keyboard = True                      \
                                    )                                               \
        
    async def on_edited_chat_message(self, messageInput_List):    
        pass
           
    async def on_chat_message(self, messageInput_List):
        
        #  -----------------------------------------------------------------------  #
        #   The main thread called when the user sends a message to the bot         #
        #   The if/else below filters the message accordingly to the stage the      #
        #   user is currently in.                                                   #
        #                                                                           #
        #   The user starts off the creation process with the /newsession command,  #
        #   or calling the /help command to get instructions on how to operate the  #
        #   bot. Otherwise the bot will be in 'chat' mode, which will not receive   #
        #   any other commands aside from /help, /newsession or /cancel             #
        #                                                                           #
        #   The bot operates on several modes which help filter the message to the  #
        #   correct mode for processing                                             #
        #  -----------------------------------------------------------------------  #
        
        #   Retrieve the input from user and save it into variables for future use  #
        messageOutline_Dict = self.view_Obj.scan_message(messageInput_List)
        
        inputContent_Str = messageInput_List['text']
        chatId_Str = messageInput_List['chat']['id']
        
        if inputContent_Str == '/cancel'or inputContent_Str == '/cancel@A_NonBot':
            self.chatMode_Str = 'chat'
            self.session_Obj.clear_session()
            self.response_Obj.clear_responses()
            self.stageCounter_Int = 0
            
            self.sessionEditMode = False
            self.responseEditMode = False
            
            self.questionCounter = 0
            
            await self.sender.sendMessage(setReply_Cancel)
            return

        if self.chatMode_Str == 'chat' :
            if messageOutline_Dict['contentType'] != 'command':
                await self.sender.sendMessage(setReply_nocommand)
                return
            
            if inputContent_Str == '/help' or inputContent_Str == '/help@A_NonBot':
                await self.sender.sendMessage(setReply_help)
                self.stageCounter_Int = 0

            elif inputContent_Str == '/newsession' or inputContent_Str == '/newsession@A_NonBot':
                if (messageOutline_Dict['chatType'] != 'private'):
                    await self.sender.sendMessage(setReply_newsession_WhenNotPrivate)
                else:
                    await self.sender.sendMessage(setReply_newsession_WhenPrivate)
                    self.session_Obj.clear_session()
                    self.chatMode_Str = 'create'
                    self.stageCounter_Int = 1

            elif inputContent_Str.startswith('/respond'):
                if (messageOutline_Dict['chatType'] != 'private'):
                    await self.sender.sendMessage(setReply_response_WhenNotPrivate)
                else:
                    validationResult_Str = self.response_Obj.validate_session_id(messageInput_List)

                    if validationResult_Str:
                        await self.sender.sendMessage(setReply_response_WhenPrivate)
                        self.chatMode_Str = 'respond'
                        self.stageCounter_Int = 1

                    else:
                        await self.sender.sendMessage(setReply_response_IDValidationError)
                        
            elif inputContent_Str.startswith('/view'):
                if (messageOutline_Dict['chatType'] != 'private'):
                    await self.sender.sendMessage(setReply_view_WhenNotPrivate)
                else:
                    validationResult_Str = self.view_Obj.validate_session_id(messageInput_List)

                    if validationResult_Str:
                        await self.sender.sendMessage(setReply_view_WhenPrivate)
                        self.chatMode_Str = 'view'
                        self.stageCounter_Int = 1

                    else:
                        await self.sender.sendMessage(setReply_view_IDValidationError)
                        
            else:
                await self.sender.sendMessage(setReply_nocommand)
                return
        # CREATION CREATION CREATION CREATION CREATION CREATION CREAT #
        elif self.chatMode_Str == 'create' :
            if self.stageCounter_Int == 1:
                if messageOutline_Dict['contentType'] == 'command':
                    if inputContent_Str.startswith('/delete'):
                        deletionItems_List = self.session_Obj.validate_deletion( \
                            messageInput_List)
                        
                        if deletionItems_List['validDeletions']:
                            for itemIdentifier_Str in deletionItems_List['validDeletions']:
                                self.session_Obj.remove_item(int(itemIdentifier_Str))
                            
                        if deletionItems_List['invalidDeletions']:
                            errorMsg_Str = 'The following inputs are not valid:'
                            for itemIdentifier_Str in deletionItems_List['invalidDeletions']:
                                errorMsg_Str += ' ' + itemIdentifier_Str
                            await self.sender.sendMessage(errorMsg_Str)
                        else:
                            await self.sender.sendMessage('Questions successfuly deleted!')
                            
                        translatedItems_Str = setReply_newsession_ItemsDisplayPrefix +\
                                            self.session_Obj.translate_items_to_text() +\
                                            setReply_newsession_ItemsDisplaySuffix
                        
                        await self.sender.sendMessage(translatedItems_Str)                    
                                
                    elif inputContent_Str == '/next':
                        if not self.session_Obj.session_List:
                            await self.sender.sendMessage(setReply_newsession_EmptyItems)
                        else:
                            self.session_Obj.session_Dict['Creator_ID'] = messageInput_List['from']['id']
                            self.session_Obj.session_Dict['Creator_Chat_ID'] = messageInput_List['chat']['id']
                            self.session_Obj.session_Dict['Creator_User_Name'] = messageInput_List['from']['first_name']
                            
                            self.session_Obj.session_Dict['Session_Content'] = self.session_Obj.session_List
                            self.session_Obj.session_Dict['Number_Of_Questions'] = len(self.session_Obj.session_List)
                            self.session_Obj.session_Dict['Date_Created'] = datetime.now()
                            
                            if self.sessionEditMode:
                                self.stageCounter_Int = 5
                                confirmationMessage_Str = setReply_newsession_SessionDisplayPrefix
                                confirmationMessage_Str += self.session_Obj.translate_session_to_text()
                                confirmationMessage_Str += setReply_newsession_SessionDisplaySuffix
                                await self.sender.sendMessage(confirmationMessage_Str, reply_markup=self.confirmationEditKeyBoard)
                                
                            else:
                                await self.sender.sendMessage(setReply_newsession_ConfirmItems)
                                await self.sender.sendMessage(setReply_newsession_SessionType,reply_markup=self.sessionTypeKeyboard)
                                self.stageCounter_Int = 2
                        return

                    else:
                        await self.sender.sendMessage(setReply_newsession_WrongCommand)
                else:
                    validatedItems_List = self.session_Obj.validate_creation(messageInput_List)
                    self.session_Obj.append_items(validatedItems_List['itemsArray'])
                    
                    translatedItems_Str = setReply_newsession_ItemsDisplayPrefix +\
                                            self.session_Obj.translate_items_to_text() +\
                                            setReply_newsession_ItemsDisplaySuffix
                    
                    if validatedItems_List['errorFlag'] == True:
                        translatedItems_Str += validatedItems_List['errorMessage']
                    
                    await self.sender.sendMessage(translatedItems_Str)
                    
            elif self.stageCounter_Int == 2:
                if messageOutline_Dict['contentType'] == 'command':
                    await self.sender.sendMessage(setReply_newsession_SessionType,reply_markup=self.sessionTypeKeyboard)
       
                else:
                    if inputContent_Str == 'Public':
                        self.session_Obj.session_Dict['Session_Type'] = 'Public'
                        self.session_Obj.session_Dict['Password'] = ''
                        await self.sender.sendMessage('"Public" selected')
                        self.session_Obj.session_Dict['Anonymity_Type'] = 'Yes'

                    elif inputContent_Str == 'Private':
                        self.session_Obj.session_Dict['Session_Type'] = 'Private'
                        await self.sender.sendMessage('"Private" selected')
                        await self.sender.sendMessage(setReply_newsession_PasswordInput)
                        self.stageCounter_Int = 3
                        return

                    elif inputContent_Str == 'Commercial':
                        self.session_Obj.session_Dict['Session_Type'] = 'Commercial'
                        self.session_Obj.session_Dict['Password'] = ''
                        self.session_Obj.session_Dict['Anonymity_Type'] = 'Yes'
                        await self.sender.sendMessage('"Commercial" selected')

                    else:
                        await self.sender.sendMessage(setReply_newsession_SessionType,reply_markup=self.sessionTypeKeyboard)
                        return

                    
                    confirmationMessage_Str = setReply_newsession_SessionDisplayPrefix
                    confirmationMessage_Str += self.session_Obj.translate_session_to_text()
                    confirmationMessage_Str += setReply_newsession_SessionDisplaySuffix
                    
                    await self.sender.sendMessage(confirmationMessage_Str, reply_markup=self.confirmationEditKeyBoard)
                    self.stageCounter_Int = 5
                    
            elif self.stageCounter_Int == 3:
                if 4 <= len(inputContent_Str) <=8 and inputContent_Str.isalnum():
                    await self.sender.sendMessage('Password set')
                    self.session_Obj.session_Dict['Password'] = inputContent_Str
                    await self.sender.sendMessage(setReply_newsession_AnonymityType,reply_markup=self.anonymityTypeKeyboard)
                    self.stageCounter_Int = 4
                    
                else:
                    await self.sender.sendMessage(setReply_newsession_PasswordError)
            
            elif self.stageCounter_Int == 4:
                if messageOutline_Dict['contentType'] == 'command':
                    await self.sender.sendMessage(setReply_newsession_AnonymityType,reply_markup=self.anonymityTypeKeyboard)
                    return
                else:
                    if inputContent_Str == 'Yes':
                        self.session_Obj.session_Dict['Anonymity_Type'] = 'Yes'
                        await self.sender.sendMessage('"Yes" selected')
                        
                    elif inputContent_Str == 'No':
                        self.session_Obj.session_Dict['Anonymity_Type'] = 'No'
                        await self.sender.sendMessage('"No" selected')

                    else:
                        await self.sender.sendMessage(setReply_newsession_AnonymityType,reply_markup=self.anonymityTypeKeyboard)
                        return
                        
                    confirmationMessage_Str = setReply_newsession_SessionDisplayPrefix
                    confirmationMessage_Str += self.session_Obj.translate_session_to_text()
                    confirmationMessage_Str += setReply_newsession_SessionDisplaySuffix
                
                    await self.sender.sendMessage(confirmationMessage_Str, reply_markup=self.confirmationEditKeyBoard)
                    self.stageCounter_Int = 5

            elif self.stageCounter_Int == 5:
                if messageOutline_Dict['contentType'] == 'command':
                    if inputContent_Str == '/done':
                        tempSQLData = self.SQL_Obj.fetch_data_from_SQL('USERS', 'User_ID', self.session_Obj.session_Dict['Creator_ID'])
                        
                        if tempSQLData == None:
                            userData_Dict = {'User_ID' : self.session_Obj.session_Dict['Creator_ID'],\
                                             'User_Name' : self.session_Obj.session_Dict['Creator_User_Name'],\
                                             'Date_Created' : datetime.now()}
                            self.SQL_Obj.commit_data_to_SQL('USERS', userData_Dict)
                        
                        lastID_Dict = self.SQL_Obj.commit_data_to_SQL('SESSIONSLIST',self.session_Obj.session_Dict)
                        lastID_Str = str(lastID_Dict['LAST_INSERT_ID()'])
                        finalCommitMessage_Str = setReply_newsession_CommitMessage                       +\
                                                 '\n\nThe ID for the session is \n\n'                    +\
                                                 lastID_Str                                              +\
                                                 '\n\nAsk your responders to respond to the session by ' +\
                                                 'private messaging this bot "/respond ' + lastID_Str + '"'
                                                 
                        self.sessionEditMode = False
                        self.stageCounter_Int = 0
                        self.chatMode_Str = 'chat'
                        self.session_Obj.clear_session()
                        
                        
                        await self.sender.sendMessage(finalCommitMessage_Str)
                        
                    else:
                        confirmationMessage_Str = setReply_newsession_SessionDisplayPrefix
                        confirmationMessage_Str += self.session_Obj.translate_session_to_text()
                        confirmationMessage_Str += setReply_newsession_SessionDisplaySuffix
                        await self.sender.sendMessage(confirmationMessage_Str, reply_markup=self.confirmationEditKeyBoard)
                
                else: 
                    if inputContent_Str == 'Change Items':
                        self.sessionEditMode = True
                        self.stageCounter_Int = 1
                        translatedItems_Str = setReply_newsession_ItemsDisplayPrefix +\
                                            self.session_Obj.translate_items_to_text() +\
                                            setReply_newsession_ItemsDisplaySuffix
                        
                        await self.sender.sendMessage(translatedItems_Str)
                    
                    elif inputContent_Str == 'Change Type':
                        self.sessionEditMode = True
                        self.stageCounter_Int = 2
                        await self.sender.sendMessage(setReply_newsession_SessionType,reply_markup=self.sessionTypeKeyboard)
                    
                    elif inputContent_Str == 'Change Password':
                        if self.session_Obj.session_Dict['Session_Type'] != 'Private':
                            await self.sender.sendMessage('You have to set session type to private first!')
                            confirmationMessage_Str = setReply_newsession_SessionDisplayPrefix
                            confirmationMessage_Str += self.session_Obj.translate_session_to_text()
                            confirmationMessage_Str += setReply_newsession_SessionDisplaySuffix
                            await self.sender.sendMessage(confirmationMessage_Str, reply_markup=self.confirmationEditKeyBoard)
                        else:
                            self.sessionEditMode = True
                            self.stageCounter_Int = 3
                            await self.sender.sendMessage(setReply_newsession_PasswordInput)
                    
                    elif inputContent_Str == 'Change Anonymity':
                        if self.session_Obj.session_Dict['Session_Type'] != 'Private':
                            await self.sender.sendMessage('You have to set session type to private first!')
                            confirmationMessage_Str = setReply_newsession_SessionDisplayPrefix
                            confirmationMessage_Str += self.session_Obj.translate_session_to_text()
                            confirmationMessage_Str += setReply_newsession_SessionDisplaySuffix
                            await self.sender.sendMessage(confirmationMessage_Str, reply_markup=self.confirmationEditKeyBoard)
                            
                        else:
                            self.sessionEditMode = True
                            self.stageCounter_Int = 4
                            await self.sender.sendMessage(setReply_newsession_AnonymityType,reply_markup=self.anonymityTypeKeyboard)
                    else:
                        confirmationMessage_Str = setReply_newsession_SessionDisplayPrefix
                        confirmationMessage_Str += self.session_Obj.translate_session_to_text()
                        confirmationMessage_Str += setReply_newsession_SessionDisplaySuffix
                        await self.sender.sendMessage(confirmationMessage_Str, reply_markup=self.confirmationEditKeyBoard)
                    
            else:
                await self.sender.sendMessage(setReply_nocommand)
                return
         
        # RESPOND RESPOND RESPOND RESPOND RESPOND RESPOND RESPOND RES #
        elif self.chatMode_Str == 'respond':
            if self.stageCounter_Int == 1:
                if messageOutline_Dict['contentType'] != 'command':
                    await self.sender.sendMessage(setReply_response_WhenPrivate)
                    return
                else:
                    if inputContent_Str == '/proceed':
                        
                        if self.response_Obj.session_Dict['Session_Type'] == 'Public':
                            await self.sender.sendMessage(setReply_response_notifyPublic)
                            self.stageCounter_Int = 3

                        elif self.response_Obj.session_Dict['Session_Type'] == 'Private':
                            if self.response_Obj.session_Dict['Anonymity_Type'] == 'Yes':
                                await self.sender.sendMessage(setReply_response_notifyPrivateAnon)
                                self.stageCounter_Int = 2
                                return

                            elif self.response_Obj.session_Dict['Anonymity_Type'] == 'No': 
                                await self.sender.sendMessage(setReply_response_notifyPrivateNotAnon)
                                self.stageCounter_Int = 2
                                return

                        elif self.response_Obj.session_Dict['Session_Type'] == 'Commercial':
                            await self.sender.sendMessage(setReply_response_notifyCommercial)
                            self.stageCounter_Int = 3
                            
                        self.response_Obj.response_Dict['Responder_ID'] = messageInput_List['from']['id']
                        self.response_Obj.response_Dict['Chat_ID'] = messageInput_List['chat']['id']
                        self.response_Obj.response_Dict['User_Name'] = messageInput_List['from']['first_name']
                        self.response_Obj.response_Dict['Session_ID'] = self.response_Obj.session_Dict['Session_ID']
                        
                        self.response_Obj.translate_session_item()
                        
                        translatedItem_Dict = self.response_Obj.translatedSession_List[0]
                        translatedItemText_Str = translatedItem_Dict['text']
                        translatedItemKeyboard_Obj = translatedItem_Dict['keyboard']
                        
                        await self.sender.sendMessage(translatedItemText_Str , reply_markup = translatedItemKeyboard_Obj)
                        
                    else:
                        await self.sender.sendMessage(setReply_response_WhenPrivate)
                        return
            
            elif self.stageCounter_Int == 2:
                if messageOutline_Dict['contentType'] == 'command':
                    await self.sender.sendMessage(setReply_response_WrongPassword)
                    return
                elif inputContent_Str == self.response_Obj.session_Dict['Password']:
                    await self.sender.sendMessage('Password is correct!')
                    self.stageCounter_Int = 3
                    
                    self.response_Obj.response_Dict['Responder_ID'] = messageInput_List['from']['id']
                    self.response_Obj.response_Dict['Chat_ID'] = messageInput_List['chat']['id']
                    self.response_Obj.response_Dict['User_Name'] = messageInput_List['from']['first_name']
                    self.response_Obj.response_Dict['Session_ID'] = self.response_Obj.session_Dict['Session_ID']
                        
                    self.response_Obj.translate_session_item()
                    
                    
                    translatedItem_Dict = self.response_Obj.translatedSession_List[self.questionCounter]
                    translatedItemText_Str = translatedItem_Dict['text']
                    translatedItemKeyboard_Obj = translatedItem_Dict['keyboard']
                        
                    await self.sender.sendMessage(translatedItemText_Str , reply_markup = translatedItemKeyboard_Obj)
                    
                else:    
                    await self.sender.sendMessage(setReply_response_WrongPassword)
                    return
            
            elif self.stageCounter_Int == 3:
                if messageOutline_Dict['contentType'] == 'command':
                    translatedItem_Dict = self.response_Obj.translatedSession_List[self.questionCounter]
                    translatedItemText_Str = translatedItem_Dict['text']
                    translatedItemKeyboard_Obj = translatedItem_Dict['keyboard']
                    
                    await self.sender.sendMessage(translatedItemText_Str , reply_markup = translatedItemKeyboard_Obj)
                    return
                else:
                    validateResponse_Bool = self.response_Obj.validate_response(messageInput_List,self.questionCounter)
                    if not validateResponse_Bool:
                        translatedItem_Dict = self.response_Obj.translatedSession_List[self.questionCounter]
                        translatedItemText_Str = translatedItem_Dict['text']
                        translatedItemKeyboard_Obj = translatedItem_Dict['keyboard']
                    
                        await self.sender.sendMessage(translatedItemText_Str , reply_markup = translatedItemKeyboard_Obj)
                    else:
                        if self.responseEditMode == True:
                            await self.sender.sendMessage(self.response_Obj.translate_responses())
                            self.stageCounter_Int = 4
                        else:
                            self.questionCounter += 1
                            if self.questionCounter < len(self.response_Obj.translatedSession_List):
                                translatedItem_Dict = self.response_Obj.translatedSession_List[self.questionCounter]
                                translatedItemText_Str = translatedItem_Dict['text']
                                translatedItemKeyboard_Obj = translatedItem_Dict['keyboard']
                            
                                await self.sender.sendMessage(translatedItemText_Str , reply_markup = translatedItemKeyboard_Obj)
                            else:
                                await self.sender.sendMessage(self.response_Obj.translate_responses())
                                self.stageCounter_Int = 4
            
            elif self.stageCounter_Int == 4:
                if messageOutline_Dict['contentType'] != 'command':
                    await self.sender.sendMessage(self.response_Obj.translate_responses())
                    return
                
                else:
                    if inputContent_Str.startswith('/change'):
                        validateChangeResult = self.response_Obj.validate_change_line(messageInput_List)
                        if validateChangeResult:
                            self.responseEditMode = True
                            self.stageCounter_Int = 3
                            
                            self.questionCounter = int(validateChangeResult) - 1
                            
                            translatedItem_Dict = self.response_Obj.translatedSession_List[self.questionCounter]
                            translatedItemText_Str = translatedItem_Dict['text']
                            translatedItemKeyboard_Obj = translatedItem_Dict['keyboard']
                            
                            await self.sender.sendMessage(translatedItemText_Str , reply_markup = translatedItemKeyboard_Obj)
                        else:
                            await self.sender.sendMessage(setReply_response_ChangeAnswerWrongFormat)
                            await self.sender.sendMessage(self.response_Obj.translate_responses())
                            
                    elif inputContent_Str.startswith('/done'):
                        self.response_Obj.response_Dict['Response_Content'] = self.response_Obj.response_List
                        self.response_Obj.response_Dict['Date_Responded'] = datetime.now()
                        
                        if self.SQL_Obj.check_response_exist:
                            print('ding!')
                            responseContent_List = self.response_Obj.response_Dict['Response_Content']
                            responderID_Str = self.response_Obj.response_Dict['Responder_ID']
                            sessionID_Str = self.response_Obj.response_Dict['Responder_ID']
                            self.SQL_Obj.update_response_to_SQL(responseContent_List,responderID_Str,sessionID_Str)
                        else:
                            self.SQL_Obj.commit_data_to_SQL('CHATRESPONSES',self.response_Obj.response_Dict)                        
                        
                        self.stageCounter_Int = 0
                        self.questionCounter = 0
                        self.responseEditMode = False
                        self.chatMode_Str = 'chat'
                        self.response_Obj.clear_responses()
                        
                        await self.sender.sendMessage('Response saved!')
                        
                    else:
                        await self.sender.sendMessage(self.response_Obj.translate_responses())
                        
            else:
                await self.sender.sendMessage(setReply_nocommand)
                return
        
        # VIEW VIEW VIEW VIEW VIEW VIEW VIEW VIEW VIEW VIEW VIEW VIEW #
        elif self.chatMode_Str == 'view':
            if self.stageCounter_Int == 1:
                if messageOutline_Dict['contentType'] != 'command':
                    await self.sender.sendMessage(setReply_view_WhenPrivate)
                elif inputContent_Str == "/proceed":
                    self.view_Obj.tabulate_results()
                    await self.sender.sendMessage(self.view_Obj.translate_result_to_text())
                    
                else:
                    await self.sender.sendMessage(setReply_view_WhenPrivate)
        else:
            await self.sender.sendMessage(setReply_nocommand)
            return
        
# ███████████████████████████████████████████████████████████████████ #
#                                                                     #
# [X05] Main Method                                                   #
#                                                                     #
# ███████████████████████████████████████████████████████████████████ #

class anonBot(telepot.aio.DelegatorBot):
    def __init__(self,token):
        self.placeholderVar = ""
        
        super(anonBot, self).__init__(token, [
            pave_event_space()(
                per_chat_id(), create_open, anonChatHandler, timeout=setBotTimeout),
        ])
        

def main():

    leBot = anonBot(TOKEN)

    loop = asyncio.get_event_loop()
    loop.create_task(leBot.message_loop())
    
    print('Listening begun at', datetime.now())
    
    loop.run_forever()    


if  __name__ =='__main__':main()