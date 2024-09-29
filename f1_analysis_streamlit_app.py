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

# Load the Formula1-Regular font
font_path = 'Formula1-Regular.otf'  # Make sure this path is correct
font_prop = fm.FontProperties(fname=font_path)

# Manually specify the colors for top drivers/teams
color_dict = {
    'Max Verstappen': '#1E41FF',  
    'Sergio Perez': '#1E41FF',    
    'Charles Leclerc': '#DC0000',   
    'Carlos Sainz': '#DC0000',     
    'Lewis Hamilton': '#00D2BE',  
    'George Russell': '#00D2BE',  
    'Fernando Alonso': '#006F62', 
    'Lance Stroll': '#006F62', 
    'Lando Norris': '#FF8700',    
    'Oscar Piastri': '#FF8700',   
    'Esteban Ocon': '#0090FF'  
}

color_dicttt = {
    'Verstappen': '#1E41FF',  
    'Perez': '#1E41FF',    
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
    'Albon': '#00A0DE'
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

st.header("Several Notable Races in 2022 Season")
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
plt.xticks(range(0, 50, 5), range(0, 50, 5), color='#bbbbbb')
plt.yticks(color='#bbbbbb')
plt.axvline(0, linewidth=1, color='#bbbbbb')
plt.grid(True, linestyle='--', alpha=0.5, color='#bbbbbb')

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
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', fontsize=9, prop=font_prop)
st.pyplot(plt)



