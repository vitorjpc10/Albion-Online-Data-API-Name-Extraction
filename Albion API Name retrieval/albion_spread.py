import csv


def load_item_mapping(file_path):
    item_mapping = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # skip empty lines
                parts = line.split(':')
                api_name = parts[1].strip()
                try:
                    item_name = parts[2].strip()
                except IndexError:
                    item_name = "UNKNOWN"

                # Check if api_name contains @1, @2, or @3 and append item_name if so
                if any(tag in api_name for tag in ["@1", "@2", "@3"]):
                    # Find the tag that is present in api_name
                    found_tag = next(tag for tag in ["@1", "@2", "@3"] if tag in api_name)
                    # Append item_name with the found tag
                    item_name = f"{item_name}{found_tag}"

                item_mapping[item_name] = api_name
    return item_mapping

def find_api_names(item_mapping, item_values):
    return [(item, item_mapping.get(item, 'Unknown item')) for item in item_values]

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Item', 'API Name'])
        writer.writerows(data)

def generate_api_url(base_url, data, locations):
    # Extract the API names from the data tuples
    api_names = [item[1] for item in data]

    # Join the API names with commas
    api_names_str = ','.join(api_names)

    # Construct the final URL
    final_url = f"{base_url}/{api_names_str}.xml?locations={','.join(locations)}"

    return final_url

def main():
    # Load the mapping from the text file
    file_path = 'items.txt'
    item_mapping = load_item_mapping(file_path)

    # List of item values to find
    item_values = [
        "Avalonian Pork Omelette",
        "Avalonian Pork Omelette@1",
        "Avalonian Pork Omelette@2",
        "Avalonian Pork Omelette@3",
        "Dusthole Crab Omelette",
        "Dusthole Crab Omelette@1",
        "Dusthole Crab Omelette@2",
        "Dusthole Crab Omelette@3",
        "Pork Omelette",
        "Pork Omelette@1",
        "Pork Omelette@2",
        "Pork Omelette@3",
        "Frostpeak Deadeye Pie",
        "Frostpeak Deadeye Pie@1",
        "Frostpeak Deadeye Pie@2",
        "Frostpeak Deadeye Pie@3",
        "Pork Pie",
        "Pork Pie@1",
        "Pork Pie@2",
        "Pork Pie@3",
        "Deepwater Kraken Salad",
        "Deepwater Kraken Salad@1",
        "Deepwater Kraken Salad@2",
        "Deepwater Kraken Salad@3",
        "Potato Salad",
        "Potato Salad@1",
        "Potato Salad@2",
        "Potato Salad@3",
        "Avalonian Mutton Sandwich",
        "Avalonian Mutton Sandwich@1",
        "Avalonian Mutton Sandwich@2",
        "Avalonian Mutton Sandwich@3",
        "Beef Sandwich",
        "Beef Sandwich@1",
        "Beef Sandwich@2",
        "Beef Sandwich@3",
        "Thunderfall Lurcher Sandwich",
        "Thunderfall Lurcher Sandwich@1",
        "Thunderfall Lurcher Sandwich@2",
        "Thunderfall Lurcher Sandwich@3",
        "Blackbog Clam Soup",
        "Blackbog Clam Soup@1",
        "Blackbog Clam Soup@2",
        "Blackbog Clam Soup@3",
        "Avalonian Beef Stew",
        "Avalonian Beef Stew@1",
        "Avalonian Beef Stew@2",
        "Avalonian Beef Stew@3",
        "Beef Stew",
        "Beef Stew@1",
        "Beef Stew@2",
        "Beef Stew@3",
        "Deadwater Eel Stew",
        "Deadwater Eel Stew@1",
        "Deadwater Eel Stew@2",
        "Deadwater Eel Stew@3",
        "Roast Pork",
        "Roast Pork@1",
        "Roast Pork@2",
        "Roast Pork@3",
        "Roasted Puremist Snapper",
        "Roasted Puremist Snapper@1",
        "Roasted Puremist Snapper@2",
        "Roasted Puremist Snapper@3",
        "Cow's Milk",
        "Raw Pork",
        "Goose Eggs",
        "Avalonian Energy",
        "Dusthole Crab",
        "Bundle of Corn",
        "Firetouched Mullein",
        "Frostpeak Deadeye",
        "Flour",
        "Sheep's Milk",
        "Basic Fish Sauce",
        "Fancy Fish Sauce",
        "Special Fish Sauce",
        "Deepwater Kraken",
        "Potatoes",
        "Raw Mutton",
        "Cabbage",
        "Raw Beef",
        "Cow's Butter",
        "Pumpkin",
        "Ghoul Yarrow",
        "Raw Goose",
        "Dragon Teasel",
        "Bread",
        "Puremist Snapper",
        "Deadwater Eel",
        "Blackbog Clam",
        "Thunderfall Lurcher",
        "Elusive Foxglove"
    ]

    # Find the API names for the item values
    data = find_api_names(item_mapping, item_values)

    # Write the results to a CSV file
    output_file = 'item_api_mapping.csv'
    write_to_csv(data, output_file)

    #? Generating full url
    # Base URL
    base_url = "https://albion-online-data.com/api/v2/stats/prices"

    # Locations
    locations = ["Martlock", "Bridgewatch", "Lymhurst", "Fort Sterling", "Thetford", "Caerleon"]

    # Generate the API URL
    api_url = generate_api_url(base_url, data, locations)

    print(api_url)

if __name__ == '__main__':
    main()
