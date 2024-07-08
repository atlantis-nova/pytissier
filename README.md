# 🥐 pytissier

The first python library for the implementation of **computational pastry**

### WORK IN PROGRESS

- supported fundamental recipes
Currently, the library only supports the recipe creation of **shortcrust pastry**, other fundamental recipes will be added soon.
- additional features
once the library has become more solid we plan to deploy it using setuptools.py

### usage
The following is an example usage on how to compute the liquids for a **shortcrust pastry** recipe. Usually, each recipe differs in terms on inputs and output:
```
from pytissier import pychef

mychef = pychef.recipe_generator()

mychef.shortcrust_pastry(
    butter_percentage=0.50, 
    sugar_percentage=0.50, 
    sugar_type='granulated_sugar', 
    liquid_type='water'
)

Output:
{
    'flower': 1000, 
    'butter': 500.0, 
    'granulated_sugar': 500.0, 
    'water': 125
}
```