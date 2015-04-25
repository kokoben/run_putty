import pyautogui
pyautogui.PAUSE = 0.5

screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(0, screenHeight)
pyautogui.click()
pyautogui.typewrite('putty')

while pyautogui.locateOnScreen('puttyIcon.png') == None:
	print("haven't found putty icon yet")

x, y = pyautogui.locateCenterOnScreen('puttyIcon.png')
pyautogui.click(x, y)
pyautogui.press(['tab', 'tab', 'tab', 'tab', 'down', 'down', 'enter'])

while pyautogui.locateOnScreen('loginAs.png') == None:
	print("Haven't found login field yet")

pyautogui.typewrite('blee')
pyautogui.press('enter')

while pyautogui.locateOnScreen('enterPassword.png') == None:
	print("Haven't found enter password field yet")

pyautogui.typewrite('133hammersmith133')
pyautogui.press('enter')
