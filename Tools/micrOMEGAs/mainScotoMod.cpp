#include"../include/micromegas.h"
#include"../include/micromegas_aux.h"
#include"lib/pmodel.h"
#include <math.h>
#include <cmath>
#include <stdlib.h> 
#include <time.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <sstream>
#include <bits/stdc++.h> 
using namespace std;



//--------------------------------------------------------------------------------------------------------
//               This part of the code allows the product between a complex and an int
//--------------------------------------------------------------------------------------------------------

// Trick to allow type promotion below
template <typename T>
struct identity_t { typedef T type; };

/// Make working with std::complex<> nubmers suck less... allow promotion.
#define COMPLEX_OPS(OP)                                                 \
  template <typename _Tp>                                               \
  std::complex<_Tp>                                                     \
  operator OP(std::complex<_Tp> lhs, const typename identity_t<_Tp>::type & rhs) \
  {                                                                     \
    return lhs OP rhs;                                                  \
  }                                                                     \
  template <typename _Tp>                                               \
  std::complex<_Tp>                                                     \
  operator OP(const typename identity_t<_Tp>::type & lhs, const std::complex<_Tp> & rhs) \
  {                                                                     \
    return lhs OP rhs;                                                  \
  }
COMPLEX_OPS(+)
COMPLEX_OPS(-)
COMPLEX_OPS(*)
COMPLEX_OPS(/)
#undef COMPLEX_OPS
//--------------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------------




//-----------------------Main----------------------------------



