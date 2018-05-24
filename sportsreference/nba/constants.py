PARSING_SCHEME = {
    'name': 'a',
    'games_played': 'td[data-stat="g"]:first',
    'minutes_played': 'td[data-stat="mp"]:first',
    'field_goals': 'td[data-stat="fg"]:first',
    'field_goal_attempts': 'td[data-stat="fga"]:first',
    'field_goal_percentage': 'td[data-stat="fg_pct"]:first',
    'three_point_field_goals': 'td[data-stat="fg3"]:first',
    'three_point_field_goal_attempts': 'td[data-stat="fg3a"]:first',
    'three_point_field_goal_percentage': 'td[data-stat="fg3_pct"]:first',
    'two_point_field_goals': 'td[data-stat="fg2"]:first',
    'two_point_field_goal_attempts': 'td[data-stat="fg2a"]:first',
    'two_point_field_goal_percentage': 'td[data-stat="fg2_pct"]:first',
    'free_throws': 'td[data-stat="ft"]:first',
    'free_throw_attempts': 'td[data-stat="fta"]:first',
    'free_throw_percentage': 'td[data-stat="ft_pct"]:first',
    'offensive_rebounds': 'td[data-stat="orb"]:first',
    'defensive_rebounds': 'td[data-stat="drb"]:first',
    'total_rebounds': 'td[data-stat="trb"]:first',
    'assists': 'td[data-stat="ast"]:first',
    'steals': 'td[data-stat="stl"]:first',
    'blocks': 'td[data-stat="blk"]:first',
    'turnovers': 'td[data-stat="tov"]:first',
    'personal_fouls': 'td[data-stat="pf"]:first',
    'points': 'td[data-stat="pts"]:first',
    'opp_minutes_played': 'td[data-stat="mp"]:first',
    'opp_field_goals': 'td[data-stat="opp_fg"]:first',
    'opp_field_goal_attempts': 'td[data-stat="opp_fga"]:first',
    'opp_field_goal_percentage': 'td[data-stat="opp_fg_pct"]:first',
    'opp_three_point_field_goals': 'td[data-stat="opp_fg3"]:first',
    'opp_three_point_field_goal_attempts': 'td[data-stat="opp_fg3a"]:first',
    'opp_three_point_field_goal_percentage':
    'td[data-stat="opp_fg3_pct"]:first',
    'opp_two_point_field_goals': 'td[data-stat="opp_fg2"]:first',
    'opp_two_point_field_goal_attempts': 'td[data-stat="opp_fg2a"]:first',
    'opp_two_point_field_goal_percentage': 'td[data-stat="opp_fg2_pct"]:first',
    'opp_free_throws': 'td[data-stat="opp_ft"]:first',
    'opp_free_throw_attempts': 'td[data-stat="opp_fta"]:first',
    'opp_free_throw_percentage': 'td[data-stat="opp_ft_pct"]:first',
    'opp_offensive_rebounds': 'td[data-stat="opp_orb"]:first',
    'opp_defensive_rebounds': 'td[data-stat="opp_drb"]:first',
    'opp_total_rebounds': 'td[data-stat="opp_trb"]:first',
    'opp_assists': 'td[data-stat="opp_ast"]:first',
    'opp_steals': 'td[data-stat="opp_stl"]:first',
    'opp_blocks': 'td[data-stat="opp_blk"]:first',
    'opp_turnovers': 'td[data-stat="opp_tov"]:first',
    'opp_personal_fouls': 'td[data-stat="opp_pf"]:first',
    'opp_points': 'td[data-stat="opp_pts"]:first'
}

SCHEDULE_SCHEME = {
    'game': 'th[data-stat="g"]:first',
    'date': 'td[data-stat="date_game"]:first',
    'time': 'td[data-stat="game_start_time"]:first',
    'location': 'td[data-stat="game_location"]:first',
    'opponent_abbr': 'td[data-stat="opp_name"]:first',
    'opponent_name': 'td[data-stat="opp_name"]:first',
    'result': 'td[data-stat="game_result"]:first',
    'overtime': 'td[data-stat="overtimes"]:first',
    'points_scored': 'td[data-stat="pts"]:first',
    'points_allowed': 'td[data-stat="opp_pts"]:first',
    'wins': 'td[data-stat="wins"]:first',
    'losses': 'td[data-stat="losses"]:first',
    'streak': 'td[data-stat="game_streak"]:first'
}

SEASON_PAGE_URL = 'http://www.basketball-reference.com/leagues/NBA_%s.html'

SCHEDULE_URL = 'http://www.basketball-reference.com/teams/%s/%s_games.html'
