t = input('請問您的身高(cm)？')
t = float(t)
h = input('請問您的體重(kg)？')
h = float(h)
t = t / 100
bmi = h / t / t
print('BMI =', bmi)
if bmi < 18.5:
	print('體重太輕')
elif bmi >= 18.5 and bmi < 24:
	print('體重標準') 
elif bmi >= 24 and bmi < 27:
	print('體重過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
elif bmi >= 35:
	print('重度肥胖')