# pbp data from https://github.com/nflverse/nflverse-data/releases/tag/pbp
# formation data from https://github.com/nflverse/nflverse-data/releases/tag/pbp_participation

import pandas as pd

#global vars
common_columns = ['old_game_id', 'play_id']

necessary_columns_formation_data = ['old_game_id', 'play_id', 'offense_formation'] # need to add other columns for data
necessary_columns_pbp_data = ['old_game_id', 'play_id'] # need to add other columns



#load in data from both sets
pbp_data_2016 = pd.read_csv(r'C:\Users\fries\Downloads\data\play_by_play_2016.csv', low_memory=False)
formation_data_2016 = pd.read_csv(r'C:\Users\fries\Downloads\data\pbp_participation_2016.csv', low_memory=False)

pbp_data_2017 = pd.read_csv(r'C:\Users\fries\Downloads\data\play_by_play_2017.csv', low_memory=False)
formation_data_2017 = pd.read_csv(r'C:\Users\fries\Downloads\data\pbp_participation_2017.csv', low_memory=False)

pbp_data_2018 = pd.read_csv(r'C:\Users\fries\Downloads\data\play_by_play_2018.csv', low_memory=False)
formation_data_2018 = pd.read_csv(r'C:\Users\fries\Downloads\data\pbp_participation_2018.csv', low_memory=False)

pbp_data_2019 = pd.read_csv(r'C:\Users\fries\Downloads\data\play_by_play_2019.csv', low_memory=False)
formation_data_2019 = pd.read_csv(r'C:\Users\fries\Downloads\data\pbp_participation_2019.csv', low_memory=False)

pbp_data_2020 = pd.read_csv(r'C:\Users\fries\Downloads\data\play_by_play_2020.csv', low_memory=False)
formation_data_2020 = pd.read_csv(r'C:\Users\fries\Downloads\data\pbp_participation_2020.csv', low_memory=False)

pbp_data_2021 = pd.read_csv(r'C:\Users\fries\Downloads\data\play_by_play_2021.csv', low_memory=False)
formation_data_2021 = pd.read_csv(r'C:\Users\fries\Downloads\data\pbp_participation_2021.csv', low_memory=False)

pbp_data_2022 = pd.read_csv(r'C:\Users\fries\Downloads\data\play_by_play_2022.csv', low_memory=False)
formation_data_2022 = pd.read_csv(r'C:\Users\fries\Downloads\data\pbp_participation_2022.csv', low_memory=False)

pbp_data_2023 = pd.read_csv(r'C:\Users\fries\Downloads\data\play_by_play_2023.csv', low_memory=False)
formation_data_2023 = pd.read_csv(r'C:\Users\fries\Downloads\data\pbp_participation_2023.csv', low_memory=False)



#clean data from both sets
cleaned_pbp_2016_data = pbp_data_2016.loc[:,necessary_columns_pbp_data].dropna(subset=necessary_columns_pbp_data)
cleaned_formation_2016_data = formation_data_2016.loc[:,necessary_columns_formation_data].dropna(subset=necessary_columns_formation_data)

cleaned_pbp_2017_data = pbp_data_2017.loc[:,necessary_columns_pbp_data].dropna(subset=necessary_columns_pbp_data)
cleaned_formation_2017_data = formation_data_2017.loc[:,necessary_columns_formation_data].dropna(subset=necessary_columns_formation_data)

cleaned_pbp_2018_data = pbp_data_2018.loc[:,necessary_columns_pbp_data].dropna(subset=necessary_columns_pbp_data)
cleaned_formation_2018_data = formation_data_2018.loc[:,necessary_columns_formation_data].dropna(subset=necessary_columns_formation_data)

cleaned_pbp_2019_data = pbp_data_2019.loc[:,necessary_columns_pbp_data].dropna(subset=necessary_columns_pbp_data)
cleaned_formation_2019_data = formation_data_2019.loc[:,necessary_columns_formation_data].dropna(subset=necessary_columns_formation_data)

