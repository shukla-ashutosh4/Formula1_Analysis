# # import streamlit as st
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# # import plotly.express as px
# # import numpy as np

# # # Set up the Streamlit page
# # st.set_page_config(page_title="Formula 1 Race Analysis (2023-2024)", layout="wide")

# # season2023RaceCalendar = pd.read_csv('Formula1_2023season_calendar.csv')
# # season2023RaceCalendar.set_index('Round', inplace=True)
# # season2023Drivers = pd.read_csv('Formula1_2023season_drivers.csv')
# # season2023Drivers.set_index('Abbreviation', inplace=True)
# # season2023Teams = pd.read_csv('Formula1_2023season_teams.csv')
# # season2023Teams.index = range(1,11)
# # season2023QualifyingResults = pd.read_csv('Formula1_2023season_qualifyingResults.csv')
# # season2023SprintRaceResults = pd.read_csv('Formula1_2023season_sprintResults.csv')
# # season2023RaceResults = pd.read_csv('Formula1_2023season_raceResults.csv')
# # season2023DotdVotes = pd.read_csv('Formula1_2023season_driverOfTheDayVotes.csv')
# # season2023DotdVotes.set_index('Track', inplace=True)
# # RaceTracks = season2023RaceCalendar.loc[:, 'Race Date':'Circuit Name']

# # # Title of the app
# # st.title("Formula 1 Race Analysis (2023-2024)")
# # st.write("### Created by Ashutosh Shukla")

# # # Load the data for the selected season
# # @st.cache
# # def load_data(season):
# #     return pd.read_csv(f"Formula1_2023season_raceResults.csv")

# # # Sidebar for selecting season, driver, and team
# # st.sidebar.header("Filter Options")
# # seasons = ['2013', '2014', '2015', '2016', '2017', '2018']
# # selected_season = st.sidebar.selectbox("Select Season", seasons)

# # # Load data for the selected season
# # data = load_data(selected_season)

# # # Convert Position to numeric, forcing non-numeric values to NaN
# # data['Position'] = pd.to_numeric(data['Position'], errors='coerce')

# # # Sidebar filters for driver and team
# # drivers = data['Driver'].unique()
# # teams = data['Team'].unique()
# # selected_driver = st.sidebar.selectbox("Select Driver", drivers)
# # selected_team = st.sidebar.selectbox("Select Team", teams)

# # # Filter data based on user selection
# # filtered_data = data[(data['Driver'] == selected_driver) & (data['Team'] == selected_team)]

# # racePoints = season2023RaceResults.groupby(['Driver', 'Team'])['Points'].sum().sort_values(ascending=False)
# # sprintRacePoints = season2023SprintRaceResults.groupby(['Driver'])['Points'].sum().sort_values(ascending=False)
# # for driver in season2023RaceResults['Driver'].unique():
# #     if driver not in season2023SprintRaceResults['Driver'].unique():
# #         sprintRacePoints.loc[driver] = 0
# # driverStandings = (racePoints + sprintRacePoints).fillna(0).sort_values(ascending=False)
# # driverStandings = pd.DataFrame(driverStandings).reset_index()
# # driverStandings['POS'] = range(1,23)
# # driverStandings['Points'] = driverStandings['Points'].astype(int)
# # driverStandings.set_index('POS', inplace=True)
# # driverStandings

# # racePoints = season2023RaceResults.groupby(['Driver', 'Team'])['Points'].sum().sort_values(ascending=False)
# # sprintRacePoints = season2023SprintRaceResults.groupby(['Driver'])['Points'].sum().sort_values(ascending=False)
# # for driver in season2023RaceResults['Driver'].unique():
# #     if driver not in season2023SprintRaceResults['Driver'].unique():
# #         sprintRacePoints.loc[driver] = 0
# # driverStandings = (racePoints + sprintRacePoints).fillna(0).sort_values(ascending=False)
# # driverStandings = pd.DataFrame(driverStandings).reset_index()
# # driverStandings['POS'] = range(1,23)
# # driverStandings['Points'] = driverStandings['Points'].astype(int)
# # driverStandings.set_index('POS', inplace=True)
# # driverStandings

