from howlongtobeatpy import HowLongToBeat
import csv

def parse_game_list(file_path):
    """Parses a text file with a list of games, each on a new line.

    Args:
        file_path (str): The path to the text file.

    Returns:
        list: A list of game titles.
    """
    games = []
    with open(file_path, 'r') as file:
        for line in file:
            game = line.strip().split(',')[0].strip()
            games.append(game)
    return games

def write_to_csv(game_list, archivo_csv):
    with open(archivo_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Main Story", "Story + Extras"])
        for game in game_list:
            try:
                results_list = HowLongToBeat().search(game)
                name = results_list[0].game_name
                mainStory = results_list[0].main_story
                storyPlusXtras = results_list[0].main_extra
                writer.writerow([name, mainStory, storyPlusXtras])
            except Exception as e:
                print(f"Error processing {game} - {str(e)}")
                writer.writerow([game, "-", "-"])

game_list = parse_game_list("gamelist.txt")
write_to_csv(game_list, "gamelist.csv")