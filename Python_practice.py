print("Hello World")
type(3)
counties = ["Arapahoe","Denver","Jefferson"]
counties.insert(2,"El Paso")
counties.remove("Arapahoe")
print(counties)
counties.insert(2,"Denver")
counties.append("Arapahoe")
print(counties)
counties.append("El Paso")
counties.pop(3)
print(counties)
counties_tuple = ("Arapahoe","Denver","Jefferson")
print(counties_tuple[0:2])
print(counties_tuple[:-1])
counties_dict = {}
counties_dict["Arapahoe"] = 422829

counties_dict1 = {"counties":["Arapahoe","Denver","Jefferson"],
                "Population" : {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}}

print(counties_dict1["Population"]["Arapahoe"])
counties_dict.items()
counties_dict.keys()

score = int(input("What is your score bro?"))
if score >= 90:
    print("That's an A!")
elif score >= 80:
    print("That's a B")
elif score >= 70:
    print("That's a C man")
elif score >= 60:
    print("That's a D brooo")
else:
    print("That's an F dude!")

if "El Paso" in counties:
    print("True")
else:
    print("False")

x = 0
while x <= 5:
    print(x)
    x = x+1

for number in range(5):
    print(number)

for i in range(len(counties_dict1["counties"])):
    print(f'{counties_dict1["counties"][i]}')

for popu_size in counties_dict1["Population"]:
    print(f'{counties_dict1["Population"][popu_size]}')

for key, value in counties_dict1.items():
    print(key, value)

for i in range(3):
    print(f'{counties_dict1["counties"][i]} county has {counties_dict1["Population"][counties_dict1["counties"][i]]} registered voters')

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

voting_data = [{"county":"Arapahoe","registered_voters":422829},
                {"county":"Denver","registered_voters":463353},
                {"county":"Jefferson","registered_voters":432438}]

counties_dict.values()

for x,y in counties_dict.items():
    print(f'{x} county has {y} registered voters.')

for counties_dict in voting_data:
    for value in counties_dict.values():
        print(f'{value} county has {value} registered voters')

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:20,.3f} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)