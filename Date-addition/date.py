def namNhuan(nam):
	if nam % 4 and not nam % 100:
		return True
	return False

def soNgay(thang, nam): 
	sn = 0
	if thang in [1, 3, 5, 7, 8, 10, 12]:
		sn = 31
	elif thang in [4, 6, 9, 11]:
		sn = 30
	elif thang == 2:
		if namNhuan(nam):
			sn = 29
		else:
			sn = 28
	return sn


d = int(input("Ngay: "))
m = int(input("Thang: "))
y = int(input("Nam: "))
print(f'Your root day: {d}/{m}/{y}')
remain = int(input("Days after root day: "))

while remain != 0:
	sn = soNgay(m, y)
	# print(f"sn: {sn}")
	if remain > sn - d:
		d = remain - sn + d 
		m += 1
		# print(f'm: {m}')
		# print(f'd: {d}')
		if m == 13:
			y += 1
			m = 1
			# print(f"y: {y}, m: {m}")
			break
		else:
			break
	else:
		d += remain
		# print(f"d: {d}")
		break
print(f"Result: {d}/{m}/{y}")
	
	


 
