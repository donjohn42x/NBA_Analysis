create table game_details (
    SEASON_ID int, 
    TEAM_ID int,
    TEAM_ABBREVIATION varchar,
    TEAM_NAME varchar,
    GAME_ID int,
    GAME_DATE date,
    MATCHUP varchar,
    WL varchar,
    MIN int,
    FGM int,
    FGA int,
    FG_PCT float,
    FG_3M int,
    FG_3A int,
    FG3_PCT int,
    FTM int,
    FTA int,
    FT_PCT float,
    OREB int,
    DREB int,
    REB int,
    AST int,
    STL int,
    BLK int,
    TOV int,
    PF int,
    PTS int,
    PLUS_MINUS int,
    VIDEO_AVAILABLE int,
    WIN int
);

create table game_detail_new (
    SEASON_ID int, 
    TEAM_ID int,
    TEAM_ABBREVIATION varchar,
    TEAM_NAME varchar,
    GAME_ID int,
    GAME_DATE date,
    MATCHUP varchar,
    WL varchar,
    MIN int,
    FGM int,
    FGA int,
    FG_PCT float,
    FG_3M int,
    FG_3A int,
    FG3_PCT int,
    FTM int,
    FTA int,
    FT_PCT float,
    OREB int,
    DREB int,
    REB int,
    AST int,
    STL int,
    BLK int,
    TOV int,
    PF int,
    PTS int,
    PLUS_MINUS int,
    VIDEO_AVAILABLE int,
    WIN int
);

create table players_2021_22 (
    PLAYER_ID int,
    PLAYER_NAME varchar,
    NICKNAME varchar,
    TEAM_ID int,
    TEAM_ABBREVIATION varchar(3),
    AGE float,
    GP int,
    W int,
    L int,
    W_PCT float,
    MIN float,
    FGM float,
    FGA float,
    FG_PCT float,
    FG3M float,
    FG3A float,
    FG3A_PCT float,
    FTM float,
    FTA float,
    FT_PCT float,
    OREB float,
    DREB float,
    REB float,
    AST float,
    TOV float,
    STL float,
    BLK float,
    BLKA float,
    PF float,
    PFD float,
    PTS float,
    PLUS_MINUS float,
    NBA_FANTACY_PTS float,
    DD2 int,
    TD3 int,
    GP_RANK int,
    W_RANK int,
    L_RANK int,
    W_PCT_RANK int,
    MINI_RANK int,
    FGM_RANK int,
    FGA_RANK int,
    FG_PCT_RANK int,
    FG3M_PCT_RANK int,
    FG3A_PCT_RANK int,
    FG3_PCT_RANK int,
    FTM_RANK int,
    FTA_RANK int,
    FT_PCT_RANK int,
    OREB_RANK int,
    DREB_RANK int,
    REB_RANK int,
    AST_RANK int,
    TOV_RANK int,
    STL_RANK int,
    BLK_RANK int,
    BLKA_RANK int,
    PF_RANK int,
    PFD_RANK int,
    PTS_RANK int,
    PLUS_MINUS_RANK int,
    NBA_FANTASY_PTS_RANK int,
    DD2_RANK int,
    TD3_RANK int,
    CFID int,
    CFPARAMS varchar
)


create table teams_2021-22 (
 TEAM_ID int,
 TEAM_NAME varchar,
 GP int,
 W int,
 L int,
 W_PCT float,
 MIN float,
 FGM float,
 FGA float,
 FG_PCT	float,
 FG3M float,
 FG3A float,
 FG3_PCT float,
 FTM float,
 FTA float,
 FT_PCT	float,
 OREB float,
 DREB	float,
 REB float,
 AST float,
 TOV float,
 STL float,
 BLK float,
 BLKA float,
 PF float,
 PFD float,
 PTS float,
 PLUS_MINUS float,
GP_RANK	int,
W_RANK int,
L_RANK int,
W_PCT_RANK int,
MIN_RANK int,
FGM_RANK int,
FGA_RANK int,
FG_PCT_RANK	 int, 
FG3M_RANK int,
FG3A_RANK int,
FG3_PCT_RANK int,
FTM_RANK int,
FTA_RANK int,
FT_PCT_RANK	 int,
OREB_RANK int, 
DREB_RANK int,
REB_RANK int,
AST_RANK int,
TOV_RANK int,
STL_RANK int,
BLK_RANK int,
BLKA_RANK int,
PF_RANK	int,
PFD_RANK int,
PTS_RANK int,
PLUS_MINUS_RANK	int,
CFID int,
CFPARAMS varchar

)