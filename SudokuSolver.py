#declare Map variable
Map = [[7,1,"x",8,"x",5,4,"x",9]
      ,[9,"x",4,6,2,7,3,1,"x"]
      ,["x","x","x",4,"x",9,5,7,6]
      ,["x","x","x","x",8,3,7,4,"x"]
      ,[4,"x","x","x",5,6,9,8,1]
      ,[8,7,1,9,"x",2,6,3,"x"]
      ,[1,"x",9,5,7,4,2,6,3]
      ,[3,"x",7,2,"x",8,1,5,4]
      ,[5,4,2,3,6,1,8,"x","x"]]

full_line = [x for x in range(1,10)]
probability = [[ ['#' for col in range(9)] for col in range(9)] for row in range(9)]

#HELPER FUNCTIONS

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

def Find_Missing_Verical(col,missing_numbers):
    for line in Map:
        if line[col] in missing_numbers:
            missing_numbers.remove(line[col])
    return missing_numbers

def Map_printer(map):
    for line in map:
        print(line)



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
                    del(probability[row][col])
        row+=1
    print("ROUND!")
    row=0
Map_printer(Map)