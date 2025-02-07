#Authors: Cristian Rodríguez, Andrés Florez, Oscar Zapata and Gustavo Ardila

import numpy as np
import os
import xslha #python module created by Florian Staub to read SLHA files. Can be found at https://github.com/fstaub/xSLHA
from itertools import product


#First, we create a directory to map the SPheno_Ids to the Madgraph Ones. 

dic_ids={
    #Keys=mG5 PDG scheme, Values= Spheno pdgs

    "25":25, #SM Higgs
    "9000010":1002, #eta i
    "9000009": 1003, #eta p 
    "9000012":2002, #P0_1
    "9000011":2002, #P0_2
    "9000006":3001, #N1
    "9000007":3002, #N2
    "9000008":3003, #N3
}

# Now, we create a dictionary to store the names of the mass parameters and associate them their MG5 pdg codes. 

mass_names_dict = {
    # MG5_ID : MG5_key
    "25": "MH",  # h
    "9000010": "emetaI",  # eta I
    "9000009": "metach",  # eta P
    "9000012": "emphi1",  # P0_1
    "9000011": "emphi2",  # P0_2
    "9000006": "emN1",  # N1
    "9000007": "emN2",  # N2
    "9000008": "emN3",  # N3
}

#Directory that stores the names of the widths and their corresponding pdgs

widths_names_dict = {
    # MG5_ID : MG5_key
    "25": "WH",  # h
    "9000010": "WetaI",  # eta I
    "9000009": "Wetach",  # eta P
    "9000012": "Wphi1",  # P0_1
    "9000011": "Wphi2",  # P0_2
    "9000006": "WN1",  # N1
    "9000007": "WN2",  # N2
    "9000008": "WN3",  # N3
}

#create a function that takes the path of a given spheno output as parameter. The -> dict implies that it is expected to return a dictionary at the end.

def spheno_reader(sp_output_path: os.PathLike)-> dict:
    #read the spheno output path using the xslha read function
    spc= xslha.read(sp_output_path)
    #as we just read the output file, we need to start accessing the information, which will be then stored in dictionaries

    widths_dict ={
        #Widths are not blocks  but rather simple lines 
        #mg5value : SP value

        #takes the key given from the names dictionary and assigns it a value read from the spheno file, if none value is given then puts 0
        widths_names_dict[key]: spc.widths.get(value, 0)
        #run this over all the possible ids 
        for key, value in dic_ids.items()
    }

    #repeat the previous thing for the masses

    mass_dict={
        #mg5 key : sp value
        # as the masses come in a block, use the block function from the xslha module to access it. In the blocks, the values are given as strings!

        mass_names_dict[key]: spc.blocks["MASS"].get(str(value))
        for key, value in dic_ids.items()
    }

    #Now, we need to parse the Yukawa matrices. In principle they work the same way as the blocks, but being a 2d array, one needs to run over all the possible combinations of the ij indices.
    #This can be done with the product module of the itertools package.

      
    YnRE_dict = {
        # MG5_key : Spheno_value
        #here we use the same syntax as in the mass block but use the get function to extract the value located at the ij element 
        f"YnRE{i}x{j}": spc.blocks["COUPLINGSYN"].get(f"{i},{j}")
        #as i,j can take values 1,2,3 and are not always the same, we create the range and put the repeat 2 to avoid a double for 
        for i, j in product(range(1, 4), repeat=2)
    }

    #Process can be repeated for the imaginary part of the Yukawas
    YnIMG_dict = {
        # MG5_key : Spheno_value
        f"YnIMG{i}x{j}": spc.blocks["IMCOUPLINGSYN"].get(f"{i},{j}")
        for i, j in product(range(1, 4), repeat=2)
    }

    #We now read the parameters of the potential. Each one comes in a different SPheno block, and we specify the position in the SPheno file

    potential_dict={
        #mg5_key:spheno value
        "Lam":spc.blocks["SM"].get("2"),
        "leta":spc.blocks["HDM"].get("2"),
	    "lsigma":spc.blocks["HDM"].get("6"),
	    "lHeta1":spc.blocks["HDM"].get("3"),
	    "lHeta2":spc.blocks["HDM"].get("4"),
	    "lHsigma":spc.blocks["HDM"].get("7"),
	    "letasigma":spc.blocks["HDM"].get("8"),
    }

    #Unify the dictionaries to establish the return of the functions

    unified_dictionary={**mass_dict, **widths_dict, **YnRE_dict, **YnIMG_dict, **potential_dict}
    return unified_dictionary