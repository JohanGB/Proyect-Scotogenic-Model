(* ::Package:: *)

OnlyLowEnergySPheno = True;

MINPAR={{1,lambda1INput},
 {2,lam4EtaINput}, 
 {3,lamHEta3INput},
  {4,lambda4HEtaINput}, 
  {5,lambda5HEtaINput}, 
  {6,lam4SigINput},
  {7,lamHSigINput},
  {8,lamEtaSigINput},
  {9, mEta2INput},
  {10, mSi2INput},
  {11, cTriINput}
};


RealParameters = {mEta2INput, mSi2INput, TINput, lambda1INput,lam4EtaINput,lamHEta3INput,lambda4HEtaINput,lambda5HEtaINput,lam4SigINput,lamHSigINput,lamEtaSigINput};
ParametersToSolveTadpoles = {mu2};


(*RenormalizationScaleFirstGuess = m0^2 + 4 m12^2;
RenormalizationScale = MSu[1]*MSu[6];

ConditionGUTscale = g1 == g2;*)



DEFINITION[MatchingConditions]= 
{{ v, vSM}, 
 {Ye, YeSM},
 {Yd, YdSM},
 {Yu, YuSM},
 {g1, g1SM},
 {g2, g2SM},
 {g3, g3SM}  };
 

BoundaryLowScaleInput={
 {\[Lambda],lambda1INput}, 
 {lam4Eta,lam4EtaINput}, 
 {lamHEta3,lamHEta3INput}, 
 {lambda4HEta,lambda4HEtaINput}, 
 {lambda5HEta,lambda5HEtaINput}, 
 {lam4Sig,lam4SigINput},
 {lamHSig,lamHSigINput},
 {lamEtaSig,lamEtaSigINput},
 {mEta2, mEta2INput},
 {mSi2,mSi2INput},
 {cTri,cTriINput},
 {mN, LHInput[mN]},
 {Yn, LHInput[Yn]}
};


AddTreeLevelUnitarityLimits=False;
(*
DEFINITION[MatchingConditions]=Default[THDMII];*)


ListDecayParticles = {Fu,Fe,Fd,Fv,hh,etaI,FX0,P0};(*{Fu,Fe,Fd,Fv,VZ,VWp,hh,etaR, etaI,etap,FX0, Ah};*)
ListDecayParticles3B = Automatic(*{{Fu,"Fu.f90"},{Fe,"Fe.f90"},{Fd,"Fd.f90"}}*);
RenConditionsDecays={
{dCosTW, 1/2*Cos[ThetaW] * (PiVWm/(MVWM^2) - PiVZ/(mVZ^2)) },
{dSinTW, -dCosTW/Tan[ThetaW]},
{dg2, 1/2*g2*(derPiVPheavy0 + PiVPlightMZ/MVZ^2 -
(-(PiVWm/MVWm^2) + PiVZ/MVZ^2)/Tan[ThetaW]^2
+ (2*PiVZVP*Tan[ThetaW])/MVZ^2) },
{dg1, dg2*Tan[ThetaW]+g2*dSinTW/Cos[ThetaW]
- dCosTW*g2*Tan[ThetaW]/Cos[ThetaW]} };
