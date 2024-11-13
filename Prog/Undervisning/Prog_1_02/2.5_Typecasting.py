# Øvelse 5, Typecasting, gnmsnt-temp på amager
temp=["21.2","20.5","21.6","22.1","21.5"]
x=0
for i in temp:
    i=float(i)
    x+=i
temp_avg=round(x/len(temp),2)
print(f"Gennemsnitstemperaturen på Amager er {temp_avg}")