import urllib.request
import re
from collections import Counter

#Search for a string within a Sring between start and end 
def get_str(start,end,data):
    return re.search('%s(.*)%s' % (start, end), data).group(1)
#Get the sequence from the URl
def get_sequence(url):
    data=str(url.read())
    start1 = '\"sequence\" :'
    end1 = "\"md5\""
    start2 = '\"'
    end2 = '\"'
    return get_str(start2,end2,get_str(start1,end1,data))

#Count the top three amino acids   
def count(data):
    count_amino_acids=Counter(data)
    #Verify if all the caracters in the sequence are amino acids
    list_non_amino_acid=["B","J","O","U","X","Z"]
    for i in count_amino_acids.copy():
        for j in list_non_amino_acid:
            if j==i:
                count_amino_acids.pop(i)
    #Get the top 3 amino acids
    top_three_amino_acids = count_amino_acids.most_common(3)  
    j=0
    for i in top_three_amino_acids: 
        if j!=2:
            print(i[0]," =",i[1],"", end = ', ') 
            j+=1
        else:
            print(i[0]," =",i[1],"", end = '') 


def main(Protein_Identifier):
    url="https://api.nextprot.org/entry/"+Protein_Identifier+"/isoform.jsone"
    try:
        url_content = urllib.request.urlopen(url)
        count(get_sequence(url_content))
    except:
        print("An exception occurred")



if __name__ == "__main__":
  Protein_Identifier="NX_P01308"
  main(Protein_Identifier)