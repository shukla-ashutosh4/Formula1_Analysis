import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.font_manager as fm  # Import the font manager
import time

# Load the Formula1-Regular font
font_path = 'Formula1-Regular.otf'  # Make sure this path is correct
font_prop = fm.FontProperties(fname=font_path)

# Manually specify the colors for top drivers/teams
color_dict = {
    'Max Verstappen': '#00008B',  
    'Sergio Perez': '#00008B',    
    'Charles Leclerc': '#DC0000',   
    'Carlos Sainz': '#DC0000',     
    'Lewis Hamilton': '#00D2BE',  
    'George Russell': '#00D2BE',  
    'Fernando Alonso': '#006F62', 
    'Lance Stroll': '#006F62', 
    'Lando Norris': '#FF8700',    
    'Oscar Piastri': '#FF8700',   
    'Esteban Ocon': '#0090FF',
    'Valterri Bottas':'#A42134',
    'Kevin Magnussen': '#E6002B',
    'Zhou Guanyu': '#A42134',
    'Liam Lawson': '#ffffff',
    'Logan Sargeant': '#00A0DE',
    'Daniel Ricciardo':'#ffffff'
}

color_dicttt = {
    'Verstappen': '#00008B',  
    'Perez': '#00008B',    
    'Leclerc': '#DC0000',   
    'Sainz': '#DC0000',     
    'Hamilton': '#00D2BE',  
    'Russell': '#00D2BE',  
    'Alonso': '#006F62', 
    'Stroll': '#006F62', 
    'Norris': '#FF8700',    
    'Piastri': '#FF8700',   
    'Ocon': '#0090FF',
    'Tsunoda':'#ffffff',
    'Riccardo':'#ffffff',
    'Gasly': '#0090FF',
    'Hulkenberg': '#E6002B',
    'Albon': '#00A0DE',
    'Bottas': '#A42134',
    'Magnussen': '#E6002B',
    'Zhou':'#A42134',
    'Lawson': '#ffffff',
    'Sargeant': '#00A0DE',
    'Ricciardo':'#ffffff'

    
}

color_dictt = {
    'Red Bull Racing Honda RBPT': '#1E41FF', 
    'Ferrari': '#DC0000', 
    'Mercedes': '#00D2BE',
    'Aston Martin Aramco Mercedes': '#006F62',
    'McLaren Mercedes': '#FF8700', 
    'Alpine Renault': '#FF69B4',     
    'Alfa Romeo Ferrari': '#A42134',
    'Williams Mercedes': '#00A0DE',
    'AlphaTauri Honda RBPT': '#ffffff',
    'Haas Ferrari':'#E6002B'
}

# Load your datasets here
season2023RaceCalendar = pd.read_csv('Formula1_2023season_calendar.csv')
season2023RaceCalendar.set_index('Round', inplace=True)
season2023Drivers = pd.read_csv('Formula1_2023season_drivers.csv')
season2023Drivers.set_index('Abbreviation', inplace=True)
season2023Teams = pd.read_csv('Formula1_2023season_teams.csv')
season2023Teams.index = range(1,11)
season2023QualifyingResults = pd.read_csv('Formula1_2023season_qualifyingResults.csv')
season2023SprintRaceResults = pd.read_csv('Formula1_2023season_sprintResults.csv')
season2023RaceResults = pd.read_csv('Formula1_2023season_raceResults.csv')
season2023DotdVotes = pd.read_csv('Formula1_2023season_driverOfTheDayVotes.csv')
season2023DotdVotes.set_index('Track', inplace=True)
RaceTracks = season2023RaceCalendar.loc[:, 'Race Date':'Circuit Name']

