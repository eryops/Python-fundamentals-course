players = [
    {
        "name": "  aLiCe  ",
        "team": "Ravens",
        "country": "sweden",
        "score": 1200,
        "matches_played": 18,
        "wins": 12,
        "active": True
    },
    {
        "name": "BRIAN",
        "team": "Wolves",
        "country": "Danmark",
        "score": 980,
        "matches_played": 20,
        "wins": 8,
        "active": True
    },
    {
        "name": "  cArLos",
        "team": "Dragons",
        "country": "mexico",
        "score": 450,
        "matches_played": 10,
        "wins": 0,
        "active": False
    },
    {
        "name": "diana ",
        "team": "Ravens",
        "country": "Sweden",
        "score": 1330,
        "matches_played": 22,
        "wins": 15,
        "active": True
    },
    {
        "name": "ELLA",
        "team": "Wolves",
        "country": "Norway",
        "score": 700,
        "matches_played": 14,
        "wins": 6,
        "active": True
    },
    {
        "name": "  frank",
        "team": "Knights",
        "country": "Germany",
        "score": 300,
        "matches_played": 8,
        "wins": 1,
        "active": False
    },
    {
        "name": "george",
        "team": "Dragons",
        "country": "MEXICO",
        "score": 1120,
        "matches_played": 19,
        "wins": 11,
        "active": True
    },
    {
        "name": "  helen ",
        "team": "Knights",
        "country": "germany",
        "score": 500,
        "matches_played": 12,
        "wins": 4,
        "active": True
    },
    {
        "name": "IVAN",
        "team": "Ravens",
        "country": "SWEDEN",
        "score": 1400,
        "matches_played": 25,
        "wins": 18,
        "active": True
    },
    {
        "name": "julia",
        "team": "Wolves",
        "country": "FinLand",
        "score": 200,
        "matches_played": 6,
        "wins": 0,
        "active": False
    },
    {
        "name": "  kevin",
        "team": "Dragons",
        "country": "Mexico",
        "score": 900,
        "matches_played": 17,
        "wins": 9,
        "active": True
    },
    {
        "name": "LISA",
        "team": "Knights",
        "country": "GERMANY",
        "score": 1100,
        "matches_played": 21,
        "wins": 10,
        "active": True
    },
    {
        "name": "  mark ",
        "team": "Ravens",
        "country": "sweden",
        "score": 50,
        "matches_played": 3,
        "wins": 0,
        "active": False
    },
    {
        "name": "Nina",
        "team": "Wolves",
        "country": "Finland",
        "score": 1250,
        "matches_played": 23,
        "wins": 14,
        "active": True
    },
    {
        "name": "oscar ",
        "team": "Dragons",
        "country": "mexico",
        "score": 780,
        "matches_played": 15,
        "wins": 7,
        "active": True
    }
]


normalized_player_data =  [
    {
        "name": player['name'].strip().title(),
        "team": player['team'].strip().title(),
        "country": player['country'].strip().title(),
        "score": player['score'],
        "matches_played": player['matches_played'],
        "wins": player['wins'],
        "active": player['active']
    } 
    for player in players
]

active_players = [
    player
    for player in normalized_player_data
    if player['active']
]
not_active_players = [
    player
    for player in normalized_player_data
    if not player['active']
]
players_with_min_three_wins = [
    player
    for player in normalized_player_data
    if player['wins'] >= 3
]
player_with_score_over_500 = [
    player
    for player in normalized_player_data
    if player['score'] > 500
]
swedish_players = [
    player 
    for player in normalized_player_data 
    if player['country'] == 'Sweden'
]
swedish_players_with_score_over_500 = [
    player 
    for player in normalized_player_data 
    if player['country'] == 'Sweden' and player['score'] > 500
]

player_countries = {player['country'] for player in normalized_player_data}
teams = {player['team'] for player in normalized_player_data}
player_scores = {player['name']: player['score'] for player in normalized_player_data}
player_wins = {player['name']: player['wins'] for player in normalized_player_data}
player_with_high_scores = {
    player['name']: player['score'] 
    for player in normalized_player_data 
    if player['score'] > 500
}

player_names = ["Anna", "David", "Sara", "Leo"]
ranking_points = [1200, 950, 1430, 1100, 100]
countries = ["Sweden", "Denmark", "Sweden", "Finland"]

ranks_list = list(zip(player_names, ranking_points))
player_countries_ranking = [
    {'name': name, 'country': country, 'ranking_points': ranking_points}
    for name, country, ranking_points in zip(player_names, countries, ranking_points)
]
player_country = list(zip(player_names, countries))

order_by_highest_scorer = sorted(normalized_player_data, key=lambda player: player['score'], reverse=True)
order_by_most_wins = sorted(normalized_player_data, key=lambda player: player['wins'], reverse=True)
order_by_matches_played = sorted(normalized_player_data, key=lambda player: player['matches_played'], reverse=True)
order_players_by_name = sorted(normalized_player_data, key=lambda player: player['name'])

# Print readable ranking
print("TOURNAMENT LEADERBOARD")
for rank, player in enumerate(order_by_highest_scorer, 1):
    name, score = player['name'], player['score']
    print(f'{rank}. {name} - {score} points')