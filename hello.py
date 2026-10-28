trips = [
    {"city": "Berlin", "distance": 10, "fare": 25},
    {"city": "Paris", "distance": 20, "fare": 60},
    {"city": "London", "distance": 15, "fare": 45},
    {"city": "Dhaka", "distance": 5, "fare": 10}
]

total = 0

for i in trips:
	fare_per_km = i['fare'] / i['distance'] 
	total = total + i["fare"]

	if fare_per_km > 2.5:
		print(f"{i['city']} | Fare/km: {fare_per_km} | Expensive")

	else:
		print(f"{i['city']} | Fare/km: {fare_per_km} | Normal")

print("Total fare:", total)
