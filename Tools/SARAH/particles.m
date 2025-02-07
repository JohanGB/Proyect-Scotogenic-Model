(* ::Package:: *)

ParticleDefinitions[GaugeES] = {
      {H0,  {    PDG -> {0},
                 Width -> 0, 
                 Mass -> Automatic,
                 FeynArtsNr -> 1,
                 LaTeX -> "H^0",
                 OutputName -> "H0" }},                         
      
      
      {Hp,  {    PDG -> {0},
                 Width -> 0, 
                 Mass -> Automatic,
                 FeynArtsNr -> 2,
                 LaTeX -> "H^+",
                 OutputName -> "Hp" }}, 

	{etap,   {  Description -> "interaction eigenstates charged scalars", 
	  PDG -> {1004},
	  PDG . IX -> {1004},
	  Mass -> LesHouches,
	  ElectricCharge -> 1,
	  LaTeX -> {"\\eta_{+}","\\eta_{-}"},
	  OutputName -> {"Etap","Etam"} }},
                 
	 {eta0,   {  Description -> "interaction eigenstates neutral scalar", 
	  PDG -> {1005},
	  PDG . IX -> {1005},
	  Mass -> LesHouches,
	  ElectricCharge -> 1,
	  LaTeX -> {"\\eta_0"},
	  OutputName -> "Eta0" }},
 
  
       
    
      {VB,   { Description -> "B-Boson"}},                                                   
      {VG,   { Description -> "Gluon"}},          
      {VWB,  { Description -> "W-Bosons"}},          
      {gB,   { Description -> "B-Boson Ghost"}},                                                   
      {gG,   { Description -> "Gluon Ghost" }},          
      {gWB,  { Description -> "W-Boson Ghost"}}
      
      };
      
      
      
      
  ParticleDefinitions[EWSB] = {
            
      
    {hh   ,  {  Description -> "Higgs",
                 PDG -> {25},
                 PDG . IX -> {101000001},
		 Mass -> Automatic }}, 
                 
     {Ah   ,  {  Description -> "Pseudo-Scalar Higgs",
                 PDG -> {0},
                 PDG . IX ->{0},
                 Mass -> {0},
                 Width -> {0} }},                        
      
      
{     Hp,     { Description -> "Charged Higgs", 
                 PDG -> {0},
                 PDG . IX ->{0},
                 Width -> {0}, 
                 Mass -> {0},
                 LaTeX -> {"H^+","H^-"},
                 OutputName -> {"Hp","Hm"},
                 ElectricCharge->1
                 }},     
                                                     
      {P0,   {  Description -> "mass eigenstates neutral scalars", 
		 PDG -> {2001,2002},
		 PDG . IX -> {2001,2002},
		 Mass -> LesHouches,
		 ElectricCharge -> 0,
		 LaTeX -> "\\phi_{0i}",
		 OutputName -> "P0"}}, 

       {etaR,     { Description -> "CP-even eta scalar", 
                 PDG -> {1001}, 
                 Mass -> LesHouches,
                 ElectricCharge->0,
                 LaTeX->"\\eta_R",
                 OutputName->"etaR"}},
                 
       {etaI,     { Description -> "CP-odd eta scalar", 
                 PDG -> {1002}, 
                 Mass -> LesHouches,
                 ElectricCharge->0,
                 LaTeX->"\\eta_I",
                 OutputName->"etaI"}},
                 
       {etap,     { Description -> "Charged eta scalar", 
                 PDG -> {1003}, 
                 Mass -> LesHouches,
                 ElectricCharge->1,
                 LaTeX->"\\eta^+",
                 OutputName->"etp"}},          


      {VP,   { Description -> "Photon"}}, 
      {VZ,   { Description -> "Z-Boson",
      			 Goldstone -> Ah }}, 
      {VG,   { Description -> "Gluon" }},          
      {VWp,  { Description -> "W+ - Boson",
      			Goldstone -> Hp }},         
      {gP,   { Description -> "Photon Ghost"}},                                                   
      {gWp,  { Description -> "Positive W+ - Boson Ghost"}}, 
      {gWpC, { Description -> "Negative W+ - Boson Ghost" }}, 
      {gZ,   { Description -> "Z-Boson Ghost" }},
      {gG,   { Description -> "Gluon Ghost" }},          
                               
                 
      {Fd,   { Description -> "Down-Quarks"}},   
      {Fu,   { Description -> "Up-Quarks"}},   
      {Fe,   { Description -> "Leptons" }},
      {Fv,   { Description -> "Neutrinos" }},                                                            

      {FX0, { Description -> "New neutral fermions",
 		PDG -> {3001,3002,3003},
 		PDG . IX -> {3001,3002,3003},
 		Mass -> LesHouches,
 		ElectricCharge -> 0,
 		LaTeX -> "\\chi^{0}",
  		OutputName -> "X0" }}

     
        };        
        
        
 WeylFermionAndIndermediate = {
     
    {H,      {   PDG -> {0},
                 Width -> 0, 
                 Mass -> Automatic,
                 LaTeX -> "H",
                 OutputName -> "" }},
     {Sig0, {LaTeX -> "S" }},
	{Eta, LaTeX->"\\eta"},
	{etaI, LaTeX->"\\eta_I"},
	{etaR, LaTeX->"\\eta_R"},

    
   {n,   {LaTeX -> "N"} }, 
   {N0,   {LaTeX -> "N_R"} },
   {X0,   {LaTeX -> "\\chi_0"} }, 
   
   {dR,     {LaTeX -> "d_R" }},
   {eR,     {LaTeX -> "e_R" }},
   {lep,     {LaTeX -> "l" }},
   {uR,     {LaTeX -> "u_R" }},
   {q,     {LaTeX -> "q" }},
   {eL,     {LaTeX -> "e_L" }},
   {dL,     {LaTeX -> "d_L" }},
   {uL,     {LaTeX -> "u_L" }},
   {vL,     {LaTeX -> "\\nu_L" }},

   {DR,     {LaTeX -> "D_R" }},
   {ER,     {LaTeX -> "E_R" }},
   {UR,     {LaTeX -> "U_R" }},
   {EL,     {LaTeX -> "E_L" }},
   {DL,     {LaTeX -> "D_L" }},
   {UL,     {LaTeX -> "U_L" }},
   {VL,     {LaTeX -> "\\nu_{LL}" }}
        };   
