import os,sys

sys.path.append(os.environ.get('PS_SITEPACKAGES'))

from Qt import QtWidgets, QtCore, QtGui

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
		self.Price = kwargs.get()

		self.lblName = QtWidgets.QLabel(self.Name)
		self.lblPrice = QtWidgets.QLabel('Price')
		self.uiPrice = QtWidgets.QDoubleSpinBox()
		self.lblEstPrice = QtWidgets.QLabel('Est. Price')
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


################################################################################
# Main Tool
################################################################################




if __name__ == '__main__':
	print 'running'
	app = QtWidgets.QApplication(sys.argv)
	# StyleUtils.setStyleSheet(app)
	tool = ExpenseItemWidget()
	tool.show()
	sys.exit(app.exec_())	