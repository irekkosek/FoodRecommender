from ast import parse
import json
from pprint import pp

class Ingredient:
    def __init__(self, section_name, name, quantity, unit, comment):
        self.section_name = section_name
        self.quantity = quantity
        self.unit = unit
        self.comment = comment
        self.name = name
    
    def __repr__(self):
        return " ".join(f'{self.section_name} {self.quantity} {self.unit} {self.comment} {self.name}'.split())
    
    def __str__(self):
        return " ".join(f'{self.section_name} {self.quantity} {self.unit} {self.comment} {self.name}'.split())

# open json file in original_tasty_dataset/ingredient_and_instructions.json
def parse_ingredients(data : dict, slug : str, debug : bool = False) -> list:    
    ingredients = []
    print (f'Parsing {slug}') if debug else None
    for section in data[slug]["ingredient_sections"]:
        if section["name"] != "":
            ingredient_section_name = section["name"]
            print(f'{ingredient_section_name}: ') if debug else None
        else:
            ingredient_section_name = None
            print(f'Ingredients: ') if debug else None
        for ingredient in section["ingredients"]:
            ingredient_quantity=ingredient["primary_unit"]["quantity"]
            ingredient_unit=ingredient["primary_unit"]["display"] or ''
            ingredient_extra_comment=ingredient["extra_comment"]
            ingredient_name=ingredient["name"]
            print(" ".join(f'{ingredient_quantity} {ingredient_unit} {ingredient_extra_comment} {ingredient_name}'.split())) if debug else None
            ingredient = Ingredient(ingredient_section_name, ingredient_name, ingredient_quantity, ingredient_unit, ingredient_extra_comment)
            ingredients.append(ingredient)
    return ingredients
def main():
    with open('original_tasty_dataset/ingredient_and_instructions.json') as f:
        data = json.load(f)
        slug="honey-lime-fruit-salad"
        slug2="homemade-cinnamon-rolls"
        print(parse_ingredients(data, slug, debug=True))
        print(parse_ingredients(data, slug2, debug=True))
        for returned_ingredient in parse_ingredients(data, slug):
            print(type(returned_ingredient))
            break

if __name__ == "__main__":
    main()