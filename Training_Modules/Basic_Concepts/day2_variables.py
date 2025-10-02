# Day 2 Practice: Variables & Data Types

# Numbers
a = 10
b = 3.5
flow_rate = 2.4
total_sum = a + b
print("a:", a, "type:", type(a))
print("b:", b, "type:", type(b))
print("flow_rate:", flow_rate, "type:", type(flow_rate))
print("total_sum:", total_sum, "type:", type(total_sum))

# Strings
name = "Kevin"
greeting = "Hello " + name
print(greeting)
tag_name = 'PT-101'
full_greeting = greeting + " " + tag_name
print(full_greeting)
new_greeting = f'Hello {name}!'
print(new_greeting)

# Lists
my_list = [10, 2, 3, 4]
print("List contents:", my_list)
print("First item:", my_list[0])

# Dictionaries
instrument = {"tag": "FT-101", "value": 45.7, "units": "gpm", 'location' : 'Reactor-2'}
print("Instrument Dictionary:", instrument)
print("Instrument Value:", instrument["value"])
print("Instrument Units:", instrument["units"])
print("Instrument Tag:", instrument["tag"])
print("Instrument Location:", instrument["location"])

# Boolean logic
is_running = False
print("Is running?", is_running)
if is_running:
    print("The machine is operational.")
else:
    print("The machine is shut down.")