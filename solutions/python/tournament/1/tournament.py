def tally(rows):
    teams = {}
    
    for row in rows:
        team1, team2, outcome = row.split(';')
        
        if team1 not in teams:
            teams[team1] = {'mp': 0, 'w': 0, 'd': 0, 'l': 0, 'p': 0}
        if team2 not in teams:
            teams[team2] = {'mp': 0, 'w': 0, 'd': 0, 'l': 0, 'p': 0}
        
        teams[team1]['mp'] += 1
        teams[team2]['mp'] += 1
        
        if outcome == 'win':
            teams[team1]['w'] += 1
            teams[team1]['p'] += 3
            teams[team2]['l'] += 1
        elif outcome == 'loss':
            teams[team1]['l'] += 1
            teams[team2]['w'] += 1
            teams[team2]['p'] += 3
        elif outcome == 'draw':
            teams[team1]['d'] += 1
            teams[team1]['p'] += 1
            teams[team2]['d'] += 1
            teams[team2]['p'] += 1
    
    sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]['p'], x[0]))
    
    result = ["Team                           | MP |  W |  D |  L |  P"]
    
    for team_name, stats in sorted_teams:
        result.append(
            f"{team_name:31}|{stats['mp']:3} |{stats['w']:3} |"
            f"{stats['d']:3} |{stats['l']:3} |{stats['p']:3}"
        )
    
    return result