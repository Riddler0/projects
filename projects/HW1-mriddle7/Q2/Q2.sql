-- Setup. DO NOT REMOVE.
.headers on
.separator ','

DROP TABLE IF EXISTS sets;
DROP TABLE IF EXISTS themes;
DROP TABLE IF EXISTS parts;
DROP VIEW IF EXISTS top_level_themes;
DROP VIEW IF EXISTS sets_years;
DROP TABLE IF EXISTS parts_fts;


-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (a.i) Create tables

-- [insert your SQL statement(s) BELOW this line]

CREATE TABLE sets(
	"set_num" TEXT, 
	"name" TEXT,
	"year" INTEGER,
	"theme_id" INTEGER,
	"num_parts" INTEGER
);

CREATE TABLE themes(
	"id" INTEGER,
	"name" TEXT,
	"parent_id" INTEGER
);

CREATE TABLE parts(
	"part_num" TEXT, 
	"name" TEXT,
 	"part_cat_id" INTEGER,
 	"part_material_id" INTEGER
);

-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]
.tables
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (a.ii) Import data

-- [insert your SQLite command(s) BELOW this line]

.mode csv
.import data/parts.csv parts
.import data/sets.csv sets
.import data/themes.csv themes

-- [insert your SQLite command(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]

.headers off
SELECT COUNT(*) FROM sets;
SELECT COUNT(*) FROM parts;
.headers on
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (b) Create indexes

-- [insert your SQL statement(s) BELOW this line]

CREATE INDEX sets_index ON sets("set_num");
CREATE INDEX parts_index ON parts("part_num");
CREATE INDEX themes_index ON themes("id");

-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]

.indexes
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (c.i) Create the top_level themes VIEW

-- [insert your SQL statement(s) BELOW this line]

CREATE VIEW top_level_themes AS SELECT DISTINCT id, name 
FROM themes WHERE parent_id = '';

-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]

.headers off
PRAGMA table_info(top_level_themes);
.headers on
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (c.ii) count the top level themes in the top_level_themes view.

-- [insert your SQL statement(s) BELOW this line]


SELECT COUNT(id) AS count FROM top_level_themes;

-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]

.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (d) Finding top level themes with the most sets.

-- [insert your SQL statement(s) BELOW this line]
DROP VIEW IF EXISTS theme_count;


CREATE VIEW theme_count AS
SELECT top_level_themes.name, COUNT(sets.name) AS num_sets
FROM top_level_themes
INNER JOIN sets on sets.theme_id = top_level_themes.id
GROUP BY theme_id
ORDER BY -num_sets;

SELECT * FROM theme_count
LIMIT 10;


-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (e) Calculate a percentage

-- [insert your SQL statement(s) BELOW this line]


SELECT name, ROUND(num_sets * 100.00 / (SELECT SUM(num_sets) FROM theme_count), 2) AS percentage
FROM theme_count
WHERE percentage > 5.00;



-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (f) Summarize a sub-theme

-- [insert your SQL statement(s) BELOW this line]

SELECT themes.name AS sub_theme, COUNT(sets.name) AS num_sets 
FROM themes 
INNER JOIN sets on sets.theme_id = themes.id 
WHERE id = 186 OR parent_id = 186
GROUP BY sets.theme_id
ORDER BY -num_sets, sub_theme;

-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (g.i.) Create the sets VIEW

-- [insert your SQL statement(s) BELOW this line]

CREATE VIEW sets_years AS
SELECT rowID, year, COUNT(name) AS sets_count
FROM sets
GROUP BY year;

-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]

.headers off
PRAGMA table_info(sets_years);
SELECT AVG(sets_count) FROM sets_years;
.headers on
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (g.ii) Find the running total of sets in the Rebrickable database each year

-- [insert your SQL statement(s) BELOW this line]

SELECT a.year, SUM(b.sets_count) AS cumsum
FROM sets_years AS a, sets_years AS b 
WHERE b.year <= a.year
GROUP BY a.year
ORDER BY a.year;

-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (h) Create the FTS table and import data.

-- [insert your SQL statement(s) BELOW this line]
DROP TABLE IF EXISTS parts_fits;


CREATE VIRTUAL TABLE parts_fits USING fts4(
	"part_num" TEXT,
	"name" TEXT,
	"part_cat_id" INTEGER,
	"part_material_id" INTEGER
);

.import C:/sqlite/Data/parts.csv parts_fits


-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]

.headers off
PRAGMA table_info(parts_fts);
.headers on
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (h.i) Count the number of unique parts whose name field begins with the prefix ‘mini’.

-- [insert your SQL statement(s) BELOW this line]

SELECT COUNT(name) AS count_overview FROM parts_fits
WHERE name MATCH '^mini*';

-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (h.ii) List the part_num’s of the unique parts that contain the terms ‘minidoll’ and ‘boy’ in the name field with no more than 5 intervening terms.

-- [insert your SQL statement(s) BELOW this line]

SELECT part_num AS part_num_boy_minidoll
FROM parts_fits
WHERE name MATCH 'boy NEAR/5 minidoll';

-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --

-- (h.iii) List the part_num’s of the unique parts that contain the terms ‘minidoll’ and ‘girl’ in the name field with no more than 5 intervening terms.

-- [insert your SQL statement(s) BELOW this line]

SELECT part_num AS part_num_girl_minidoll
FROM parts_fits
WHERE name MATCH 'girl NEAR/5 minidoll';

-- [insert your SQL statement(s) ABOVE this line]

-- [the following statement(s) are for autograding. DO NOT REMOVE.]
.print '~~~~~'

-- ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** --