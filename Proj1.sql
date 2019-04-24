
CREATE TABLE Messages(
  User char(50),
  Message char(250),
  Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT Username FOREIGN KEY (User) REFERENCES Users (Username)
);

CREATE TABLE Users(
  Username char(50),
  Name char(50),
  PasswordHashes char(64),
  CONSTRAINT Username UNIQUE (Username),
  CONSTRAINT P_Key_Username PRIMARY KEY (Username)
);
