# creating a dictionary
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome",
  "England": "London"
}

# printing the dictionary
print(country_capitals)
# Valid dictionary

my_dict = {
  1: "Hello",
  (1, 2): "Hello Hi",
  3: [1, 2, 3]
}

print(my_dict)

country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome",
  "England": "London"
}

# get dictionary's length
print(len(country_capitals)) # 3
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome",
  "England": "London"
}

print(country_capitals["United States"])  # Washington D.C.

print(country_capitals["England"]) # London
country_capitals = {
  "United States": "New York",
  "Italy": "Naples",
  "England": "London"
}

# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)
country_capitals = {
  "United States": "New York",
  "Italy": "Naples"
}

# add an item with "Germany" as key and "Berlin" as its value
country_capitals["Germany"] = "Berlin"

print(country_capitals)
country_capitals = {
  "United States": "New York",
  "Italy": "Naples"
}

# delete item having "United States" key
del country_capitals["United States"]


print(country_capitals)
