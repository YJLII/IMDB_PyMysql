
create table title_akas(
	titleid text,
    ordering text,
    title text,
    region text,
    language text,
    types text,
    attributes text,
    isOriginalTitle text
);
create table title_basics(
	tconst text,
    titleType text,
    primaryTitle text,
    originalTitle text,
    isAdult text,
    startYear text,
    endYear text,
    runtimeMinutes text,
    genres text
);

create table title_crew(
	tconst text,
    directors text,
    writers text
); 
      
    
    

  

create table title_episode(
	tconst text, 
	parentTconst text, 
	seasonNumber text, 
	episodeNumber text);   

create table title_principals(
	tconst text, 
	ordering text, 
	nconst text, 
	category text,
    job text,
    characters text
    );  

create table title_ratings(
	tconst text, 
	averageRating text,
    numVotes text
    );

create table name_basics(
	nconst text,
    primaryName text,
    birthYear text,
    deathYear text,
    primaryProfession text,
    knownForTitles text
);  
  