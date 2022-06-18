s=0
p=0
flag=False
str=input('enter string : ')
for ch in str:
	if ch=='+' or ch=='-' or ch=='*' or ch=='/' :
		op=ch
		flag=True
	elif 48<=ord(ch) and ord(ch)<=57:
		if flag==False:
			s=s*10+(ord(ch)-48)
		else:
			p=p*10+(ord(ch)-48)
	elif(ch=='='):
		if op=='+':
			print(s+p)
		elif op=='-':
			print(s-p)
		elif op=='*':
			print(s*p)
		elif op=='/':
			print(s/p)