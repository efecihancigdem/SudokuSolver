#declare Map variable
Map = [[2,7,6,9,5,1,"x",3,4]
      ,["x","x","x",6,2,"x","x","x",1]
      ,[1,4,"x","x",3,7,2,"x",6]
      ,[5,"x","x","x",8,9,"x",2,7]
      ,[7,"x",4,3,"x",2,1,5,"x"]
      ,[3,2,"x","x",7,"x",6,"x",9]
      ,["x","x","x","x","x",3,4,1,5]
      ,[4,"x","x","x","x",8,"x",6,2]
      ,[9,1,2,"x","x","x","x","x","x"]]

full_line = [x for x in range(1,10)]
probability = [[ ['#' for x in range(1,10)] for col in range(9)] for row in range(9)]

#HELPER FUNCTIONS--------------------------------------------------------------------

#Finds missing elements in the horizontal line and returns a list of missing colomn numbers list and missing numbers list 
def Find_Missing_Horizontal(row):
    remaining_line=full_line.copy()
    col_locations=[]
    col=0
    for element in row:
        if element in remaining_line:
            remaining_line.remove(element)
        else:
            col_locations.append(col)
        col+=1
    return [col_locations, remaining_line]

#Checks the vertical line and removes the probablity if it already exist
def Find_Missing_Verical(col,missing_numbers):
    for line in Map:
        if line[col] in missing_numbers:
            missing_numbers.remove(line[col])
        
    return Square_search(row, col,  missing_numbers)

#Prints Map
def Map_printer(map):
    for line in map:
        print(line)

#Square Search
def Square_search(row,col,missing_numbers):
    #finding the square
    if row <3:
        row_range=[x for x in range(0,3)]
    elif row<6:
        row_range=[x for x in range(3,6)]
    else:
        row_range=[x for x in range(6,9)]
    
    if col <3:
        col_range=[x for x in range(0,3)]
    elif col<6:
        col_range=[x for x in range(3,6)]
    else:
        col_range=[x for x in range(6,9)]

    #eliminate the number posibility if it exist in the square
    for r in row_range:
        for c in col_range:
            if Map[r][c] in missing_numbers:
                missing_numbers.remove(Map[r][c])

    return missing_numbers

#Main ----------------------------------------------------------------------------------
#Run it in a for while loop if nothing is changing stop to avoid endless run
row = 0
Hit = 0
Map_printer(Map)

while Hit == 0 :
    Hit = 1
    for line in Map:
        missing_elements = Find_Missing_Horizontal(line)
        if len(missing_elements[0]) !=0:
            #print(missing_elements[1])
            for col in missing_elements[0]:
                probability[row][col]= Find_Missing_Verical(col,missing_elements[1].copy()).copy()
                if len(probability[row][col]) == 1:
                    Hit = 0
                    Map[row][col] = probability[row][col][0]
                    probability[row][col].clear()
        row+=1
    print("ROUND!")
    row=0

Map_printer(Map)