import os
import shutil
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

from io import StringIO
from subprocess import Popen
from parser import spheno_reader
from organizer import unify_data


# Function can be exported as part of a module!


# define the function to calculate the XS. The paths must be relative to the user account or parent directory
def calculate_xs(
    process: str,  # enter the process in mg5 syntax
    params_dict: dict,  # parameters dictionary
    outputs_dir: os.PathLike,  # MG5 ouput folders
    ufo_path: os.PathLike,  # UFO
    mg5_bin_path: os.PathLike,  # mg5 executable file
    n_events: int = 1000,  # Usually, to calculate the XS is enough with 1K points. We suggest to increaste to 10K in case of fermionic
    n_workers: int = 20,  # Cores
    sde_strategy: bool = False,  # true for approx strategy, false for exact strategy
    jpeg: bool = False,  # Produce FDiagrams or not
    seed: int = 0,  # 0 for auto seed
) -> dict:  # return a dictionary

    # We create a random output directory to store the MG5 outputs generated after each run. The randomness arises from the tagging!

    output_dir = os.path.join(outputs_dir, str(random.randint(0, 1000000)))

    # If the output folder exists deletes it and creates it again

    try:
        os.makedirs(output_dir)  # tries to create the folder
    except FileExistsError:
        shutil.rmtree(output_dir)  # removes it if exists
        os.makedirs(output_dir)

    # creates the mg5 file that will contain the processes associated to each case

    process_file= os.path.join(os.path.dirname(__file__), "process_scalars_nodecay.mg5") #process file for the etai etar production XS

    # CHANGE COMMENTARY HERE FOR FULL XS---------------------------
    #process_file = os.path.join(os.path.dirname(__file__), "process_scalars_full.mg5")

    # opens the file to write the commands in it
    with open(process_file, "w") as f:
        # write the commands in the usual mg5 syntax
        f.write(f"import model {ufo_path} \n")  # \n means new line after this
        # process information
        f.write(f"{process}\n")
        # choose if we want the FDiagrams or nor (if you know what are you analyzing, then keep the default option)

        if jpeg:
            f.write(f"output {output_dir}\n")
        else:
            f.write(f"output {output_dir} -nojpeg\n")
        # launch the process
        f.write(f"launch {output_dir} -m\n")
        f.write(f"{n_workers}\n")
        # set the parsed param card parameters. Parameter names must come in capital letters
        [f.write(f"set {key.upper()} {value}\n") for key, value in params_dict.items()]
        f.write(f"set WETAR auto \n")
        f.write(f"set WETAP auto \n")
        f.write(f"set WN1 auto \n")
        f.write(f"set WN2 auto \n")
        f.write(f"set WN3 auto \n")
        # set the seed. 0 as automatic
        f.write(f"set iseed {seed}\n")
        # set the number of events
        f.write(f"set nevents {n_events}\n")
        # integration strategy. Set it to 0 if sde_strategy=True. Else 1
        sde = 2 if sde_strategy else 1
        f.write(f"set sde_strategy {sde}\n")

        # done
        f.write("done \n")

    # Run the mg5 executable with the process file associated
    Popen([mg5_bin_path, process_file]).wait()
    # copy the process file into the outputs folder
    shutil.copy(process_file, output_dir)

    # get the XS from the crossx html file generated in each mg5 run

    with open(os.path.join(output_dir, "crossx.html")) as f:
        # read the whole html as a set of strings
        html_string = f.read()
    # use pandas to recognize the html table structure from the string defined above
    data = pd.read_html(StringIO(html_string))[0]
    # searches the XS value in  the pandas object. if it is not given, assigns 0.0 as value
    try:
        xs_value = float(data["Cross section (pb)"][0].split(" ")[0])
    except ValueError:
        xs_value = 0.0

    # function finishes and returns the xs value

    return xs_value


# if the script is not imported as module, run the code as follows

