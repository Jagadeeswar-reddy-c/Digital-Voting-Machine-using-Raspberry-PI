import pandas as pd
import os

file = "insert.csv"
loc = os.getcwd()

if os.path.exists(file)==True:
    os.remove(file)

    

df = {'Adhar':[],'Photo':[]}
tp = os.getcwd()
lt = os.listdir(tp+"/Images")
# n1 = int(input())
for i in range(len(lt)):
	#adhr = input()
	#for j in range(len(lt)):
	ele = lt[i]
	print(ele)
	p = df['Adhar']
	p.append(ele[0])
	df['Adhar'] = p
	p = df['Photo']
	p.append(lt[i])
	df['Photo'] = p
	#break
		#if adhr in lt[i]:
	#		p = df['Adhar']
	#		p.append(adhr)
	#		df['Adhar'] = p
	#		p.append(lt[i])
	#		df['Photo'] = p

print(df)
df = pd.DataFrame(df)
df.to_csv("insert.csv",index = False)
