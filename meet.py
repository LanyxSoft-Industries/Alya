import selenium, os, time, datetime, random, warnings, sys, argparse, tkinter
from tkinter import *
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

warnings.filterwarnings("ignore", category=DeprecationWarning) 
print("Timestamp: " + datetime.datetime.now().strftime("%D  %H:%M:%S"))

"""
Arguments
-c	--code			Specifies the class code.
-e	--email			Specifies the email to use.
-u	--usermame		Specifies the Active Directory username.
-p	--password		Specifies the Active Directory password and the regular user's password.
-fc	--force-code	Specifies weather to force using a Google Meet code.
-ua	--user-agent	Specifies a custom user agent.
-ex	--expiramental	Specify weather to use expiramental feautures.
-tk --tk-title      Specifies a custom tkinter interface title.

USER AGENTS:
Windows 10 - Firefox User Agent:
	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0

iPadOS 14.1 - Safari User Agent:
	Mozilla/5.0 (iPad; CPU OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1

"""

CUSTOM_USER_AGENT = ""
CUSTOM_TK_INTERFACE_TITLE = "Google Meets Automation"
FIREFOX_BINARY = "/usr/lib/firefox/firefox"
AUTOMATION_FAILED = False
USE_FAILSAFE_PERCAUTIONS = True
FORCE_USE_CODE = False
EXPIRAMENTAL_FEATURES = False
CLASS_CODE = ""
EMAIL_ADDRESS = ""
AD_USERNAME = ""
AD_PASSWORD = ""

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-c", "--code", type=str, help="Specifies the class code")
arg_parser.add_argument("-e", "--email", type=str, help="Specifies the email to use")
arg_parser.add_argument("-u", "--username", type=str, help="Specifies the Active Directory username")
arg_parser.add_argument("-p", "--password", type=str, help="Specifies the Active Directory password and the regular user's password")
arg_parser.add_argument("-fc", "--force-code", type=str, help="Specifies weather to force using a Google Meet code")
arg_parser.add_argument("-ua", "--user-agent", type=str, help="Specifies a custom user agent")
arg_parser.add_argument("-ex", "--expiramental", type=str, help="Specify weather to use expiramental feautures")
arg_parser.add_argument("-tk", "--tk-title", type=str, help="Specifies a custom tkinter interface title")
arguments = arg_parser.parse_args()

if arguments.code is not None:
	CLASS_CODE = arguments.code
if arguments.email is not None:
	EMAIL_ADDRESS = arguments.email
if arguments.username is not None:
	if arguments.username == "None" or arguments.username == "none" or arguments.username == "" or arguments.username == None:
		AD_USERNAME = None
	else:
		AD_USERNAME = arguments.username
if arguments.password is not None:
	AD_PASSWORD = arguments.password
if arguments.force_code is not None:
	if arguments.force_code == "true":
		FORCE_USE_CODE = True
	else:
		FORCE_USE_CODE = False
if arguments.user_agent is not None:
	CUSTOM_USER_AGENT = arguments.user_agent
if arguments.expiramental is not None:
	if arguments.expiramental == "true":
		EXPIRAMENTAL_FEATURES = True
	else:
		EXPIRAMENTAL_FEATURES = False
if arguments.tk_title is not None:
    CUSTOM_TK_INTERFACE_TITLE = arguments.tk_title


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class Tk_Interface(Tk):
	def __init__(self, name='Interface', size=None):
		super(Tk_Interface, self).__init__()
		if size:
			self.geometry(size)
		self.title(name)
		self.frame = Frame(self)
		self.frame.pack()

	def do_nothing(self, var=""):
		pass

	def gui_print(self, text='This is some text', command=None):
		self.frame.destroy()
		self.frame = Frame(self)
		self.frame.pack()
		Label(self.frame, text=text).pack()
		Button(self.frame, text='Ok', command=command).pack()

	def gui_input(self, text='Enter something', command=None):
		self.frame.destroy()
		self.frame = Frame(self)
		self.frame.pack()        
		Label(self.frame, text=text).pack()
		entry = StringVar(self)
		Entry(self.frame, textvariable=entry).pack()
		Button(self.frame, text='Ok', command=lambda: command(entry.get())).pack()

	def end(self):
		self.destroy()

	def start(self):
		mainloop()

def get_continue(value):
	if value == "y":
		print("Continuing...")
	else:
		print("Exiting...\n\n")
		sys.exit(0)
	tk_main.end()

def initiate():
	global tk_main
	tk_main.gui_input('Continue? [y/n]', get_continue)

