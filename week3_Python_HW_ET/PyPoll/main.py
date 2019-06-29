
from collections import defaultdict
#filename = "election_data.csv"

count = 0
Total_Votes = 0
Candidate_Name_List = defaultdict(int)
Candidate_Percentage_of_Votes = 0
Candidate_Total_Votes = {}
Candidate_Most_Votes = {}

with open("election_data.csv") as file_object:
    # Columns: Voter ID, County, Candidate
    #Voter ID,County,Candidate
    #12864552,Marsh,Khan
    #17444633,Marsh,Correy
    #19330107,Marsh,Khan
    #19865775,Queen,Khan
    #11927875,Marsh,Khan
    #19014606,Marsh,Li
    
    for line in file_object:
        count += 1
        if ( count == 1 ):
            continue      # continue will cause the next line to be read
        else:
            Total_Votes += 1   # increment the total votes count
            (VoterID, County, Candidate) = line.split(",")   # each line has three fields
            Candidate = Candidate.rstrip() 
#            print("Candidate: " + Candidate +
 #                 ", County: " + County +
  #                ", Voter ID: " + VoterID +
   #               "\n")
            Candidate_Name_List[Candidate] += 1

Winner = Candidate    # just initialize the winning variable here but do test below             
# print the results to the Python console

print("Election Results\n")
print("-------------------------\n")
print("Total Votes: " + str(Total_Votes) + "\n")
print("-------------------------\n")
print("Candidate List: \n")
for Name in sorted(Candidate_Name_List.keys()):
    percent_of_votes = Candidate_Name_List[Name] / Total_Votes * 100
    if Candidate_Name_List[Name] > Candidate_Name_List[Winner]:
        Winner = Name
        
    print("\t" + Name + ": " +
          str(round(percent_of_votes,4)) +
          "% (" +
          str(Candidate_Name_List[Name]) +
          ")\n")
print("-------------------------\n")
print("Winner: " + Winner + "\n")
print("-------------------------\n")

#  Do the output file creation and writing
outfile = open("election_data.txt","w+")
outfile.write("\n\nElection Results\n")
outfile.write("\n-------------------------\n")
outfile.write("\nTotal Votes: " + str(Total_Votes) + "\n")
outfile.write("\n-------------------------\n")
outfile.write("\nCandidate List: \n")
for Name in sorted(Candidate_Name_List.keys()):
    percent_of_votes = Candidate_Name_List[Name] / Total_Votes * 100
    outfile.write("\n\t" + Name + ": " +
        str(round(percent_of_votes,4)) +
        "% ("  +
        str(Candidate_Name_List[Name]) +
        ")\n")
    
outfile.write("\n-------------------------\n")
outfile.write("\nWinner: " + Winner + "\n")
outfile.write("\n-------------------------\n")
    
outfile.close()