# # teamNames = constructorStandings['Team'].unique()
# # teamPoints = {};   teamPointsSprint = {}
# # trackTeamPtsMerged = season2023RaceResults.groupby(['Track','Team'])['Points'].sum()
# # trackTeamPtsSprintMerged = season2023SprintRaceResults.groupby(['Track','Team'])['Points'].sum()


# # tracks = season2023RaceResults['Track'].unique()
# # tracksSprint = season2023SprintRaceResults['Track'].unique()

# # plt.style.use('seaborn-v0_8-dark-palette')
# # plt.style.use('dark_background')
# # plt.rcParams['axes.facecolor'] = '#15151d'
# # plt.rcParams['figure.facecolor'] = '#15151d'
# # plt.rcParams['grid.color'] = '#444444'
# # plt.rcParams['font.family'] = 'Formula1'

# # plt.figure(figsize=(11.5,7))
# # plt.axis([0, len(tracks) + 0.2, -5, 800])

# # c = assign_color('drivers', driverStandingsTop10)
# # c = c[:10]
# # if len(c) < 10:
# #     c += ['#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) for _ in range(10 - len(c))]

# # for i in range(10):
# #     if driverStandingsTop10[i] in ['Sergio Perez', 'Carlos Sainz', 'Lewis Hamilton', 'Fernando Alonso']:
# #         ls = '--'
# #     else:
# #         ls = '-'
# #     sprint_points = driverPointsTop10Sprint[driverStandingsTop10[i]]
# #     interpolated_sprint_points = np.interp(np.arange(len(driverPointsTop10[driverStandingsTop10[i]])), np.arange(len(sprint_points)), sprint_points)
# #     driver_name = driverStandingsTop10[i].split()
# #     if len(driver_name) > 1:
# #         label = driver_name[1]
# #     else:
# #         label = driver_name[0]
# #     plt.plot(np.cumsum(driverPointsTop10[driverStandingsTop10[i]] + interpolated_sprint_points),
# #              label=label, c=c[i], linewidth=2, ls=ls)

# # plt.title('Formula 1 - 2024 Season\nTop 10 Drivers\' Points Progression (including sprint points)',
# #          fontsize=19, fontweight='bold', color='#bbbbbb')
# # plt.xlabel('RACES', fontsize=16, fontweight='bold', color='#bbbbbb')
# # plt.ylabel('POINTS', fontsize=16, fontweight='bold', color='#bbbbbb')
# # plt.xticks(np.arange(len(tracks)), tracks, rotation=80, fontsize=10, color='#bbbbbb')
# # plt.yticks(np.arange(0, 800, 50), fontsize=12, color='#bbbbbb')
# # plt.axvline(0, linewidth=1, color='#bbbbbb')
# # plt.axhline(0, linewidth=1, color='#bbbbbb')
# # plt.grid(True, linestyle='--', alpha=0.5)
# # plt.legend(loc=(0.04,0.61), fontsize=9)
# # plt.show()

# # for team in teamNames:
# #     if team in trackTeamPtsMerged.index.get_level_values('Team'):
# #         teamPoints[team] = trackTeamPtsMerged[slice(None), team].reindex(tracks).values
# #     else:
# #         teamPoints[team] = np.zeros(len(tracks))

# #     if team in trackTeamPtsSprintMerged.index.get_level_values('Team'):
# #         teamPointsSprint[team] = trackTeamPtsSprintMerged[slice(None), team].reindex(tracksSprint).values
# #     else:
# #         teamPointsSprint[team] = np.zeros(len(tracksSprint))
# # sp = [3, 10, 20]
# # for team in teamNames:
# #     for i in range(len(sp)):
# #         teamPoints[team][sp[i]] = teamPoints[team][sp[i]] + teamPointsSprint[team][i]
        
# # # Display filtered data
# # st.write(f"### Race Results for {selected_driver} ({selected_team}) in {selected_season} Season")
# # st.dataframe(filtered_data.head())

