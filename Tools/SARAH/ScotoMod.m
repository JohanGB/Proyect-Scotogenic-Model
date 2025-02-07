(* ::Package:: *)

Off[General::spell] (* Tells Mathematica to shut off warnings related to similar symbol names*)

Model`Name = "Scotogenic_SLNV"; (*Model*)
Model`NameLaTeX ="Scotogenic Model with Spontaneous Lepton Number Violation";(*Model Name*)
Model`Authors = "V. De Romeri, J. Nava, M. Puerta, A. Vicente, G. Ardila, A.Florez, O. Zapata";(*Authors of the file*)
Model`Date = "2023-07-07";(*Implementation date*)

(* " 2023-07-07 (First implementation by G. Ardila)"*) (*Comments must contain basic lines related to updates*)

SuperSymmetricModel=False; (*Not mandatory but clarifies SARAH if the model is SUSY or nonSUSY*)


(*-------------------------------------------*)
(*   Particle Content*)
(*-------------------------------------------*)

(* Global Groups *)

Global[[1]] = { Z[2], Z2 };

(* Gauge Groups *)

Gauge[[1]]={B,   U[1], hypercharge, g1,False,1};
Gauge[[2]]={WB, SU[2], left,        g2,True, 1};
Gauge[[3]]={G,  SU[3], color,       g3,False,1};




(* Matter Fields *)

(*
	Structure: Fermion(Scalar)Fields[[number]]={name, number of gens,
	name of the SU2L components, hypercharge, SU2L representation, SU3C representation, 
	charge under globals} 
	
	NOTE: if some field belongs in the antifundamental irrep, use -
*)

(*SM Fermions*)

FermionFields[[1]] = {q, 3, {uL, dL},     1/6, 2,  3,1};  
FermionFields[[2]] = {l, 3, {vL, eL},    -1/2, 2,  1,1};
FermionFields[[3]] = {d, 3, conj[dR],     1/3, 1, -3,1};
FermionFields[[4]] = {u, 3, conj[uR],    -2/3, 1, -3,1};
FermionFields[[5]] = {e, 3, conj[eR],       1, 1,  1,1};

(*New Fermions*)

FermionFields[[6]]={n, 3, conj[N0], 0, 1, 1, -1};

(*SM Scalars*)

ScalarFields[[1]] =  {H, 1, {Hp, H0},     1/2, 2,  1,1};


(*New Scalars*)

ScalarFields[[2]] = {Eta, 1, {etap,eta0}, 1/2, 2, 1, -1};

ScalarFields[[3]] = {S, 1, sig0, 0, 1, 1, -1};(*Sigma field*)

RealScalars = { S };


        
(*----------------------------------------------*)
(*   DEFINITION                                 *)
(*----------------------------------------------*)

NameOfStates={GaugeES, EWSB}; 
(*Two sets of states, gauge eigenstates first and then mass eigenstates*)

(* ----- Before EWSB ----- *)

(*Here the lagrangian is defined.
The kinetic terms are canonical, such that they must not be added.
AddHC is used to add the hermitian conjugate of any term. 
Barred spinors are automatically introduced via the structure of the lagrangian.
*)

DEFINITION[GaugeES][LagrangianInput]= {
	{LagFer, {AddHC->True}},
	{LagNV, {AddHC->True}},
	{LagH, {AddHC->False}},
	{LagEt, {AddHC->False}},
	{LagSi, {AddHC->False}},
	{LagHEt, {AddHC->False}},
	{LagHEtHC, {AddHC->True}},
	{LagHSi,{AddHC->False}},
	{LagTrilinear,{AddHC->True}},
	{LagEtSi, {AddHC->False}}
};


(*For multiplication of fields use the dot*)

(*SM yukawas plus the terms associated with neutrino mass*)

LagFer= Yd conj[H] . d . q+ Ye conj[H] . e . l+ Yu H . u . q+ Yn l . Eta . n;

(*Heavy neutrino mass*)

LagNV= - 1/2 mN n . n; 

(*Usual Higgs lagrangian*)

LagH=-(mu2 conj[H] . H+ 1/2 \[Lambda] conj[H] . H . conj[H] . H);

(*Higgs-like lagrangian for eta*)

LagEt=-(mEta2 conj[Eta] . Eta+ 1/2 lam4Eta conj[Eta] . Eta . conj[Eta] . Eta);

(*Higgs-like Lagrangian for the sigma field*)

LagSi=-(1/2 mSi2 conj[S] . S+ 1/2 lam4Sig conj[S] . S . conj[S] . S);

(*Portal terms*)

LagHEt=-(lamHEta3 conj[H] . H . conj[Eta] . Eta + lambda4HEta conj[H] . Eta . conj[Eta] . H);

LagHEtHC=-(1/2 lambda5HEta conj[H] . Eta . conj[H] . Eta);

LagHSi=-( lamHSig conj[S] . S . conj[H] . H );

LagEtSi= -( lamEtaSig  conj[S] . S . conj[Eta] . Eta);
LagTrilinear = - (1/2 cTri conj[S] . conj[H] . Eta);


			  		  

(* Gauge Sector *)

DEFINITION[EWSB][GaugeSector] =
{ 
  {{VB,VWB[3]},{VP,VZ},ZZ},
  {{VWB[1],VWB[2]},{VWp,conj[VWp]},ZW}
};     
        
   
        
          	

(* ----- VEVs ---- *)

(*The structure is:
	{neutral component, {vev, its normalization}, {Goldstone, prefactor of goldstone},{Higgs, prefactor}}
*)
DEFINITION[EWSB][VEVs]= 
{    {H0, {v, 1/Sqrt[2]}, {Ah, \[ImaginaryI]/Sqrt[2]}, {hh, 1/Sqrt[2]}}, 

	{eta0, {0,0}, {etaI,\[ImaginaryI]/Sqrt[2]},{etaR,1/Sqrt[2]}}
};
 
(*Here, the mass eigenstates are defined in terms of the weak eigenstates 
	Structure for Majoranas and scalars: {{gaugeeigen1, gaugeeigen2,...}, {massmatrix, mixingmatrix}}
	Structure for Diracs:{{gaugeleft1, gaugeleft2,...},{massleft, mixingleft}, {gaugeright1,...}, {mass right, mixing right}}
*)
DEFINITION[EWSB][MatterSector]=   
   { {{{dL}, {conj[dR]}}, {{DL,Vd}, {DR,Ud}}},
     {{{uL}, {conj[uR]}}, {{UL,Vu}, {UR,Uu}}},
     {{{eL}, {conj[eR]}}, {{EL,Ve}, {ER,Ue}}}, 
     { {vL}, {VL, Vv}},
     {{sig0,etaR}         , {P0,ZSc}},
     {{conj[N0]},{X0, ZX}}
    };  



(*------------------------------------------------------*)
(* Dirac-Spinors *)
(*------------------------------------------------------*)

DEFINITION[EWSB][DiracSpinors]={
 Fd ->{  DL, conj[DR]},
 Fe ->{  EL, conj[ER]},
 Fu ->{  UL, conj[UR]},
 Fv ->{  VL, conj[VL]},
 FX0 -> {  X0, conj[X0]}
};

DEFINITION[EWSB][GaugeES]={
 Fd1 ->{  FdL, 0},
 Fd2 ->{  0, FdR},
 Fu1 ->{  Fu1, 0},
 Fu2 ->{  0, Fu2},
 Fe1 ->{  Fe1, 0},
 Fe2 ->{  0, Fe2}};