int main(int argc,char** argv)
{
   srand(time(NULL)); 	//initialise la sequence de la fonction rand afin que la serie ne commence pas tjs au meme pt (va prendre l'heure)
   int err;
   char cdmName[10];
   int spin2, charge3, cdim;

  ForceUG=0;  /* to Force Unitary Gauge assign 1 */
  VZdecay=0; VWdecay=0;  
  
   int taille = 100;
   double Q;
   char chaine[taille] ;
   int errSph;

	int nblines = 324;
	ifstream inFile;

//--------------------------------------------------------
//                Parameter definitions 
//--------------------------------------------------------

	//COUPLINGS FROM THE SCALAR SECTOR
	
  double l1; //Higgs coupling, it has to be changed to obtain Mh = 125Gev

   // COUPLINGS FROM THE SCALAR SECTOR
  double LHS;
  double LES;
  double L4S;
  double L4Et;
  double LHE33;
  double LHE32;
  double LHE31;

  double cTri;
  // COUPLINGS FROM THE FERMION SECTOR
  //coupling of : Yn L Et N
  double RYn11, IYn11 ; //Real and Imaginary parts
  double RYn12, IYn12 ; 
  double RYn13, IYn13 ;  
  
  double RYn21, IYn21 ; 
  double RYn22, IYn22 ; 
  double RYn23, IYn23 ;  

  double RYn31, IYn31 ; 
  double RYn32, IYn32 ; 
  double RYn33, IYn33 ;  
  
  //mN couplings
  double mN11; 
  double mN12; 
  double mN13;  
  double mN21; 
  double mN22; 
  double mN23;
  double mN31; 
  double mN32; 
  double mN33;

  double RZX33;
  double RZX32;
  double RZX31;
  double RZX23;
  double RZX22;
  double RZX21;
  double RZX13;
  double RZX12;
  double RZX11;
  
  double RZUR33;
  double RZUR32;
  double RZUR31;
  double RZUR23;
  double RZUR22;
  double RZUR21;
  double RZUR13;
  double RZUR12;
  double RZUR11;
  
  double RZUL33;
  double RZUL32;
  double RZUL31;
  double RZUL23;
  double RZUL22;
  double RZUL21;
  double RZUL13;
  double RZUL12;
  double RZUL11;
  
  double RZS22;
  double RZS21;
  double RZS12;
  double RZS11;
  
  double RZER33;
  double RZER32;
  double RZER31;
  double RZER23;
  double RZER22;
  double RZER21;
  double RZER13;
  double RZER12;
  double RZER11;
  
  double RZEL33;
  double RZEL32;
  double RZEL31;
  double RZEL23;
  double RZEL22;
  double RZEL21;
  double RZEL13;
  double RZEL12;
  double RZEL11;
  
  double RZDR33;
  double RZDR32;
  double RZDR31;
  double RZDR23;
  double RZDR22;
  double RZDR21;
  double RZDR13;
  double RZDR12;
  double RZDR11;
  
  double RZDL33;
  double RZDL32;
  double RZDL31;
  double RZDL23;
  double RZDL22;
  double RZDL21;
  double RZDL13;
  double RZDL12;
  double RZDL11;
  
  double RUV33;
  double RUV32;
  double RUV31;
  double RUV23;
  double RUV22;
  double RUV21;
  double RUV13;
  double RUV12;
  double RUV11;
  
  double IZX33;
  double IZX32;
  double IZX31;
  double IZX23;
  double IZX22;
  double IZX21;
  double IZX13;
  double IZX12;
  double IZX11;
  
  double IZUR33;
  double IZUR32;
  double IZUR31;
  double IZUR23;
  double IZUR22;
  double IZUR21;
  double IZUR13;
  double IZUR12;
  double IZUR11;
  
  double IZUL33;
  double IZUL32;
  double IZUL31;
  double IZUL23;
  double IZUL22;
  double IZUL21;
  double IZUL13;
  double IZUL12;
  double IZUL11;
  
  double IZS22;
  double IZS21;
  double IZS12;
  double IZS11;
  
  double IZER33;
  double IZER32;
  double IZER31;
  double IZER23;
  double IZER22;
  double IZER21;
  double IZER13;
  double IZER12;
  double IZER11;
  
  double IZEL33;
  double IZEL32;
  double IZEL31;
  double IZEL23;
  double IZEL22;
  double IZEL21;
  double IZEL13;
  double IZEL12;
  double IZEL11;
  
  double IZDR33;
  double IZDR32;
  double IZDR31;
  double IZDR23;
  double IZDR22;
  double IZDR21;
  double IZDR13;
  double IZDR12;
  double IZDR11;
  
  double IZDL33;
  double IZDL32;
  double IZDL31;
  double IZDL23;
  double IZDL22;
  double IZDL21;
  double IZDL13;
  double IZDL12;
  double IZDL11;
  
  double IUV33;
  double IUV32;
  double IUV31;
  double IUV23;
  double IUV22;
  double IUV21;
  double IUV13;
  double IUV12;
  double IUV11;


  // COUPLINGS FROM THE GAUGE SECTOR
  double MSi;
  double MSi2 = pow(MSi,2);
  double MEt2, MEt, MPsi, MSigma;
  double mEtaI_tree, mEtp_tree, mEt0_tree,mSi_tree; 
  double mEtaI_tree_oneloop, mEtp_tree_oneloop , mEt0_tree_oneloop, mSi_tree_oneloop;

  double Metp;
  double Mh;
  double MetaI;
  double MP01;
  double MP02;
  double MZ;
  
  double Md1;
  double Md2;
  double Md3;
  
  double Mu1;
  double Mu2;
  double Mu3;
  
  double Me1;
  double Me2;
  double Me3;
  
  double Mnu1;
  double Mnu2;
  double Mnu3;
  
  double MX01;
  double MX02;
  double MX03;
  
  double HPP1;
  double HGG1; 
  
  double BrMEG ;  //Branching ratio : mu -> e gamma
  double BrTEG ;  //Branching ratio : tau -> e gamma
  double BrTMG ;  //Branching ratio : tau -> mu gamma
  double BrM3e ;  //Branching ratio : mu -> 3e
  double BrT3e ;  //Branching ratio : tau -> 3e 
  double BrT3m ;  //Branching ratio : tau -> 3mu


  double g_2e;  //(g-2)electron 
  double g_2m;  //muon
  double g_2t;  //tau
  double v = 246.22;
// Continue to write all your double parameters



//--------------------------------------------------------------------
// 			SPheno commands
//	     readings of the values in SPheno Output
//--------------------------------------------------------------------


    string name = ""; 
	if(argc == 2){ //Check if there is smthg given in the command
	name = argv[1];}
 
    int n = name.length(); 
  
    // declaring character array 
    char filename[n + 1]; 
  
    // copying the contents of the 
    // string to char array 
    strcpy(filename, name.c_str()); 

    FILE *output = NULL; 
    output = fopen(filename,"r");


    if(output != NULL) {   

    errSph = slhaRead(filename,0);


    Mh     = slhaVal("MASS",Q,1,25);     
    MP01   = slhaVal("MASS",Q,1,2001); 
    MP02   = slhaVal("MASS",Q,1,2002); 
    MZ     = slhaVal("MASS",Q,1,23); 
    
    double Md1    = slhaVal("MASS",Q,1,1); 
    double Md2    = slhaVal("MASS",Q,1,3); 
    double Md3    = slhaVal("MASS",Q,1,5); 
    double Mu1    = slhaVal("MASS",Q,1,2); 
    double Mu2    = slhaVal("MASS",Q,1,4); 
    double Mu3    = slhaVal("MASS",Q,1,6); 
    double Me1    = slhaVal("MASS",Q,1,11); 
    double Me2    = slhaVal("MASS",Q,1,13); 
    double Me3    = slhaVal("MASS",Q,1,15); 
    
    Mnu1   = slhaVal("MASS",Q,1,12); 
    Mnu2   = slhaVal("MASS",Q,1,14); 
    Mnu3   = slhaVal("MASS",Q,1,16); 
    
    Metp  = slhaVal("MASS",Q,1,1003); 
    MetaI  = slhaVal("MASS",Q,1,1002);     
    MX01   = slhaVal("MASS",Q,1,3001); 
    MX02   = slhaVal("MASS",Q,1,3002); 
    MX03   = slhaVal("MASS",Q,1,3003); 
    
    g_2e = slhaVal("SPhenoLowEnergy",Q,1,20);
    g_2m = slhaVal("SPhenoLowEnergy",Q,1,21);
    g_2t = slhaVal("SPhenoLowEnergy",Q,1,22);

    BrMEG = slhaVal("FlavorKitLFV",Q,1,701);
    BrTEG = slhaVal("FlavorKitLFV",Q,1,702); // tau e gamma
    BrTMG = slhaVal("FlavorKitLFV",Q,1,703);
    BrM3e = slhaVal("FlavorKitLFV",Q,1,901); // mu -> 3e
    BrT3e = slhaVal("FlavorKitLFV",Q,1,902); // tau -> 3e 
    BrT3m = slhaVal("FlavorKitLFV",Q,1,903); // tau -> 3mu
    
    RYn11  = slhaVal("COUPLINGSYN",Q,2,1,1); 
    RYn12  = slhaVal("COUPLINGSYN",Q,2,1,2); 
    RYn13  = slhaVal("COUPLINGSYN",Q,2,1,3); 
    RYn21  = slhaVal("COUPLINGSYN",Q,2,2,1); 
    RYn22  = slhaVal("COUPLINGSYN",Q,2,2,2); 
    RYn23  = slhaVal("COUPLINGSYN",Q,2,2,3); 
    RYn31  = slhaVal("COUPLINGSYN",Q,2,3,1); 
    RYn32  = slhaVal("COUPLINGSYN",Q,2,3,2); 
    RYn33  = slhaVal("COUPLINGSYN",Q,2,3,3); 
    
    IYn11  = slhaVal("IMCOUPLINGSYN",Q,2,1,1); 
    IYn12  = slhaVal("IMCOUPLINGSYN",Q,2,1,2); 
    IYn13  = slhaVal("IMCOUPLINGSYN",Q,2,1,3); 
    IYn21  = slhaVal("IMCOUPLINGSYN",Q,2,2,1); 
    IYn22  = slhaVal("IMCOUPLINGSYN",Q,2,2,2); 
    IYn23  = slhaVal("IMCOUPLINGSYN",Q,2,2,3); 
    IYn31  = slhaVal("IMCOUPLINGSYN",Q,2,3,1); 
    IYn32  = slhaVal("IMCOUPLINGSYN",Q,2,3,2); 
    IYn33  = slhaVal("IMCOUPLINGSYN",Q,2,3,3); 
  
    l1   = slhaVal("MINPAR",Q,1,1); 
    L4Et  = slhaVal("MINPAR",Q,1,2);
    LHE31 = slhaVal("MINPAR",Q,1,3);     
    LHE32 = slhaVal("MINPAR",Q,1,4); 
    LHE33 = slhaVal("MINPAR",Q,1,5); 
    L4S   = slhaVal("MINPAR",Q,1,6); 
    LHS   = slhaVal("MINPAR",Q,1,7); 
    LES   = slhaVal("MINPAR",Q,1,8); 
    
    cTri  = slhaVal("MINPAR",Q,1,11); 
    
    RZDL11 = slhaVal("UDLMIX",Q,2,1,1); 
    RZDL12 = slhaVal("UDLMIX",Q,2,1,2); 
    RZDL13 = slhaVal("UDLMIX",Q,2,1,3); 
    RZDL21 = slhaVal("UDLMIX",Q,2,2,1); 
    RZDL22 = slhaVal("UDLMIX",Q,2,2,2); 
    RZDL23 = slhaVal("UDLMIX",Q,2,2,3); 
    RZDL31 = slhaVal("UDLMIX",Q,2,3,1); 
    RZDL32 = slhaVal("UDLMIX",Q,2,3,2); 
    RZDL33 = slhaVal("UDLMIX",Q,2,3,3); 
        
    IZDL11 = slhaVal("IMUDLMIX",Q,2,1,1); 
    IZDL12 = slhaVal("IMUDLMIX",Q,2,1,2); 
    IZDL13 = slhaVal("IMUDLMIX",Q,2,1,3); 
    IZDL21 = slhaVal("IMUDLMIX",Q,2,2,1); 
    IZDL22 = slhaVal("IMUDLMIX",Q,2,2,2); 
    IZDL23 = slhaVal("IMUDLMIX",Q,2,2,3); 
    IZDL31 = slhaVal("IMUDLMIX",Q,2,3,1); 
    IZDL32 = slhaVal("IMUDLMIX",Q,2,3,2); 
    IZDL33 = slhaVal("IMUDLMIX",Q,2,3,3); 
    
    RZDR11 = slhaVal("UDRMIX",Q,2,1,1); 
    RZDR12 = slhaVal("UDRMIX",Q,2,1,2); 
    RZDR13 = slhaVal("UDRMIX",Q,2,1,3); 
    RZDR21 = slhaVal("UDRMIX",Q,2,2,1); 
    RZDR22 = slhaVal("UDRMIX",Q,2,2,2);  
    RZDR23 = slhaVal("UDRMIX",Q,2,2,3); 
    RZDR31 = slhaVal("UDRMIX",Q,2,3,1); 
    RZDR32 = slhaVal("UDRMIX",Q,2,3,2);  
    RZDR33 = slhaVal("UDRMIX",Q,2,3,3); 
        
    IZDR11 = slhaVal("IMUDRMIX",Q,2,1,1); 
    IZDR12 = slhaVal("IMUDRMIX",Q,2,1,2); 
    IZDR13 = slhaVal("IMUDRMIX",Q,2,1,3); 
    IZDR21 = slhaVal("IMUDRMIX",Q,2,2,1); 
    IZDR22 = slhaVal("IMUDRMIX",Q,2,2,2); 
    IZDR23 = slhaVal("IMUDRMIX",Q,2,2,3); 
    IZDR31 = slhaVal("IMUDRMIX",Q,2,3,1); 
    IZDR32 = slhaVal("IMUDRMIX",Q,2,3,2); 
    IZDR33 = slhaVal("IMUDRMIX",Q,2,3,3); 
    
    RZUL11 = slhaVal("UULMIX",Q,2,1,1); 
    RZUL12 = slhaVal("UULMIX",Q,2,1,2); 
    RZUL13 = slhaVal("UULMIX",Q,2,1,3);    
    RZUL21 = slhaVal("UULMIX",Q,2,2,1);    
    RZUL22 = slhaVal("UULMIX",Q,2,2,2);    
    RZUL23 = slhaVal("UULMIX",Q,2,2,3);  
    RZUL31 = slhaVal("UULMIX",Q,2,3,1);     
    RZUL32 = slhaVal("UULMIX",Q,2,3,2);    
    RZUL33 = slhaVal("UULMIX",Q,2,3,3);   
    
    IZUL11 = slhaVal("IMUULMIX",Q,2,1,1); 
    IZUL12 = slhaVal("IMUULMIX",Q,2,1,2); 
    IZUL13 = slhaVal("IMUULMIX",Q,2,1,3); 
    IZUL21 = slhaVal("IMUULMIX",Q,2,2,1); 
    IZUL22 = slhaVal("IMUULMIX",Q,2,2,2); 
    IZUL23 = slhaVal("IMUULMIX",Q,2,2,3); 
    IZUL31 = slhaVal("IMUULMIX",Q,2,3,1); 
    IZUL32 = slhaVal("IMUULMIX",Q,2,3,2); 
    IZUL33 = slhaVal("IMUULMIX",Q,2,3,3); 
    
    RZUR11 = slhaVal("UURMIX",Q,2,1,1); 
    RZUR12 = slhaVal("UURMIX",Q,2,1,2);    
    RZUR13 = slhaVal("UURMIX",Q,2,1,3);     
    RZUR21 = slhaVal("UURMIX",Q,2,2,1);    
    RZUR22 = slhaVal("UURMIX",Q,2,2,2);     
    RZUR23 = slhaVal("UURMIX",Q,2,2,3);    
    RZUR31 = slhaVal("UURMIX",Q,2,3,1);     
    RZUR32 = slhaVal("UURMIX",Q,2,3,2); 
    RZUR33 = slhaVal("UURMIX",Q,2,3,3);      
     
    IZUR11 = slhaVal("IMUURMIX",Q,2,1,1); 
    IZUR12 = slhaVal("IMUURMIX",Q,2,1,2);
    IZUR13 = slhaVal("IMUURMIX",Q,2,1,3); 
    IZUR21 = slhaVal("IMUURMIX",Q,2,2,1); 
    IZUR22 = slhaVal("IMUURMIX",Q,2,2,2); 
    IZUR23 = slhaVal("IMUURMIX",Q,2,2,3); 
    IZUR31 = slhaVal("IMUURMIX",Q,2,3,1); 
    IZUR32 = slhaVal("IMUURMIX",Q,2,3,2); 
    IZUR33 = slhaVal("IMUURMIX",Q,2,3,3); 
    
    RZEL11 = slhaVal("UELMIX",Q,2,1,1); 
    RZEL12 = slhaVal("UELMIX",Q,2,1,2);     
    RZEL13 = slhaVal("UELMIX",Q,2,1,3);    
    RZEL21 = slhaVal("UELMIX",Q,2,2,1);    
    RZEL22 = slhaVal("UELMIX",Q,2,2,2);     
    RZEL23 = slhaVal("UELMIX",Q,2,2,3);    
    RZEL31 = slhaVal("UELMIX",Q,2,3,1);    
    RZEL32 = slhaVal("UELMIX",Q,2,3,2);     
    RZEL33 = slhaVal("UELMIX",Q,2,3,3); 

    IZEL11 = slhaVal("IMUELMIX",Q,2,1,1); 
    IZEL12 = slhaVal("IMUELMIX",Q,2,1,2); 
    IZEL13 = slhaVal("IMUELMIX",Q,2,1,3); 
    IZEL21 = slhaVal("IMUELMIX",Q,2,2,1); 
    IZEL22 = slhaVal("IMUELMIX",Q,2,2,2); 
    IZEL23 = slhaVal("IMUELMIX",Q,2,2,3); 
    IZEL31 = slhaVal("IMUELMIX",Q,2,3,1); 
    IZEL32 = slhaVal("IMUELMIX",Q,2,3,2); 
    IZEL33 = slhaVal("IMUELMIX",Q,2,3,3); 

 
    RZER11 = slhaVal("UERMIX",Q,2,1,1); 
    RZER12 = slhaVal("UERMIX",Q,2,1,2);     
    RZER13 = slhaVal("UERMIX",Q,2,1,3);     
    RZER21 = slhaVal("UERMIX",Q,2,2,1);     
    RZER22 = slhaVal("UERMIX",Q,2,2,2);    
    RZER23 = slhaVal("UERMIX",Q,2,2,3);    
    RZER31 = slhaVal("UERMIX",Q,2,3,1);    
    RZER32 = slhaVal("UERMIX",Q,2,3,2); 
    RZER33 = slhaVal("UERMIX",Q,2,3,3);  
   

    IZER11 = slhaVal("IMUERMIX",Q,2,1,1); 
    IZER12 = slhaVal("IMUERMIX",Q,2,1,2); 
    IZER13 = slhaVal("IMUERMIX",Q,2,1,3); 
    IZER21 = slhaVal("IMUERMIX",Q,2,2,1); 
    IZER22 = slhaVal("IMUERMIX",Q,2,2,2); 
    IZER23 = slhaVal("IMUERMIX",Q,2,2,3); 
    IZER31 = slhaVal("IMUERMIX",Q,2,3,1); 
    IZER32 = slhaVal("IMUERMIX",Q,2,3,2); 
    IZER33 = slhaVal("IMUERMIX",Q,2,3,3);     

 
    RUV11  = slhaVal("UVMIX",Q,2,1,1); 
    RUV12  = slhaVal("UVMIX",Q,2,1,2);     
    RUV13  = slhaVal("UVMIX",Q,2,1,3);    
    RUV21  = slhaVal("UVMIX",Q,2,2,1);     
    RUV22  = slhaVal("UVMIX",Q,2,2,2);    
    RUV23  = slhaVal("UVMIX",Q,2,2,3);     
    RUV31  = slhaVal("UVMIX",Q,2,3,1);    
    RUV32  = slhaVal("UVMIX",Q,2,3,2); 
    RUV33  = slhaVal("UVMIX",Q,2,3,3);     
    
    IUV11  = slhaVal("IMUVMIX",Q,2,1,1); 
    IUV12  = slhaVal("IMUVMIX",Q,2,1,2); 
    IUV13  = slhaVal("IMUVMIX",Q,2,1,3); 
    IUV21  = slhaVal("IMUVMIX",Q,2,2,1); 
    IUV22  = slhaVal("IMUVMIX",Q,2,2,2); 
    IUV23  = slhaVal("IMUVMIX",Q,2,2,3); 
    IUV31  = slhaVal("IMUVMIX",Q,2,3,1); 
    IUV32  = slhaVal("IMUVMIX",Q,2,3,2); 
    IUV33  = slhaVal("IMUVMIX",Q,2,3,3); 
    
    RZS11  = slhaVal("ZScalar",Q,2,1,1); 
    RZS12  = slhaVal("ZScalar",Q,2,1,2);     
    RZS21  = slhaVal("ZScalar",Q,2,2,1);     
    RZS22  = slhaVal("ZScalar",Q,2,2,2);     

 /*
    IZS11  = slhaVal("IMZScalar",Q,2,1,1); 
    IZS12  = slhaVal("IMZScalar",Q,2,1,2); 
    IZS21  = slhaVal("IMZScalar",Q,2,2,1); 
    IZS22  = slhaVal("IMZScalar",Q,2,2,2); 
*/

    RZX11  = slhaVal("ZX",Q,2,1,1);     
    RZX12  = slhaVal("ZX",Q,2,1,2);     
    RZX13  = slhaVal("ZX",Q,2,1,3); 
    RZX21  = slhaVal("ZX",Q,2,2,1);     
    RZX22  = slhaVal("ZX",Q,2,2,2);     
    RZX23  = slhaVal("ZX",Q,2,2,3); 
    RZX31  = slhaVal("ZX",Q,2,3,1);     
    RZX32  = slhaVal("ZX",Q,2,3,2); 
    RZX33  = slhaVal("ZX",Q,2,3,3);     
 

    IZX11  = slhaVal("IMZX",Q,2,1,1); 
    IZX12  = slhaVal("IMZX",Q,2,1,2);
    IZX13  = slhaVal("IMZX",Q,2,1,3); 
    IZX21  = slhaVal("IMZX",Q,2,2,1); 
    IZX22  = slhaVal("IMZX",Q,2,2,2); 
    IZX23  = slhaVal("IMZX",Q,2,2,3); 
    IZX31  = slhaVal("IMZX",Q,2,3,1); 
    IZX32  = slhaVal("IMZX",Q,2,3,2); 
    IZX33  = slhaVal("IMZX",Q,2,3,3); 

    mN11 = slhaVal("MassMatrixMN",Q,2,1,1);
    mN12 = slhaVal("MassMatrixMN",Q,2,1,2);
    mN13 = slhaVal("MassMatrixMN",Q,2,1,3);

    mN21 = slhaVal("MassMatrixMN",Q,2,2,1);
    mN22 = slhaVal("MassMatrixMN",Q,2,2,2);
    mN23 = slhaVal("MassMatrixMN",Q,2,2,3);

    mN31 = slhaVal("MassMatrixMN",Q,2,3,1);
    mN32 = slhaVal("MassMatrixMN",Q,2,3,2);
    mN33 = slhaVal("MassMatrixMN",Q,2,3,3);
 
    g_2e = slhaVal("SPhenoLowEnergy",Q,1,20);
    g_2m = slhaVal("SPhenoLowEnergy",Q,1,21);
    g_2t = slhaVal("SPhenoLowEnergy",Q,1,22);
 
    HPP1   = slhaVal("EFFHIGGSCOUPLINGS",Q,3,25,22,22); 
    HGG1   = slhaVal("EFFHIGGSCOUPLINGS",Q,3,25,21,21); 
   
//-------Extract PMNS angles-------
//PMNS*Majorana phases = ( A B C
//                         D E F
//                         G H I )
// PMNS = Ue^dagger * Unu

	complex<double> Ue11(RZEL11,IZEL11);
	complex<double> Ue12(RZEL12,IZEL12);
	complex<double> Ue13(RZEL13,IZEL13);
	complex<double> Ue21(RZEL21,IZEL21);
	complex<double> Ue22(RZEL22,IZEL22);
	complex<double> Ue23(RZEL23,IZEL23);
	complex<double> Ue31(RZEL31,IZEL31);
	complex<double> Ue32(RZEL32,IZEL32);
	complex<double> Ue33(RZEL33,IZEL33);

	complex<double> Unu11(RUV11,IUV11);
	complex<double> Unu12(RUV12,IUV12);
	complex<double> Unu13(RUV13,IUV13);
	complex<double> Unu21(RUV21,IUV21);
	complex<double> Unu22(RUV22,IUV22);
	complex<double> Unu23(RUV23,IUV23);
	complex<double> Unu31(RUV31,IUV31);
	complex<double> Unu32(RUV32,IUV32);
	complex<double> Unu33(RUV33,IUV33);

	complex<double> A = conj(Ue11)*Unu11 + conj(Ue21)*Unu21 + conj(Ue31)*Unu31;
	complex<double> D = conj(Ue12)*Unu11 + conj(Ue22)*Unu21 + conj(Ue32)*Unu31;
	complex<double> G = conj(Ue13)*Unu11 + conj(Ue23)*Unu21 + conj(Ue33)*Unu31;
	complex<double> B = conj(Ue11)*Unu12 + conj(Ue21)*Unu22 + conj(Ue31)*Unu32;
	complex<double> E = conj(Ue12)*Unu12 + conj(Ue22)*Unu22 + conj(Ue32)*Unu32;
	complex<double> H = conj(Ue13)*Unu12 + conj(Ue23)*Unu22 + conj(Ue33)*Unu32;
	complex<double> C = conj(Ue11)*Unu13 + conj(Ue21)*Unu23 + conj(Ue31)*Unu33;
	complex<double> F = conj(Ue12)*Unu13 + conj(Ue22)*Unu23 + conj(Ue32)*Unu33;
	complex<double> I = conj(Ue13)*Unu13 + conj(Ue23)*Unu23 + conj(Ue33)*Unu33;

	complex<double> PMNS[3][3] = { {A, B, C},
				       {D, E, F},
				       {G, H, I} };




	//complex<double> nb1(2,3);
	//complex<double> nb2(5,1);
	//cout <<" nb cplx 1 : " << nb1 << " et nb cplex 2 : " << nb2 << endl;
	//cout << "nb1 * nb2 = " << nb1*nb2 << endl;


	complex<double> Theta_13_cpp = asin(abs(PMNS[0][2]))	;
	complex<double> Theta_12_cpp = atan(abs(PMNS[0][1]/PMNS[0][0]));
	complex<double> Theta_23_cpp = atan(abs(PMNS[1][2]/PMNS[2][2]));


   
   //Conitnue to read all the params from SPheno output
   // Close the file
  
  
   fclose(output); 



//--------------------------------------------------
//          Micromegas Code Assigning values
//--------------------------------------------------

  // SM particles

  assignValW("Mh",Mh);
  assignValW("MP01",MP01);
  assignValW("MP02",MP02);
  assignValW("MZ",91.2);
  assignValW("Md1",Md1);
  assignValW("Md2",Md2);
  assignValW("Md3",4.2);
  assignValW("Mu1",Mu1);
  assignValW("Mu2",1.3);
  assignValW("Mu3",173.2);
  assignValW("Me1",Me1);
  assignValW("Me2",Me2);
  assignValW("Me3",1.7);
  assignValW("Mnu1",Mnu1);
  assignValW("Mnu2",Mnu2);
  assignValW("Mnu3",Mnu3);
  
  assignValW("Metp",Metp);
  assignValW("MetaI",MetaI);
  assignValW("MX01",MX01);
  assignValW("MX02",MX02);
  assignValW("MX03",MX03);


  assignValW("RYn11",RYn11);
  assignValW("RYn12",RYn12);
  assignValW("RYn13",RYn13);
  
  assignValW("RYn21",RYn21);
  assignValW("RYn22",RYn22);
  assignValW("RYn23",RYn23);
  
  assignValW("RYn31",RYn31);
  assignValW("RYn32",RYn32);
  assignValW("RYn33",RYn33);


  assignValW("IYn11",0.0);
  assignValW("IYn12",0.0);
  assignValW("IYn13",0.0);
  
  assignValW("IYn21",0.0);
  assignValW("IYn22",0.0);
  assignValW("IYn23",0.0);
  
  assignValW("IYn31",0.0);
  assignValW("IYn32",0.0);
  assignValW("IYn33",0.0);

  assignValW("mN11",mN11);
  assignValW("mN12",mN12);  
  assignValW("mN13",mN13);  
 
  assignValW("mN21",mN21);
  assignValW("mN22",mN22);  
  assignValW("mN23",mN23);  
  
  assignValW("mN31",mN31);
  assignValW("mN32",mN32);  
  assignValW("mN33",mN33);  

  assignValW("RL4Et",L4Et);
  assignValW("IL4Et",0.0);
  
  assignValW("L4S",L4S);
  assignValW("l1",l1);
  
  assignValW("RLHE32",LHE32);
  assignValW("ILHE32",0.0);
  
  assignValW("RLHE31",LHE31);
  assignValW("ILHE31",0.0);
  
  assignValW("LHE33",LHE33);
  
  assignValW("LHS",LHS);
  
  assignValW("RcTri",cTri);
  assignValW("IcTri",0.0);
  
  
  assignValW("LES",LES);
  

  assignValW("RZX11", RZX11);
  assignValW("RZX12", RZX12);
  assignValW("RZX13", RZX13);
  assignValW("RZX21", RZX21);
  assignValW("RZX22", RZX22);
  assignValW("RZX23", RZX23);
  assignValW("RZX31", RZX31);
  assignValW("RZX32", RZX32);
  assignValW("RZX33", RZX33);
  assignValW("IZX11", 0.0);
  assignValW("IZX12", 0.0);
  assignValW("IZX13", 0.0);
  assignValW("IZX21", 0.0);
  assignValW("IZX22", 0.0);
  assignValW("IZX23", 0.0);
  assignValW("IZX31", 0.0);
  assignValW("IZX32", 0.0);
  assignValW("IZX33", 0.0); 

  assignValW("RZS11", RZS11);
  assignValW("RZS12", RZS12);
  assignValW("RZS21", RZS21);
  assignValW("RZS22", RZS22);
  assignValW("IZS11", 0.0);
  assignValW("IZS12", 0.0);
  assignValW("IZS21", 0.0);
  assignValW("IZS22", 0.0);

  assignValW("RZDL11", RZDL11);
  assignValW("RZDL12", RZDL12);
  assignValW("RZDL13", RZDL13);
  assignValW("RZDL21", RZDL21);
  assignValW("RZDL22", RZDL22);
  assignValW("RZDL23", RZDL23);
  assignValW("RZDL31", RZDL31);
  assignValW("RZDL32", RZDL32);
  assignValW("RZDL33", RZDL33);

  assignValW("RZDR11", RZDR11);
  assignValW("RZDR12", RZDR12);
  assignValW("RZDR13", RZDR13);
  assignValW("RZDR21", RZDR21);
  assignValW("RZDR22", RZDR22);
  assignValW("RZDR23", RZDR23);
  assignValW("RZDR31", RZDR31);
  assignValW("RZDR32", RZDR32);
  assignValW("RZDR33", RZDR33);

  assignValW("RZUL11", RZUL11);
  assignValW("RZUL12", RZUL12);
  assignValW("RZUL13", RZUL13);
  assignValW("RZUL21", RZUL21);
  assignValW("RZUL22", RZUL22);
  assignValW("RZUL23", RZUL23);
  assignValW("RZUL31", RZUL31);
  assignValW("RZUL32", RZUL32);
  assignValW("RZUL33", RZUL33);

  assignValW("RZUR11", RZUR11);
  assignValW("RZUR12", RZUR12);
  assignValW("RZUR13", RZUR13);
  assignValW("RZUR21", RZUR21);
  assignValW("RZUR22", RZUR22);
  assignValW("RZUR23", RZUR23);
  assignValW("RZUR31", RZUR31);
  assignValW("RZUR32", RZUR32);
  assignValW("RZUR33", RZUR33);

  assignValW("RZEL11", RZEL11);
  assignValW("RZEL12", RZEL12);
  assignValW("RZEL13", RZEL13);
  assignValW("RZEL21", RZEL21);
  assignValW("RZEL22", RZEL22);
  assignValW("RZEL23", RZEL23);
  assignValW("RZEL31", RZEL31);
  assignValW("RZEL32", RZEL32);
  assignValW("RZEL33", RZEL33);

  assignValW("RZER11", RZER11);
  assignValW("RZER12", RZER12);
  assignValW("RZER13", RZER13);
  assignValW("RZER21", RZER21);
  assignValW("RZER22", RZER22);
  assignValW("RZER23", RZER23);
  assignValW("RZER31", RZER31);
  assignValW("RZER32", RZER32);
  assignValW("RZER33", RZER33);

  assignValW("RUV11", RUV11);
  assignValW("RUV12", RUV12);
  assignValW("RUV13", RUV13);
  assignValW("RUV21", RUV21);
  assignValW("RUV22", RUV22);
  assignValW("RUV23", RUV23);
  assignValW("RUV31", RUV31);
  assignValW("RUV32", RUV32);
  assignValW("RUV33", RUV33);

  assignValW("IZDL11", IZDL11);
  assignValW("IZDL12", IZDL12);
  assignValW("IZDL13", IZDL13);
  assignValW("IZDL21", IZDL21);
  assignValW("IZDL22", IZDL22);
  assignValW("IZDL23", IZDL23);
  assignValW("IZDL31", IZDL31);
  assignValW("IZDL32", IZDL32);
  assignValW("IZDL33", IZDL33);

  assignValW("IZDR11", IZDR11);
  assignValW("IZDR12", IZDR12);
  assignValW("IZDR13", IZDR13);
  assignValW("IZDR21", IZDR21);
  assignValW("IZDR22", IZDR22);
  assignValW("IZDR23", IZDR23);
  assignValW("IZDR31", IZDR31);
  assignValW("IZDR32", IZDR32);
  assignValW("IZDR33", IZDR33);

  assignValW("IZUL11", IZUL11);
  assignValW("IZUL12", IZUL12);
  assignValW("IZUL13", IZUL13);
  assignValW("IZUL21", IZUL21);
  assignValW("IZUL22", IZUL22);
  assignValW("IZUL23", IZUL23);
  assignValW("IZUL31", IZUL31);
  assignValW("IZUL32", IZUL32);
  assignValW("IZUL33", IZUL33);

  assignValW("IZUR11", IZUR11);
  assignValW("IZUR12", IZUR12);
  assignValW("IZUR13", IZUR13);
  assignValW("IZUR21", IZUR21);
  assignValW("IZUR22", IZUR22);
  assignValW("IZUR23", IZUR23);
  assignValW("IZUR31", IZUR31);
  assignValW("IZUR32", IZUR32);
  assignValW("IZUR33", IZUR33);

  assignValW("IZEL11", IZEL11);
  assignValW("IZEL12", IZEL12);
  assignValW("IZEL13", IZEL13);
  assignValW("IZEL21", IZEL21);
  assignValW("IZEL22", IZEL22);
  assignValW("IZEL23", IZEL23);
  assignValW("IZEL31", IZEL31);
  assignValW("IZEL32", IZEL32);
  assignValW("IZEL33", IZEL33);

  assignValW("IZER11", IZER11);
  assignValW("IZER12", IZER12);
  assignValW("IZER13", IZER13);
  assignValW("IZER21", IZER21);
  assignValW("IZER22", IZER22);
  assignValW("IZER23", IZER23);
  assignValW("IZER31", IZER31);
  assignValW("IZER32", IZER32);
  assignValW("IZER33", IZER33);

  assignValW("IUV11", IUV11);
  assignValW("IUV12", IUV12);
  assignValW("IUV13", IUV13);
  assignValW("IUV21", IUV21);
  assignValW("IUV22", IUV22);
  assignValW("IUV23", IUV23);
  assignValW("IUV31", IUV31);
  assignValW("IUV32", IUV32);
  assignValW("IUV33", IUV33);



  assignValW("HPP1",HPP1);
  assignValW("HGG1",HGG1);
  
  //Continue to assign to all you vars1.mdl
  
  
//---------------------------------------------------------------
//             Compute the relic density
//---------------------------------------------------------------
                 err=sortOddParticles(cdmName);

     //printf("Mass of X01 = %e",pMass("~X01"));
     qNumbers(CDM1, &spin2, &charge3, &cdim);
     printf("\nDark matter candidate is '%s' with spin=%d/2 mass=%.2E and charge %d \n",CDM1,  spin2,Mcdm1, charge3); 
     if(charge3) printf("Dark Matter has electric charge %d/3\n",charge3);
     if(cdim!=1) printf("Dark Matter is a color particle\n"); 

    int chargeDM; //DM should be a neutral particle
	if(Mcdm1 == pMass("~etaI") || Mcdm1 == pMass("~P01") || Mcdm1 == pMass("~X01")){
	chargeDM = 1;}
	else{
	chargeDM = 100;};
  
    //Compute DM relic density
	printf("\n==== Calculation of relic density =====\n");   
	double Omegah2;
 	double Beps= 1.E-4;
 	int fast=1; 
	double Xf;
    double cut=0.01;
	qNumbers(CDM1, &spin2, &charge3, &cdim);
   Omegah2=darkOmega(&Xf,fast,Beps,&err);
   //Omegah2=darkOmega2(fast,Beps,&err);
    printf("Xf = %lf       Omegah2 = %lf       \n", Xf, Omegah2 );
   if(Omegah2>0)printChannels(Xf,cut,Beps,1,stdout);





    printf("\n=== MASSES OF HIGGS AND ODD PARTICLES: ===\n");
    printHiggs(stdout);
    printMasses(stdout,1);

//------------------------------------------------------------------------------------------
//		Prepare calculation of direct detection cross-section and limit
//------------------------------------------------------------------------------------------


  double pA0[2],pA5[2],nA0[2],nA5[2];
  double Nmass=0.939; /*nucleon mass*/
  double SCcoeff;        

  double dNdE[300];
  double nEvents;

 	 //printf("\n======== Direct Detection ========\n");    

 	nEvents=nucleusRecoil(Maxwell,73,Z_Ge,J_Ge73,SxxGe73,dNdE);
	nucleonAmplitudes(CDM1, pA0,pA5,nA0,nA5);
       // printf("\nCDM[antiCDM]-nucleon micrOMEGAs amplitudes for %s \n",CDM1);
       // printf("proton:  SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",pA0[0], pA0[1],  pA5[0], pA5[1] );
       // printf("neutron: SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",nA0[0], nA0[1],  nA5[0], nA5[1] );

        SCcoeff=4/M_PI*3.8937966E8*pow(Nmass*Mcdm/(Nmass+ Mcdm),2.);
       // printf("\nCDM[antiCDM]-nucleon cross sections[pb]:\n");
       // printf(" proton  SI %.3E [%.3E] SD %.3E [%.3E]\n",
       //    SCcoeff*pA0[0]*pA0[0],SCcoeff*pA0[1]*pA0[1],3*SCcoeff*pA5[0]*pA5[0],3*SCcoeff*pA5[1]*pA5[1]);
       // printf(" neutron SI %.3E [%.3E] SD %.3E [%.3E]\n",
       // SCcoeff*nA0[0]*nA0[0],SCcoeff*nA0[1]*nA0[1],3*SCcoeff*nA5[0]*nA5[0],3*SCcoeff*nA5[1]*nA5[1]);

        double sigSIP, sigSIN, sigSDP, sigSDN;
        sigSIP = SCcoeff*pA0[0]*pA0[0]; //cross-section proton, Spin Independent
        sigSIN = SCcoeff*nA0[0]*nA0[0]; //cross-section neutron, Spin Independent
        sigSDP = 3*SCcoeff*pA5[0]*pA5[0]; //cross-section proton, Spin Dependent
        sigSDN = 3*SCcoeff*nA5[0]*nA5[0]; //cross-section neutron, Spin Dependent

       	//Conversion pb -> cm2 : 1pb = 1.0*10^-36 cm2
	double sigSIP_cm2, sigSIN_cm2, sigSDP_cm2, sigSDN_cm2; //cm2
	sigSIP_cm2 = sigSIP * 1.0*pow(10,-36);
	sigSIN_cm2 = sigSIN * 1.0*pow(10,-36);
	sigSDP_cm2 = sigSDP * 1.0*pow(10,-36);
	sigSDN_cm2 = sigSDN * 1.0*pow(10,-36);





//==========================================================
//          Print the result into the output
//==========================================================
//---------------------------------Test of NAN---------------------------------------
//---------------------------------0 no nan, -1 nan----------------------------------

	mEtaI_tree = sqrt(MEt2 + (LHE31+LHE32-LHE33)*pow(v,2)/2);
   	mEtp_tree = sqrt(2*MEt2 + (LHE31)*pow(v,2));
   	mEt0_tree = sqrt(MEt2 + (LHE31+LHE32+LHE33)*pow(v,2)/2)   ;
   	mSi_tree  = sqrt(MSi2 + (LHS)*pow(v,2)/2) ;

	FILE *SPhenoend = NULL;
	SPhenoend = fopen(filename,"a");
	fprintf(SPhenoend ," \nBlock RELIC DENSITY    #from micromegas \n");
	fprintf(SPhenoend ,"   1    %lf    #Omega_h2 \n",Omegah2);
  fprintf(SPhenoend ,"   2    %d     #Test for the charge of the DM 1=neutral, 100=not neutral \n",chargeDM);
  fprintf(SPhenoend ,"   3    %lf    #Mass of DM \n",Mcdm1);
  fprintf(SPhenoend ," \nBlock DIRECT DETECTION  #from micromegas in [cm2] \n");
	fprintf(SPhenoend ,"   1      %e   #Proton Spin Dependent \n",sigSDP_cm2);
	fprintf(SPhenoend ,"   2      %e   #Proton Spin Independent \n",sigSIP_cm2);
	fprintf(SPhenoend ,"   3      %e   #Neutron Spin Dependent \n",sigSDN_cm2);
	fprintf(SPhenoend ,"   4      %e   #Neutron Spin Independent \n",sigSIN_cm2);


	
	
	fclose(SPhenoend);  




 };  //enf if output non null

	  


  
  // End of program
  return 0;
}


//You have finished!