print("Determining weather to continue.")
tk_main = Tk_Interface(CUSTOM_TK_INTERFACE_TITLE, size="350x80")
initiate()
tk_main.start()


options = Options()
options.headless = False

profile = webdriver.FirefoxProfile()
if CUSTOM_USER_AGENT == "":
	pass
else:
	profile.set_preference("general.useragent.override", CUSTOM_USER_AGENT)
binary = FirefoxBinary(FIREFOX_BINARY) # Absolute path to Firefox executable
driver = webdriver.Firefox(profile, options=options, firefox_binary=binary)
driver.maximize_window()
driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
print(f"{bcolors.OKGREEN}Successfully loaded Google Authetication point! [Gmail]{bcolors.ENDC}")

time.sleep(6)

if AUTOMATION_FAILED == False:
	for i in range(6):
		try:
			driver.find_element_by_id("identifierId").send_keys(EMAIL_ADDRESS)
			driver.find_element_by_id("identifierNext").click()
			print(f"{bcolors.OKGREEN}Sucessfully uploaded email...{bcolors.ENDC}")
			break
		except selenium.common.exceptions.NoSuchElementException:
			print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}]: Attempting to resend email address...")
			if USE_FAILSAFE_PERCAUTIONS: time.sleep(6)
			else: driver.implicitly_wait(6)
		except selenium.common.exceptions.WebDriverException as e:
			print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}]: Web driver error.\n[ERROR DETAILS]:",e)
			AUTOMATION_FAILED = True
			break

if AUTOMATION_FAILED == False:
	for i in range(6):
		try:
			driver.find_element_by_id("userNameInput").send_keys(AD_USERNAME)
			driver.find_element_by_id("passwordInput").send_keys(AD_PASSWORD)
			driver.find_element_by_id("submitButton").click()
			print(f"{bcolors.OKGREEN}Sucessfully sent Active Directory credentials...{bcolors.ENDC}")
			break
		except selenium.common.exceptions.NoSuchElementException:
			try:
				driver.find_element_by_name("password").send_keys(AD_PASSWORD)
				driver.find_element_by_id("passwordNext").click()
				print(f"{bcolors.OKGREEN}Sucessfully sent credentials...{bcolors.ENDC}")
				break
			except selenium.common.exceptions.NoSuchElementException:
				print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}]: Attempting to find password input...")
				if USE_FAILSAFE_PERCAUTIONS: time.sleep(6)
				else: driver.implicitly_wait(6)
		except selenium.common.exceptions.WebDriverException as e:
			print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}]: Web driver error.\n[ERROR DETAILS]:",e)
			AUTOMATION_FAILED = True
			break


time.sleep(6)
print("Loading Google Meets...")
driver.get("https://meet.google.com")
time.sleep(6)

if FORCE_USE_CODE == False:
	scheduled_classes = driver.find_elements_by_class_name("mobgod")
	now_container_divs = driver.find_elements_by_class_name("SjBtYb")
	print("Number of found classes in calendar:", len(scheduled_classes), "\nNumber of found 'now_container_divs' in Google Meets:", len(now_container_divs))

	if EXPIRAMENTAL_FEATURES == True:
		temp_boolean = False
		while temp_boolean == False:
			scheduled_classes = driver.find_elements_by_class_name("mobgod")
			now_container_divs = driver.find_elements_by_class_name("SjBtYb")
			if len(scheduled_classes) != 0 and len(now_container_divs) != 0 and len(scheduled_classes) == len(now_container_divs):
				for i in range(len(now_container_divs)):
					try:
						now_container_divs[i].find_element_by_class_name("Ql1xRb")
						scheduled_classes[i].click()
						temp_boolean = True
						print(f"{bcolors.OKGREEN}Sucessfully found active class.{bcolors.ENDC}")
						break
					except selenium.common.exceptions.NoSuchElementException:
						print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}]: Attempting to find active class...")
						if USE_FAILSAFE_PERCAUTIONS: time.sleep(6)
						else: driver.implicitly_wait(6)
					except selenium.common.exceptions.StaleElementReferenceException:
						print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}]: Stale element found, reloading website...")
						driver.refresh()
						if USE_FAILSAFE_PERCAUTIONS: time.sleep(6)
						else: driver.implicitly_wait(6)
	else:
		if len(scheduled_classes) != 0:
			print("Selecting first class in list.")
			scheduled_classes[0].click()

