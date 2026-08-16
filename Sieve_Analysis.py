import pandas as pd
import sys
import numpy as np
import scipy.interpolate as scpi
import matplotlib.pyplot as plt
print('This program can be used for sieve analysis of only 1 material at a time')
print('''Enter 1 if you want to enter a csv/excel file
Enter 2 if you want to enter values manually''')
co=int(input())
if co==1:
    print('''Ensure that the weight retained is in g. Otherwise won't work.
Also µ should be U+00B5 format, the one entered using Alt+0181 on Windows''')
    f=input('Enter filename')
    if f[-4:]=='.csv':
        df=pd.read_csv(f)
    elif f[-5:]=='.xlsx':
        df=pd.read_excel(f)
    else:
        print('Invalid file format. Only Excel or Csv file')
        sys.exit()
    if 'Sieve Size' not in list(df.columns):
        print(list(df.columns))
        m=input('Enter the name of the column containing the sieve size')
        df=df.rename(columns={m:'Sieve Size'})
    if  'Weight Retained (in g)' not in list(df.columns):
        print(list(df.columns))
        m=input('Enter the name of the column containing the Weight Retained (in g)')
        df=df.rename(columns={m:'Weight Retained (in g)'})
    if 'PAN' in df.loc[list(df.index)[-1],'Sieve Size'].upper():
        p=float(df.loc[list(df.index)[-1],'Weight Retained (in g)'])
        df=df.drop(len(df)-1)
    df['Sieve Size in µm']=[np.nan for i in range(len(df))]
    for i in list(df.index):
        if df.loc[i,'Sieve Size'][-2:]=='mm':
            df.loc[i,'Sieve Size in µm']=float(df.loc[i,'Sieve Size'][:-2])*1000
        elif df.loc[i,'Sieve Size'][-2:]=='µm':
            df.loc[i,'Sieve Size in µm']=float(df.loc[i,'Sieve Size'][:-2])
elif co==2:
    n=int(input('''Enter the number of sieves. Don't include Pan'''))
    l=[]
    print('''To enter µ, on Windows turn on num lock then press Alt and type 0181. Then leave the Alt key
For macOS long press fn and search for it in emojis section.''')
    ws=0
    for i in range(n):
        l1=[]
        s1=input(f'''Enter the sieve size for dataset {i+1} along with unit. Only in mm or µm.''')
        if s1[-2:]=='mm':
            s2=float(s1[:-2])*1000
        elif s1[-2:]=='µm':
            s2=float(s1[:-2])

        l1+=[s1,s2]
        w=float(input('Enter weight retained in g for '+str(s1)+' sieve.'))
        l1+=[w]
        ws+=w
        l+=[l1]
    p=float(input('Enter weight retained on pan (in g)'))
    df=pd.DataFrame(l,columns=['Sieve Size','Sieve Size in µm','Weight Retained (in g)'])
W1=float(input('Enter total weight of the sample in g'))
e=float(input('Enter maximum % error in weight calculation'))
W2=np.nansum(df['Weight Retained (in g)'])
W2+=p
if not W2>=W1*(1-(e/100)) and not W2<=W1*(1+(e/100)):
    print('Calculation Error. Test needs to be redone')
    sys.exit()
x=list(df['Sieve Size in µm'])
df=df.drop('Sieve Size in µm',axis=1)
df['% Weight Retained']=(df['Weight Retained (in g)']/W2)*100
df['Cumulative % Weight Retained']=[np.nan for i in range(len(df))]
for i in range(len(df)):
    df.loc[list(df.index)[i],'Cumulative % Weight Retained']=np.nansum(df.loc[list(df.index)[:i+1],'% Weight Retained'])  
df['Cumulative % Weight Passing']=100-df['Cumulative % Weight Retained']
f=input('Enter Output Filename. Exclude .xlsx')
df.to_excel(f+'.xlsx',index=False)
co=input('Do you want to find out the graph of the % finer vs Sieve Size. Enter Yes or No')
if co.upper()=='NO':
    sys.exit()
xs=sorted(x)
ys=sorted(list(df['Cumulative % Weight Passing']))
xl=np.log10(xs)
pchip=scpi.PchipInterpolator(xl,ys)
xls=np.logspace(min(xl),max(xl),1000000)
yls=pchip(np.log10(xls))
plt.semilogx(xls,yls,color='lime')
plt.scatter(xs,ys)
plt.xlabel('Sieve size in µm')
plt.ylabel('% Finer')
plt.xticks(xs)
plt.gca().xaxis.set_major_formatter(plt.ScalarFormatter())
plt.yticks(np.arange(0, 101, 10))
plt.minorticks_on()
plt.grid(True, which='major', linestyle='-', linewidth=0.8, color='gray', alpha=0.8)
plt.grid(True, which='minor', linestyle=':', linewidth=0.5, color='gray', alpha=0.5)
plt.grid(True,alpha=0.7)
plt.show()
