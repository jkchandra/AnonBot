CREATE DATABASE IF NOT EXISTS anondb;

use anondb;

DROP TABLE IF EXISTS CHATRESPONSES;
DROP TABLE IF EXISTS SESSIONSLIST;
DROP TABLE IF EXISTS USERS;

CREATE TABLE USERS(
User_ID             VARCHAR(40) NOT NULL,
User_Name           VARCHAR(40) NOT NULL,
Date_Created        TIMESTAMP   NOT NULL,
User_Type	        VARCHAR(40),
Credits             INT,

PRIMARY KEY (User_ID))
ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

CREATE TABLE SESSIONSLIST(
Session_ID          INT         NOT NULL    AUTO_INCREMENT,
Creator_ID          VARCHAR(40) NOT NULL,
Creator_Chat_ID	    VARCHAR(40) NOT NULL,
Creator_User_Name   VARCHAR(40) NOT NULL,
Password            VARCHAR(40),
Session_Type        VARCHAR(15) NOT NULL,
Anonymity_Type      VARCHAR(15) NOT NULL,
Number_Of_Questions INT         NOT NULL,
Date_Created        TIMESTAMP   NOT NULL,
Date_Expiry         TIMESTAMP,
Session_Content	    TEXT(500),

PRIMARY KEY (Session_ID),
FOREIGN KEY (Creator_ID)    REFERENCES USERS(User_ID))
ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

CREATE TABLE CHATRESPONSES(
Response_ID 	    INT         NOT NULL    AUTO_INCREMENT,
Responder_ID        VARCHAR(40) NOT NULL,
Chat_ID	            VARCHAR(40) NOT NULL,
User_Name           VARCHAR(40) NOT NULL,
Date_Responded      TIMESTAMP   NOT NULL,
Session_ID          INT         NOT NULL,
Response_Content	TEXT(500),

PRIMARY KEY (Response_ID),
FOREIGN KEY (Session_ID)    REFERENCES SESSIONSLIST(Session_ID),
FOREIGN KEY (Responder_ID)  REFERENCES USERS(User_ID))
ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;