# # # Visualization: Driver's race positions over different tracks
# # st.write(f"### Race Positions of {selected_driver} across Tracks in {selected_season}")
# # fig, ax = plt.subplots(figsize=(10, 6))
# # sns.lineplot(data=filtered_data, x="Track", y="Position", marker="o", ax=ax)
# # plt.title(f"Race Positions of {selected_driver} ({selected_team}) across Tracks in {selected_season}")
# # plt.ylabel("Race Position")
# # plt.xticks(rotation=90)  # Rotate the x-axis labels for better readability
# # st.pyplot(fig)

# # # Display Key Statistics
# # if not filtered_data['Position'].isnull().all():
# #     avg_position = filtered_data['Position'].mean()
# #     podiums = len(filtered_data[filtered_data['Position'] <= 3])
# #     wins = len(filtered_data[filtered_data['Position'] == 1])

# #     st.write(f"### Key Stats for {selected_driver} in {selected_season}")
# #     st.metric(label="Average Position", value=round(avg_position, 2))

# #     st.metric(label="Podium Finishes", value=podiums)
# #     st.metric(label="Wins", value=wins)
# # else:
# #     st.write(f"No valid race position data available for {selected_driver}.")

# # # Team comparison chart using Plotly
# # st.write("### Compare Team Performances")
# # fig = px.bar(data, x="Team", y="Points", color="Team", title="Team Performance in the Season")
# # st.plotly_chart(fig)

# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.colors as mcolors
# import matplotlib.font_manager as fm  # Import the font manager



# def assign_color(val_type, values):
#     cl = []
#     for val in values:
#         if val_type == 'drivers':  abbr = val.split()[1].upper()[0:3]
#         elif val_type == 'teams':  abbr = val[0:4].upper()
#         if abbr in ['ALFA','BOT','ZHO']:           cl.append('#900000')
#         elif abbr in ['HAAS','HUL','MAG']:         cl.append('#ffffff')
#         elif abbr in ['ASTO','VET','STR']:         cl.append('#006f62')
#         elif abbr in ['WILL','ALB','LAT','DE']:    cl.append('#0072ff')
#         elif abbr in ['ALPH','RIC','TSU']:         cl.append('#2b5962')
#         elif abbr in ['MCLA','RIC','NOR']:         cl.append('#ff8700')
#         elif abbr in ['RED ','VER','PER']:         cl.append('#0600f0')
#         elif abbr in ['FERR','LEC','SAI']:         cl.append('#cb0000')
#         elif abbr in ['MERC','HAM','RUS']:         cl.append('#00d2bd')
#         elif abbr in ['ALPI','ALO','OCO']:         cl.append('#0090ff')
#     return cl

# # Load the Formula1 font
# font_path = 'Formula1-Regular.otf'  # Ensure this path is correct
# font_prop = fm.FontProperties(fname=font_path)

# # Load your datasets here
# season2023RaceResults = pd.read_csv('Formula1_2023season_raceResults.csv')
# season2023SprintRaceResults = pd.read_csv('Formula1_2023season_sprintResults.csv')
# season2023Drivers = pd.read_csv('Formula1_2023season_drivers.csv')

# # Function to assign colors based on teams or drivers
# def assign_color(num_colors):
#     color_map = plt.cm.get_cmap('tab10', num_colors)  # Using a colormap with 10 colors
#     return [mcolors.to_hex(color_map(i)) for i in range(num_colors)]  # Use mcolors.to_hex

# # Set Streamlit title with custom font
# st.markdown(
#     """
#     <style>
#     @font-face {
#         font-family: 'Formula1';
#         src: url('Formula1-Regular.otf') format('opentype');
#     }
    
#     body {
#         font-family: 'Formula1', sans-serif;
#     }

#     h1, h2, h3, h4, h5, h6, p {
#         font-family: 'Formula1', sans-serif;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Set Streamlit title
# st.title("Formula 1 2023 Season Analysis")

