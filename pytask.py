# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
import sys,os
import win32api
import win32con
from PyQt5.QtWidgets import QApplication , QMainWindow,QMessageBox
from PyQt5.QtCore import  QDateTime,QStringListModel
from PyQt5.QtGui import QIcon
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from PyQt5.QtWidgets import QSystemTrayIcon
import logging

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 548)
        MainWindow.setMinimumSize(QtCore.QSize(546, 548))
        MainWindow.setMaximumSize(QtCore.QSize(546, 548))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_2.setObjectName("label_2")
        self.taskpath = QtWidgets.QLineEdit(self.centralwidget)
        self.taskpath.setGeometry(QtCore.QRect(80, 20, 341, 21))
        self.taskpath.setObjectName("taskpath")
        self.taskopenfile = QtWidgets.QPushButton(self.centralwidget)
        self.taskopenfile.setGeometry(QtCore.QRect(440, 20, 75, 23))
        self.taskopenfile.setObjectName("taskopenfile")
        self.taskadd = QtWidgets.QPushButton(self.centralwidget)
        self.taskadd.setGeometry(QtCore.QRect(420, 130, 75, 23))
        self.taskadd.setObjectName("taskadd")
        self.taskname = QtWidgets.QLineEdit(self.centralwidget)
        self.taskname.setGeometry(QtCore.QRect(80, 60, 113, 20))
        self.taskname.setObjectName("taskname")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 60, 61, 16))
        self.label_3.setObjectName("label_3")
        self.tasktype = QtWidgets.QComboBox(self.centralwidget)
        self.tasktype.setGeometry(QtCore.QRect(270, 60, 71, 22))
        self.tasktype.setObjectName("tasktype")
        self.tasktype.addItem("")
        self.tasktype.addItem("")
        self.tasktype.addItem("")
        self.tasktype.addItem("")
        self.tasktype.addItem("")
        self.tasktype.addItem("")
        self.tasktype.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 62, 54, 20))
        self.label_4.setObjectName("label_4")
        self.taskrate = QtWidgets.QLineEdit(self.centralwidget)
        self.taskrate.setGeometry(QtCore.QRect(400, 60, 113, 20))
        self.taskrate.setObjectName("taskrate")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 100, 61, 16))
        self.label_6.setObjectName("label_6")
        self.taskstartime = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.taskstartime.setGeometry(QtCore.QRect(80, 100, 181, 22))
        self.taskstartime.setObjectName("taskstartime")
        self.taskendtime = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.taskendtime.setGeometry(QtCore.QRect(330, 100, 181, 22))
        self.taskendtime.setDateTime(QtCore.QDateTime(QtCore.QDate(2099, 1, 1), QtCore.QTime(0, 0, 0)))
        self.taskendtime.setObjectName("taskendtime")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 130, 71, 21))
        self.label_7.setObjectName("label_7")
        self.taskboot = QtWidgets.QPushButton(self.centralwidget)
        self.taskboot.setGeometry(QtCore.QRect(400, 450, 91, 31))
        self.taskboot.setObjectName("taskboot")
        self.tasklist = QtWidgets.QListView(self.centralwidget)
        self.tasklist.setGeometry(QtCore.QRect(20, 161, 481, 231))
        self.tasklist.setObjectName("tasklist")
        self.tasklist.setAutoScroll(True)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 420, 54, 12))
        self.label_8.setObjectName("label_8")
        self.taskdeletename = QtWidgets.QLineEdit(self.centralwidget)
        self.taskdeletename.setGeometry(QtCore.QRect(80, 415, 131, 21))
        self.taskdeletename.setObjectName("taskdeletename")
        self.taskdelete = QtWidgets.QPushButton(self.centralwidget)
        self.taskdelete.setGeometry(QtCore.QRect(320, 410, 75, 31))
        self.taskdelete.setObjectName("taskdelete")
        self.taskdeleteall = QtWidgets.QPushButton(self.centralwidget)
        self.taskdeleteall.setGeometry(QtCore.QRect(410, 410, 81, 31))
        self.taskdeleteall.setObjectName("taskdeleteall")
        self.taskstartnow = QtWidgets.QPushButton(self.centralwidget)
        self.taskstartnow.setGeometry(QtCore.QRect(230, 410, 75, 31))
        self.taskstartnow.setObjectName("taskstartnow")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 460, 54, 12))
        self.label_9.setObjectName("label_9")
        self.taskprocessnum = QtWidgets.QLineEdit(self.centralwidget)
        self.taskprocessnum.setGeometry(QtCore.QRect(70, 450, 113, 21))
        self.taskprocessnum.setObjectName("taskprocessnum")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(220, 460, 54, 12))
        self.label_10.setObjectName("label_10")
        self.taskthreadnum = QtWidgets.QLineEdit(self.centralwidget)
        self.taskthreadnum.setGeometry(QtCore.QRect(270, 450, 113, 21))
        self.taskthreadnum.setObjectName("taskthreadnum")
        self.taskstar = QtWidgets.QPushButton(self.centralwidget)
        self.taskstar.setGeometry(QtCore.QRect(364, 490, 121, 31))
        self.taskstar.setObjectName("taskstar")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(230, 490, 101, 31))
        self.stop.setObjectName("stop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStatusTip("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.taskstartime.setMinimumDateTime(QDateTime.currentDateTime())
        self.taskendtime.setMinimumDateTime(QDateTime.currentDateTime())
        self.taskstartime.setCalendarPopup(True)
        self.taskendtime.setCalendarPopup(True)

        self.retranslateUi(MainWindow)
        self.taskopenfile.clicked.connect(MainWindow.onopenfile)
        self.taskstartnow.clicked.connect(MainWindow.onstartnow)
        self.taskdelete.clicked.connect(MainWindow.ondeletetask)
        self.taskdeleteall.clicked.connect(MainWindow.ondeleteall)
        self.taskboot.clicked.connect(MainWindow.onstartboot)
        self.stop.clicked.connect(MainWindow.onstop)
        self.taskstar.clicked.connect(MainWindow.onstart)
        self.taskadd.clicked.connect(MainWindow.onadd)
        self.tasklist.clicked['QModelIndex'].connect(MainWindow.onselecttask)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "定时任务"))
        self.label.setText(_translate("MainWindow", "输入任务："))
        self.label_2.setText(_translate("MainWindow", "任务名称："))
        self.taskpath.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">手动输入任务或从打开文件中选择</span></p></body></html>"))
        self.taskpath.setPlaceholderText(_translate("MainWindow", "D:\\text.exe"))
        self.taskopenfile.setText(_translate("MainWindow", "打开文件"))
        self.taskadd.setText(_translate("MainWindow", "添加任务"))
        self.taskname.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">任务名称不可重复</span></p></body></html>"))
        self.taskname.setPlaceholderText(_translate("MainWindow", "task_test"))
        self.label_3.setText(_translate("MainWindow", "计划类型："))
        self.tasktype.setCurrentText(_translate("MainWindow", "运行一次"))
        self.tasktype.setItemText(0, _translate("MainWindow", "运行一次"))
        self.tasktype.setItemText(1, _translate("MainWindow", "秒(1-59)"))
        self.tasktype.setItemText(2, _translate("MainWindow", "分(1-59)"))
        self.tasktype.setItemText(3, _translate("MainWindow", "时(1-23)"))
        self.tasktype.setItemText(4, _translate("MainWindow", "天(1-31)"))
        self.tasktype.setItemText(5, _translate("MainWindow", "周(1-53)"))
        self.tasktype.setItemText(6, _translate("MainWindow", "月(1-12)"))
        self.label_4.setText(_translate("MainWindow", "频率："))
        self.taskrate.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">频率必须为数字。运行一次的频率不需要填写，只需要填写开始日期</span></p></body></html>"))
        self.taskrate.setPlaceholderText(_translate("MainWindow", "10"))
        self.label_5.setText(_translate("MainWindow", "开始日期："))
        self.label_6.setText(_translate("MainWindow", "结束日期："))
        self.taskstartime.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.taskendtime.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.label_7.setText(_translate("MainWindow", "当前任务："))
        self.taskboot.setText(_translate("MainWindow", "加入开机启动"))
        self.label_8.setText(_translate("MainWindow", "任务名称："))
        self.taskdelete.setText(_translate("MainWindow", "删除任务"))
        self.taskdeleteall.setText(_translate("MainWindow", "清空任务"))
        self.taskstartnow.setText(_translate("MainWindow", "立即执行"))
        self.label_9.setText(_translate("MainWindow", "进程数："))
        self.taskprocessnum.setPlaceholderText(_translate("MainWindow", "2"))
        self.label_10.setText(_translate("MainWindow", "线程数："))
        self.taskthreadnum.setPlaceholderText(_translate("MainWindow", "8"))
        self.taskstar.setText(_translate("MainWindow", "启动"))
        self.stop.setText(_translate("MainWindow", "停止"))

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.ttype=0
        self.qList = []
        self.namelist=[]
        self.taskprocessnum.setText("2")
        self.taskthreadnum.setText("8")
        self.loadfile()
        self.scheduler = BackgroundScheduler()
        self.tuopan = QSystemTrayIcon(self)
        self.icon1 = QIcon('test.png')
        self.tuopan.setIcon(self.icon1)
        #self.tuopan.messageClicked.connect(self.message)
        self.tuopan.activated.connect(self.mainwindowshow)
        if self.iskjqd():
            self.taskboot.setText("取消开机启动")
        else:
            self.taskboot.setText("开机启动")
        logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                            filename='taskhistory.log',
                            filemode='a',
                            format= '%(asctime)s : %(message)s')
        self.workdir=os.path.abspath('.')

    def mainwindowshow(self):
      try:
        self.tuopan.hide()
        self.showNormal()
        self.activateWindow()
      except Exception as e:
          logging.info(e)
    def changeEvent(self, e):
        if e.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                self.tuopan.show()
                self.hide()
            else:
                QMainWindow.changeEvent(self, e)
    def loadfile(self):
      try:
        self.qList = []
        self.namelist=[]
        slm = QStringListModel();  # 创建mode
        with open("tasklist.txt") as f:
            lines=f.readlines()
            for x in lines:
                 self.qList.append(x.strip("\n"))
                 self.namelist.append(x.split(";")[1])
        slm.setStringList(self.qList)  # 将数据设置到model
        self.tasklist.setModel(slm)  ##绑定 listView 和 model
      except Exception as e:
          logging.info(e)
    def onopenfile(self):
        file,_=QtWidgets.QFileDialog.getOpenFileName(self,
                    "打开","C:/","ALL Files (*);;Text Files (*.exe)")
        self.taskpath.setText(file)
    def onstartnow(self):
      try:
        if self.taskdeletename.text().strip()=="":
            QMessageBox.about(self,"执行任务？","请先选择要执行的任务！")
            return
        taskname=self.taskdeletename.text().strip()+";"
        taskpath=""
        for l in self.qList:
            if taskname in l:
                taskpath=l.split(";")[2].strip()
        if taskpath:
            self.startexe(taskpath)
      except Exception as e:
          logging.info(e)
    def startexe(self,py):
      try:
        dt=datetime.datetime.now()
        dir = os.path.dirname(py)
        os.chdir(dir)
        base = os.path.basename(py)
        re=os.system('start {}'.format(base))
        if re==0:
            res="成功"
        else:
            res="失败"
        self.tuopan.showMessage("运行结果", "{}的任务{}运行结果为{}"
                                .format(dt,py,res), icon=3)
        logging.info("{}运行结果为{}".format(py,res))
        self.statusbar.showMessage("{}的任务{}运行结果为{}".format(dt,py,res))
        os.chdir(self.workdir)
      except Exception as e:
          logging.info(e)
    def ondeletetask(self):
      try:
        if self.taskdeletename.text().strip()=="":
            QMessageBox.about(self,"删除任务？","请先选择要删除的任务！")
            return
        re=QMessageBox.information(self, '确认删除？',
                                   '删除任务{}'.format(self.taskdeletename.text()),
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if re==QMessageBox.Yes:
            self.deletefileline(self.taskdeletename.text().strip())
            self.loadfile()
            self.taskdeletename.setText('')
            self.statusbar.showMessage('删除任务{}成功'.format(self.taskdeletename.text()))
      except Exception as e:
          logging.info(e)
    def ondeleteall(self):
      try:
        re = QMessageBox.information(self, '确认删除？',
                                     '确认删除所有任务？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if re==QMessageBox.Yes:
            with open('tasklist.txt', "r+") as f:
                f.truncate()
            self.loadfile()
            self.statusbar.showMessage("所有任务都已删除")
      except Exception as e:
          logging.info(e)
    def kjqd(self):
        zdynames = os.path.basename(__file__)  # 当前文件名的名称如：newsxiao.py
        name = os.path.splitext(zdynames)[0]  # 获得文件名的前部分,如：newsxiao
        path = os.path.abspath(os.path.dirname(__file__)) + '\\' + "runpytask.vbs"  # 要添加的exe完整路径如：
        # 注册表项名
        KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        # 异常处理
        try:
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
            win32api.RegSetValueEx(key, "runpytask", 0, win32con.REG_SZ, path)
            win32api.RegCloseKey(key)
            self.statusbar.showMessage('开机启动添加成功！')
            self.taskboot.setText("取消开机启动")
        except:
            self.statusbar.showMessage('开机启动添加失败')
    def qxqd(self):
        zdynames = os.path.basename(__file__)  # 当前文件名的名称如：newsxiao.py
        name = os.path.splitext(zdynames)[0]  # 获得文件名的前部分,如：newsxiao
        path = os.path.abspath(os.path.dirname(__file__)) + '\\' + "runpytask.vbs"  # 要添加的exe完整路径如：
        # 注册表项名
        KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        # 异常处理
        try:
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
            win32api.RegDeleteValue(key, "runpytask")
            win32api.RegCloseKey(key)
            self.statusbar.showMessage('开机启动删除成功')
            self.taskboot.setText("开机启动")
        except:
            self.statusbar.showMessage('开机启动删除失败')
    def iskjqd(self):
        zdynames = os.path.basename(__file__)  # 当前文件名的名称如：newsxiao.py
        name = os.path.splitext(zdynames)[0]  # 获得文件名的前部分,如：newsxiao
        path = os.path.abspath(os.path.dirname(__file__)) + '\\' + "runpytask.vbs"  # 要添加的exe完整路径如：
        # 注册表项名
        KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        # 异常处理
        try:
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
            value, key_type = win32api.RegQueryValueEx(key, "runpytask")
            win32api.RegCloseKey(key)
            return True
        except:
            return False
    def onstartboot(self):
      try:
        if self.iskjqd():
            self.qxqd()
        else:
            self.kjqd()
      except Exception as e:
          logging.info(e)
    def onstop(self):
      try:
        self.scheduler.shutdown()
        self.taskstar.setEnabled(True)
        self.statusbar.showMessage("任务已停止")
      except Exception as e:
          logging.info(e)
    def onstart(self):
      try:
        self.scheduler.remove_all_jobs()
        for l in self.qList:
            ls=l.split(";")
            if ls[0]=="onetime":
                self.scheduler.add_job(func=self.startexe, args=(ls[2],),
                                  trigger=DateTrigger(
                                  datetime.datetime.strptime(ls[3], "%Y-%m-%d %H:%M:%S")))
            elif ls[0]=="second":
                self.scheduler.add_job(self.startexe, 'interval',
                                       seconds=int(ls[5]),
                                       start_date=ls[3],
                                       end_date=ls[4],
                                       args=(ls[2],))
            elif ls[0]=="minute":
                self.scheduler.add_job(self.startexe, 'interval',
                                       minutes=int(ls[5]),
                                       start_date=ls[3],
                                       end_date=ls[4],
                                       args=(ls[2],))
            elif ls[0]=="hour":
                self.scheduler.add_job(self.startexe, 'interval',
                                       hours=int(ls[5]),
                                       start_date=ls[3],
                                       end_date=ls[4],
                                       args=(ls[2],))
            elif ls[0]=="day":
                self.scheduler.add_job(self.startexe, 'interval',
                                       days=int(ls[5]),
                                       start_date=ls[3],
                                       end_date=ls[4],
                                       args=(ls[2],))
            elif ls[0]=="week":
                self.scheduler.add_job(self.startexe, 'interval',
                                       weeks=int(ls[5]),
                                       start_date=ls[3],
                                       end_date=ls[4],
                                       args=(ls[2],))
            elif ls[0]=="month":
                self.scheduler.add_job(self.startexe, 'interval',
                                       months=int(ls[5]),
                                       start_date=ls[3],
                                       end_date=ls[4],
                                       args=(ls[2],))
        try:
            th=int(self.taskthreadnum.text())
        except:
            th=8
        try:
            pr=int(self.taskprocessnum.text())
        except:
            pr=4
        executors = {
            'default': ThreadPoolExecutor(th),
            'processpool': ProcessPoolExecutor(pr)
        }
        self.scheduler.configure(executors=executors)
        self.scheduler.start()
        self.taskstar.setEnabled(False)
        self.statusbar.showMessage("任务已启动")
      except Exception as e:
          logging.info(e)
    def onselecttask(self,qModelIndex):
        self.taskdeletename.setText(self.qList[qModelIndex.row()].split(";")[1])
    def onadd(self):
      try:
        if self.tasktype.currentIndex()==0:
            if not self.checkonetype()[0]:
                QMessageBox.about(self, '填写错误',self.checkonetype()[1])
                return
        elif self.tasktype.currentIndex()==1:
            if not self.checksecond()[0]:
                QMessageBox.about(self, '填写错误',self.checksecond()[1])
                return
        elif self.tasktype.currentIndex()==2:
            if not self.checkminute()[0]:
                QMessageBox.about(self, '填写错误',self.checkminute()[1])
                return
        elif self.tasktype.currentIndex()==3:
            if not self.checkhour()[0]:
                QMessageBox.about(self, '填写错误',self.checkhour()[1])
                return
        elif self.tasktype.currentIndex()==4:
            if not self.checkday()[0]:
                QMessageBox.about(self, '填写错误',self.checkday()[1])
                return
        elif self.tasktype.currentIndex()==5:
            if not self.checkweek()[0]:
                QMessageBox.about(self, '填写错误',self.checkweek()[1])
                return
        elif self.tasktype.currentIndex()==6:
            if not self.checkmonth()[0]:
                QMessageBox.about(self, '填写错误',self.checkmonth()[1])
                return
        self.writefile()
        self.loadfile()
        self.statusbar.showMessage("任务添加成功")
      except Exception as e:
          logging.info(e)
    def checkonetype(self):
        message=""
        result=True
        if self.taskpath.text().strip()=="":
            message+="要运行的任务不能为空！\n"
            result=False
        if self.taskname.text().strip()=="":
            message+="任务的名称不能为空！\n"
            result=False
        elif self.taskname.text().strip() in self.namelist:
            message += "任务的名称不能重复！\n"
            result = False
        return (result,message)
    def checksecond(self):
        message=self.checkonetype()[1]
        result=self.checkonetype()[0]
        try:
            minute=int(self.taskrate.text().strip())
            if minute<1 or minute>59:
                message += "秒必须是1-59的数字！\n"
                result = False
                return (result, message)
        except:
            message+="秒必须是1-59的数字！\n"
            result=False
            return (result,message)
        startime=datetime.datetime.strptime(self.taskstartime.text(), "%Y-%m-%d %H:%M:%S")
        endtime=datetime.datetime.strptime(self.taskendtime.text(), "%Y-%m-%d %H:%M:%S")
        if startime>endtime:
            message += "开始时间不能大于结束时间！\n"
            result = False
            return (result, message)
        return (result, message)
    def checkminute(self):
        message=self.checkonetype()[1]
        result=self.checkonetype()[0]
        try:
            minute=int(self.taskrate.text().strip())
            if minute<1 or minute>59:
                message += "分必须是1-59的数字！\n"
                result = False
                return (result, message)
        except:
            message+="分必须是1-59的数字！\n"
            result=False
            return (result,message)
        startime = datetime.datetime.strptime(self.taskstartime.text(), "%Y-%m-%d %H:%M:%S")
        endtime = datetime.datetime.strptime(self.taskendtime.text(), "%Y-%m-%d %H:%M:%S")
        if startime > endtime:
            message += "开始时间不能大于结束时间！\n"
            result = False
            return (result, message)
        return (result, message)
    def checkhour(self):
        message=self.checkonetype()[1]
        result=self.checkonetype()[0]
        try:
            hour=int(self.taskrate.text().strip())
            if hour<1 or hour>23:
                message += "时必须是1-23的数字！\n"
                result = False
                return (result, message)
        except:
            message+="时必须是1-23的数字！\n"
            result=False
            return (result,message)
        startime = datetime.datetime.strptime(self.taskstartime.text(), "%Y-%m-%d %H:%M:%S")
        endtime = datetime.datetime.strptime(self.taskendtime.text(), "%Y-%m-%d %H:%M:%S")
        if startime > endtime:
            message += "开始时间不能大于结束时间！\n"
            result = False
            return (result, message)
        return (result, message)
    def checkday(self):
        message=self.checkonetype()[1]
        result=self.checkonetype()[0]
        try:
            day=int(self.taskrate.text().strip())
            if day<1 or day>31:
                message += "天必须是1-31的数字！\n"
                result = False
                return (result, message)
        except:
            message+="天必须是1-31的数字！\n"
            result=False
            return (result,message)
        startime = datetime.datetime.strptime(self.taskstartime.text(), "%Y-%m-%d %H:%M:%S")
        endtime = datetime.datetime.strptime(self.taskendtime.text(), "%Y-%m-%d %H:%M:%S")
        if startime > endtime:
            message += "开始时间不能大于结束时间！\n"
            result = False
            return (result, message)
        return (result, message)
    def checkweek(self):
        message=self.checkonetype()[1]
        result=self.checkonetype()[0]
        try:
            week=int(self.taskrate.text().strip())
            if week<1 or week>23:
                message += "周必须是1-53的数字！\n"
                result = False
                return (result, message)
        except:
            message+="周必须是1-53的数字！\n"
            result=False
            return (result,message)
        startime = datetime.datetime.strptime(self.taskstartime.text(), "%Y-%m-%d %H:%M:%S")
        endtime = datetime.datetime.strptime(self.taskendtime.text(), "%Y-%m-%d %H:%M:%S")
        if startime > endtime:
            message += "开始时间不能大于结束时间！\n"
            result = False
            return (result, message)
        return (result, message)
    def checkmonth(self):
        message=self.checkonetype()[1]
        result=self.checkonetype()[0]
        try:
            month=int(self.taskrate.text().strip())
            if month<1 or month>12:
                message += "月必须是1-12的数字！\n"
                result = False
                return (result, message)
        except:
            message+="月必须是1-12的数字！\n"
            result=False
            return (result,message)
        startime = datetime.datetime.strptime(self.taskstartime.text(), "%Y-%m-%d %H:%M:%S")
        endtime = datetime.datetime.strptime(self.taskendtime.text(), "%Y-%m-%d %H:%M:%S")
        if startime > endtime:
            message += "开始时间不能大于结束时间！\n"
            result = False
            return (result, message)
        return (result, message)
    def deletefileline(self,taskname):
       try:
        taskname+=";"
        with open("tasklist.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open("tasklist.txt", "w", encoding="utf-8") as f_w:
            for line in lines:
                if taskname in line:
                    continue
                f_w.write(line)
       except Exception as e:
           logging.info(e)
           self.statusbar.showMessage(e)
    def writefile(self):
      try:
        with open("tasklist.txt","a+") as f:
            if self.tasktype.currentIndex()==0:
                f.write("onetime;{};{};{}\n"
                        .format(self.taskname.text().strip(),
                                self.taskpath.text().strip(),
                                self.taskstartime.text().strip()))
            elif self.tasktype.currentIndex() == 1:
                f.write("second;{};{};{};{};{}\n"
                        .format(self.taskname.text().strip(),
                                self.taskpath.text().strip(),
                                self.taskstartime.text().strip(),
                                self.taskendtime.text().strip(),
                                self.taskrate.text().strip()))
            elif self.tasktype.currentIndex() == 2:
                f.write("minute;{};{};{};{};{}\n"
                        .format(self.taskname.text().strip(),
                                self.taskpath.text().strip(),
                                self.taskstartime.text().strip(),
                                self.taskendtime.text().strip(),
                                self.taskrate.text().strip()))
            elif self.tasktype.currentIndex() == 3:
                f.write("hour;{};{};{};{};{}\n"
                        .format(self.taskname.text().strip(),
                                self.taskpath.text().strip(),
                                self.taskstartime.text().strip(),
                                self.taskendtime.text().strip(),
                                self.taskrate.text().strip()))
            elif self.tasktype.currentIndex() == 4:
                f.write("day;{};{};{};{};{}\n"
                        .format(self.taskname.text().strip(),
                                self.taskpath.text().strip(),
                                self.taskstartime.text().strip(),
                                self.taskendtime.text().strip(),
                                self.taskrate.text().strip()))
            elif self.tasktype.currentIndex() == 5:
                f.write("week;{};{};{};{};{}\n"
                        .format(self.taskname.text().strip(),
                                self.taskpath.text().strip(),
                                self.taskstartime.text().strip(),
                                self.taskendtime.text().strip(),
                                self.taskrate.text().strip()))
            elif self.tasktype.currentIndex() == 6:
                f.write("month;{};{};{};{};{}\n"
                        .format(self.taskname.text().strip(),
                                self.taskpath.text().strip(),
                                self.taskstartime.text().strip(),
                                self.taskendtime.text().strip(),
                                self.taskrate.text().strip()))
        self.namelist.append(self.taskname.text().strip())
        self.loadfile()
      except Exception as e:
          logging.info(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    myWin.onstart()
    sys.exit(app.exec_())

