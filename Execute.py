from generator import main
from data import randomChoice

NumberOfNFTS = len(randomChoice())

for i in range(NumberOfNFTS):
    main(i)
    
print("reached end of loop")