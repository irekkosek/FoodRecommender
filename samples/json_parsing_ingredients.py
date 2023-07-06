import json
import csv

def parse_ingredients(data):
    ingredients_data = []
    counter = 0

    for recipe_id, recipe_data in data.items():
        ingredient_sections = recipe_data['ingredient_sections']
        for section in ingredient_sections:
            for ingredient in section['ingredients']:
                quantity = ""
                if (ingredient['primary_unit']['quantity'] == None):
                    quantity = ""
                else: quantity = ingredient['primary_unit']['quantity']

                comment = ""
                if (ingredient['extra_comment'] == None):
                    comment = ""
                else: comment = ingredient['extra_comment']

                display = ""
                if (ingredient['primary_unit']['display'] == None):
                    display = ""
                else: display = ingredient['primary_unit']['display']

                ingredients_data.append({
                    'id': counter,
                    'name': ingredient['name'],
                    'comment': comment,
                    'quantity': quantity,
                    'display': display,
                    'recipe_id': recipe_id
                })
                counter += 1
                
    with open('ingredients.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['id', 'name', 'comment', 'quantity', 'display', 'recipe_id']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(ingredients_data)

def main():
    with open('original_tasty_dataset/ingredient_and_instructions.json') as f:
        parse_ingredients(json.load(f))

if __name__ == "__main__":
    main()