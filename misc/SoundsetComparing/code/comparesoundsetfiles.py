import pandas as pd
import matplotlib.pyplot as plt


csound2DA = pd.read_csv("csound2DA.csv",sep="\s+", header=None)

# Fisrt five elements
csound2DA.head()

# Number of elements
len(csound2DA)

# Number of unique values in first column
len(csound2DA[0].unique())

# Number of unique values in second column
len(csound2DA[1].unique())

# All unique values in second column
csound2DA[1].unique()

"""## sndslotIDS"""

sndslotIDS = pd.read_csv("sndslotIDS.csv",sep="\s+", header=None)

# Fisrt five elements
sndslotIDS.head()

# Number of elements
len(sndslotIDS)

# Number of unique values in second column
len(sndslotIDS[1].unique())

# Number of unique values in first column
len(sndslotIDS[0].unique())

# All unique values in second column
sndslotIDS[0].unique()

"""# Filter file content by equal numbers and write it into a file"""

sndslotIDS[1][73]

# Compare both lists with their first column and write the result into a list
L = []
U = []
flag = True
c = 0
for x in sndslotIDS[0]:
  for y in csound2DA[0]:
    if(x == y):
      L.append((sndslotIDS[1][c],csound2DA[1][x]))
      flag = False

  if(flag):
    U.append(sndslotIDS[1][c])
    print(x)
    print(sndslotIDS[1][c])
  c = c+1
  flag = True

# Write list into a dataframe
df = pd.DataFrame(data=L)

# First five rows
df.head()

# Number of elements in df
len(df)

# Write list into a dataframe
df_notUsed = pd.DataFrame(data=U)

df_notUsed.head()

len(df_notUsed)

# Write df into a file
#df.to_csv("SoundsetFilteredBGEE.csv",sep="\t", header=False)
#df_notUsed.to_csv("SoundsetNotUsedBGEE.csv",sep="\t", header=False)
#df.to_csv("SoundsetFilteredBGEEII.csv",sep="\t", header=False)
#df_notUsed.to_csv("SoundsetNotUsedBGEEII.csv",sep="\t", header=False)
df.to_csv("SoundsetFilteredIWDEE.csv",sep="\t", header=False)
df_notUsed.to_csv("SoundsetNotUsedIWDEE.csv",sep="\t", header=False)

"""# Join all three soundset prefix"""

# Load all files
BGEE = pd.read_csv("SoundsetFilteredBGEE.csv",sep="\s+", header=None)
BGEE2 = pd.read_csv("SoundsetFilteredBGEEII.csv",sep="\s+", header=None)
IWDEE = pd.read_csv("SoundsetFilteredIWDEE.csv",sep="\s+", header=None)

all_joins = BGEE.join(BGEE2,lsuffix='_BGEE', rsuffix='_BGEE2',how="outer")

all_joins

all_joins = all_joins.join(IWDEE, how="outer")

all_joins

# Write df into a file
all_joins.to_csv("allSoundsets.csv",sep="\t", header=True)

"""## Join all three not used soundset elements"""

NuBGEE = pd.read_csv("SoundsetNotUsedBGEE.csv",sep="\s+", header=None)
NuBGEE2 = pd.read_csv("SoundsetNotUsedBGEEII.csv",sep="\s+", header=None)
NuIWDEE = pd.read_csv("SoundsetNotUsedIWDEE.csv",sep="\s+", header=None)

all_joins = NuBGEE.join(NuBGEE2,lsuffix='_BGEE', rsuffix='_BGEE2',how="outer")

all_joins = all_joins.join(NuIWDEE, how="outer")

all_joins

# Write df into a file
all_joins.to_csv("allNotUsedSoundsets.csv",sep="\t", header=True)

"""# Compare"""

# Load all files
BGEE = pd.read_csv("SoundsetFilteredBGEE.csv",sep="\s+", header=None)
BGEE2 = pd.read_csv("SoundsetFilteredBGEEII.csv",sep="\s+", header=None)
IWDEE = pd.read_csv("SoundsetFilteredIWDEE.csv",sep="\s+", header=None)

# Check length of all dataframes
len(BGEE),len(BGEE2),len(IWDEE)

"""## BGEE vs BGEE2"""

BGEE.compare(BGEE2)

"""## BGEE vs IWDEE"""

IWDEE.head()

# Compare both lists
L = []
M = []
c = 0
for x in IWDEE[1]:
  #print("X: ",x)
  for y in BGEE[1]:
    if(x == y):
      L.append(BGEE.iloc[BGEE.index[BGEE[1]==y].tolist()[0]])
      M.append(IWDEE.iloc[IWDEE.index[IWDEE[1]==x].tolist()[0]])

      #print("BGEE:", L[c])
      #print(BGEE.iloc[BGEE.index[BGEE[1]==x].tolist()[0]])
      #print("Y: ", y, " ",c)
      #c = c+1

len(L),len(M)

BGEE_compared = pd.DataFrame(data=L)
IWDEE_compared =pd.DataFrame(data=M)

len(BGEE_compared),len(IWDEE_compared)

BGEE_compared.head()

IWDEE_compared.head()

BGEEvsIWDEE = BGEE_compared.join(IWDEE_compared,lsuffix='_BGEE', rsuffix='_IWDEE', how="outer")

BGEEvsIWDEE

BGEEvsIWDEE.index[BGEEvsIWDEE["1_IWDEE"]=="SELECT_RARE1"].tolist()

# Write df into a file
BGEEvsIWDEE.to_csv("BGEEcomparedIWDEE.csv",sep="\t", header=True)

len(BGEEvsIWDEE)

"""## BGEE2 vs IWDEE"""

IWDEE.head()

# Compare both lists
L = []
M = []
c = 0
for x in IWDEE[1]:
  for y in BGEE2[1]:
    if(x == y):
      L.append(BGEE2.iloc[BGEE2.index[BGEE2[1]==x].tolist()[0]])
      M.append(IWDEE.iloc[IWDEE.index[IWDEE[1]==x].tolist()[0]])
      #print(IWDEE.iloc[c])
      #print(BGEE2.iloc[BGEE2.index[BGEE2[1]==x].tolist()[0]])
      #c = c+1

len(L),len(M)

BGEE2_compared = pd.DataFrame(data=L)
IWDEE_compared =pd.DataFrame(data=M)

IWDEE_compared.head()

BGEE2vsIWDEE = BGEE2_compared.join(IWDEE_compared,lsuffix='_BGEE2', rsuffix='_IWDEE', how="outer")

BGEE2vsIWDEE.index[BGEE2vsIWDEE["1_IWDEE"]=="SELECT_RARE1"].tolist()

# Write df into a file
BGEE2vsIWDEE.to_csv("BGEE2comparedIWDEE.csv",sep="\t", header=True)

len(BGEE2vsIWDEE)

"""## Join all compared three"""

all_compared_joins = BGEE_compared.join(BGEE2_compared,lsuffix='_BGEE', rsuffix='_BGEE2', how="outer")

all_compared_joins = all_compared_joins.join(IWDEE_compared, how="outer")

# Write df into a file
all_compared_joins.to_csv("allCompared.csv",sep="\t", header=True)