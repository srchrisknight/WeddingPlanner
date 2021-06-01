import os,sys,json

from Qt import QtWidgets, QtCore, QtGui

import qtmodern.styles
import qtmodern.windows

################################################################################
# Item Widgets
################################################################################
class PersonItemWidget(QtWidgets.QWidget):
	def __init__(self, **kwargs):
		super(PersonItemWidget,self).__init__()

		self.Name = kwargs.get('Name','Bob George')
		self.GuestPermission = kwargs.get('GuestPermission', False)
		self.PlusOne = kwargs.get('PlusOne',False)
		self.Family = kwargs.get('Family',False)
		self.RSVP = kwargs.get('RSVP','Maybe')

		self.lblName = QtWidgets.QLabel(self.Name)
		self.uiRSVP = QtWidgets.QComboBox()
		self.uiPlusOne = QtWidgets.QCheckBox('PlusOne')
		self.uiGuestName = QtWidgets.QLineEdit()

		self.uiRSVP.addItems(['Going', 'Not Going', 'Maybe'])
		index = self.uiRSVP.findText(self.RSVP)
		self.uiRSVP.setCurrentIndex(index)

		self.layMain = QtWidgets.QVBoxLayout()
		self.layH = QtWidgets.QHBoxLayout()

		self.layMain.addLayout(self.layH)

		self.layH.addWidget(self.lblName)
		self.layH.addWidget(self.uiRSVP)
		self.layH.addStretch()
		self.layH.addWidget(self.uiPlusOne)
		self.layH.addWidget(self.uiGuestName)

		self.setLayout(self.layMain)


class ExpenseItemWidget(QtWidgets.QWidget):
	def __init__(self, **kwargs):
		super(ExpenseItemWidget,self).__init__()

		self.Name = kwargs.get('Name','Temp Expense')
		self.Price = kwargs.get('Price')

		self.lblName = QtWidgets.QLabel(self.Name + ':')
		self.lblPrice = QtWidgets.QLabel('Price:')
		self.uiPrice = QtWidgets.QDoubleSpinBox()
		self.lblEstPrice = QtWidgets.QLabel('Est. Price:')
		self.uiEstPice = QtWidgets.QDoubleSpinBox()
		self.uiNotes = QtWidgets.QTextEdit()

		self.layH = QtWidgets.QHBoxLayout()
		self.layMain = QtWidgets.QVBoxLayout()

		self.layH.addWidget(self.lblName)
		self.layH.addStretch()
		self.layH.addWidget(self.lblPrice)
		self.layH.addWidget(self.uiPrice)
		self.layH.addWidget(self.lblEstPrice)
		self.layH.addWidget(self.uiEstPice)

		self.layMain.addLayout(self.layH)
		self.layMain.addWidget(self.uiNotes)

		self.setLayout(self.layMain)


################################################################################
# Sub Widgets
################################################################################
class WeddingInfo(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.layMain = QtWidgets.QFormLayout()

		self.layMain.addRow('Confirmed Guest Count:',QtWidgets.QLabel('Temp'))
		self.layMain.addRow('Estimated Guest Count:',QtWidgets.QLabel('Temp'))
		self.layMain.addRow('Confirmed Price:',QtWidgets.QLabel('Temp'))
		self.layMain.addRow('Estimated Price:',QtWidgets.QLabel('Temp'))

		self.setLayout(self.layMain)


class GuestList(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.uiTree = QtWidgets.QTreeWidget()

		self.layMain = QtWidgets.QVBoxLayout()

		self.layMain.addWidget(self.uiTree)

		self.setLayout(self.layMain)


class ExpenseList(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__()

		self.uiTree = QtWidgets.QTreeWidget()

		self.layMain = QtWidgets.QVBoxLayout()

		self.layMain.addWidget(self.uiTree)
		self.layMain.addWidget(QtWidgets.QPushButton(QtGui.QIcon(QtGui.QPixmap(r"/home/chris/Repos/material-design-icons/src/social/outdoor_grill/materialiconstwotone/24px.svg")),'Copy'))

		self.setLayout(self.layMain)		



################################################################################
# Main Tool
################################################################################
class WeddingPlanner(QtWidgets.QMainWindow):
	def __init__(self, **kwargs):
		super().__init__()
		self.resize(800,600)
		self.setWindowTitle('Wedding Planner')

		self.uiSplitter = QtWidgets.QSplitter()
		self.uiTabs = QtWidgets.QTabWidget()

		self.uiWeddingInfo = WeddingInfo()
		self.uiGuestList = GuestList()
		self.uiExpenseList = ExpenseList()

		self.menuFile = QtWidgets.QMenu('File')

		self.actOpen = QtWidgets.QAction()

		self.uiTabs.addTab(self.uiGuestList, 'Guests')
		self.uiTabs.addTab(self.uiExpenseList, 'Expenses')

		self.uiSplitter.addWidget(self.uiWeddingInfo)
		self.uiSplitter.addWidget(self.uiTabs)

		self.setCentralWidget(self.uiSplitter)


def setStyleSheet(tool):
	styleFile = os.path.join(os.path.dirname(__file__),'resources/stylesheets/QTDark.stylesheet')

	with open(styleFile,'r') as sf:
		tool.setStyleSheet(sf.read())

if __name__ == '__main__':
	print('running')
	app = QtWidgets.QApplication(sys.argv)
	# StyleUtils.setStyleSheet(app)
	tool = WeddingPlanner()
	setStyleSheet(tool)
	tool.show()
	sys.exit(app.exec_())	