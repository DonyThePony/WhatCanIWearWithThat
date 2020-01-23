# What can i wear with that?

This Python-Script is a little prototype to see which products in a shop are compatible to the given outfit.

At this state everything is stored in json. In future releases we are going to implement Database-Support.

## Example
We have a black jacket and a white pair of pants.
What we need are some shoes and a shirt.
request:
```PYTHON
["Shirt", "Shoes"]
```

output:
```PYTHON
['003', '004']
```
Next Todo is to show the compatible colors in the Output

## How does it work
Example JSON for Shop:
```JSON
{
  "001": {
    "type": "Jacket",
    "colors": [
      "black",
      "white",
      "blue"
    ]
  },
  "002": {
    "type": "Pants",
    "colors": [
      "black",
      "blue"
    ]
  }
 }
```

Example JSON for User_Outfit:
```JSON
{
  "Jacket": {
    "color": [
      "black"
    ]
  },
  "Pants": {
    "color": [
      "white"
    ]
  }
}
```

And now with our given rule we can define how which type of products have to be "color-matching":
```JSON
{
  "Jacket": {
    "mustMatch": [
      "Shirt",
      "Pants"
    ]
  },
  "Shirt": {
    "mustMatch": [
      "Jacket",
      "Pants"
    ]
  }
}
```

Now the script looks for a desired product and checks if the given "mustMatch" products share the same color.
And it returns the productId's
```PYTHON
['004']
``` 
