for i in range(3):
    print('This is lesson 2:' , i)
# Open the file in read mode ('r')
with open('flow_meter_data2.csv', 'r') as file:
    # Use a for loop to iterate over each line in the file
    for line in file:
        print(line)