# # Section: Red Bull Wins by Track
# st.header("Top 10 Red Bull Racing Wins by Track")
# redbull_wins = season2023RaceResults[(season2023RaceResults['Position'] == '1') & (season2023RaceResults['Team'] == 'Red Bull Racing Honda RBPT')]
# top_redbull_wins = redbull_wins.groupby('Track').head(10)
# st.write(top_redbull_wins)

# # Section: Top 3 World Champions
# st.header("Top 3 World Champions")
# world_champions = season2023Drivers[season2023Drivers['World Championships'] != 0]
# st.write(world_champions[['Driver', 'Team', 'World Championships']])

# # Section: Most Pole Positions
# st.header("Drivers with Most Pole Positions")
# no_pole_pos = season2023Drivers[season2023Drivers['Highest Grid Position'] != 1]
# no_pole_pos = no_pole_pos.sort_values('Highest Grid Position')
# st.write(no_pole_pos[['Driver', 'Team', 'Highest Grid Position']])

# # Section: Podiums
# st.header("Drivers with Most Podiums")
# podiums = season2023Drivers[season2023Drivers['Podiums'] >= 10]
# podiums = podiums.sort_values('Podiums', ascending=False)
# st.write(podiums[['Driver', 'Team', 'Podiums']])

# # Section: Driver Standings
# st.header("Driver Standings")
# racePoints = season2023RaceResults.groupby(['Driver', 'Team'])['Points'].sum().sort_values(ascending=False)
# sprintRacePoints = season2023SprintRaceResults.groupby(['Driver'])['Points'].sum().sort_values(ascending=False)

# # Handle missing drivers in sprint results
# for driver in season2023RaceResults['Driver'].unique():
#     if driver not in season2023SprintRaceResults['Driver'].unique():
#         sprintRacePoints.loc[driver] = 0

# driverStandings = (racePoints + sprintRacePoints).fillna(0).sort_values(ascending=False)
# driverStandings = pd.DataFrame(driverStandings).reset_index()
# driverStandings['POS'] = range(1, 23)
# driverStandings['Points'] = driverStandings['Points'].astype(int)
# driverStandings.set_index('POS', inplace=True)
# st.write(driverStandings)

# # Section: Driver Points Progression
# st.header("2023 Season Top 10 Drivers' Points Progression")
# driverStandingsTop10 = driverStandings['Driver'][:10].values
# driverPointsTop10 = {}
# driverPointsTop10Sprint = {}

# for driver in driverStandingsTop10:
#     driverPointsTop10[driver] = season2023RaceResults[season2023RaceResults['Driver'] == driver]['Points'].values
#     driverPointsTop10Sprint[driver] = season2023SprintRaceResults[season2023SprintRaceResults['Driver'] == driver]['Points'].values

# # Adjust points based on sprint results
# sp = [3, 10, 20]
# for driver in driverStandingsTop10:
#     for i in range(len(sp)):
#         if i < len(driverPointsTop10Sprint[driver]):
#             driverPointsTop10[driver][sp[i]] += driverPointsTop10Sprint[driver][i]

# # Plotting Driver Points Progression
# plt.style.use('dark_background')
# plt.figure(figsize=(11.5, 7))
# plt.axis([0, len(season2023RaceResults['Track'].unique()) + 0.2, -5, 800])
# c = assign_color(len(driverStandingsTop10))  # Use the number of top drivers

# for i in range(len(driverStandingsTop10)):
#     ls = '--' if driverStandingsTop10[i] in ['Sergio Perez', 'Carlos Sainz', 'Lewis Hamilton', 'Fernando Alonso'] else '-'
#     sprint_points = driverPointsTop10Sprint[driverStandingsTop10[i]]
#     interpolated_sprint_points = np.interp(np.arange(len(driverPointsTop10[driverStandingsTop10[i]])), np.arange(len(sprint_points)), sprint_points)
#     label = driverStandingsTop10[i].split()[-1]  # Get last name for label
#     plt.plot(np.cumsum(driverPointsTop10[driverStandingsTop10[i]] + interpolated_sprint_points), 
#              label=label, color=c[i], linewidth=2, linestyle=ls)

