import json
import csv

def parse_instructions(data):
    instructions_data = []
    counter = 0

    for recipe_id, recipe_data in data.items():
        instruction_sections = recipe_data['instructions']
        counter2 = 0
        for step in instruction_sections:
                instructions_data.append({
                    'id': counter,
                    'step': step['display_text'],
                    'step_number': counter2,
                    'recipe_id': recipe_id
                })
                counter2 += 1
                counter += 1
                
    with open('instructions.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['id', 'step', 'step_number', 'recipe_id']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(instructions_data)

def main():
    with open('original_tasty_dataset/ingredient_and_instructions.json') as f:
        parse_instructions(json.load(f))

if __name__ == "__main__":
    main()