# Set Streamlit title with custom font
st.markdown(
    """
    <style>
    @font-face {
        font-family: 'Formula1';
        src: url('Formula1-Regular.otf') format('opentype');
    }
    body {
        font-family: 'Formula1', sans-serif;
    }
    h1, h2, h3, h4, h5, h6, p {
        font-family: 'Formula1', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display your profile image
st.image("F1_new_logo.png", width=600)

# Set Streamlit title
st.title("🏎️ Formula 1 2023 Season Analysis")
st.write("Developed by Ashutosh Shukla")

st.header("Season Calendar 📅")    
season2023RaceCalendar

st.header("The Drivers 🙎🏻‍♂️")
season2023Drivers

st.header("Race Tracks 🏁")
RaceTracks

st.header("RedBull 2023 Wins 🥇")
redbull_wins = season2023RaceResults[(season2023RaceResults['Position'] == '1') & (season2023RaceResults['Team'] == 'Red Bull Racing Honda RBPT')]
redbull_wins.groupby('Track').head(10)
st.write(redbull_wins)

# Section: Driver Points Progression
st.header("2023 Season Top 10 Drivers' Points Progression")
driverStandingsTop10 = season2023Drivers['Driver'][:10].values
driverPointsTop10 = {}
driverPointsTop10Sprint = {}

for driver in driverStandingsTop10:
    driverPointsTop10[driver] = season2023RaceResults[season2023RaceResults['Driver'] == driver]['Points'].values
    driverPointsTop10Sprint[driver] = season2023SprintRaceResults[season2023SprintRaceResults['Driver'] == driver]['Points'].values

# Adjust points based on sprint results
sp = [3, 10, 20]
for driver in driverStandingsTop10:
    for i in range(len(sp)):
        if i < len(driverPointsTop10Sprint[driver]):
            driverPointsTop10[driver][sp[i]] += driverPointsTop10Sprint[driver][i]

# Plotting Driver Points Progression
plt.style.use('dark_background')
plt.figure(figsize=(11.5, 7))
plt.axis([0, len(season2023RaceResults['Track'].unique()) + 0.2, -5, 800])

# Use manually assigned colors
for i, driver in enumerate(driverStandingsTop10):
    ls = '--' if driver in ['Sergio Perez', 'Carlos Sainz', 'Lewis Hamilton', 'Fernando Alonso'] else '-'
    sprint_points = driverPointsTop10Sprint[driver]
    interpolated_sprint_points = np.interp(np.arange(len(driverPointsTop10[driver])), np.arange(len(sprint_points)), sprint_points)
    label = driver.split()[-1]  # Get last name for label
    color = color_dict.get(driver, '#ffffff')  # Use default white if no color specified
    plt.plot(np.cumsum(driverPointsTop10[driver] + interpolated_sprint_points), 
             label=label, color=color, linewidth=2, linestyle=ls)

plt.title('Formula 1 - 2023 Season\nTop 10 Drivers\' Points Progression (including sprint points)', 
          fontproperties=font_prop, fontsize=19, fontweight='bold', color='#bbbbbb')
plt.xlabel('RACES', fontproperties=font_prop, fontsize=16, fontweight='bold', color='#bbbbbb')
plt.ylabel('POINTS', fontproperties=font_prop, fontsize=16, fontweight='bold', color='#bbbbbb')
plt.xticks(np.arange(len(season2023RaceResults['Track'].unique())), 
           season2023RaceResults['Track'].unique(), rotation=80, fontsize=10, fontproperties=font_prop, color='#bbbbbb')
plt.yticks(np.arange(0, 800, 50), fontsize=12, fontproperties=font_prop, color='#bbbbbb')
plt.axvline(0, linewidth=1, color='#bbbbbb')
plt.axhline(0, linewidth=1, color='#bbbbbb')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', fontsize=9, prop=font_prop)
st.pyplot(plt)

st.header("Drivers Standings 2023")
racePoints = season2023RaceResults.groupby(['Driver', 'Team'])['Points'].sum().sort_values(ascending=False)
sprintRacePoints = season2023SprintRaceResults.groupby(['Driver'])['Points'].sum().sort_values(ascending=False)
for driver in season2023RaceResults['Driver'].unique():
    if driver not in season2023SprintRaceResults['Driver'].unique():
        sprintRacePoints.loc[driver] = 0
driverStandings = (racePoints + sprintRacePoints).fillna(0).sort_values(ascending=False)
driverStandings = pd.DataFrame(driverStandings).reset_index()
driverStandings['POS'] = range(1,23)
driverStandings['Points'] = driverStandings['Points'].astype(int)
driverStandings.set_index('POS', inplace=True)
driverStandings


st.header("Formula 1 - 2023 Season Points Earned From Sprint Races (Drivers)")

sprintRacePointsNonZero = sprintRacePoints[sprintRacePoints > 0]

plt.figure(figsize=(10, 5))
plt.axis([0, 50, 15, -0.6])

# Use the new color dictionary (color_dicttt) to set the bar colors
for i, driver in enumerate(sprintRacePointsNonZero.index.values):
    driver_name = driver.split()[1]
    color = color_dicttt.get(driver_name, '#bbbbbb')  # Default to '#bbbbbb' if driver not found in color_dicttt
    plt.barh([driver_name], [sprintRacePointsNonZero[i]], color=color)

for i in range(len(sprintRacePointsNonZero)):
    driver_name = sprintRacePointsNonZero.index.values[i].split()[1]
    color = color_dicttt.get(driver_name, '#bbbbbb')  # Use color_dicttt for text color as well
    plt.text(sprintRacePointsNonZero[i] - 1.7, i + 0.3, "{:2}".format(sprintRacePointsNonZero[i]),
             color=color, fontsize=14, fontweight='bold', fontproperties=font_prop)

plt.title('Formula 1 - 2023 Season\nPoints Earned From Sprint Races (Drivers)', 
          fontproperties=font_prop, fontsize=19, fontweight='bold', color='#bbbbbb')
plt.xlabel('POINTS', fontproperties=font_prop, fontsize=16, fontweight='bold', color='#bbbbbb')
plt.ylabel('DRIVERS', fontproperties=font_prop, fontsize=16, fontweight='bold', color='#bbbbbb')
plt.xticks(range(0, 50, 5), range(0, 50, 5), fontproperties=font_prop, color='#bbbbbb')
plt.yticks(fontproperties=font_prop,color='#bbbbbb')
plt.axvline(0, linewidth=1, color='#bbbbbb')

# Display the plot in Streamlit
st.pyplot(plt)


# Section: Constructor Standings
st.header("Constructor Standings")
racePointsTeam = season2023RaceResults.groupby('Team')['Points'].sum().sort_values(ascending=False)
sprintRacePointsTeam = season2023SprintRaceResults.groupby('Team')['Points'].sum().sort_values(ascending=False)
constructorStandings = (racePointsTeam + sprintRacePointsTeam).fillna(0).sort_values(ascending=False)
constructorStandings = pd.DataFrame(constructorStandings).reset_index()
constructorStandings['POS'] = range(1, len(constructorStandings) + 1)
constructorStandings.set_index('POS', inplace=True)
st.write(constructorStandings)

# Plotting Constructor Standings
teamNames = constructorStandings['Team'].unique()
teamPoints = {}
teamPointsSprint = {}
trackTeamPtsMerged = season2023RaceResults.groupby(['Track', 'Team'])['Points'].sum()
trackTeamPtsSprintMerged = season2023SprintRaceResults.groupby(['Track', 'Team'])['Points'].sum()

# Initialize team points
for team in teamNames:
    if team in trackTeamPtsMerged.index.get_level_values('Team'):
        teamPoints[team] = trackTeamPtsMerged[slice(None), team].reindex(season2023RaceResults['Track'].unique()).values
    else:
        teamPoints[team] = np.zeros(len(season2023RaceResults['Track'].unique()))

    if team in trackTeamPtsSprintMerged.index.get_level_values('Team'):
        teamPointsSprint[team] = trackTeamPtsSprintMerged[slice(None), team].reindex(season2023SprintRaceResults['Track'].unique()).values
    else:
        teamPointsSprint[team] = np.zeros(len(season2023SprintRaceResults['Track'].unique()))

# Adjust points based on sprint results
sp = [3, 10, 20]
for team in teamNames:
    for i in range(len(sp)):
        if i < len(teamPointsSprint[team]):
            teamPoints[team][sp[i]] += teamPointsSprint[team][i]

# Plotting team points progression
plt.figure(figsize=(11.5, 7))
plt.axis([0.2, len(season2023RaceResults['Track'].unique()) , -5, 800])

# Use manually assigned colors for teams
for i, team in enumerate(teamNames):
    color = color_dictt.get(team, '#ffffff')  # Use white if no color specified
    plt.plot(np.cumsum(teamPoints[team]), label=team, color=color, linewidth=2)

plt.title('Formula 1 - 2023 Season\nConstructor Points Progression', 
          fontproperties=font_prop, fontsize=19, fontweight='bold', color='#bbbbbb')
plt.xlabel('RACES', fontproperties=font_prop, fontsize=16, fontweight='bold', color='#bbbbbb')
plt.ylabel('POINTS', fontproperties=font_prop, fontsize=16, fontweight='bold', color='#bbbbbb')
plt.xticks(np.arange(len(season2023RaceResults['Track'].unique())), 
           season2023RaceResults['Track'].unique(), rotation=80, fontsize=10, fontproperties=font_prop, color='#bbbbbb')
plt.yticks(np.arange(0, 900, 50), fontsize=12, fontproperties=font_prop, color='#bbbbbb')
plt.axvline(0, linewidth=1, color='#bbbbbb')
plt.axhline(0, linewidth=1, color='#bbbbbb')
plt.legend(loc='upper left', fontsize=9, prop=font_prop)
st.pyplot(plt)

st.header("Race Results")
season2023RaceResults[season2023RaceResults['Position'] == '1'].set_index('Track').drop('Position', axis=1)


winners = season2023RaceResults[season2023RaceResults['Position'] == '1']['Driver'].value_counts()
plt.figure(figsize=(9,4.5))
plt.axis((0,20,3,-0.5))
for i, driver in enumerate(winners.index):
    driver_name = driver.split()[1]
    color = color_dicttt.get(driver_name, '#bbbbbb')
    plt.barh([driver_name], [winners[i]], color=color)

for i in range(len(winners)):
    driver_name = winners.index[i].split()[1]
    color = color_dicttt.get(driver_name, '#bbbbbb')
    plt.text(winners[i]-1.3, i+0.15, "{:>3}".format(winners[i]), fontsize=19, fontproperties=font_prop,fontweight='bold', color='#000000')
    plt.text(winners[i]+0.2, i+0.15, "{:>3}".format(winners[i]), fontsize=19, fontproperties=font_prop,fontweight='bold', color='k')

plt.title('Formula 1 - 2023 Season\n# of Race Wins (Drivers)', fontproperties=font_prop, fontsize=19, fontweight='bold', color='#bbbbbb')
plt.xlabel('RACE WINS', fontsize=14, fontweight='bold', fontproperties=font_prop,color='#bbbbbb')
plt.ylabel('DRIVERS',  fontsize=14, fontweight='bold', fontproperties=font_prop,color='#bbbbbb')
plt.xticks(fontproperties=font_prop,color='#bbbbbb')
plt.yticks(fontproperties=font_prop,color='#bbbbbb')
plt.axvline(0, color='#bbbbbb')
st.pyplot(plt)


st.header("Pole Position")
season2023PolePos = season2023RaceResults[season2023RaceResults['Starting Grid'] == 1].set_index('Track')
polePos = {}
for driver in season2023PolePos['Driver']:
    if driver not in polePos:   polePos[driver] = 1
    else:   polePos[driver] += 1
season2023PolePos


st.header("Sprint Pole Position")
season2023PolePosSprint = season2023SprintRaceResults[season2023SprintRaceResults['Starting Grid'] == 1] \
    .set_index('Track').drop('Starting Grid', axis=1)
polePosSprint = {}
for driver in season2023PolePosSprint['Driver']:
    if driver not in polePos:   polePos[driver] = 1
    else:   polePos[driver] += 1
season2023PolePosSprint


polePositions = pd.Series(polePos).sort_values(ascending=False)
plt.figure(figsize=(9,4.5))
plt.axis([0,20,7,-0.9])
for i, driver in enumerate(polePositions.index.values):
    driver_name = driver.split()[1]
    color = color_dicttt.get(driver_name, '#bbbbbb')  # Default to '#bbbbbb' if driver not found in color_dicttt
    plt.barh([driver_name], [polePositions[i]], color=color)

for i in range(len(polePositions)):
    driver_name = polePositions.index.values[i].split()[1]
    color = color_dicttt.get(driver_name, '#bbbbbb')  # Use color_dicttt for text color as well
    plt.text(polePositions[i] - 1, i + 0.3, "{:2}".format(polePositions[i]),
             color='#000000', fontsize=14, fontweight='bold', fontproperties=font_prop)

plt.title('Formula 1 - 2023 Season\n# of Pole Positions (Drivers)', fontproperties=font_prop, fontsize=19, fontweight='bold', color='#bbbbbb')
plt.xlabel('POLE POSITIONS', fontproperties=font_prop, fontsize=14, fontweight='bold', color='#bbbbbb')
plt.ylabel('DRIVERS', fontsize=14, fontproperties=font_prop, fontweight='bold', color='#bbbbbb')
plt.xticks(fontproperties=font_prop, color='#bbbbbb')
plt.yticks(fontproperties=font_prop,color='#bbbbbb')
plt.axvline(0, color='#bbbbbb')
st.pyplot(plt)


st.header("Formula 1 - 2023 Season Pole Positions Insights")

# Verstappen's Dominance
st.subheader("Verstappen's Dominance")
st.write("Max Verstappen secured 15 pole positions, far more than any other driver.")
st.write("This reflects his exceptional qualifying pace and Red Bull's strong car performance.")
st.write("Verstappen's dominance in qualifying set the stage for many of his race victories.")

# Ferrari's Strong Qualifying
st.subheader("Ferrari's Strong Qualifying")
st.write("Charles Leclerc managed to claim 6 pole positions, the second-highest number in the season.")
st.write("Carlos Sainz also contributed with 2 pole positions.")
st.write("Ferrari showcased a strong overall qualifying performance, indicating that they often had the pace to challenge for pole but couldn't always convert it into race wins.")

# Limited Competition at the Top
st.subheader("Limited Competition at the Top")
st.write("Only 7 drivers managed to secure a pole position throughout the entire season.")
st.write("This highlights the concentration of qualifying performance among a few top drivers and teams, with most pole positions coming from Red Bull and Ferrari.")

# Unexpected Performances
st.subheader("Unexpected Performances")
st.write("Kevin Magnussen (Haas) and Lando Norris (McLaren) each achieved 1 pole position.")
st.write("These results were unexpected and represent breakthrough performances from midfield teams, showing that on certain weekends, smaller teams can outperform expectations.")

# Hamilton's Struggles
st.subheader("Hamilton's Struggles")
st.write("Lewis Hamilton only secured 1 pole position during the season, a significant decline from his usual performance in previous years.")
st.write("This reflects Mercedes' struggles throughout the 2023 season, as they couldn't consistently compete for pole positions like they had in the past.")

# Final Insights
st.write("These insights highlight the competitive landscape of the 2023 Formula 1 season in qualifying, with Verstappen and Red Bull showing clear superiority, while Ferrari remained competitive and other teams had occasional standout performances.")



podiumFinishes = season2023RaceResults[season2023RaceResults['Position'].isin(['1','2','3'])]['Driver'].value_counts()

fig, ax = plt.subplots(figsize=(9,5))
ax.axis([0,25,11,-0.5])
ax.barh([driver.split()[1] for driver in podiumFinishes.index], podiumFinishes, color=[color_dicttt[driver.split()[1]] for driver in podiumFinishes.index])
for i in range(len(podiumFinishes)):
    ax.text(podiumFinishes[i]-1.35, i+0.2, "{:>3}".format(podiumFinishes[i]), fontsize=16, color='k')
ax.set_title('Formula 1 - 2023 Season\n# of Podium Finishes (Drivers)',fontproperties=font_prop, fontsize=19, weight='bold', color='#bbbbbb')
ax.set_xlabel('PODIUMS', fontproperties=font_prop, fontsize=14, fontweight='bold', color='#bbbbbb')
ax.set_ylabel('DRIVERS', fontproperties=font_prop, fontsize=14, fontweight='bold', color='#bbbbbb')
plt.xticks(fontproperties=font_prop, color='#bbbbbb')
plt.yticks(fontproperties=font_prop,color='#bbbbbb')
ax.axvline(0, color='#bbbbbb')

st.pyplot(fig)


st.header("Formula 1 - 2023 Season Podium Finishes Insights")

# Verstappen's Dominance
st.subheader("Verstappen's Dominance")
st.write("Max Verstappen achieved an extraordinary 21 podium finishes, far surpassing any other driver.")
st.write("This reflects his exceptional consistency and performance throughout the season, solidifying his dominance in the championship.")

# Red Bull's Strength
st.subheader("Red Bull's Strength")
st.write("With Verstappen’s 21 podiums and Sergio Perez securing 9 podiums, Red Bull Racing demonstrated they had the strongest overall package.")
st.write("Both drivers frequently finished in top positions, highlighting Red Bull’s competitive edge throughout the season.")

# Alonso’s Resurgence
st.subheader("Alonso’s Resurgence")
st.write("Fernando Alonso managed to secure 8 podium finishes, signaling a resurgence for both Aston Martin and Alonso himself.")
st.write("This indicates a strong performance from the veteran driver and his team, competing effectively at the front of the grid.")

# Tight Midfield Battle
st.subheader("Tight Midfield Battle")
st.write("Several drivers, including Lando Norris, Lewis Hamilton, and Charles Leclerc, achieved a close number of podium finishes.")
st.write("This reflects a competitive midfield, with multiple teams and drivers capable of reaching the podium at different stages of the season.")

# Ferrari’s Struggles
st.subheader("Ferrari’s Struggles")
st.write("Charles Leclerc achieved 6 podiums, while Carlos Sainz only managed 3, suggesting that Ferrari had a less competitive season compared to their 2022 performance.")
st.write("This indicates struggles in both performance and consistency for Ferrari throughout the year.")

# Mercedes Consistency
st.subheader("Mercedes Consistency")
st.write("Both Lewis Hamilton and George Russell consistently reached the podium, showing that Mercedes maintained a level of competitiveness, even if they were not as dominant as in previous years.")
st.write("Their podium finishes reflect the team’s ability to compete regularly, even if they couldn't match Red Bull’s level of performance.")

# Conclusion
st.subheader("Conclusion")
st.write("The 2023 season was dominated by Red Bull, particularly through Verstappen’s exceptional form. However, there was a competitive battle for the remaining podium positions among the midfield teams. The season also saw a resurgence for Fernando Alonso and Aston Martin, while Ferrari and Mercedes experienced varied levels of success compared to previous seasons.")
top10Finishes = season2023RaceResults[season2023RaceResults['Position'].isin([str(i) for i in range(1,11)])] \
                ['Driver'].value_counts()

fig, ax = plt.subplots(figsize=(10,6.5))
ax.axis([0,25,21,-0.6])
ax.barh([" ".join(driver.split()[1:]) for driver in top10Finishes.index], top10Finishes, color=[color_dicttt.get(" ".join(driver.split()[1:]), 'gray') for driver in top10Finishes.index])
for i in range(len(top10Finishes)):
    ax.text(top10Finishes[i]-0.9, i+0.25, "{:>3}".format(top10Finishes[i]), fontsize=12,  fontweight='bold', color='k')
ax.set_title('Formula 1 - 2023 Season\n# of Top 10 Finishes (Drivers)', fontsize=25, fontproperties=font_prop,fontweight='bold', color='#bbbbbb')
ax.set_xlabel('TOP 10 FINISHES', fontsize=14, fontproperties=font_prop, fontweight='bold', color='#bbbbbb')
ax.set_ylabel('DRIVERS', fontsize=14,fontproperties=font_prop, fontweight='bold', color='#bbbbbb')
plt.xticks(fontproperties=font_prop, color='#bbbbbb')
plt.yticks(fontproperties=font_prop,color='#bbbbbb')
ax.set_xticks(range(0,22,2))
ax.axvline(0, color='#bbbbbb')

st.pyplot(fig)


st.header("Formula 1 - 2023 Season Top 10 Finishes")

# 1. Verstappen's Exceptional Season
st.subheader("1. Verstappen's Exceptional Season")
st.write("22 top 10 finishes (potentially perfect record)")
st.write("Indicates dominant championship performance")

# 2. Mercedes' Resurgence
st.subheader("2. Mercedes' Resurgence")
st.write("Hamilton: 20 top 10 finishes")
st.write("Russell: 17 top 10 finishes")
st.write("Significant improvement from 2022 struggles")

# 3. Red Bull's Strong Package
st.subheader("3. Red Bull's Strong Package")
st.write("Verstappen: 22 top 10 finishes")
st.write("Perez: 19 top 10 finishes")
st.write("Most competitive car on the grid")

# 4. Alonso's Renaissance
st.subheader("4. Alonso's Renaissance")
st.write("19 top 10 finishes")
st.write("Demonstrates top-tier performance")
st.write("Significant improvement for Aston Martin")

# 5. Ferrari's Consistency Issues
st.subheader("5. Ferrari's Consistency Issues")
st.write("Sainz: 18 top 10 finishes")
st.write("Leclerc: 16 top 10 finishes")
st.write("Suggests potential reliability or strategic challenges")

# 6. Tight Midfield Battle
st.subheader("6. Tight Midfield Battle")
st.write("Sainz, Russell, Norris, Leclerc: 16-18 top 10 finishes each")
st.write("Highly competitive midfield")

# 7. Alpine's Solid Performance
st.subheader("7. Alpine's Solid Performance")
st.write("Ocon and Gasly: 11+ top 10 finishes each")
st.write("Consistent points-scoring presence")

# 8. Struggles of Bottom Teams
st.subheader("8. Struggles of Bottom Teams")
st.write("Magnussen, Zhou, Hulkenberg: ≤5 top 10 finishes")
st.write("Illustrates performance gap in current F1")

# 9. Rookie Performances
st.subheader("9. Rookie Performances")
st.write("Piastri: 11 top 10 finishes (promising)")
st.write("Sargeant: 1 top 10 finish (steeper learning curve)")

# 10. Midseason Driver Changes
st.subheader("10. Midseason Driver Changes")
st.write("Lawson, Ricciardo: 1 top 10 finish each")
st.write("Suggests dynamic driver lineup changes during the season")

# Conclusion
st.subheader("Conclusion")
st.write("This analysis provides a comprehensive overview of the 2023 F1 season's competitive landscape, team performances, and individual driver achievements.")

st.header("Qualifying Results")
st.write(season2023QualifyingResults[season2023QualifyingResults['Position'] == '1'].set_index('Track').drop('Position', axis=1))

fastestTimeQualifying = season2023QualifyingResults[season2023QualifyingResults['Position'] == '1']['Driver'].value_counts()

fig, ax = plt.subplots(figsize=(9,5))
ax.axis([0,15,5,-0.6])
ax.barh([driver.split()[1] for driver in fastestTimeQualifying.index], fastestTimeQualifying, color=[color_dicttt[driver.split()[1]] for driver in fastestTimeQualifying.index])
for i in range(len(fastestTimeQualifying)):
    ax.text(fastestTimeQualifying[i]-0.59, i+0.15, fastestTimeQualifying[i], fontsize=17, fontweight='bold', color='k', fontproperties=font_prop)
ax.set_title('Formula 1 - 2023 Season\n# of Fastest Time Set in Qualifying (Drivers)', fontsize=19, fontweight='bold', color='#bbbbbb', fontproperties=font_prop)
ax.set_xlabel('FASTEST TIME SET', fontsize=14, fontweight='bold', color='#bbbbbb', fontproperties=font_prop)
ax.set_ylabel('DRIVERS', fontsize=14, fontweight='bold', color='#bbbbbb', fontproperties=font_prop)
ax.tick_params(axis='x', colors='#bbbbbb')
ax.tick_params(axis='y', colors='#bbbbbb')
ax.axvline(0, color='#bbbbbb')

st.pyplot(fig)

# Title
st.header("Formula 1 - 2023 Season Fastest Qualifying Times Insights")

# Data
data = {
    "Driver": ["Verstappen", "Leclerc", "Sainz", "Perez", "Hamilton"],
    "FastestTimes": [13, 4, 2, 2, 1],
    "Team": ["Red Bull", "Ferrari", "Ferrari", "Red Bull", "Mercedes"]
}
df = pd.DataFrame(data)

# Animated bar chart
st.subheader("Fastest Qualifying Times by Driver")

# Key Insights
st.subheader("Key Insights")

insights = [
    "Verstappen's Dominance: 13 out of 22 fastest qualifying times",
    "Ferrari's Competitiveness: 6 combined fastest times (Leclerc 4, Sainz 2)",
    "Red Bull's Overall Strength: 15 out of 22 fastest qualifying sessions",
    "Mercedes' Struggles: Only 1 fastest qualifying time for Hamilton",
    "Limited Top Performers: Only 5 drivers set fastest qualifying times all season"
]

for insight in insights:
    st.write("• " + insight)
    time.sleep(0.1)  # Add a slight delay for animation effect

# Team Dominance
st.subheader("Team Dominance in Fastest Qualifying Times")

team_data = df.groupby('Team')['FastestTimes'].sum().reset_index()
st.bar_chart(team_data.set_index('Team')['FastestTimes'])

# Conclusion
st.subheader("Conclusion")
conclusion = """
The 2023 Formula 1 season's qualifying sessions were largely dominated by Red Bull and Ferrari,
with Verstappen and Leclerc leading their teams. While Red Bull's overall strength was clear,
Ferrari remained competitive in qualifying, but Mercedes and other teams struggled to match the top two.
Verstappen's consistency in setting fastest laps and starting from pole contributed significantly to his dominance,
while Leclerc and Ferrari put up a fight in one-lap performance.
"""
st.write(conclusion)

# Interactive element
st.subheader("Explore Driver Performance")
selected_driver = st.selectbox("Select a driver:", df['Driver'])
driver_data = df[df['Driver'] == selected_driver]
if selected_driver == "Hamilton":
    st.write(f"{selected_driver} set the fastest qualifying time in {driver_data['FastestTimes'].values[0]} race.")
else:
    st.write(f"{selected_driver} set the fastest qualifying time in {driver_data['FastestTimes'].values[0]} races.")

# # Add a fun fact
# st.sidebar.title("Fun Fact")
# st.sidebar.write("Did you know? The total number of fastest qualifying times set in the 2023 season was", 
#                  df['FastestTimes'].sum())

# Data
qualiQ2 = season2023QualifyingResults[season2023QualifyingResults['Position'].isin([str(i) for i in range(1,16)])] \
    ['Driver'].value_counts()

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10,6))

# Set the axis limits
ax.axis([0,25,22,-0.6])

# Create a horizontal bar chart
ax.barh([" ".join(driver.split()[1:]) for driver in qualiQ2.index], qualiQ2, color=[color_dicttt.get(" ".join(driver.split()[1:]), 'gray') for driver in qualiQ2.index])

# Add text to the bars
for i in range(len(qualiQ2)):
    ax.text(qualiQ2[i]-0.75, i+0.24, "{:>2}".format(qualiQ2[i]), fontsize=12, fontweight='bold',color='k')

# Set the title and labels
ax.set_title("Formula 1 - 2023 Season\n# of Q2 Appearances in Qualifying (Drivers)", fontsize=19, fontweight='bold', fontproperties = font_prop, color='#bbbbbb')
ax.set_xlabel('Q2 APPEARANCES', fontsize=14, fontweight='bold', fontproperties=font_prop, color='#bbbbbb')
ax.set_ylabel('DRIVERS', fontsize=14, fontweight='bold', fontproperties=font_prop, color='#bbbbbb')

# Set the tick colors and labels
ax.tick_params(axis='x', colors='#bbbbbb', labelsize=9)
ax.tick_params(axis='y', colors='#bbbbbb', labelsize=9)

# Add a vertical line at x=0
ax.axvline(0, color='#bbbbbb')

# Display the plot
st.pyplot(fig)


st.header("Formula 1 - 2023 Season Number of Q2 Appearances in Qualifying (Drivers)")

st.subheader("Dominance and Consistency")
st.write("Verstappen and Hamilton: The chart clearly demonstrates the dominance of Max Verstappen and Lewis Hamilton. Both drivers have appeared in Q2 a significant number of times, showcasing their exceptional qualifying performances throughout the season. Verstappen's 22 appearances highlight his consistent ability to secure a place in the second qualifying session.")

st.subheader("Close Competition")
st.write("Leclerc, Sainz, Alonso, and Russell: Following closely behind Verstappen and Hamilton are Charles Leclerc, Carlos Sainz, Fernando Alonso, and George Russell. These drivers have also made consistent appearances in Q2, indicating a high level of competition among the top teams.")

st.subheader("Midfield Battle")
st.write("Perez, Ocon, Norris, Gasly, Albon, Hulkenberg: The midfield drivers, including Sergio Perez, Esteban Ocon, Lando Norris, Pierre Gasly, Alex Albon, and Nico Hulkenberg, have shown a decent level of performance in qualifying. Their appearances in Q2 suggest that the competition in the midfield was also intense.")

st.subheader("Variability in Performance")
st.write("Piastri, Stroll, Bottas, Tsunoda, Magnussen: Drivers like Oscar Piastri, Lance Stroll, Valtteri Bottas, Yuki Tsunoda, and Kevin Magnussen experienced some fluctuations in their qualifying performances. While they managed to secure Q2 appearances on multiple occasions, their numbers were slightly lower compared to the top contenders.")

st.subheader("Struggling Drivers")
st.write("Zhou, Sargeant, Ricciardo, De Vries, Lawson: Zhou Guanyu, Logan Sargeant, Daniel Ricciardo, Nyck de Vries, and Liam Lawson faced challenges in qualifying, with significantly fewer Q2 appearances. These drivers might have struggled to adapt to the demands of Formula 1 or encountered difficulties with their cars or teams.")

# Data
qualiQ3 = season2023QualifyingResults[season2023QualifyingResults['Position'].isin([str(i) for i in range(1,11)])] \
    ['Driver'].value_counts()

# Create figure
fig, ax = plt.subplots(figsize=(10,6))

# Set axis limits
ax.axis([0,22,21,-0.6])

# Create bar chart
ax.barh([" ".join(driver.split()[1:]) for driver in qualiQ3.index], qualiQ3, color=[color_dicttt.get(" ".join(driver.split()[1:]), 'gray') for driver in qualiQ3.index])

# Add text to bars
for i in range(len(qualiQ3)):
    ax.text(qualiQ3[i]-0.75, i+0.24, "{:>2}".format(qualiQ3[i]), fontsize=12, fontweight='bold', color='k')

# Set title and labels
ax.set_title("Formula 1 - 2023 Season\n# of Q3 Appearances in Qualifying (Drivers)", fontsize=19,fontproperties = font_prop, fontweight='bold', color='#bbbbbb')
ax.set_xlabel('Q3 APPEARANCES', fontproperties = font_prop, fontsize=14, fontweight='bold', color='#bbbbbb')
ax.set_ylabel('DRIVERS', fontsize=14, fontproperties = font_prop, fontweight='bold', color='#bbbbbb')

# Set ticks
# ax.set_xticks(range(0,23,2))
# ax.set_xticklabels(range(0,23,2), color='#bbbbbb')
# ax.set_yticks(fontsize=9, color='#bbbbbb')

# Add vertical line
ax.axvline(0, color='#bbbbbb')

# Display plot
st.pyplot(fig)

import streamlit as st

st.header("Elaborated Insights from the Formula 1 2023 Season Q3 Appearances Chart")

st.subheader("Dominance and Consistency")
st.write("Verstappen, Leclerc, and Alonso: The chart highlights the exceptional qualifying performances of Max Verstappen, Charles Leclerc, and Fernando Alonso. Their consistent appearances in Q3 underscore their dominance and ability to secure top starting positions throughout the season.")

st.subheader("Close Competition")
st.write("Sainz, Russell, and Hamilton: Following closely behind the top three are Carlos Sainz, George Russell, and Lewis Hamilton. These drivers have also made significant appearances in Q3, showcasing a competitive level of qualifying performance.")

st.subheader("Midfield Battle")
st.write("Norris, Piastri, Perez, Gasly: The midfield drivers, including Lando Norris, Oscar Piastri, Sergio Perez, and Pierre Gasly, have demonstrated solid qualifying performances, with multiple appearances in Q3. This indicates a competitive and dynamic midfield battle.")

st.subheader("Variability in Performance")
st.write("Ocon, Hulkenberg, Stroll, Albon, Bottas, Tsunoda: Drivers like Esteban Ocon, Nico Hulkenberg, Lance Stroll, Alex Albon, Valtteri Bottas, and Yuki Tsunoda experienced some fluctuations in their qualifying performances. While they secured Q3 appearances on several occasions, their numbers were lower compared to the top contenders.")

st.subheader("Struggling Drivers")
st.write("Magnussen, Zhou, Sargeant, Lawson, Ricciardo: Zhou Guanyu, Logan Sargeant, Kevin Magnussen, Nyck de Vries, and Liam Lawson faced significant challenges in qualifying, with very few Q3 appearances. These drivers might have struggled to adapt to the demands of Formula 1 or encountered difficulties with their cars or teams.")

# Data
DNFdriver = season2023RaceResults[season2023RaceResults['Time/Retired'] == 'DNF']['Driver'].value_counts()

# Create figure
fig, ax = plt.subplots(figsize=(9,6))

# Set axis limits
ax.axis([0,8,19,-0.6])

# Create bar chart
ax.barh([driver.split()[1] for driver in DNFdriver.index], DNFdriver, color=[color_dicttt.get(driver.split()[1], 'gray') for driver in DNFdriver.index])

# Add text to bars
for i in range(len(DNFdriver)):
    ax.text(DNFdriver[i]-0.17, i+0.22, DNFdriver[i], fontsize=12, fontweight='bold', color='k')

# Set title and labels
ax.set_title('Formula 1 - 2023 Season\n# of DNFs in Races (Drivers)', fontsize=19, fontproperties = font_prop, fontweight='bold', color='#bbbbbb')
ax.set_xlabel('DNFs', fontsize=14, fontweight='bold', fontproperties = font_prop, color='#bbbbbb')
ax.set_ylabel('DRIVERS', fontsize=14, fontweight='bold', fontproperties = font_prop, color='#bbbbbb')

# Add vertical line
ax.axvline(0, color='#bbbbbb')

# Display plot
st.pyplot(fig)

st.header("Elaborated Insights from the Formula 1 2023 Season DNFs Chart")

st.subheader("Reliability Issues")
st.write("Ocon and Sargeant: The chart highlights the reliability concerns for Esteban Ocon and Logan Sargeant, both of whom experienced a significant number of DNFs (7 each). This suggests potential mechanical issues or driver errors that contributed to their retirements.")

st.subheader("Consistent Performance")
st.write("Magnussen, Stroll, Russell, and Albon: A group of drivers, including Kevin Magnussen, Lance Stroll, George Russell, and Alex Albon, demonstrated relatively consistent performance with 4 DNFs each. While they faced some reliability issues, their overall performance was more stable compared to the top two.")

st.subheader("Midfield Challenges")
st.write("Piastri, Leclerc, Zhou, Bottas, De, Hulkenberg: The midfield drivers, including Oscar Piastri, Charles Leclerc, Zhou Guanyu, Valtteri Bottas, Nyck de Vries, and Nico Hulkenberg, faced their fair share of reliability problems. This suggests that the midfield competition was not only close on the track but also in terms of car reliability.")

st.subheader("Variability in Performance")
st.write("Sainz, Tsunoda, Perez, Alonso, Hamilton, Norris: Drivers like Carlos Sainz, Yuki Tsunoda, Sergio Perez, Fernando Alonso, Lewis Hamilton, and Lando Norris experienced a mix of reliability issues and strong performances. Their DNF numbers were relatively low, indicating a balance between reliability and competitiveness.")

# Data
DNFtrack = season2023RaceResults[season2023RaceResults['Time/Retired'] == 'DNF']['Track'].value_counts()

# Create figure
fig, ax = plt.subplots(figsize=(9,6))

# Set axis limits
ax.axis([0,10,20,-0.6])

# Create bar chart
ax.barh(DNFtrack.index, DNFtrack, color='#6abeca')

# Add text to bars
for i in range(len(DNFtrack)):
    ax.text(DNFtrack[i]-0.18, i+0.22, DNFtrack[i], fontsize=12, fontproperties=font_prop, fontweight='bold', color='k')

# Set title and labels
ax.set_title('Formula 1 - 2023 Season\n# of DNFs in Races (Tracks)', fontproperties = font_prop,fontsize=19, fontweight='bold', color='#bbbbbb')
ax.set_xlabel('DNFs', fontsize=14, fontweight='bold',fontproperties = font_prop, color='#bbbbbb')
ax.set_ylabel('TRACKS', fontsize=14, fontweight='bold', fontproperties = font_prop,color='#bbbbbb')

plt.xticks(fontproperties=font_prop, color='#bbbbbb')
plt.yticks(fontproperties=font_prop,color='#bbbbbb')
# Add vertical line
ax.axvline(0, color='#bbbbbb')

# Display plot
st.pyplot(fig)

import streamlit as st

st.header("Elaborated Insights from the Formula 1 2023 Season DNFs (Tracks) Chart")

st.subheader("Reliability Challenges")
st.write("Australia, Brazil, and Mexico: The chart highlights the reliability concerns at certain tracks, particularly Australia, Brazil, and Mexico, which experienced a higher number of DNFs. These circuits might have specific characteristics or conditions that contributed to mechanical failures or driver errors.")

st.subheader("Consistent Issues")
st.write("Bahrain, Las Vegas, United States, Netherlands, Hungary, Great Britain: Several tracks, including Bahrain, Las Vegas, the United States, the Netherlands, Hungary, and Great Britain, consistently faced reliability challenges throughout the season. This suggests underlying issues with the track layout, conditions, or infrastructure that affected driver performance.")

st.subheader("Variability in Performance")
st.write("Belgium, Saudi Arabia, Canada, Qatar, Monaco, Azerbaijan: Tracks like Belgium, Saudi Arabia, Canada, Qatar, Monaco, and Azerbaijan experienced a mix of reliability issues and relatively consistent performance. This indicates that factors like track layout, weather conditions, and driver skill played a significant role in determining the number of DNFs.")

st.subheader("Few Reliability Concerns")
st.write("Italy, Austria, Abu Dhabi: The tracks of Italy, Austria, and Abu Dhabi had the fewest DNFs, suggesting that their conditions and layouts were more conducive to consistent racing.")

st.header("Driver Of The Day 2023")
season2023DotdVotes

# Data
DotdAwards = season2023DotdVotes['1st Place'].value_counts()

# Create figure
fig, ax = plt.subplots(figsize=(9,5))

# Set axis limits
ax.axis([0,5.5,11,-0.5])

# Create bar chart
ax.barh([" ".join(driver.split()[1:]) for driver in DotdAwards.index], DotdAwards, color=[color_dicttt.get(" ".join(driver.split()[1:]), 'gray') for driver in DotdAwards.index])

# Add text to bars
for i in range(len(DotdAwards)):
    ax.text(DotdAwards[i]-0.18, i+0.2, DotdAwards[i], fontsize=16, fontproperties = font_prop,fontweight='bold', color='k')

# Set title and labels
ax.set_title('Formula 1 - 2023 Season\n# of Driver of the Day Awards (Drivers)', fontproperties = font_prop, fontsize=19, fontweight='bold', color='#bbbbbb')
ax.set_xlabel('DotD AWARDS', fontsize=14, fontweight='bold', fontproperties = font_prop,color='#bbbbbb')
ax.set_ylabel('DRIVERS', fontsize=14, fontweight='bold', fontproperties = font_prop,color='#bbbbbb')
plt.xticks(fontproperties=font_prop, color='#bbbbbb')
plt.yticks(fontproperties=font_prop,color='#bbbbbb')
# Add vertical line
ax.axvline(0, color='#bbbbbb')

# Display plot
st.pyplot(fig)

st.header("Elaborated Insights from the Formula 1 2023 Season Driver of the Day Awards Chart")

st.subheader("Dominance")
st.write("Norris: Lando Norris emerged as a clear leader in terms of Driver of the Day awards, securing five such accolades throughout the season. This highlights his impressive performances and ability to consistently impress fans and experts.")

st.subheader("Close Competition")
st.write("Verstappen and Perez: Max Verstappen and Sergio Perez, both from Red Bull Racing, finished in second place with three awards each. This close competition among the top drivers demonstrates the high level of racing and the difficulty of securing Driver of the Day honors.")

st.subheader("Consistent Performance")
st.write("Alonso, Sainz, and Piastri: Fernando Alonso, Carlos Sainz, and Oscar Piastri each received two Driver of the Day awards, showcasing their consistent performances and ability to deliver standout drives throughout the season.")

st.subheader("Variability in Performance")
st.write("Ocon, Hamilton, Albon, Leclerc, and Tsunoda: A group of drivers, including Esteban Ocon, Lewis Hamilton, Alex Albon, Charles Leclerc, and Yuki Tsunoda, received one Driver of the Day award each. This indicates that while they had some standout performances, their overall consistency might have been less compared to the top contenders.")

# Data
DotdAppearance = {}
for place in range(5):
    for driver in range(len(season2023DotdVotes)):
        d = season2023DotdVotes.iloc[driver,place*2]
        if d not in DotdAppearance.keys():   DotdAppearance[d] = 1
        else:   DotdAppearance[d] += 1
DotdAppearanceDf = pd.Series(DotdAppearance).sort_values(ascending=False)

# Create figure
fig, ax = plt.subplots(figsize=(9.5,6))

# Set axis limits
ax.axis([0,22,15,-0.5])

# Create bar chart
ax.barh([" ".join(driver.split()[1:]) for driver in DotdAppearanceDf.index], DotdAppearanceDf, color=[color_dicttt.get(" ".join(driver.split()[1:]), 'gray') for driver in DotdAppearanceDf.index])

# Add text to bars
for i in range(len(DotdAppearanceDf)):
    ax.text(DotdAppearanceDf[i]-0.9, i+0.25, "{:>3}".format(DotdAppearanceDf[i]), fontproperties=font_prop, fontsize=12, fontweight='bold', color='k')

# Set title and labels
ax.set_title('Formula 1 - 2023 Season\n# of Appearances in Driver of the Day Votes (Drivers)',fontproperties=font_prop, fontsize=18, fontweight='bold', color='#bbbbbb')
ax.set_xlabel('DotD APPEARANCES', fontsize=14, fontweight='bold',fontproperties=font_prop, color='#bbbbbb')
ax.set_ylabel('DRIVERS', fontsize=14, fontweight='bold',fontproperties=font_prop, color='#bbbbbb')

plt.xticks(fontproperties=font_prop, color='#bbbbbb')
plt.yticks(fontproperties=font_prop,color='#bbbbbb')

# Add vertical line
ax.axvline(0, color='#bbbbbb')

# Display plot
st.pyplot(fig)

import streamlit as st

st.header("Elaborated Insights from the Formula 1 2023 Season Driver of the Day Votes (Drivers) Chart")

st.subheader("Dominance")
st.write("Verstappen: Max Verstappen's 21 appearances in Driver of the Day votes clearly demonstrate his dominance throughout the season. His consistent strong performances and ability to impress fans and experts earned him a significant number of nominations.")

st.subheader("Close Competition")
st.write("Perez and Hamilton: Following closely behind Verstappen are Sergio Perez and Lewis Hamilton, both with 15 and 14 appearances, respectively. This indicates a competitive battle for the top spot, with Perez and Hamilton consistently delivering impressive drives.")

st.subheader("Consistent Performance")
st.write("Norris and Leclerc: Lando Norris and Charles Leclerc both secured 12 appearances in Driver of the Day votes, showcasing their consistent ability to deliver standout performances and earn recognition from fans and experts.")

st.subheader("Midfield Contenders")
st.write("Alonso, Piastri, Russell, and Sainz: Fernando Alonso, Oscar Piastri, George Russell, and Carlos Sainz demonstrated solid performances in the midfield, with appearances in Driver of the Day votes ranging from 4 to 10. This highlights the competitive nature of the midfield battle.")

st.subheader("Variability in Performance")
st.write("Albon, Tsunoda, Gasly, Ocon, Lawson, and Ricciardo: Drivers like Alex Albon, Yuki Tsunoda, Pierre Gasly, Esteban Ocon, Nyck de Vries, and Daniel Ricciardo experienced some fluctuations in their performances, as evidenced by their lower number of appearances in Driver of the Day votes.")

# Data
driversTotalLaps = season2023RaceResults.groupby('Driver')['Laps'].sum().sort_values(ascending=False)[:20]

# Create figure
fig, ax = plt.subplots(figsize=(10,6))

# Set axis limits
ax.axis([90,1500,19.6,-0.6])

# Create bar chart
ax.barh([" ".join(driver.split()[1:]) for driver in driversTotalLaps.index], driversTotalLaps, color=[color_dicttt.get(" ".join(driver.split()[1:]), 'gray') for driver in driversTotalLaps.index])

# Add text to bars
for i in range(len(driversTotalLaps)):
    ax.text(driversTotalLaps[i]-100, i+0.25, driversTotalLaps[i], fontproperties=font_prop,fontsize=12, fontweight='bold', color='k')

# Add note
ax.text(999, 19.3, "* Reserve Drivers Not Included",fontproperties=font_prop, fontweight='bold', color='#bbbbbb')

# Set title and labels
ax.set_title('Formula 1 - 2023 Season\nTotal Laps Driven in Race Sessions (Drivers)',fontproperties=font_prop, fontsize=19, fontweight='bold', color='#bbbbbb')
ax.set_xlabel('TOTAL LAPS', fontsize=14, fontweight='bold',fontproperties=font_prop, color='#bbbbbb')
ax.set_ylabel('DRIVERS', fontsize=14, fontweight='bold',fontproperties=font_prop, color='#bbbbbb')

plt.xticks(fontproperties=font_prop, color='#bbbbbb')
plt.yticks(fontproperties=font_prop,color='#bbbbbb')

# Add vertical line
ax.axvline(90, color='#bbbbbb')

# Display plot
st.pyplot(fig) 

st.header("Elaborated Insights from the Formula 1 2023 Season Total Laps Driven (Drivers) Chart")

st.subheader("Verstappen's Dominance")
st.write("Max Verstappen's impressive total of 1325 laps driven clearly demonstrates his dominance throughout the 2023 season. His consistent participation in races and his ability to complete a high number of laps highlight his reliability and performance.")

st.subheader("Close Competition")
st.write("Alonso, Norris, Hamilton, and Russell: Following closely behind Verstappen are Fernando Alonso, Lando Norris, Lewis Hamilton, and George Russell, all of whom have driven over 1200 laps. This indicates a competitive battle among the top drivers, with consistent participation and strong performance.")

st.subheader("Midfield Battle")
st.write("Hulkenberg, Gasly, Sainz, Zhou, Bottas, Perez, Tsunoda, and Piastri: The midfield drivers, including Nico Hulkenberg, Pierre Gasly, Carlos Sainz, Zhou Guanyu, Valtteri Bottas, Sergio Perez, Yuki Tsunoda, and Oscar Piastri, have also driven a significant number of laps, showcasing their consistent participation and competitive nature.")

st.subheader("Variability in Performance")
st.write("Magnussen, Albon, Stroll, Leclerc, Sargeant, Ocon, and de Vries: Drivers like Kevin Magnussen, Alex Albon, Lance Stroll, Charles Leclerc, Logan Sargeant, Esteban Ocon, and Nyck de Vries have driven fewer laps, indicating some missed races or retirements during the season.")

import streamlit as st
import matplotlib.pyplot as plt

# Data
teamsTotalLaps = season2023RaceResults.groupby('Team')['Laps'].sum().sort_values(ascending=False)

# Create figure
fig, ax = plt.subplots(figsize=(10,5))

# Set axis limits
ax.axis([2000,2600,9.5,-0.5])

# Create bar chart
teamLabel = [" ".join(team.split()[:2]) if len(team.split()) > 2 else team.split()[0] for team in teamsTotalLaps.index]
ax.barh(teamLabel, teamsTotalLaps, color=[color_dictt.get(team, 'gray') for team in teamsTotalLaps.index])

# Add text to bars
for i in range(len(teamsTotalLaps)):
    ax.text(teamsTotalLaps[i]-45, i+0.2, teamsTotalLaps[i],fontproperties=font_prop, fontsize=14, fontweight='bold', color='k')

# Add note
ax.text(2400, 8.6, "* Reserve Drivers Included", fontproperties=font_prop,fontweight='bold', color='#bbbbbb')

# Set title and labels
ax.set_title('Formula 1 - 2023 Season\nTotal Laps Driven in Race Sessions (Teams)', fontproperties=font_prop,fontsize=19, fontweight='bold', color='#bbbbbb')
ax.set_xlabel('TOTAL LAPS', fontsize=14, fontweight='bold', fontproperties=font_prop,color='#bbbbbb')
ax.set_ylabel('TEAMS', fontsize=14, fontweight='bold', fontproperties=font_prop,color='#bbbbbb')

plt.xticks(fontproperties=font_prop, color='#bbbbbb')
plt.yticks(fontproperties=font_prop,color='#bbbbbb')
# Add vertical line
ax.axvline(2000, color='#bbbbbb')

# Display plot
st.pyplot(fig)

st.header("Elaborated Insights from the Formula 1 2023 Season Total Laps Driven (Teams) Chart")

st.subheader("Red Bull's Dominance")
st.write("Red Bull Racing once again showcased their supremacy in the 2023 season, leading all teams in total laps driven. This dominance reflects their consistent performance, reliability, and ability to keep their cars on the track.")

st.subheader("Mercedes' Close Challenge")
st.write("Mercedes-Benz closely followed Red Bull, indicating a competitive battle between the two top teams. Their high total laps driven demonstrate their strong performance and reliability, making them a formidable opponent throughout the season.")

st.subheader("Midfield Competition")
st.write("The midfield teams engaged in a fiercely competitive battle, with Alfa Romeo, AlphaTauri, Aston Martin, McLaren, Haas, Ferrari, and Alpine all vying for positions. The close proximity of their total laps driven underscores the tight competition for points and positions throughout the season.")

st.subheader("Williams' Challenges")
st.write("Williams Racing faced challenges during the season, as indicated by their lower total laps driven. This suggests potential issues with reliability or performance, which hindered their ability to consistently compete at the same level as the other teams. However, it's important to note that this ranking includes reserve drivers, which may impact the overall comparison.")

st.subheader("Overall Insights")
st.write("Overall, the chart highlights Red Bull's dominance, the competitive nature of the midfield battle, and the challenges faced by Williams Racing during the 2023 season.")

trackDistance = season2023RaceCalendar['Circuit Length(km)'].values
drivers = season2023RaceResults['Driver'].unique()
driversLaps = {}
for driver in drivers:
    driversLaps[driver] = season2023RaceResults[season2023RaceResults['Driver'] == driver]['Laps'].values
driversDist = {}
for driver in driversLaps.keys():
    if len(driversLaps[driver]) != len(trackDistance):
        driversLaps[driver] = np.resize(driversLaps[driver], len(trackDistance))
    driversDist[driver] = round((driversLaps[driver] * trackDistance).sum(), 2)
driversTotalDist = pd.Series(driversDist).sort_values(ascending=False)[:20]

# Create figure
fig, ax = plt.subplots(figsize=(10,6))

# Set axis limits
ax.axis([2000,7336,19.6,-0.6])

# Create bar chart
ax.barh([" ".join(driver.split()[1:]) for driver in driversTotalDist.index], driversTotalDist, color=[color_dicttt.get(" ".join(driver.split()[1:]), 'gray') for driver in driversTotalDist.index])

# Add text to bars
for i in range(len(driversTotalDist)):
    ax.text(driversTotalDist[i]-666, i+0.22, "{:4.2f}".format(driversTotalDist[i]), fontproperties=font_prop, fontsize=12, fontweight='bold', color='k')

# Add note
ax.text(6333, 19.3, '* Reserve Drivers \nNot Included', fontproperties=font_prop, fontweight='bold', color='#bbbbbb')

# Set title and labels
ax.set_title('Formula 1 - 2023 Season\nTotal Distance Driven in Race Sessions (Drivers)', fontproperties=font_prop, fontsize=19, fontweight='bold', color='#bbbbbb')
ax.set_xlabel('DISTANCE (km)', fontsize=14, fontweight='bold', fontproperties=font_prop, color='#bbbbbb')
ax.set_ylabel('DRIVERS', fontsize=14, fontweight='bold', fontproperties=font_prop, color='#bbbbbb')

# Set ticks
plt.xticks(fontproperties=font_prop, color='#bbbbbb')
plt.yticks(fontproperties=font_prop,color='#bbbbbb')

# Add vertical line
ax.axvline(2000, color='#bbbbbb')

# Display plot
st.pyplot(fig)


# Formula 1 2023 Season Review
st.header("🏎️ 2023 Formula 1 Season Review")

# Max Verstappen and Red Bull's Dominance
st.subheader("Max Verstappen and Red Bull's Dominance 🏆")
st.markdown("""
- **Max Verstappen** secured his third consecutive **World Drivers’ Championship** in 2023 with **19 race wins out of 22**. It was a record-breaking performance that underlined Red Bull’s superiority on the grid. 🚀
- **Sprint Races**: Verstappen also topped the sprint race points, showing consistent performance across different race formats. 🏁

Key Stats:
- Total Wins: **19 out of 22 races** 🎉
- Podiums: **21 podium finishes** 🏆
- Constructors' Championship: **Red Bull** secured the championship early thanks to both Verstappen and **Sergio Pérez**. 🏅
""")

# Ferrari's Inconsistency
st.subheader("Ferrari's Inconsistency 🚦")
st.markdown("""
- **Charles Leclerc** and **Carlos Sainz** had mixed seasons, unable to consistently challenge Red Bull, but still competitive with some podium finishes. Sainz’s win was a rare non-Red Bull victory. 🌟
""")

# Mercedes’ Struggles and Developments
st.subheader("Mercedes' Struggles and Developments ⚙️")
st.markdown("""
- **Lewis Hamilton** and **George Russell** achieved several podiums, but despite mid-season upgrades, Mercedes struggled to consistently compete with Red Bull. ⚡️
""")

# Fernando Alonso’s Aston Martin Revival
st.subheader("Fernando Alonso’s Aston Martin Revival 💥")
st.markdown("""
- **Fernando Alonso** had a resurgent season with **8 podiums**, bringing Aston Martin into the midfield battle and outperforming teammate **Lance Stroll**. 🔥
""")

# Midfield Battle
st.subheader("Midfield Battle ⚔️")
st.markdown("""
- Teams like **McLaren**, **Alpine**, and **Aston Martin** had competitive showings, especially **Lando Norris** and **Oscar Piastri** for McLaren, who had significant improvements during the second half of the season. 📈
""")

# New Tech and Sprint Races
st.subheader("Introduction of New Tech and Sprint Races 🛠️")
st.markdown("""
- The 2023 season saw an expansion of **sprint races**, requiring teams to adapt their strategies for both qualifying and race days. 🏎️
""")

# Formula 1 2024 Season Insights
st.header("🔮 Formula 1 2024 Season - Detailed Analysis (as of September)")

# Max Verstappen’s Continued Dominance
st.subheader("Max Verstappen’s Continued Dominance 🏆")
st.markdown("""
- **Max Verstappen** continues his dominant streak in 2024, winning the majority of races and securing pole positions. His consistent and strategic brilliance, coupled with Red Bull's technical superiority, puts him well ahead of the competition. 🔥
""")

# Red Bull Racing's Strength
st.subheader("Red Bull Racing's Strength 💪")
st.markdown("""
- **Red Bull Racing** remains the dominant force in 2024. While **Sergio Pérez** has delivered key performances, Verstappen's consistency is what keeps Red Bull ahead. 🥇
""")

# Competitive Midfield Battle
st.subheader("Competitive Midfield Battle ⚔️")
st.markdown("""
- Teams like **Ferrari**, **Mercedes**, and **Aston Martin** continue their fight for podiums. While **Charles Leclerc** and **Lewis Hamilton** show flashes of brilliance, the midfield remains fiercely competitive. 🚗💨
""")

# Sustainability and Logistical Adjustments
st.subheader("Sustainability and Logistical Adjustments 🌍")
st.markdown("""
- Formula 1 has focused on sustainability in 2024 by adjusting the calendar to reduce the sport’s carbon footprint. The regionalized races are part of a broader effort to achieve net-zero carbon emissions by 2030. ♻️
""")

# Daniel Ricciardo’s Retirement
st.subheader("Daniel Ricciardo’s Retirement 😢")
st.markdown("""
- **Daniel Ricciardo** announced his retirement after the Singapore Grand Prix. Known for his bold overtakes and charming personality, Ricciardo leaves behind a legacy of **8 Grand Prix wins** and unforgettable moments. 🏁
""")

# McLaren’s New Tech Upgrades
st.subheader("McLaren's New Tech Upgrades 🚀")
st.markdown("""
- **McLaren** introduced significant **aerodynamic upgrades** in 2024, leading to improved performance. **Lando Norris** and **Oscar Piastri** have been strong contenders, challenging for podiums more frequently. ⚙️
""")

# Upcoming Challenges
st.subheader("Upcoming Challenges 🔮")
st.markdown("""
- The final third of the season features pivotal races in **Austin**, **Mexico City**, **Brazil**, and the grand finale in **Abu Dhabi**. 🏁 Teams like **Ferrari** and **Mercedes** will look to disrupt Red Bull’s dominance. 🌟
""")

# News for 2025 Season
st.header("📰 News for the 2025 Formula 1 Season")

st.markdown("""
As we look ahead to 2025, there are some exciting developments and changes anticipated:

1. **New Engine Regulations 🔧**:  
   Formula 1 will introduce new engine regulations in 2025 focused on sustainability, including increased use of biofuels and hybrid systems, pushing the boundaries of speed and environmental responsibility.

2. **Driver Lineup Changes 🏎️**:  
   - **Fernando Alonso** may retire at the end of 2024, sparking rumors about potential replacements at Aston Martin.
   - **Oscar Piastri** is rumored to be on Mercedes' radar, with **Lewis Hamilton** potentially considering his retirement after the 2024 season.

3. **Audi's Full Entry 🏁**:  
   - Audi is set to make its full entry into Formula 1 as a factory team in 2025, raising anticipation about how they will perform in their debut season.

4. **Sprint Races Expansion 🏁**:  
   - More sprint races are expected in 2025, potentially introducing exciting new formats that could shake up the strategy for teams.

5. **Calendar Expansion 🌍**:  
   - Formula 1 is expected to add new races in regions like **Africa** and **South America** as part of its global expansion efforts.
""")

# Section: About the Author
st.write("---")
st.subheader("About Me")

# Add some introductory text
st.write("""
Hello, my name is **Ashutosh Shukla**, a passionate Computer Science and Engineering student with huge interest in Data Science and Machine Learning enthusiast with a deep interest in AI, Formula 1, and advanced data analytics. 
""")

# Add LinkedIn and GitHub links with emojis
st.write("Feel free to connect with me:")
st.markdown("""
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Ashutosh%20Shukla-blue)](https://www.linkedin.com/in/ashutosh-shukla4/)
- [![GitHub](https://img.shields.io/badge/GitHub-ashutoshshukla-blue?logo=github)](https://github.com/shukla-ashutosh4)
""")
st.write("Also check out the [Colab Notebook](https://colab.research.google.com/drive/1NrpSs2ZlJZdBQqjkT0W9sCDyE7_Ap1vA?usp=sharing) for much Detailed Analyis ")



# Add a thank you message
st.write("""
The 2024 season is shaping up to be another dominant year for Max Verstappen and Red Bull Racing, but the battles in the midfield and technological advancements from teams like McLaren ensure that the season remains thrilling. 🌟
Thank you for reading the analysis! 🙌 If you have any questions or feedback, feel free to reach out via LinkedIn, and stay tuned for more insights as we move towards the season’s end! 🏁  
""")