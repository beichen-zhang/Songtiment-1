import csv
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import sentiwordnet as swn
count=1
c = csv.writer(open("final output_.csv", "wb"))
c.writerow(["Singer ID","Singer name","Singer score","Song name","lyrics","Song score"])
name_list=["Adele.txt","Ariana Grande.txt","Beyonce.txt","Bruno Mars.txt","Coldplay.txt","Drake.txt","Ed Sheeran.txt","Eminem.txt","Jay-Z.txt","Justin Bieber.txt","Justin Timberlake.txt","Katy Perry.txt","Lady Gaga.txt","Maroon 5.txt","Metallica.txt","Rihanna.txt","Selena Gomez.txt","Shawn Mendes.txt","Taylor Swift.txt","The Chainsmokers.txt"]
sum_list=[3.9909232773082657, 6.2255414926903425, 6.930403545915004, 5.776500265324192, 2.9767297572994567, 1.4195666654102903, 8.510408275516571, -5.276493500817448, -0.6028820854405443, 8.91570269208651, 6.992024979179761, 5.352698174660363, 7.5789014302545885, 2.9686123718944883, -4.942795151234057, 5.233881159785481, 10.245948094203852, 4.657076372496296, 6.139916016691898, 7.417627824024926]
print(len(sum_list))
for fil in name_list:
	F=open(fil,"r")
	sum=0
	length_=0
#c.writerow(["Singer ID","singer name","singer score","song name","lyrics","song score"])
	for line in F:
		sent=line.split(".")
		name="."
		result=0
		song_length=0
		sentence=[]
        	for sentence_ in sent:
        		if name==".":
                		name=sentence_
            		else:
				song_length+=1
                		sentence.append(sentence_)
        	sid= SentimentIntensityAnalyzer()
        	for sen in sentence:
            		ss=sid.polarity_scores(sen)
                	for k in sorted(ss):
                    		if k=="compound":
                        		result+=ss[k]


	#sum+=result
	#print("sum: {}".format(sum))
	#print(count)
		result=float(result)/float(song_length)
		result*=100
		lyrics=line[len(name)+1:len(name)+101]
		c.writerow([count,fil[:-4],sum_list[count-1],name,"{}...".format(lyrics),result])
		result=0
		name='.'
	print(fil[:-4])
	count+=1
F.close()