# plt.title('Formula 1 - 2023 Season\nTop 10 Drivers\' Points Progression (including sprint points)', 
#           fontproperties=font_prop, fontsize=19, fontweight='bold', color='#bbbbbb')
# plt.xlabel('RACES', fontproperties=font_prop, fontsize=16, fontweight='bold', color='#bbbbbb')
# plt.ylabel('POINTS', fontproperties=font_prop, fontsize=16, fontweight='bold', color='#bbbbbb')
# plt.xticks(np.arange(len(season2023RaceResults['Track'].unique())), 
#            season2023RaceResults['Track'].unique(), rotation=80, fontsize=10, fontproperties=font_prop, color='#bbbbbb')
# plt.yticks(np.arange(0, 800, 50), fontsize=12, fontproperties=font_prop, color='#bbbbbb')
# plt.axvline(0, linewidth=1, color='#bbbbbb')
# plt.axhline(0, linewidth=1, color='#bbbbbb')
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.legend(loc='upper left', fontsize=9, prop=font_prop)
# st.pyplot(plt)

# # Section: Constructor Standings
# st.header("Constructor Standings")
# racePointsTeam = season2023RaceResults.groupby('Team')['Points'].sum().sort_values(ascending=False)
# sprintRacePointsTeam = season2023SprintRaceResults.groupby('Team')['Points'].sum().sort_values(ascending=False)
# constructorStandings = (racePointsTeam + sprintRacePointsTeam).fillna(0).sort_values(ascending=False)
# constructorStandings = pd.DataFrame(constructorStandings).reset_index()
# constructorStandings['POS'] = range(1, len(constructorStandings) + 1)
# constructorStandings.set_index('POS', inplace=True)
# st.write(constructorStandings)

# # Plotting Constructor Standings
# teamNames = constructorStandings['Team'].unique()
# teamPoints = {}
# teamPointsSprint = {}
# trackTeamPtsMerged = season2023RaceResults.groupby(['Track', 'Team'])['Points'].sum()
# trackTeamPtsSprintMerged = season2023SprintRaceResults.groupby(['Track', 'Team'])['Points'].sum()

# # Initialize team points
# for team in teamNames:
#     if team in trackTeamPtsMerged.index.get_level_values('Team'):
#         teamPoints[team] = trackTeamPtsMerged[slice(None), team].reindex(season2023RaceResults['Track'].unique()).values
#     else:
#         teamPoints[team] = np.zeros(len(season2023RaceResults['Track'].unique()))

#     if team in trackTeamPtsSprintMerged.index.get_level_values('Team'):
#         teamPointsSprint[team] = trackTeamPtsSprintMerged[slice(None), team].reindex(season2023SprintRaceResults['Track'].unique()).values
#     else:
#         teamPointsSprint[team] = np.zeros(len(season2023SprintRaceResults['Track'].unique()))

# # Adjust points based on sprint results
# sp = [3, 10, 20]
# for team in teamNames:
#     for i in range(len(sp)):
#         if i < len(teamPointsSprint[team]):
#             teamPoints[team][sp[i]] += teamPointsSprint[team][i]

# # Plotting team points progression
# plt.figure(figsize=(11.5, 7))
# plt.axis([0.2, len(season2023RaceResults['Track'].unique()) + 0.2, -5, 800])
# c = assign_color(len(teamNames))

# for i, team in enumerate(teamNames):
#     plt.plot(np.cumsum(teamPoints[team]), label=team, color=c[i], linewidth=2)

# plt.title('Formula 1 - 2023 Season\nConstructor Points Progression', 
#           fontproperties=font_prop, fontsize=19, fontweight='bold', color='#bbbbbb')
# plt.xlabel('RACES', fontproperties=font_prop, fontsize=16, fontweight='bold', color='#bbbbbb')
# plt.ylabel('POINTS', fontproperties=font_prop, fontsize=16, fontweight='bold', color='#bbbbbb')
# plt.xticks(np.arange(len(season2023RaceResults['Track'].unique())), 
#            season2023RaceResults['Track'].unique(), rotation=80, fontsize=10, fontproperties=font_prop, color='#bbbbbb')
# plt.yticks(np.arange(0, 800, 50), fontsize=12, fontproperties=font_prop, color='#bbbbbb')
# plt.axvline(0, linewidth=1, color='#bbbbbb')
# plt.axhline(0, linewidth=1, color='#bbbbbb')
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.legend(loc='upper left', fontsize=9, prop=font_prop)
# st.pyplot(plt)


