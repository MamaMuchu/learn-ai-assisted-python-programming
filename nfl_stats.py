import pandas as pd
import matplotlib.pyplot as plt
nfl_data = pd.read_csv('nfl_offensive_stats.csv')
aaron_rodgers_passing_yards = nfl_data.loc[nfl_data.iloc[:, 3] == "Aaron Rodgers", nfl_data.columns[7]].sum()
print(aaron_rodgers_passing_yards)
"""
the 3rd column in data is player position, the fourth column is the player, and the 8th column is the passing yards. For
each player whose position in column 3 is "QB", determine the sum of yards from column 8
"""
qbs = nfl_data.loc[nfl_data.iloc[:, 2] == "QB"]
passing_yards_by_qb = qbs.groupby(qbs.columns[3])[qbs.columns[7]].sum()
print(passing_yards_by_qb)
"""
print the sum of the passing yards sorted by sum of passing yards in descending order
""" 
print(passing_yards_by_qb.sort_values(ascending=False))
"""
print the sum of the passing yards sorted by sum of passing yards in descending order. Do not include Tom Brady because
he win too much
"""
passing_yards_by_qb_no_brady = passing_yards_by_qb.drop('Tom Brady')
print(passing_yards_by_qb_no_brady.sort_values(ascending=False))
"""
plot the players by their number of passing yards only for players with more than 4000 passing yards
"""
filtered_qbs = passing_yards_by_qb[passing_yards_by_qb > 4000]
plt.figure(figsize=(12, 6))
plt.bar(filtered_qbs.index, filtered_qbs.values)
plt.xlabel("Quarterbacks")
plt.ylabel("Passing Yards")
plt.title("Passing Yards for QBs with over 4000 yards")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

