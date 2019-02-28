print("Welcome Newral Network");
a = eval(input("Enter the Number of Epoch's: \n"));
w1of = 0; w2of = 0; b=0; ans=0;

"""for i in range(0,a):
	xofi.append(eval(input("Enter the X[{}]".format(i))));
	#wofi.append(eval(input("Enter the W[{}]".format(i))));
"""
print("Initially all weight is 0");
print("Binary Sigmoid funtion is: 1/1+e^-x\n\n");
print("Calculation using OR gate Logic");
table = [];

def replacing(j,k,val):
	if j == 0 and k!=0:
		table.append([-1,k,val])
	elif j!=0 and k==0:
		table.append([j,-1,val])
	elif j==0 and k==0:
		table.append([-1,-1,val])
	else:
		table.append([j,k,val])


for j in range(2):
	for k in range(2):
		if j or k:
			replacing(j,k,1);
		else:
			replacing(j,k,-1)



def  calculations(index):
	global w1of 
	global w2of
	global b
	global ans
	if index>3:
		return;
	entry = table[index];
	print("\nInitially Values x1:{}, x2:{}, Y:{}, W1:{}, W2:{}, b:{}".format(entry[0],entry[1],entry[2],w1of,w2of,b))
	ans = entry[0]*w1of + entry[1]*w2of + b
	print("Target is:{} {} {}".format(entry[0],entry[1],entry[2]))
	print("Output is: ",ans)
	if(ans == entry[2]):
		print("Target Value Matched no need to change weight");
		calculations(index+1)
	else:
		print("Need to change weight")
		w1of = w1of+entry[0]*entry[2]
		w2of = w2of+entry[1]*entry[2]
		b= entry[2]
		calculations(index+1)


#print(table)

for i in range(0,a):
	calculations(0)


print("\n\nAfter {} Epochs\nWeight 1 of: {}\nWeight 2 of: {}\nBias is: {}\nYin Value: {}".format(a,w1of,w2of,b,ans))








