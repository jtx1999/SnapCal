import datefinder

def returnLocationTime(wordlist):
    Context = wordlist
    
    buildings = "East Hill Plaza  345 Pine Tree Road Engineering Quad Statler Hotel Big Red Barn Alice Cook House AD White House Africana Center AG Quad Akwe:Kon Appel Commons Appel Tennis Courts Academic Surge A Academic Surge B Arts Quad Anabel Taylor Hall Balch Hall Baker North Baker South Baker Tower Beebe Hall Bradfield Hall Bethe House Baker Laboratory Becker House Boldt Hall Bard Hall Barnes Hall Basic Science Building Biotechnology Building Boyce Thompson Institute Bartels Hall Barton Hall Cascadilla Hall College Ave  301 Computing & Communications Ctr Cornell Golf Center Clinical Programs   Ambulatory Caldwell Hall Clark Hall Clinical Programs barn Clinical Programs   Surgery Clinical Programs   Multipurpose Biological Sciences Atrium Comstock Hall Anna Comstock House Carpenter Hall Court Residence Hall Day Hall Clara Dickson Hall Mary Donlon Hall Dufflield Hall Hurlburt House East Hill Office Building  395 Pine Tree Rd Emerson Hall Judith Eisner Pavillion Foundry Newman  Floyd D. Laboratory Flora Rose House Fernow Hall Friedman Wrestling Center Gnva Barton Laboratory Green Greenhouse Bldg G Grumman Squash Courts Goldwin Smith Hall Guterman Bioclimatic Lab Bill and Melinda Gates Hall Human Ecology Building Hollister Hall Helen Newman Hall Ho Plaza HIGH RISE #1 High Rise #5 High Voltage Laboratory ILR Conference Center ILR Research Building Ives Hall Ornithology  Cornell Lab of Johnson Museum Of Art Stewart Ave 640 Kahin Center Klarman Hall Kimball Hall Kennedy Hall Kinzelberg Hall Kroch Carl A Library William T. Keeton House Liddell Laboratory Lincoln Hall Lynah Rink Low Rise #6 Low Rise #7 Low Rise #8 Low Rise #9 Lyon Hall Mcfaddin Hall McGraw Hall Mews Residence Hall Moakley House   Golf Course Milstein Hall Malott Hall Mann Library Muenscher Laboratory Moore Laboratory Morrill Hall Morrison Hall Merrill Family Sailing Center Hughes Hall Myron Taylor Hall M Van Rensselaer Hall Noyes Lodge   Beebe Lake Noyes Community And Rec Ctr Nevin Welcome Center Olin Chemistry Research Wing Olin Hall Olin Library John T Oxley Equestrian Center Pomology Cold Storage Sales Phillips Hall Physical Sciences Building Plant Science Building Roberts Hall Rice Hall Rockefeller Hall Frank H T Rhodes Hall Rand Hall Robert Purcell Community Center Riley Robb Hall Risley  Prudence Resd. College Risley Tennis Court Reis Tennis Center Rawlings Green Sibley Hall Sage Chapel Sage Hall Schoellkopf Memorial Hall Schoellkopf Field Schoellkopf Track Snyd Hill Baker Inst Thaw Lec Snee Hall Geological Science Schurman Hall Space Science Building Stocking Hall Statler Hall Stimson Hall Savage Hall Schwartz Center Townhouse Community Center Teagle Hall Thurston Avenue 626 Thurston Hall Olive Tjaden Hall Ujamaa University Ave 726 A&S Upson Hall Uris Hall Uris Library Vet Center For Mobility Vet Education Center Vet Medical Center Vet Research Tower White Hall Weill Hall Wolpe Center Wing Hall Warren Hall Willard Straight Hall ACH  ADW  AFC  AGQ  AKW  APP  APT  ASA  ASB  ASQ  ATH  BAL  BAN  BAS  BAT  BBH  BDF  BET  BKL  BKR  BOL  BRD  BRN  BSC  BTB  BTI  BTL  BTN  CAS  CAV  CCC  CGC  CLA  CLD  CLK  CLM  CLS  CLU  CMH  CMS  COM  CRP  CRT  DAY  DCK  DON  DUF  ECO  EHO  EMR  ESN  FND  FNL  FRH  FRN  FWC  GBL  GGG  GRS  GSH  GTR  GTS  HEB  HLS  HNH  HOP  HR1  HR5  HVL  ICC  IRB  IVS  JLO  JMA  KHN  KLR  KMB  KND  KNZ  KRC  KTN  LDL  LNC  LNH  LR6  LR7  LR8  LR9  LYO  MCF  MCG  MEW  MKL  MLS  MLT  MNL  MNS  MRB  MRL  MRS  MSC  MTH  MTH  MVR  NLB  NRC  NVN  OLC  OLH  OLL  OXL  PCS  PHL  PHS  PLS  RBT  RCE  RCK  RHD  RND  RPC  RRB  RSL  RST  RTC  RWL  SBL  SGC  SGH  SHK  SKF  SKT  SNB  SNE  SRM  SSB  STK  STL  STM  SVG  SWZ  TCC  TGL  THA  THR  TJN  UJM  UNI  UPS  URH  URL  VCM  VEC  VMC  VRT  WHT  WLL  WLP  WNG  WRN  WSH "
    buildingList = buildings.split()
    location = ""
    contexts = ""

    i = -1
    j = -1
    for word in Context:
        contexts = contexts + " " + word
        index = Context.index(word)
        if (word in buildingList):
            if (i==-1):
                i = index
                j = index
            else:
                j = index
            location = location + " " + word
    dates = datefinder.find_dates(contexts)
    if (i!=-1 and j!=-1):
        if (i!=0 and Context[i-1].isdigit() and (int)(Context[i-1])>=100 and (int)(Context[i-1])<1000):
            location = location + " " + Context[i-1]
        elif (Context[j+1].isdigit() and (int)(Context[j+1])>=100 and (int)(Context[j+1])<1000):
            location = location + " " + Context[j+1]
    
    for date in dates:
        return location, date
     #   elif (("PM" in word) or ("AM" in word) or ("o'clock" in word)):
      #      if (index==1 and Context[0].isdigit()):
       #         time = Context[0]+word
        #    if (index >=2):
         #       if (word[0:-2].isdigit()):
          #          if (Context[index-1].isdigit()):
           #             time = Context[index-1]+":"+word
            #        else:
             #           time = word[:-2]+":00"+word[-2:]
              #  elif (Context[index-1].isdigit()):
               #     if (not Context[index-2].isdigit()):
                #        time = Context[index-1]+":00"+word
                 #   else:
                  #      time = Context[index-2] + ":" + Context[index-1]+word
        #elif (":" in word):
         #   valid = True
          #  time += ':'
           # if (word==':'):
            #    text = Context[index-1]
             #   for i in range(len(text)):
              #      if (text[-i-1].isdigit()):
               #         time = text[-i-1]+time

    return location, dates
