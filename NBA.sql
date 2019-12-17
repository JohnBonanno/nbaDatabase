SET FOREIGN_KEY_CHECKS=0;  -- temporarily disable foreign key checking
DROP TABLE IF EXISTS Player;
DROP TABLE IF EXISTS Team;
-- add similar DROP TABLE lines for all tables in schema
SET FOREIGN_KEY_CHECKS=1;  -- re enable foreign key checking

-- your table creation code goes here

CREATE TABLE Player (
    id INT AUTO_INCREMENT NOT NULL,
    jersey_num INT NOT NULL,
    fname VARCHAR(30),
    lname VARCHAR(30),
    position ENUM( 'G', 'F', 'C'),
    heightInCm INT NOT NULL,
    weightInLbs INT NOT NULL,
    home_state VARCHAR(50) NOT NULL,
    team_id INT,
    
    PRIMARY KEY(id)
);

INSERT INTO Player (jersey_num, fname, lname, position, heightInCm, weightInLbs, home_state, team_id)
	VALUES(3, 'Anthony', 'Davis', 'F', 208, 253, 'Kentucky', 1),
        (23, 'LeBron', 'James', 'F', 205, 250, 'Ohio', 1),
   		  (39, 'Dwight', 'Howard', 'C', 208, 265, 'Georgia', 1),
   		  (4, 'Alex', 'Caruso', 'G', 195, 186, 'Texas', 1),
        (2, 'Quinn', 'Cook', 'G', 185, 180, 'North Carolina', 1),
   		  (30, 'Troy', 'Daniels', 'G', 193, 200, 'Virginia', 1),
   		  (14, 'Danny', 'Green', 'G', 198, 215, 'North Carolina', 1),
   		  (0, 'Kyle', 'Kuzma', 'F', 203, 221, 'Utah', 1),
   		  (11,  'Avery', 'Bradley', 'G', 190, 180, 'Texas', 1),
        (7, 'JaVale', 'McGee','C', 213, 270, 'Nevada', 1),
  		  (23, 'Lou', 'Williams', 'G', 185,175,'Tennessee', 2),
        (21, 'Patrick', 'Beverly', 'G', 185, 180, 'Arkansas', 2),
        (13, 'Paul', 'George', 'G', 203, 220, 'California', 2),
        (4, 'JaMychal', 'Green', 'F', 203, 227, 'Alabama', 2),
        (8, 'Maurice', 'Harkless', 'F', 204, 220, 'Connecticut', 2),
        (5, 'Montrezl', 'Harrell', 'F', 207, 235, 'Florida', 2),
     		(54, 'Patrick', 'Patterson', 'F', 206, 230, 'Kentucky', 2),
        (2, 'Kawhi', 'Leonard', 'F', 202, 225, 'California', 2 ),
        (15, 'Johnathan', 'Motley', 'F', 203, 230, 'Texas', 2),
        (25, 'Mfiondu', 'Kabengele', 'F', 204, 250, 'Florida', 2),
        (0,'Trevor', 'Ariza', 'F', 203,215, 'FL',3),
        (10, 'Justin', 'James', 'G', 200, 190,'WY', 3),
        (35, 'Marvin', 'Bagley', 'F', 210, 235, 'AZ', 3),
        (13, 'Dewayne', 'Dedmon', 'C',  213, 245,'CA', 3),
        (20, 'Harry' ,'Giles', 'F', 210, 240,'NC', 3),
        (22, 'Richaun', 'Holmes', 'F', 208, 235, 'IL', 3),
        (88, 'Nemanja', 'Bjelica', 'F', 208, 234, 'Yugoslavia',3),
        (50, 'Caleb', 'Swanigan', 'F', 205, 260, 'IN', 3),
        (32, 'Wenyen', 'Gabriel', 'F', 203, '205', 'KY', 3),
        (40, 'Harrison', 'Barnes', 'F', 203, 215, 'CA', 3),
        (12, 'Ky', 'Bowman', 'G', 185, 187, 'Massachusetts', 4),
        (8, 'Alec', 'Burks', 'G', 196, 187, 'Colorado', 4),
        (2, 'Willie', 'Cauley-Stein', 'C', 213, 240, 'Kentucky', 4),
        (32, 'Marquese', 'Chriss', 'F', 210, 240, 'Washington', 4),
        (30, 'Stephen', 'Curry', 'G', 190, 185, 'Georgia', 4),
        (10, 'Jacob', 'Evans', 'G', 198, 230, 'Ohio', 4),
        (23, 'Draymond', 'Green', 'F', 198, 230, 'Michigan', 4),
        (1, 'Damion', 'Lee', 'G', 196, 210, 'Kentucky', 4),
        (5, 'Kevon', 'Looney', 'F', 206, 222, 'California', 4),
        (0, 'D’Angelo', 'Russell', 'G', 198, 193, 'Ohio', 4),
        (11, 'Klay', 'Thompson', 'G', 200, 210, 'Washington', 4),
        (12, 'Jared', 'Harper', 'G', 190, 180, 'California', 5),
        (16, 'Tyler', 'Johnson', 'G', 190, 186, 'California', 5),
        (22, 'Deandre', 'Ayton', 'C', 206, 240, 'Texas', 5),
        (10, 'Ty', 'Jerome', 'G', 195, 195, 'Virginia', 5),
        (1, 'Devin', 'Booker', 'G', 195, 206, 'Kentucky', 5),
        (46, 'Aron', 'Baynes','C',  208, 260, 'Washington', 5),
        (25,'Mikal', 'Bridges', 'F', 200, 205, 'Michigan', 5),  
        (11, 'Ricky', 'Rubio', 'G', 190, 190, 'Spain', 5),
        (3, 'Kelly', 'Oubre', 'G', 202, 195, 'Kansas', 5),
        (2, 'Elie', 'Okobo', 'F', 190, 190, 'France', 5);

CREATE TABLE team(
    id INT AUTO_INCREMENT NOT NULL ,
    city VARCHAR(64) NOT NULL,
    team_name VARCHAR(64), 
    primary key (id)
);



INSERT INTO team(id, team_name, city)
	VALUES (1,'Los Angeles Lakers', 'Los Angeles'),
        (2,'LA Clippers', 'Los Angeles'),
        (3,'Sacramento Kings', 'Sacramento'),
        (4,'Golden State Warriors', 'San Francisco'),
        (5,'Phoenix Suns', 'Phoenix');