cleaned_pbp_2020_data = pbp_data_2020.loc[:,necessary_columns_pbp_data].dropna(subset=necessary_columns_pbp_data)
cleaned_formation_2020_data = formation_data_2020.loc[:,necessary_columns_formation_data].dropna(subset=necessary_columns_formation_data)

cleaned_pbp_2021_data = pbp_data_2021.loc[:,necessary_columns_pbp_data].dropna(subset=necessary_columns_pbp_data)
cleaned_formation_2021_data = formation_data_2021.loc[:,necessary_columns_formation_data].dropna(subset=necessary_columns_formation_data)

cleaned_pbp_2022_data = pbp_data_2022.loc[:,necessary_columns_pbp_data].dropna(subset=necessary_columns_pbp_data)
cleaned_formation_2022_data = formation_data_2022.loc[:,necessary_columns_formation_data].dropna(subset=necessary_columns_formation_data)

cleaned_pbp_2023_data = pbp_data_2023.loc[:,necessary_columns_pbp_data].dropna(subset=necessary_columns_pbp_data)
cleaned_formation_2023_data = formation_data_2023.loc[:,necessary_columns_formation_data].dropna(subset=necessary_columns_formation_data)



#merge data from both sets and save to files
merged_2016_data = pd.merge(cleaned_pbp_2016_data, cleaned_formation_2016_data, on=common_columns, how='left')
merged_2016_data.to_csv(r'C:\Users\fries\Downloads\data\clean_and_merged_data_2016.csv', index=False)

print("2016 Success!")

merged_2017_data = pd.merge(cleaned_pbp_2017_data, cleaned_formation_2017_data, on=common_columns, how='left')
merged_2017_data.to_csv(r'C:\Users\fries\Downloads\data\clean_and_merged_data_2017.csv', index=False)

print("2017 Success!")

merged_2018_data = pd.merge(cleaned_pbp_2018_data, cleaned_formation_2018_data, on=common_columns, how='left')
merged_2018_data.to_csv(r'C:\Users\fries\Downloads\data\clean_and_merged_data_2018.csv', index=False)

print("2018 Success!")

merged_2019_data = pd.merge(cleaned_pbp_2019_data, cleaned_formation_2019_data, on=common_columns, how='left')
merged_2019_data.to_csv(r'C:\Users\fries\Downloads\data\clean_and_merged_data_2019.csv', index=False)

print("2019 Success!")

merged_2020_data = pd.merge(cleaned_pbp_2020_data, cleaned_formation_2020_data, on=common_columns, how='left')
merged_2020_data.to_csv(r'C:\Users\fries\Downloads\data\clean_and_merged_data_2020.csv', index=False)

print("2020 Success!")

merged_2021_data = pd.merge(cleaned_pbp_2021_data, cleaned_formation_2021_data, on=common_columns, how='left')
merged_2021_data.to_csv(r'C:\Users\fries\Downloads\data\clean_and_merged_data_2021.csv', index=False)

print("2021 Success!")

merged_2022_data = pd.merge(cleaned_pbp_2022_data, cleaned_formation_2022_data, on=common_columns, how='left')
merged_2022_data.to_csv(r'C:\Users\fries\Downloads\data\clean_and_merged_data_2022.csv', index=False)

print("2022 Success!")

merged_2023_data = pd.merge(cleaned_pbp_2023_data, cleaned_formation_2023_data, on=common_columns, how='left')
merged_2023_data.to_csv(r'C:\Users\fries\Downloads\data\clean_and_merged_data_2023.csv', index=False)

print("2023 Success!")


#count 2016 games
file_path = r'C:\Users\fries\Downloads\data\clean_and_merged_data_2016.csv'
df = pd.read_csv(file_path)
unique_game_ids = df['old_game_id'].nunique()
print(f'The number of unique game IDs is: {unique_game_ids}')

#count 2023 games
file_path = r'C:\Users\fries\Downloads\data\clean_and_merged_data_2023.csv'
df = pd.read_csv(file_path)
unique_game_ids = df['old_game_id'].nunique()
print(f'The number of unique game IDs is: {unique_game_ids}')
