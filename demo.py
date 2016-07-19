#encoding=utf-8*

# Form implementation generated from reading ui file 'py.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys,time, os
from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Telnet():
	'''设置路由器IP地址信息模块'''
	def setIp(self,tn=None,ip_info=None):
		'''
		# newhost = input("Please input the new IP address:")
		tn.write('uci set network.wan.ipaddr=%s'%newhost+'\r\n')
		time.sleep(0.5)
		tn.write('uci commit\r\n')
		time.sleep(0.5)
		tn.write('/etc/init.d/network restart\r\n')
		time.sleep(0.5)
		tn.write('ifconfig'+'\r\n')
		time.sleep(0.5)
		temp = tn.read_very_eager()
		print temp
		del tn
		return temp
		'''
		newhost=ip_info.newhost
		mask=ip_info.mask
		# print 'uci set network.lan.ipaddr=%s'%newhost
		# snmp 模拟器对应命令
		# newhost='192.168.7.3'
		# mask='255.255.255.0'
		tn.write('system-view'+'\r\n')
		tn.write('interface GigabitEthernet0/4'+'\r\n')
		tn.write('ip address %s %s\r\n'%(newhost,mask))
		tn.write('quit'+'\r\n')
		tn.write('quit'+'\r\n')
		tn.write('screen-length disable'+'\r\n')
		tn.write('display current-configuration'+'\r\n')
		time.sleep(0.5)
		temp=tn.read_until('#\r\nreturn')
		# temp = tn.read_very_eager()
		print temp
		tn.close()
		del tn
		return temp

	def telnetprocess(self,router_info=None,ip_info=None):
		import telnetlib,sys,time,os
		HOST=router_info.host
		USER=router_info.user
		PASS=router_info.password
		if not HOST:
			try:
				HOST = sys.argv[1]
				USER = sys.argv[2]
				PASS = sys.argv[3]
			except:
				print "This program needs host,username and password"
				HOST = input("Please input the HOST:")
				USER = input("Please input the Username:")
				PASS = input("Please input the Password:")
		#tn = telnetlib.Telnet()
		# print newhost
		try:
			tn = telnetlib.Telnet(HOST)
		except:
			print "Cannot open host"
			return
		#print("正在连接，请稍等...")
		print("The program is trying to connect,please wait for a momment")
		time.sleep(0.5)
			
			# newhost = input("Please input the new host address:")
			# tn.write('ip address '%newhost+'\n')
			# tn.write('ifconfig'+'\n')
			# tn.close()
			# del tn
			# return temp
		index=tn.expect(['.*Username:.*','.*Password:.*'],timeout=3)
		path1='Failed_info.txt'
		path1=path1.decode('utf8')

		try:
			if index[0] == 0:
				# print -2
				tn.write(USER+'\r\n')
				time.sleep(0.5)
				if PASS:
					# data=''
					# while data.find('Password:') == -1:
					#   data = tn.read_very_eager()
					# print PASS
					tn.read_until('Password:')
					tn.write(PASS+'\r\n')
				print 'The program is checking whether login succeeds,please wait for a momment'
				response=tn.expect(['.*>.*','% Login failed.*'])
				if response[0]==1:
					print 'the password is wrong!'
					file=open(path1,'a')
					tempstr=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'\n'
					file.write(tempstr)
					tempstr=HOST+' 用户名和密码不匹配'
					file.write(tempstr)
					file.close()
					return
				else:#成功登录后，设置路由器信息
					print 'Login successfully!'
					return self.setIp(tn,ip_info)
			elif index[0] == 1:
				tn.write(PASS+'\n')
				print 'The program is checking whether login succeeds,please wait for a momment'
				time.sleep(0.5)
				response=tn.expect(['.*Password:.*'])
				if response[0]==0:
					file = open(path1,'a')
					tempstr=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'\n'
					file.write(tempstr)
					tempstr=HOST+' 密码出错'+'\n'
					file.write(tempstr)
					file.close()
					return
				else:
					return self.setIp(tn,ip_info)
		except (-1,None,'\r\n'):
			print 'Timeout happened'
			file = open(path1,'a')
			tempstr=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'\n'
			file.write(tempstr)
			tempstr=HOST+' 连接超时'+'\n'
			file.close()
			return

class Ip_info():
	def __init__(self,newhost,mask):
		self.newhost=newhost
		self.mask=mask

class Router_info():
	def __init__(self,host,user,password):
		self.host=host
		self.user=user
		self.password=password

