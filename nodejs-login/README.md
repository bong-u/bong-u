# nodejs-login
express, passport, bcrypt를 이용한 로그인 구현


### mysql(mydb -> user) 구조
| uid       | id                 |  pw          | name         |
| -------  | ------------- | ---------- | ------------ |
| int(11)  | varchar(20)  | char(60)  |  varchar(10) |
| PRI, auto_increment |   | hash with salt | |  |