# winners = season2023RaceResults[season2023RaceResults['Position'] == '1']['Driver'].value_counts()
# c = assign_color('drivers', winners.index)
# plt.figure(figsize=(9,4.5))
# plt.axis([0,20,3,-0.5])
# plt.barh([driver.split()[1] for driver in winners.index], winners, color=c)
# for i in range(len(winners)):
#     plt.text(winners[i]-1.3, i+0.15, "{:>3}".format(winners[i]), fontsize=19, fontweight='bold', color='k')
# plt.title('Formula 1 - 2023 Season\n# of Race Wins (Drivers)', fontsize=19, fontweight='bold', color='#bbbbbb')
# plt.xlabel('RACE WINS', fontsize=14, fontweight='bold', color='#bbbbbb')
# plt.ylabel('DRIVERS', fontsize=14, fontweight='bold', color='#bbbbbb')
# plt.xticks(color='#bbbbbb')
# plt.yticks(color='#bbbbbb')
# plt.axvline(0, color='#bbbbbb')
# st.pyplot(plt)

# # Final remarks
# st.markdown("This analysis provides an overview of the 2023 Formula 1 season, focusing on driver standings, team performance, and key statistics.")




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

# Set Streamlit title
st.title("Formula 1 2023 Season Analysis")

st.header("Season Calendar")    
season2023RaceCalendar

st.header("The Drivers")
season2023Drivers

st.header("Race Tracks")
RaceTracks

st.header("Several Notable Races in 2023 Season")
season2023RaceResults[season2023RaceResults['Track'] == 'Bahrain'].drop('Track', axis=1).set_index('Position').head(10)

st.header("RedBull 2023 Wins")
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
    plt.text(winners[i]-1.3, i+0.15, "{:>3}".format(winners[i]), fontsize=19, fontweight='bold', color='#000000')
    plt.text(winners[i]+0.2, i+0.15, "{:>3}".format(winners[i]), fontsize=19, fontweight='bold', color='k')

plt.title('Formula 1 - 2023 Season\n# of Race Wins (Drivers)', fontproperties=font_prop, fontsize=19, fontweight='bold', color='#bbbbbb')
plt.xlabel('RACE WINS', fontproperties=font_prop, fontsize=14, fontweight='bold', color='#bbbbbb')
plt.ylabel('DRIVERS', fontproperties=font_prop, fontsize=14, fontweight='bold', color='#bbbbbb')
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

# def stream_data():
#     for word in "Qualifying Results".split(" "):
#         yield word + " "
#         time.sleep(0.02)
# if st.button("Qualifying results"):
#     st.write(stream_data())

# Set page config (this must be the first Streamlit command)

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

# progress_bar = st.progress(0)
# chart = st.bar_chart(df.set_index('Driver')['FastestTimes'])

# for i in range(len(df)):
#     # Updating progress bar
#     progress_bar.progress((i + 1) / len(df))
    
#     # Updating chart
#     chart.add_rows(df.iloc[:i+1].set_index('Driver')['FastestTimes'])
    
#     time.sleep(0.5)

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
    ax.text(DNFtrack[i]-0.18, i+0.22, DNFtrack[i], fontsize=12, fontweight='bold', color='k')

# Set title and labels
ax.set_title('Formula 1 - 2023 Season\n# of DNFs in Races (Tracks)', fontsize=19, fontweight='bold', color='#bbbbbb')
ax.set_xlabel('DNFs', fontsize=14, fontweight='bold', color='#bbbbbb')
ax.set_ylabel('TRACKS', fontsize=14, fontweight='bold', color='#bbbbbb')

# Add vertical line
ax.axvline(0, color='#bbbbbb')

# Display plot
st.pyplot(fig)