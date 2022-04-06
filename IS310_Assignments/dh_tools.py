import csv

# Step 1
# Downloaded csv file in the same folder

# Step 2
with open("tools_dh_proceedings.csv","r") as input_file:
    csv_reader = csv.DictReader(input_file)

# Step 3 
    for row in csv_reader:
        count = (int(row['2015']), int(row['2016']), int(row['2017']), int(row['2018']), int(row['2019']))
        overall_count = sum(count)
        print("Tool:" + row['Tool'], 
        "\n2015: " + row['2015'], 
        "\n2019: " + row['2019'],
        "\nOverall Count: " + str(overall_count) + "\n")
        
# Step 4
    def make_dh_tool(name, v2015, v2016, v2017, v2018, v2019):
        count = (v2015, v2016, v2017, v2018, v2019)
        overall_count = sum(count)
        print("Tool:" + name, 
        "\n2015: " + str(v2015),
        "\n2016: " + str(v2016), 
        "\n2017: " + str(v2017), 
        "\n2018: " + str(v2018),  
        "\n2019: " + str(v2019),
        "\nOverall Count: " + str(overall_count) + "\n")

    make_dh_tool("New Tool", 5, 1, 4, 3, 2)