class Ui_Dialog(QtGui.QWidget):
	def __init__(self, parent):
		QtGui.QWidget.__init__(self)
		parent.setObjectName(_fromUtf8("Dialog"))
		parent.resize(483, 368)

		# hbox_1=QtGui.QHBoxLayout()
		# grid=QtGui.QGridLayout()
		# grid.setSpacing(10)

		# self.label = QtGui.QLabel(parent)
		# # self.label.setFixedSize(81,20)
		# self.label.setGeometry(QtCore.QRect(40, 50, 81, 20))
		# self.label.setObjectName(_fromUtf8("label"))

		# self.hostEdit = QtGui.QLineEdit(parent)
		# # self.hostEdit.setFixedSize(130,20)
		# self.hostEdit.setGeometry(QtCore.QRect(130, 50, 150, 20))
		# self.hostEdit.setObjectName(_fromUtf8("hostEdit"))

		# self.pushButton = QtGui.QPushButton(parent)
		# # self.pushButton.setFixedSize(75,20)
		# self.pushButton.setGeometry(QtCore.QRect(300, 50, 75, 20))
		# self.pushButton.setObjectName(_fromUtf8("pushButton"))
		# self.setFocus()

		self.pushButton = QtGui.QPushButton(parent)
		self.pushButton.setGeometry(QtCore.QRect(180, 140, 71, 20))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.setFocus()
		self.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.on_pushButton_clicked)

		self.hostEdit = QtGui.QLineEdit(parent)
		self.hostEdit.setGeometry(QtCore.QRect(220, 50, 161, 20))
		self.hostEdit.setObjectName(_fromUtf8("hostEdit"))

		self.label = QtGui.QLabel(parent)
		self.label.setGeometry(QtCore.QRect(90, 50, 81, 20))
		self.label.setObjectName(_fromUtf8("label"))

		self.label_2 = QtGui.QLabel(parent)
		self.label_2.setGeometry(QtCore.QRect(90, 90, 81, 20))
		self.label_2.setObjectName(_fromUtf8("label_2"))

		self.maskEdit = QtGui.QLineEdit(parent)
		self.maskEdit.setGeometry(QtCore.QRect(220, 90, 161, 20))
		self.maskEdit.setObjectName(_fromUtf8("maskEdit"))
		# hbox_1.addWidget(self.label)
		# hbox_1.addWidget(self.hostEdit)
		# hbox_1.addWidget(self.pushButton)
		# grid.addLayout(hbox_1,0,0)
		# grid.addWidget(self.label,0,0,1,1,Qt.AlignCenter)
		# grid.addWidget(self.hostEdit,0,1,1,2,Qt.AlignCenter)
		# grid.addWidget(self.pushButton,0,2,1,1,Qt.AlignCenter)

		# vbox_1=QtGui.QVBoxLayout()
		# vbox_1.addLayout(hbox_1)
		# vbox_1.addStretch(1)
		# parent.setLayout(vbox_1)
		parent.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
		parent.setFixedSize(parent.width(), parent.height());

		self.retranslateUi(parent)
		QtCore.QMetaObject.connectSlotsByName(parent)

		self.telnet_obj=Telnet()
	def retranslateUi(self, parent):
		parent.setWindowTitle(_translate("Dialog", "Dialog", None))
		self.pushButton.setText(_translate("Dialog", "Connect", None))
		self.label.setText(_translate("Dialog", "New Host IP:", None))
		self.label_2.setText(_translate("Dialog", "NetWork Mask:", None))

	def on_pushButton_clicked(self):
		newhost=self.hostEdit.text()
		mask=self.maskEdit.text()
		file = open("result.txt","w")
		HOST='192.168.6.10'
		USER='admin'
		PASS='metarnetbupt'
		ip_info=Ip_info(str(newhost).strip(),str(mask).strip())
		router_info=Router_info(HOST,USER,PASS)
		print ip_info.newhost,ip_info.mask
		content=self.telnet_obj.telnetprocess(router_info,ip_info)
		if content!=None:
			#print '设备成功设置IP地址信息'
			print 'You set the information of equipment successfully!'
			file.write(content)
		else:
			print 'Your operation fails!'
			#print '设置IP地址失败！'
		file.close()

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	form=QtGui.QWidget()
	ui=Ui_Dialog(form)
	# ui.setupUi(form)
	form.show()
	sys.exit(app.exec_())