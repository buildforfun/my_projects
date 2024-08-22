CREATE DATABASE IF NOT EXISTS FilmData;
USE FilmData;

CREATE TABLE IF NOT EXISTS FavMovieData (
    Position INT,
    Const VARCHAR(20),
    Created DATE,
    Modified DATE,
    Description TEXT,
    Title VARCHAR(255),
    Original_Title VARCHAR(255),
    URL VARCHAR(255),
    Title_Type VARCHAR(50),
    IMDb_Rating DECIMAL(3,1),
    Runtime_mins INT,
    Year INT,
    Genres VARCHAR(255),
    Num_Votes INT,
    Release_Date DATE,
    Directors VARCHAR(255),
    Your_Rating DECIMAL(3,1),
    Date_Rated DATE,
    PRIMARY KEY (Const)
);

LOAD DATA INFILE '/data/fav_movies.csv'
INTO TABLE FavMovieData
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;