if AD_USERNAME == "" or AD_USERNAME == None or FORCE_USE_CODE == True:
	for i in range(6):
		try:
			driver.find_element_by_class_name("cmvVG").click()
			ck = ActionChains(driver);ck.send_keys(CLASS_CODE).perform()
			pe = ActionChains(driver);pe.key_down(Keys.ENTER).key_up(Keys.ENTER).perform();
			print(f"{bcolors.OKGREEN}Sucessfully uploaded meeting code.{bcolors.ENDC}")
			break
		except selenium.common.exceptions.NoSuchElementException:
			print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}]: Attempting to upload meeting code...")
			try:
				driver.find_element_by_id("i3").send_keys(CLASS_CODE)
				press_enter = ActionChains(driver)
				press_enter.key_down(Keys.ENTER).key_up(Keys.ENTER).perform();
				print(f"{bcolors.OKGREEN}Sucessfully uploaded meeting code.{bcolors.ENDC}")
				break
			except selenium.common.exceptions.NoSuchElementException:
				print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}]: Attempting to upload meeting code...")
				if USE_FAILSAFE_PERCAUTIONS: time.sleep(6)
				else: driver.implicitly_wait(6)
		except selenium.common.exceptions.ElementNotInteractableException:
			print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}]: Element 'cmVG' is out of view.")
			try:
				driver.find_element_by_id("i3").send_keys(CLASS_CODE)
				press_enter = ActionChains(driver)
				press_enter.key_down(Keys.ENTER).key_up(Keys.ENTER).perform();
				print(f"{bcolors.OKGREEN}Sucessfully uploaded meeting code.{bcolors.ENDC}")
				break
			except selenium.common.exceptions.NoSuchElementException:
				print(f"[ERROR]: Attempting to upload meeting code...")
				if USE_FAILSAFE_PERCAUTIONS: time.sleep(6)
				else: driver.implicitly_wait(6)

time.sleep(7) # Ensure that the browser fully loads the next part.

for i in range(6):
	try:
		WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Join now')]")))

		time.sleep(2)
		turn_off_mic_action = ActionChains(driver)
		turn_off_mic_action.key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL).perform();
		turn_off_camera_action = ActionChains(driver)
		turn_off_camera_action.key_down(Keys.CONTROL).send_keys("e").key_up(Keys.CONTROL).perform();
		print(f"{bcolors.OKGREEN}Sucessfully found landmark...turned off camera and microphone.{bcolors.ENDC}")
		break
	except selenium.common.exceptions.TimeoutException:
		try:
			WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Ask to join')]")))

			time.sleep(2)
			turn_off_mic_action = ActionChains(driver)
			turn_off_mic_action.key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL).perform();
			turn_off_camera_action = ActionChains(driver)
			turn_off_camera_action.key_down(Keys.CONTROL).send_keys("e").key_up(Keys.CONTROL).perform();
			print(f"{bcolors.OKGREEN}Sucessfully found landmark...turned off camera and microphone.{bcolors.ENDC}")
			break
		except selenium.common.exceptions.TimeoutException:
			print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}]: Attempting to find landmark...")
			if USE_FAILSAFE_PERCAUTIONS: time.sleep(6)
			else: driver.implicitly_wait(6)

try:
	join_button = WebDriverWait(driver, 36).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Join now')]")))
	driver.execute_script("arguments[0].click();", join_button)
except selenium.common.exceptions.TimeoutException:
	try:
		join_button = WebDriverWait(driver, 36).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Ask to join')]")))
		driver.execute_script("arguments[0].click();", join_button)
	except selenium.common.exceptions.TimeoutException:
		print(f"{bcolors.WARNING}Couldn't join Google Meet. Are you sure you have the right code?{bcolors.ENDC}")

if AD_USERNAME != "" or AD_USERNAME != None or FORCE_USE_CODE == False:
	CLASS_CODE = driver.current_url.replace("https://meet.google.com/", "")

print("\nRunning with FailSafe Percautions on: True" if USE_FAILSAFE_PERCAUTIONS == True else "\nRunning with FailSafe Percautions on: False")
print("\nRunning with Expiramental Features on: True" if EXPIRAMENTAL_FEATURES == True else "\nRunning with Expiramental Features on: False")
print("FORCE Using code: True" if FORCE_USE_CODE == True else "FORCE Using code: False")
print("Signed into Google Auth point using Email:", EMAIL_ADDRESS, "| Username:", AD_USERNAME, "| Password:", AD_PASSWORD)
print("Joined with code:", CLASS_CODE)
print("\n")