
import utils

def read_data(path):
    f = open(path,"r")
    genome = f.read()
    f.close()
    return genome

genome = read_data("E-coli.txt")
k = 9 
L = 500
t = 3

patterns = utils.clumpFinding(genome, k , t , L)

    
