password = "a123456"   # 初始密碼
time = 3  # 次數

while True :
	your_pass = input ('請輸入密碼：  ')

	if your_pass == password  :
		print ('登入成功')
		break

	else :
		time  = time - 1
		print ('密碼錯誤！還有', time , '次機會')
		if time == 0 :
			print ('登入失敗')
			break

    

