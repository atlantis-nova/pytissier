# 🥐 pytissier

The first python library for the implementation of **computational pastry**.<br>
Our goal is simple: digitalize pastry in an open-source fashion.

## WORK IN PROGRESS

- **we are looking for pastry chefs and engineers**
We are thrilled to accept the contribution of pastry chefs and passionate engineer who wish to join the project
- **support for more recipes**
Currently, the library only supports a few of the most important recipes, other fundamental recipes will be added soon.
- **additional features**
once the library has become more solid we plan to deploy it using setuptools.py

## supported functions

- **shortcrust_pastry**
- **puff_pastry**

## example usage
The following is an example of how to compute the liquids for a **shortcrust pastry** recipe. Usually, each recipe differs in terms on inputs and output:
```
from pytissier import pychef

mychef = pychef.recipe_generator()

mychef.shortcrust_pastry(
    butter_percentage=0.50, 
    sugar_percentage=0.50, 
    dough_type='regular',
    sugar_type='icing', 
    liquid_type='eggwhites'
)

Output:
{
    'flower': 1000, 
    'butter': 500.0, 
    'granulated_sugar': 500.0, 
    'water': 125
}
```

### about the project
Managed and curated by Michelangiolo Mazzeschi
