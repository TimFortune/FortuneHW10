#Tim Fortune HW 10 costructSentence.py
# Description: This script reads two text files with reversed word order and reconstructs the complete output.
# Command Line Arguments: input1.txt input2.txt
# Example Invocation: python3 reconstructSentence.py input1.txt input2.txt

import sys

def main():
 # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 reconstructSentence.py <input_file1> <input_file2>")
        sys.exit(1)

# Extract input file names from command line arguments
    input_file1 = sys.argv[1]
    input_file2 = sys.argv[2]
    
# basic list declareations
    f1 = open(input_file1)
    f2 = open(input_file2)
    f3 = open("output.txt","w")
    out = []
# Original attempt for steps
    #while list1_length > 0 or list2_length > 0:
     #  if list2_length > 0:
      #   out.append(list2.pop().strip())  # Append to maintain order
       #  list2_length -= 1
     #  if list1_length > 0:
      #  out.append(list1.pop().strip())  # Append to maintain order
       # list1_length -= 1

# Steps through and Len each list
    for line1 in f1.readlines():
        list1 = line1.split()
        list1_length = len(list1)
    for line2 in f2.readlines():
        list2 = line2.split()
        list2_length = len(list2)
# Iterate through the lists and construct the output list
# tried to make simple, but strait stepping breaks the problem out
# more which makes debugging easier
    if (list1_length > list2_length):
        while list1_length >0:
            if(list2_length != 0):
                out.append(list1[list1_length-1])
                out.append(list2[list2_length-1])
            else:
                out.append(list1[list1_length-1])
                break
            list1_length = list1_length - 1
            list2_length = list2_length - 1
    else:
        while list2_length > 0:
            if (list1_length != 0):
                out.append(list1[list1_length-1])
                out.append(list2[list2_length-1])
            else:
                break
            list1_length = list1_length - 1
            list2_length = list2_length - 1

    print(f"List1 is: {list1}")
    print(f"List2 is: {list2}")
    print(f"The list out is: {out}")


    f3.writelines([str(i)+' ' for i in out])
    f3.close()

# Started as functions which turns out are not needed :(
#def read_file(filename):
## Open the file and read its contents into a list
  #  try:
   #      with open(filename, 'r') as file:
    #        return file.readlines()
    #except FileNotFoundError:
     #   print(f"Error: File '{filename}' not found.")
      #  sys.exit(1)

  # Open the output file for writing
  # Write each word to the output file

        #f3.writelines([str(i)+' ' for i in out])


       
#print(f"Output written to 'output.txt'.")
#if __name__ == "__main__":
main()