if __name__ == "__main__":
    # search for the .dat files in the directory containing the SPheno outputs
    directory= "SPhenos/Scalars_246_D30"
    #directory= "SPhenos/Runs_before_wednesday"
    #directory= "SPhenos/Runs_2"
    #directory = "SPhenos/Testing"
    # UFOPATH
    model_path = os.path.join(os.path.dirname(__file__), "Scoto_Singlet_Doublet_UFO")

    # Process information. Define the 5 quark scheme

    process = """
    define ll l+ l- ta+ ta-
    define n n1 n2 n3
    define w w+ w- 
    generate p p > etai etar
    """

    # TURN  OFF COMMENT  and switch between processes FOR THE FULL SCALAR DECAY-------------

    # generate p p > etai etar
    # generate p p > etai w ll n
    # """
    # --------------------------------------------

    # get into the mg5 bin path
    mg5_bin_path = os.path.join(os.sep, "Collider", "MG5_aMC_v3_1_0", "bin", "mg5_aMC")

    # list of paths for each SPheno file
    spheno_paths = [
        os.path.join(directory, file)
        for file in os.listdir(directory)
        if file.endswith(".dat")
    ]
    # given the spheno paths, we now must parse them
    param_dicts = [
        # filename: unified_dict
        spheno_reader(path)
        for path in spheno_paths
    ]
    # list for the xs and DM masses
    
    xs_list_1_500 = []
    MDM_1_500 = []
    xs_list_2_500 = []
    MDM_2_500 = []
    xs_list_3_500 = []
    MDM_3_500 = []
    xs_list_4_500 = []
    MDM_4_500 = []
    xs_list_5_500 = []
    MDM_5_500 = []
    xs_list_6_500 = []
    MDM_6_500 = []
    xs_list_9_500 = []
    MDM_9_500 = []

    MN1_1_500 = []
    MN1_2_500 = []
    MN1_3_500 = []
    MN1_4_500 = []
    MN1_5_500 = []
    MN1_6_500 = []
    MN1_9_500 = []

    METAR_1_500 = []
    METAR_2_500 = []
    METAR_3_500 = []
    METAR_4_500 = []
    METAR_5_500 = []
    METAR_6_500 = []
    METAR_9_500 = []

    VEV_1000_500 = []
    VEV_2000_500 = []
    VEV_3000_500 = []
    VEV_4000_500 = []
    VEV_5000_500 = []
    VEV_6000_500 = []
    VEV_9000_500 = []

    xs_list_1_246 = []
    MDM_1_246 = []
    xs_list_2_246 = []
    MDM_2_246 = []
    xs_list_3_246 = []
    MDM_3_246 = []
    xs_list_4_246 = []
    MDM_4_246 = []
    xs_list_5_246 = []
    MDM_5_246 = []
    xs_list_6_246 = []
    MDM_6_246 = []
    xs_list_9_246 = []
    MDM_9_246 = []

    MN1_1_246 = []
    MN1_2_246 = []
    MN1_3_246 = []
    MN1_4_246 = []
    MN1_5_246 = []
    MN1_6_246 = []
    MN1_9_246 = []

    METAR_1_246 = []
    METAR_2_246 = []
    METAR_3_246 = []
    METAR_4_246 = []
    METAR_5_246 = []
    METAR_6_246 = []
    METAR_9_246 = []

    VEV_1000_246 = []
    VEV_2000_246 = []
    VEV_3000_246 = []
    VEV_4000_246 = []
    VEV_5000_246 = []
    VEV_6000_246 = []
    VEV_9000_246 = []

    # neutrino yukawas
    y11_1_246_re = []
    y11_1_246_im = []
    y11_2_246_re = []
    y11_2_246_im = []
    y11_3_246_re = []
    y11_3_246_im = []
    y11_4_246_re = []
    y11_4_246_im = []
    y11_5_246_re = []
    y11_5_246_im = []
    y11_6_246_re = []
    y11_6_246_im = []
    y11_9_246_re = []
    y11_9_246_im = []

    y11_1_500_re = []
    y11_1_500_im = []
    y11_2_500_re = []
    y11_2_500_im = []
    y11_3_500_re = []
    y11_3_500_im = []
    y11_4_500_re = []
    y11_4_500_im = []
    y11_5_500_re = []
    y11_5_500_im = []
    y11_6_500_re = []
    y11_6_500_im = []
    y11_9_500_re = []
    y11_9_500_im = []

    y12_1_246_re = []
    y12_1_246_im = []
    y12_2_246_re = []
    y12_2_246_im = []
    y12_3_246_re = []
    y12_3_246_im = []
    y12_4_246_re = []
    y12_4_246_im = []
    y12_5_246_re = []
    y12_5_246_im = []
    y12_6_246_re = []
    y12_6_246_im = []
    y12_9_246_re = []
    y12_9_246_im = []

    y12_1_500_re = []
    y12_1_500_im = []
    y12_2_500_re = []
    y12_2_500_im = []
    y12_3_500_re = []
    y12_3_500_im = []
    y12_4_500_re = []
    y12_4_500_im = []
    y12_5_500_re = []
    y12_5_500_im = []
    y12_6_500_re = []
    y12_6_500_im = []
    y12_9_500_re = []
    y12_9_500_im = []

    y13_1_246_re = []
    y13_1_246_im = []
    y13_2_246_re = []
    y13_2_246_im = []
    y13_3_246_re = []
    y13_3_246_im = []
    y13_4_246_re = []
    y13_4_246_im = []
    y13_5_246_re = []
    y13_5_246_im = []
    y13_6_246_re = []
    y13_6_246_im = []
    y13_9_246_re = []
    y13_9_246_im = []

    y13_1_500_re = []
    y13_1_500_im = []
    y13_2_500_re = []
    y13_2_500_im = []
    y13_3_500_re = []
    y13_3_500_im = []
    y13_4_500_re = []
    y13_4_500_im = []
    y13_5_500_re = []
    y13_5_500_im = []
    y13_6_500_re = []
    y13_6_500_im = []
    y13_9_500_re = []
    y13_9_500_im = []

    lam1_1_246 = []
    lam1_2_246 = []
    lam1_3_246 = []
    lam1_4_246 = []
    lam1_5_246 = []
    lam1_6_246 = []
    lam1_9_246 = []

    lam1_1_500 = []
    lam1_2_500 = []
    lam1_3_500 = []
    lam1_4_500 = []
    lam1_5_500 = []
    lam1_6_500 = []
    lam1_9_500 = []

    # calculate the xs for each parameter set parsed above.

    for param_dict in param_dicts:
        xs_value = calculate_xs(
            process, param_dict, "outputs", model_path, mg5_bin_path, n_events=int(1e4)
        )
        if (param_dict.get("vevSig") == 1.00000000e03) and (
            (param_dict.get("Mh2") - 246) < 1
        ):
            xs_list_1_246.append(xs_value)
            MDM_1_246.append(param_dict.get("METAI"))
            MN1_1_246.append(param_dict.get("MN1"))
            METAR_1_246.append(param_dict.get("METAR"))
            VEV_1000_246.append(param_dict.get("vevSig"))
            y11_1_246_re.append(param_dict.get("YnRE1x1"))
            y11_1_246_im.append(param_dict.get("YnIMG1x1"))
            y12_1_246_re.append(param_dict.get("YnRE1x2"))
            y12_1_246_im.append(param_dict.get("YnIMG1x2"))
            y13_1_246_re.append(param_dict.get("YnRE1x3"))
            y13_1_246_im.append(param_dict.get("YnIMG1x3"))
            lam1_1_246.append(param_dict.get("lam1"))

        elif (param_dict.get("vevSig") == 2.00000000e03) and (
            (param_dict.get("Mh2") - 246) < 1
        ):
            xs_list_2_246.append(xs_value)
            MDM_2_246.append(param_dict.get("METAI"))
            MN1_2_246.append(param_dict.get("MN1"))
            VEV_2000_246.append(param_dict.get("vevSig"))
            METAR_2_246.append(param_dict.get("METAR"))
            y11_2_246_re.append(param_dict.get("YnRE1x1"))
            y11_2_246_im.append(param_dict.get("YnIMG1x1"))
            y12_2_246_re.append(param_dict.get("YnRE1x2"))
            y12_2_246_im.append(param_dict.get("YnIMG1x2"))
            y13_2_246_re.append(param_dict.get("YnRE1x3"))
            y13_2_246_im.append(param_dict.get("YnIMG1x3"))
            lam1_2_246.append(param_dict.get("lam1"))

        elif (param_dict.get("vevSig") == 3.00000000e03) and (
            (param_dict.get("Mh2") - 246) < 1
        ):
            xs_list_3_246.append(xs_value)
            MDM_3_246.append(param_dict.get("METAI"))
            MN1_3_246.append(param_dict.get("MN1"))
            VEV_3000_246.append(param_dict.get("vevSig"))
            METAR_3_246.append(param_dict.get("METAR"))
            y11_3_246_re.append(param_dict.get("YnRE1x1"))
            y11_3_246_im.append(param_dict.get("YnIMG1x1"))
            y12_3_246_re.append(param_dict.get("YnRE1x2"))
            y12_3_246_im.append(param_dict.get("YnIMG1x2"))
            y13_3_246_re.append(param_dict.get("YnRE1x3"))
            y13_3_246_im.append(param_dict.get("YnIMG1x3"))
            lam1_3_246.append(param_dict.get("lam1"))

        elif (param_dict.get("vevSig") == 4.00000000e03) and (
            (param_dict.get("Mh2") - 246) < 1
        ):
            xs_list_4_246.append(xs_value)
            MDM_4_246.append(param_dict.get("METAI"))
            MN1_4_246.append(param_dict.get("MN1"))
            VEV_4000_246.append(param_dict.get("vevSig"))
            METAR_4_246.append(param_dict.get("METAR"))
            y11_4_246_re.append(param_dict.get("YnRE1x1"))
            y11_4_246_im.append(param_dict.get("YnIMG1x1"))
            y12_4_246_re.append(param_dict.get("YnRE1x2"))
            y12_4_246_im.append(param_dict.get("YnIMG1x2"))
            y13_4_246_re.append(param_dict.get("YnRE1x3"))
            y13_4_246_im.append(param_dict.get("YnIMG1x3"))
            lam1_4_246.append(param_dict.get("lam1"))

        elif (param_dict.get("vevSig") == 5.00000000e03) and (
            (param_dict.get("Mh2") - 246) < 1
        ):
            xs_list_5_246.append(xs_value)
            MDM_5_246.append(param_dict.get("METAI"))
            MN1_5_246.append(param_dict.get("MN1"))
            VEV_5000_246.append(param_dict.get("vevSig"))
            METAR_5_246.append(param_dict.get("METAR"))
            y11_5_246_re.append(param_dict.get("YnRE1x1"))
            y11_5_246_im.append(param_dict.get("YnIMG1x1"))
            y12_5_246_re.append(param_dict.get("YnRE1x2"))
            y12_5_246_im.append(param_dict.get("YnIMG1x2"))
            y13_5_246_re.append(param_dict.get("YnRE1x3"))
            y13_5_246_im.append(param_dict.get("YnIMG1x3"))
            lam1_5_246.append(param_dict.get("lam1"))

        elif (param_dict.get("vevSig") == 6.00000000e03) and (
            (param_dict.get("Mh2") - 246) < 1
        ):
            xs_list_6_246.append(xs_value)
            MDM_6_246.append(param_dict.get("METAI"))
            MN1_6_246.append(param_dict.get("MN1"))
            VEV_6000_246.append(param_dict.get("vevSig"))
            METAR_6_246.append(param_dict.get("METAR"))
            y11_6_246_re.append(param_dict.get("YnRE1x1"))
            y11_6_246_im.append(param_dict.get("YnIMG1x1"))
            y12_6_246_re.append(param_dict.get("YnRE1x2"))
            y12_6_246_im.append(param_dict.get("YnIMG1x2"))
            y13_6_246_re.append(param_dict.get("YnRE1x3"))
            y13_6_246_im.append(param_dict.get("YnIMG1x3"))
            lam1_6_246.append(param_dict.get("lam1"))


        elif (param_dict.get("vevSig") == 9.00000000e03) and (
            (param_dict.get("Mh2") - 246) < 1
        ):
            xs_list_9_246.append(xs_value)
            MDM_9_246.append(param_dict.get("METAI"))
            MN1_9_246.append(param_dict.get("MN1"))
            VEV_9000_246.append(param_dict.get("vevSig"))
            METAR_9_246.append(param_dict.get("METAR"))
            y11_9_246_re.append(param_dict.get("YnRE1x1"))
            y11_9_246_im.append(param_dict.get("YnIMG1x1"))
            y12_9_246_re.append(param_dict.get("YnRE1x2"))
            y12_9_246_im.append(param_dict.get("YnIMG1x2"))
            y13_9_246_re.append(param_dict.get("YnRE1x3"))
            y13_9_246_im.append(param_dict.get("YnIMG1x3"))
            lam1_9_246.append(param_dict.get("lam1"))

        elif (param_dict.get("vevSig") == 1.00000000e03) and (
            (param_dict.get("Mh2") - 500) < 1
        ):
            xs_list_1_500.append(xs_value)
            MDM_1_500.append(param_dict.get("METAI"))
            MN1_1_500.append(param_dict.get("MN1"))
            VEV_1000_500.append(param_dict.get("vevSig"))
            METAR_1_500.append(param_dict.get("METAR"))
            y11_1_500_re.append(param_dict.get("YnRE1x1"))
            y11_1_500_im.append(param_dict.get("YnIMG1x1"))
            y12_1_500_re.append(param_dict.get("YnRE1x2"))
            y12_1_500_im.append(param_dict.get("YnIMG1x2"))
            y13_1_500_re.append(param_dict.get("YnRE1x3"))
            y13_1_500_im.append(param_dict.get("YnIMG1x3"))
            lam1_1_500.append(param_dict.get("lam1"))


        elif (param_dict.get("vevSig") == 2.00000000e03) and (
            (param_dict.get("Mh2") - 500) < 1
        ):
            xs_list_2_500.append(xs_value)
            MDM_2_500.append(param_dict.get("METAI"))
            MN1_2_500.append(param_dict.get("MN1"))
            VEV_2000_500.append(param_dict.get("vevSig"))
            METAR_2_500.append(param_dict.get("METAR"))
            y11_2_500_re.append(param_dict.get("YnRE1x1"))
            y11_2_500_im.append(param_dict.get("YnIMG1x1"))
            y12_2_500_re.append(param_dict.get("YnRE1x2"))
            y12_2_500_im.append(param_dict.get("YnIMG1x2"))
            y13_2_500_re.append(param_dict.get("YnRE1x3"))
            y13_2_500_im.append(param_dict.get("YnIMG1x3"))
            lam1_2_500.append(param_dict.get("lam1"))

        elif (param_dict.get("vevSig") == 3.00000000e03) and (
            (param_dict.get("Mh2") - 500) < 1
        ):
            xs_list_3_500.append(xs_value)
            MDM_3_500.append(param_dict.get("METAI"))
            MN1_3_500.append(param_dict.get("MN1"))
            VEV_3000_500.append(param_dict.get("vevSig"))
            METAR_3_500.append(param_dict.get("METAR"))
            y11_3_500_re.append(param_dict.get("YnRE1x1"))
            y11_3_500_im.append(param_dict.get("YnIMG1x1"))
            y12_3_500_re.append(param_dict.get("YnRE1x2"))
            y12_3_500_im.append(param_dict.get("YnIMG1x2"))
            y13_3_500_re.append(param_dict.get("YnRE1x3"))
            y13_3_500_im.append(param_dict.get("YnIMG1x3"))
            lam1_3_500.append(param_dict.get("lam1"))

        elif (param_dict.get("vevSig") == 4.00000000e03) and (
            (param_dict.get("Mh2") - 500) < 1
        ):
            xs_list_4_500.append(xs_value)
            MDM_4_500.append(param_dict.get("METAI"))
            MN1_4_500.append(param_dict.get("MN1"))
            VEV_4000_500.append(param_dict.get("vevSig"))
            METAR_4_500.append(param_dict.get("METAR"))
            y11_4_500_re.append(param_dict.get("YnRE1x1"))
            y11_4_500_im.append(param_dict.get("YnIMG1x1"))
            y12_4_500_re.append(param_dict.get("YnRE1x2"))
            y12_4_500_im.append(param_dict.get("YnIMG1x2"))
            y13_4_500_re.append(param_dict.get("YnRE1x3"))
            y13_4_500_im.append(param_dict.get("YnIMG1x3"))
            lam1_4_500.append(param_dict.get("lam1"))


        elif (param_dict.get("vevSig") == 5.00000000e03) and (
            (param_dict.get("Mh2") - 500) < 1
        ):
            xs_list_5_500.append(xs_value)
            MDM_5_500.append(param_dict.get("METAI"))
            MN1_5_500.append(param_dict.get("MN1"))
            VEV_5000_500.append(param_dict.get("vevSig"))
            METAR_5_500.append(param_dict.get("METAR"))
            y11_5_500_re.append(param_dict.get("YnRE1x1"))
            y11_5_500_im.append(param_dict.get("YnIMG1x1"))
            y12_5_500_re.append(param_dict.get("YnRE1x2"))
            y12_5_500_im.append(param_dict.get("YnIMG1x2"))
            y13_5_500_re.append(param_dict.get("YnRE1x3"))
            y13_5_500_im.append(param_dict.get("YnIMG1x3"))
            lam1_5_500.append(param_dict.get("lam1"))

        elif (param_dict.get("vevSig") == 6.00000000e03) and (
            (param_dict.get("Mh2") - 500) < 1
        ):
            xs_list_6_500.append(xs_value)
            MDM_6_500.append(param_dict.get("METAI"))
            MN1_6_500.append(param_dict.get("MN1"))
            VEV_6000_500.append(param_dict.get("vevSig"))
            METAR_6_500.append(param_dict.get("METAR"))
            y11_6_500_re.append(param_dict.get("YnRE1x1"))
            y11_6_500_im.append(param_dict.get("YnIMG1x1"))
            y12_6_500_re.append(param_dict.get("YnRE1x2"))
            y12_6_500_im.append(param_dict.get("YnIMG1x2"))
            y13_6_500_re.append(param_dict.get("YnRE1x3"))
            y13_6_500_im.append(param_dict.get("YnIMG1x3"))
            lam1_6_500.append(param_dict.get("lam1"))

        elif (param_dict.get("vevSig") == 9.00000000e03) and (
            (param_dict.get("Mh2") - 500) < 1
        ):
            xs_list_9_500.append(xs_value)
            MDM_9_500.append(param_dict.get("METAI"))
            MN1_9_500.append(param_dict.get("MN1"))
            VEV_9000_500.append(param_dict.get("vevSig"))
            METAR_9_500.append(param_dict.get("METAR"))
            y11_9_500_re.append(param_dict.get("YnRE1x1"))
            y11_9_500_im.append(param_dict.get("YnIMG1x1"))
            y12_9_500_re.append(param_dict.get("YnRE1x2"))
            y12_9_500_im.append(param_dict.get("YnIMG1x2"))
            y13_9_500_re.append(param_dict.get("YnRE1x3"))
            y13_9_500_im.append(param_dict.get("YnIMG1x3"))
            lam1_9_500.append(param_dict.get("lam1"))

    # sum the two lists of each yukawa after converting their data to floats
    y11_1_246_re = [float(i) for i in y11_1_246_re]
    y11_1_246_im = [float(i) for i in y11_1_246_im]
    y11_1_246 = [x + y * 1j for x, y in zip(y11_1_246_re, y11_1_246_im)]

    y11_2_246_re = [float(i) for i in y11_2_246_re]
    y11_2_246_im = [float(i) for i in y11_2_246_im]
    y11_2_246 = [x + y * 1j for x, y in zip(y11_2_246_re, y11_2_246_im)]

    y11_3_246_re = [float(i) for i in y11_3_246_re]
    y11_3_246_im = [float(i) for i in y11_3_246_im]
    y11_3_246 = [x + y * 1j for x, y in zip(y11_3_246_re, y11_3_246_im)]

    y11_4_246_re = [float(i) for i in y11_4_246_re]
    y11_4_246_im = [float(i) for i in y11_4_246_im]
    y11_4_246 = [x + y * 1j for x, y in zip(y11_4_246_re, y11_4_246_im)]

    y11_5_246_re = [float(i) for i in y11_5_246_re]
    y11_5_246_im = [float(i) for i in y11_5_246_im]
    y11_5_246 = [x + y * 1j for x, y in zip(y11_5_246_re, y11_5_246_im)]

    y11_6_246_re = [float(i) for i in y11_6_246_re]
    y11_6_246_im = [float(i) for i in y11_6_246_im]
    y11_6_246 = [x + y * 1j for x, y in zip(y11_6_246_re, y11_6_246_im)]

    y11_9_246_re = [float(i) for i in y11_9_246_re]
    y11_9_246_im = [float(i) for i in y11_9_246_im]
    y11_9_246 = [x + y * 1j for x, y in zip(y11_9_246_re, y11_9_246_im)]

    y11_1_500_re = [float(i) for i in y11_1_500_re]
    y11_1_500_im = [float(i) for i in y11_1_500_im]
    y11_1_500 = [x + y * 1j for x, y in zip(y11_1_500_re, y11_1_500_im)]

    y11_2_500_re = [float(i) for i in y11_2_500_re]
    y11_2_500_im = [float(i) for i in y11_2_500_im]
    y11_2_500 = [x + y * 1j for x, y in zip(y11_2_500_re, y11_2_500_im)]

    y11_3_500_re = [float(i) for i in y11_3_500_re]
    y11_3_500_im = [float(i) for i in y11_3_500_im]
    y11_3_500 = [x + y * 1j for x, y in zip(y11_3_500_re, y11_3_500_im)]

    y11_4_500_re = [float(i) for i in y11_4_500_re]
    y11_4_500_im = [float(i) for i in y11_4_500_im]
    y11_4_500 = [x + y * 1j for x, y in zip(y11_4_500_re, y11_4_500_im)]

    y11_5_500_re = [float(i) for i in y11_5_500_re]
    y11_5_500_im = [float(i) for i in y11_5_500_im]
    y11_5_500 = [x + y * 1j for x, y in zip(y11_5_500_re, y11_5_500_im)]

    y11_6_500_re = [float(i) for i in y11_6_500_re]
    y11_6_500_im = [float(i) for i in y11_6_500_im]
    y11_6_500 = [x + y * 1j for x, y in zip(y11_6_500_re, y11_6_500_im)]

    y11_9_500_re = [float(i) for i in y11_9_500_re]
    y11_9_500_im = [float(i) for i in y11_9_500_im]
    y11_9_500 = [x + y * 1j for x, y in zip(y11_9_500_re, y11_9_500_im)]

    # remaining yukawas
    y12_1_246_re = [float(i) for i in y12_1_246_re]
    y12_1_246_im = [float(i) for i in y12_1_246_im]
    y12_1_246 = [x + y * 1j for x, y in zip(y12_1_246_re, y12_1_246_im)]
    y12_2_246_re = [float(i) for i in y12_2_246_re]
    y12_2_246_im = [float(i) for i in y12_2_246_im]
    y12_2_246 = [x + y * 1j for x, y in zip(y12_2_246_re, y12_2_246_im)]
    y12_3_246_re = [float(i) for i in y12_3_246_re]
    y12_3_246_im = [float(i) for i in y12_3_246_im]
    y12_3_246 = [x + y * 1j for x, y in zip(y12_3_246_re, y12_3_246_im)]
    y12_4_246_re = [float(i) for i in y12_4_246_re]
    y12_4_246_im = [float(i) for i in y12_4_246_im]
    y12_4_246 = [x + y * 1j for x, y in zip(y12_4_246_re, y12_4_246_im)]
    y12_5_246_re = [float(i) for i in y12_5_246_re]
    y12_5_246_im = [float(i) for i in y12_5_246_im]
    y12_5_246 = [x + y * 1j for x, y in zip(y12_5_246_re, y12_5_246_im)]
    y12_6_246_re = [float(i) for i in y12_6_246_re]
    y12_6_246_im = [float(i) for i in y12_6_246_im]
    y12_6_246 = [x + y * 1j for x, y in zip(y12_6_246_re, y12_6_246_im)]
    y12_9_246_re = [float(i) for i in y12_9_246_re]
    y12_9_246_im = [float(i) for i in y12_9_246_im]
    y12_9_246 = [x + y * 1j for x, y in zip(y12_9_246_re, y12_9_246_im)]
    y12_1_500_re = [float(i) for i in y12_1_500_re]
    y12_1_500_im = [float(i) for i in y12_1_500_im]
    y12_1_500 = [x + y * 1j for x, y in zip(y12_1_500_re, y12_1_500_im)]
    y12_2_500_re = [float(i) for i in y12_2_500_re]
    y12_2_500_im = [float(i) for i in y12_2_500_im]
    y12_2_500 = [x + y * 1j for x, y in zip(y12_2_500_re, y12_2_500_im)]
    y12_3_500_re = [float(i) for i in y12_3_500_re]
    y12_3_500_im = [float(i) for i in y12_3_500_im]
    y12_3_500 = [x + y * 1j for x, y in zip(y12_3_500_re, y12_3_500_im)]
    y12_4_500_re = [float(i) for i in y12_4_500_re]
    y12_4_500_im = [float(i) for i in y12_4_500_im]
    y12_4_500 = [x + y * 1j for x, y in zip(y12_4_500_re, y12_4_500_im)]
    y12_5_500_re = [float(i) for i in y12_5_500_re]
    y12_5_500_im = [float(i) for i in y12_5_500_im]
    y12_5_500 = [x + y * 1j for x, y in zip(y12_5_500_re, y12_5_500_im)]
    y12_6_500_re = [float(i) for i in y12_6_500_re]
    y12_6_500_im = [float(i) for i in y12_6_500_im]
    y12_6_500 = [x + y * 1j for x, y in zip(y12_6_500_re, y12_6_500_im)]
    y12_9_500_re = [float(i) for i in y12_9_500_re]
    y12_9_500_im = [float(i) for i in y12_9_500_im]
    y12_9_500 = [x + y * 1j for x, y in zip(y12_9_500_re, y12_9_500_im)]
    y13_1_246_re = [float(i) for i in y13_1_246_re]
    y13_1_246_im = [float(i) for i in y13_1_246_im]
    y13_1_246 = [x + y * 1j for x, y in zip(y13_1_246_re, y13_1_246_im)]
    y13_2_246_re = [float(i) for i in y13_2_246_re]
    y13_2_246_im = [float(i) for i in y13_2_246_im]
    y13_2_246 = [x + y * 1j for x, y in zip(y13_2_246_re, y13_2_246_im)]
    y13_3_246_re = [float(i) for i in y13_3_246_re]
    y13_3_246_im = [float(i) for i in y13_3_246_im]
    y13_3_246 = [x + y * 1j for x, y in zip(y13_3_246_re, y13_3_246_im)]
    y13_4_246_re = [float(i) for i in y13_4_246_re]
    y13_4_246_im = [float(i) for i in y13_4_246_im]
    y13_4_246 = [x + y * 1j for x, y in zip(y13_4_246_re, y13_4_246_im)]
    y13_5_246_re = [float(i) for i in y13_5_246_re]
    y13_5_246_im = [float(i) for i in y13_5_246_im]
    y13_5_246 = [x + y * 1j for x, y in zip(y13_5_246_re, y13_5_246_im)]
    y13_6_246_re = [float(i) for i in y13_6_246_re]
    y13_6_246_im = [float(i) for i in y13_6_246_im]
    y13_6_246 = [x + y * 1j for x, y in zip(y13_6_246_re, y13_6_246_im)]
    y13_9_246_re = [float(i) for i in y13_9_246_re]
    y13_9_246_im = [float(i) for i in y13_9_246_im]
    y13_9_246 = [x + y * 1j for x, y in zip(y13_9_246_re, y13_9_246_im)]
    y13_1_500_re = [float(i) for i in y13_1_500_re]
    y13_1_500_im = [float(i) for i in y13_1_500_im]
    y13_1_500 = [x + y * 1j for x, y in zip(y13_1_500_re, y13_1_500_im)]
    y13_2_500_re = [float(i) for i in y13_2_500_re]
    y13_2_500_im = [float(i) for i in y13_2_500_im]
    y13_2_500 = [x + y * 1j for x, y in zip(y13_2_500_re, y13_2_500_im)]
    y13_3_500_re = [float(i) for i in y13_3_500_re]
    y13_3_500_im = [float(i) for i in y13_3_500_im]
    y13_3_500 = [x + y * 1j for x, y in zip(y13_3_500_re, y13_3_500_im)]
    y13_4_500_re = [float(i) for i in y13_4_500_re]
    y13_4_500_im = [float(i) for i in y13_4_500_im]
    y13_4_500 = [x + y * 1j for x, y in zip(y13_4_500_re, y13_4_500_im)]
    y13_5_500_re = [float(i) for i in y13_5_500_re]
    y13_5_500_im = [float(i) for i in y13_5_500_im]
    y13_5_500 = [x + y * 1j for x, y in zip(y13_5_500_re, y13_5_500_im)]
    y13_6_500_re = [float(i) for i in y13_6_500_re]
    y13_6_500_im = [float(i) for i in y13_6_500_im]
    y13_6_500 = [x + y * 1j for x, y in zip(y13_6_500_re, y13_6_500_im)]
    y13_9_500_re = [float(i) for i in y13_9_500_re]
    y13_9_500_im = [float(i) for i in y13_9_500_im]
    y13_9_500 = [x + y * 1j for x, y in zip(y13_9_500_re, y13_9_500_im)]

    data_1_246 = {
        "MDM": MDM_1_246,
        "XS": xs_list_1_246,
        "MN1": MN1_1_246,
        "METAR": METAR_1_246,
        "VEV": VEV_1000_246,
        "Y11": y11_1_246,
        "Y12": y12_1_246,
        "Y13": y13_1_246,
        "LAM1": lam1_1_246,
    }
    data_2_246 = {
        "MDM": MDM_2_246,
        "XS": xs_list_2_246,
        "MN1": MN1_2_246,
        "METAR": METAR_2_246,
        "VEV": VEV_2000_246,
        "Y11": y11_2_246,
        "Y12": y12_2_246,
        "Y13": y13_2_246,
        "LAM1": lam1_2_246,
    }
    data_3_246 = {
        "MDM": MDM_3_246,
        "XS": xs_list_3_246,
        "MN1": MN1_3_246,
        "METAR": METAR_3_246,
        "VEV": VEV_3000_246,
        "Y11": y11_3_246,
        "Y12": y12_3_246,
        "Y13": y13_3_246,
        "LAM1": lam1_3_246,
    }
    data_4_246 = {
        "MDM": MDM_4_246,
        "XS": xs_list_4_246,
        "MN1": MN1_4_246,
        "METAR": METAR_4_246,
        "VEV": VEV_4000_246,
        "Y11": y11_4_246,
        "Y12": y12_4_246,
        "Y13": y13_4_246,
        "LAM1": lam1_4_246,
    }
    data_5_246 = {
        "MDM": MDM_5_246,
        "XS": xs_list_5_246,
        "MN1": MN1_5_246,
        "METAR": METAR_5_246,
        "VEV": VEV_5000_246,
        "Y11": y11_5_246,
        "Y12": y12_5_246,
        "Y13": y13_5_246,
        "LAM1": lam1_5_246,
    }
    data_6_246 = {
        "MDM": MDM_6_246,
        "XS": xs_list_6_246,
        "MN1": MN1_6_246,
        "METAR": METAR_6_246,
        "VEV": VEV_6000_246,
        "Y11": y11_6_246,
        "Y12": y12_6_246,
        "Y13": y13_6_246,
        "LAM1": lam1_6_246,
    }
    data_9_246 = {
        "MDM": MDM_9_246,
        "XS": xs_list_9_246,
        "MN1": MN1_9_246,
        "METAR": METAR_9_246,
        "VEV": VEV_9000_246,
        "Y11": y11_9_246,
        "Y12": y12_9_246,
        "Y13": y13_9_246,
        "LAM1": lam1_9_246,
    }

    df_1_246 = pd.DataFrame(data_1_246)
    df_2_246 = pd.DataFrame(data_2_246)
    df_3_246 = pd.DataFrame(data_3_246)
    df_4_246 = pd.DataFrame(data_4_246)
    df_5_246 = pd.DataFrame(data_5_246)
    df_6_246 = pd.DataFrame(data_6_246)
    df_9_246 = pd.DataFrame(data_9_246)

    # unify the data frames for the 246 case and passes it to the corresponding csv file
    data_246 = unify_data(
        df_1_246, df_2_246, df_3_246, df_4_246, df_5_246, df_6_246, df_9_246
    )
    #data_246.to_csv('XS_246_D30.csv', index=False)
    data_246.to_csv('XSBefDecay_246_D30.csv', index=False)
    #data_246.to_csv('XS_246_D50.csv', index=False)
    #data_246.to_csv("testing.csv", index=False)
    #data_246.to_csv('XSBefDecay_246_D50.csv', index=False)

    data1_500 = {
        "MDM": MDM_1_500,
        "XS": xs_list_1_500,
        "MN1": MN1_1_500,
        "METAR": METAR_1_500,
        "VEV": VEV_1000_500,
        "Y11": y11_1_500,
        "Y12": y12_1_500,
        "Y13": y13_1_500,
        "LAM1": lam1_1_500,
    }
    data2_500 = {
        "MDM": MDM_2_500,
        "XS": xs_list_2_500,
        "MN1": MN1_2_500,
        "METAR": METAR_2_500,
        "VEV": VEV_2000_500,
        "Y11": y11_2_500,
        "Y12": y12_2_500,
        "Y13": y13_2_500,
        "LAM1": lam1_2_500,
    }
    data3_500 = {
        "MDM": MDM_3_500,
        "XS": xs_list_3_500,
        "MN1": MN1_3_500,
        "METAR": METAR_3_500,
        "VEV": VEV_3000_500,
        "Y11": y11_3_500,
        "Y12": y12_3_500,
        "Y13": y13_3_500,
        "LAM1": lam1_3_500,
    }
    data4_500 = {
        "MDM": MDM_4_500,
        "XS": xs_list_4_500,
        "MN1": MN1_4_500,
        "METAR": METAR_4_500,
        "VEV": VEV_4000_500,
        "Y11": y11_4_500,
        "Y12": y12_4_500,
        "Y13": y13_4_500,
        "LAM1": lam1_4_500,
    }
    data5_500 = {
        "MDM": MDM_5_500,
        "XS": xs_list_5_500,
        "MN1": MN1_5_500,
        "METAR": METAR_5_500,
        "VEV": VEV_5000_500,
        "Y11": y11_5_500,
        "Y12": y12_5_500,
        "Y13": y13_5_500,
        "LAM1": lam1_5_500,
    }
    data6_500 = {
        "MDM": MDM_6_500,
        "XS": xs_list_6_500,
        "MN1": MN1_6_500,
        "METAR": METAR_6_500,
        "VEV": VEV_6000_500,
        "Y11": y11_6_500,
        "Y12": y12_6_500,
        "Y13": y13_6_500,
        "LAM1": lam1_6_500,
    }
    data9_500 = {
        "MDM": MDM_9_500,
        "XS": xs_list_9_500,
        "MN1": MN1_9_500,
        "METAR": METAR_9_500,
        "VEV": VEV_9000_500,
        "Y11": y11_9_500,
        "Y12": y12_9_500,
        "Y13": y13_9_500,
        "LAM1": lam1_9_500,
    }

    df1_500 = pd.DataFrame(data1_500)
    df2_500 = pd.DataFrame(data2_500)
    df3_500 = pd.DataFrame(data3_500)
    df4_500 = pd.DataFrame(data4_500)
    df5_500 = pd.DataFrame(data5_500)
    df6_500 = pd.DataFrame(data6_500)
    df9_500 = pd.DataFrame(data9_500)

    # unify the data frames for the 500 case and passes it to the corresponding csv file
    #data_500 = unify_data(df1_500, df2_500, df3_500, df4_500, df5_500, df6_500, df9_500)
    #data_500.to_csv('XS_500_D30.csv', index=False)
    #data_500.to_csv('XSBefDecay_500_D30.csv', index=False)
    #data_500.to_csv('XS_500_D50.csv', index=False)
    #data_500.to_csv('XSBefDecay_500_D50.csv', index=False)
    print("XS data saved")
