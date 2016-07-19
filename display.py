#!/usr/bin/python

import sys
from PyQt4 import QtGui

import subprocess


from mainwindow import Ui_MainWindow

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.systemInformation()
    
    def systemInformation(self):
        subprocess.call('ps -ef > processlist.txt', shell=True)

       
        with open('processlist.txt', 'r') as processList:
            lines = processList.read().split('\n')
            
            firstLine = lines[0].split()[::-1]
            
            model = QtGui.QStandardItemModel(2,3,self)
          
            increment = 0
            first = True
            for line in lines:
                
                line = line.split()
                fullCMD = ''
                size = len(line)
                incrementor = 7
                while incrementor < size:
                    fullCMD = fullCMD + ' ' + line.pop(-1)
                    incrementor = incrementor + 1
                
                line.append(fullCMD)
                
                line = line[::-1]
                
                columnIncrement = 0
                for column in line:
                    if first:
                        model.setHorizontalHeaderItem(columnIncrement, QtGui.QStandardItem(column))
                    else:
                        model.setItem(increment, columnIncrement, QtGui.QStandardItem(column))
                    
                    columnIncrement = columnIncrement + 1
                
                if first:
                    first = False
                else:
                    increment = increment + 1
 
            self.ui.tableView.setModel(model)
 
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
  
