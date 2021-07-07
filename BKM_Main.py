from bkmSettings import
from bkmCheckInformation import
# from bkmCheckInformation import Ui_mainWindow
from bkmCheckInformationPythonFile import

from PyQt4.QtGui import
from PyQt4.QtCore import QFileInfo, QSettings
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import qApp, QApplication, QMainWindow, QFormLayout, QLineEdit, QTabWidget, QWidget, QAction
from PyQt4.QtCore import
from bs4 import BeautifulSoup
import lxml
import inspect

try
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError
    def _fromUtf8(s)
        return s

try
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig)
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError
    def _translate(context, text, disambig)
        return QtGui.QApplication.translate(context, text, disambig)


class bkmGuiInfoEntry(Ui_MainWindow)
    def __init__(self)
        super(bkmGuiInfoEntry, self).__init__()
        # self.app = QtGui.QApplication(sys.argv)
        self.MainWindow = QtGui.QMainWindow()
        super().setupUi(self.MainWindow)
        header = self.packageFilesTableWidget.horizontalHeader()
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        self.packageDirectoryBrowseButton.setStyleSheet(_fromUtf8(background - color
        rgb(0, 85, 255);
        colorrgb(255, 255, 255)))
        self.QuitBkmButton.setStyleSheet(_fromUtf8(background - color
        rgb(0, 128, 255);
        colorrgb(255, 255, 255)))
        self.launchBkmButton.setStyleSheet(_fromUtf8(background - colorrgb(0, 170, 0);
        color
        rgb(255, 255, 255)))
        self.viewBkmReportButton.setStyleSheet(_fromUtf8(background - colorrgb(0, 170, 0);
        color
        rgb(255, 255, 255)))
        self.openReleaseNotesButtoon.setStyleSheet(_fromUtf8(background - colorrgb(0, 170, 0);
        color
        rgb(255, 255, 255)))
        DF = pd.DataFrame()
        DF = pd.read_csv(fileOfChecks, sep=t +, usecols=['#ID', 'Step', 'Check Name', 'Check Type', 'Description'],
                         engine='python')
        l = []
        for column in DF[['#ID', 'Check Name', 'Check Type', 'Step', 'Description']]
            columnSeriesObj = DF[column]

            a = columnSeriesObj.values
            l.append(a)
        zero_count = np.sum(l[2] == 0)

        one_count = np.sum(l[2] == 1)
        rowsOfErrorChecks_1 = (zero_count)
        2
        rowsOfWarningChecks_1 = (one_count)
        2

        x = 0
        y = 0
        index = 0
        row_1 = 1
        row_2 = 1
        row_3 = 1
        row_4 = 1
        gridLayout = QGridLayout()
        self.checksGroupBox.setLayout(gridLayout)
        self.button5 = QPushButton('ERROR CHECKS')
        gridLayout.addWidget(self.button5, 0, 0)
        self.button5.setStyleSheet(background - colorblue;
        colorwhite)

        self.button6 = QPushButton('ERROR CHECKS')
        gridLayout.addWidget(self.button6, 0, 1)
        self.button6.setStyleSheet(background - colorblue;
        colorwhite)

        self.button7 = QPushButton('WARNING CHECKS')
        gridLayout.addWidget(self.button7, 0, 2)
        self.button7.setStyleSheet(background - colorblue;
        colorwhite)

        self.button8 = QPushButton('WARNING CHECKS')
        gridLayout.addWidget(self.button8, 0, 3)
        self.button8.setStyleSheet(background - colorblue;
        colorwhite)
        m = []
        n = []
        self.btn = []
        self.dfFile = pd.DataFrame()
        self.dfFile['CheckNo'] = ''
        self.dfFile['CheckName'] = ''
        self.dfFile['CheckType'] = ''
        self.dfFile['CheckButtonWidgetName'] = ''
        self.dfFile['Step'] = ''
        self.dfFile['Description'] = ''
        i = 0
        for a in np.nditer(l[2])
            if a == 0
                if x  rowsOfErrorChecks_1
                self.button1 = QPushButton(l[1][index])

                gridLayout.addWidget(self.button1, row_1, 0)

                row_1 += 1
                self.dfFile.loc[len(self.dfFile)] = [l[0][index], l[1][index], a, self.button1, l[3][index],
                                                     l[4][index]]

                self.button1.setStyleSheet(background - colorrgb(126, 126, 94);
                colorwhite;
                Text - alignleft)
                self.button1.setDisabled(True)

                self.button1.setDisabled(True)

                # self.button1.clicked.connect(lambda self.openGui(self.button1))

            if x = rowsOfErrorChecks_1 and x  zero_count
            self.button2 = QPushButton(l[1][index])

            gridLayout.addWidget(self.button2, row_2, 1)

            row_2 += 1
            self.button2.setStyleSheet(background - colorrgb(126, 126, 94);
            colorwhite;
            Text - alignleft)
            self.dfFile.loc[len(self.dfFile)] = [l[0][index], l[1][index], a, self.button2, l[3][index], l[4][index]]

            self.button2.setDisabled(True)
            # self.button2.clicked.connect(lambda self.openGui(self.button2))
        x += 1

    if a == 1
        if y  rowsOfWarningChecks_1
        self.button3 = QPushButton(l[1][index])

        gridLayout.addWidget(self.button3, row_3, 2)

        row_3 += 1
        self.dfFile.loc[len(self.dfFile)] = [l[0][index], l[1][index], a, self.button3, l[3][index], l[4][index]]
        self.button3.setStyleSheet(background - colorrgb(126, 126, 94);
        colorwhite;
        Text - alignleft)

        self.button3.setDisabled(True)
        # self.button3.clicked.connect(lambda self.openGui(self.button3))

    if y = rowsOfWarningChecks_1 and y  one_count
    self.button4 = QPushButton(l[1][index])

    gridLayout.addWidget(self.button4, row_4, 3)

    row_4 += 1
    self.dfFile.loc[len(self.dfFile)] = [l[0][index], l[1][index], a, self.button4, l[3][index], l[4][index]]
    self.button4.setStyleSheet(background - colorrgb(126, 126, 94);
    colorwhite;
    Text - alignleft)

    self.button4.setDisabled(True)


y += 1
i += 1
index += 1
self.listOfCheckNo = []
self.listOfCheckName = []
self.listOfCheckType = []
self.listOfCheckButtonWidgetName = []
self.listOfStep = []
self.listOfDescription = []
for checkno in self.dfFile['CheckNo'].iteritems()
    self.listOfCheckNo.append(checkno)

for checkname in self.dfFile['CheckName'].iteritems()
    self.listOfCheckName.append(checkname)

for checktype in self.dfFile['CheckType'].iteritems()
    self.listOfCheckType.append(checktype)

for buttonwidgetname in self.dfFile['CheckButtonWidgetName'].iteritems()
    self.listOfCheckButtonWidgetName.append(buttonwidgetname)
for step in self.dfFile['Step'].iteritems()
    self.listOfStep.append(step)
for description in self.dfFile['Description'].iteritems()
    self.listOfDescription.append(description)

self.packageDirectoryLineEdit.setEnabled(False)

self.QuitBkmButton.clicked.connect(self.buttonClicked)

self.libRepository = opcPackageCommonFunc()
self.packageDirectoryBrowseButton.clicked.connect(lambda self.getUserPackageDetails())
self.launchBkmButton.clicked.connect(lambda self.launchBkm(self.dfFile))
self.viewBkmReportButton.clicked.connect(lambda self.viewBkmReport())
self.dialogs = list()
self.MainWindow.show()


# sys.exit(self.app.exec_())

def buttonClicked(self)
    exit()

    sys.exit(self.app.exec_())


def openGui(self, button, color)

    text = self.MainWindow.sender().text()

    self.newWindow = bkmCheckInformation()

    for i in range(len(self.listOfCheckNo))
        if text == self.listOfCheckName[i][1]
            self.newWindow.checkNoLabel_2.setText(self.listOfCheckNo[i][1])

            self.newWindow.checkNameLabel_2.setText(self.listOfCheckName[i][1])

            self.newWindow.inputFileLabel_2.setText(self.listOfStep[i][1])
            for k in range(len(self.dataFrameOfCsv[0]))
                if self.listOfCheckNo[i][1] == (self.dataFrameOfCsv[0][k][35])

                    self.newWindow.resultLabel.setText(self.dataFrameOfCsv[2][k][6])

            k = self.listOfStep[i][1]
            print('kkkkkkkkkkkkkk', k)
            self.newWindow.openInputFileButton.clicked.connect(lambda self.allFiles())
            self.newWindow.viewBkmButton.clicked.connect(lambda self.openHtmlFile())
            self.newWindow.launchBkmButton.clicked.connect(lambda self.runPythonScript())
            self.newWindow.autoCorrectBkmButton.clicked.connect(lambda self.runAnotherPythonScript())
            self.newWindow.openBkmDocumentButton.clicked.connect(lambda self.runAnotherOnePythonScript())

            l = []
            l.append(self.listOfDescription[i][1])
            print('bbbbbbbbbb', l)
            words = [j.split('n') for j in l]
            print('wwwwwwwwwwwwwwwwwwwwwwwwwwww', words)
            for k in range((len(words[0])))

                self.newWindow.descriptionListWidget.addItem(words[0][k])
                self.newWindow.descriptionListWidget.setStyleSheet(colorblack)
            l = []

            self.newWindow.descriptionListWidget.setFocusPolicy(Qt.NoFocus)
            self.newWindow.descriptionListWidget.setSelectionMode(QAbstractItemView.NoSelection)

            self.newWindow.viewBkmButton.setText((View BKM {} Result).format(self.listOfCheckNo[i][1]))
            self.newWindow.viewBkmButton.setStyleSheet(background - color
            rgb(0, 170, 0);
            colorblack)
            self.newWindow.launchBkmButton.setStyleSheet(background - color
            rgb(0, 170, 0);
            colorblack)
            self.newWindow.autoCorrectBkmButton.setStyleSheet(background - color
            rgb(0, 170, 0);
            colorblack)
            self.newWindow.openBkmDocumentButton.setStyleSheet(background - color
            rgb(0, 170, 0);
            colorblack)
            self.newWindow.launchBkmButton.setText((Launch BKM {}).format(self.listOfCheckNo[i][1]))
            self.newWindow.autoCorrectBkmButton.setText((Auto Correct BKM {}).format(self.listOfCheckNo[i][1]))
            self.newWindow.openBkmDocumentButton.setText((Open BKM {} Document).format(self.listOfCheckNo[i][1]))
            if color == 'green'
                self.newWindow.statusLabel_2.setText('PASS')
                self.newWindow.statusLabel_2.setStyleSheet(background - color
                rgb(0, 170, 0);
                colorblack)
                self.newWindow.statusLabel_1.setStyleSheet(background - color
                rgb(0, 170, 0);
                colorblack)
                if color == 'red'
                    self.newWindow.statusLabel_2.setText('FAIL')
                    self.newWindow.statusLabel_2.setStyleSheet(background - color
                    rgb(217, 0, 0);
                    colorblack)
                    self.newWindow.statusLabel_1.setStyleSheet(background - color
                    rgb(217, 0, 0);
                    colorblack)
                    if color == 'orange'
                        self.newWindow.statusLabel_2.setText('FAIL')
                        self.newWindow.statusLabel_2.setStyleSheet(background - color
                        rgb(217, 0, 0);
                        colorblack)
                        self.newWindow.statusLabel_1.setStyleSheet(background - color
                        rgb(217, 0, 0);
                        colorblack)

                def runAnotherOnePythonScript(self)
                    path = self.packageDirectoryLineEdit.text()
                    text = self.newWindow.checkNoLabel_2.text()
                    print('texttttttttttt', text)
                    resultList = getTechLayAbrFromDir(self.packageDirectoryLineEdit.text())

                    self.techno, self.level = resultList[0], resultList[1]
                    os.system(
                        'workratsoftbinpython prjopcalluserssource_opcallRETToolsBoxModulesRETBKMlastBKM_main.py BKM_DocLink {} {} {} NO {}reportsBKM BKM{}'.format(
                            path, self.techno, self.level, path, text))

                def runAnotherPythonScript(self)
                    path = self.packageDirectoryLineEdit.text()
                    text = self.newWindow.checkNoLabel_2.text()
                    print('texttttttttttt', text)
                    resultList = getTechLayAbrFromDir(self.packageDirectoryLineEdit.text())

                    self.techno, self.level = resultList[0], resultList[1]

                    # print(self.dataFrameOfCsv[0])
                    for i in range(len(self.dataFrameOfCsv[0]))

                        if self.dataFrameOfCsv[0][i][35] == text
                            # print(self.dataFrameOfCsv[0][i][35])
                            # print(self.dataFrameOfCsv[4][i])
                            self.autoCorrect = self.dataFrameOfCsv[0][i][35]

                    os.system(
                        'workratsoftbinpython prjopcalluserssource_opcallRETToolsBoxModulesRETBKMlastBKM_main.py BKM_checktest {} {} {} {} {}reportsBKM BKM{}'.format(
                            path, self.techno, self.level, self.autoCorrect, path, text))
                    os.system(
                        'workratsoftbinpython prjopcalluserssource_opcallRETToolsBoxModulesRETBKMlastBKM_main.py BKM_checktest {} {} {} NO {}reportsBKM BKM{}'.format(
                            path, self.techno, self.level, path, text))

                def showdialog(self, title, message)
                    msg = QMessageBox()
                    msg.setText(message)
                    msg.setWindowTitle(title)
                    msg.setStandardButtons(QMessageBox.Ok)
                    if QMessageBox.Ok
                        msg.close()
                    msg.exec_()

                def showDialog(self, title, message)

                    msg = QMessageBox()
                    msg.setText(message)
                    msg.setWindowTitle(title)
                    msg.setStandardButtons(QMessageBox.Ok)

                    # msg.setStandardButtons(QMessageBox.skipMessage)
                    msg.setDetailedText('Details')
                    if QMessageBox.Ok
                        msg.close()
                    msg.exec_()

                def showMessage(self)

                    msg = QMessageBox()
                    text = self.newWindow.checkNoLabel_2.text()
                    msg.setText(
                        'New BKM Report has been created for CHECK {}!!n Press Button View BKM{} Result to see the latest report.'.format(
                            text, text))
                    msg.setWindowTitle('Information')
                    msg.setStandardButtons(QMessageBox.Ok)

                    if QMessageBox.Ok
                        msg.close()
                    msg.exec_()

                def getUserPackageDetails(self)


                    self.packagePath = self.libRepository.getUserDirectory()

                    directory = self.packagePath
                    print('kkkkkkkk', directory)

                    if self.packagePath !=
                        self.packageDirectoryLineEdit.clear()
                        self.packageDirectoryLineEdit.insert(self.packagePath)
                        self.packageFilesTableWidget.verticalHeader().setVisible(False)
                        self.packageFilesTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
                        xml = []
                        if path.exists(self.packagePath + package)

                            def get_xml_files(path)
                                xml_list = []
                                for filename in os.listdir(path)

                                    if filename.endswith(.xml)
                                    xml_list.append(os.path.join(filename))

                            return xml_list

                        xml = get_xml_files(self.packagePath + package)

                    if path.exists(self.packagePath + package + templates)
                        listOfFiles = []
                        pathOfFiles = os.listdir(self.packagePath + package + templates)

                        for l in pathOfFiles
                            listOfFiles.append(l)

                        xml.extend(listOfFiles)
                    # print(xml)

                    self.packageFilesTableWidget.setRowCount(0)
                    for i in range(10)
                        rowPosition = self.packageFilesTableWidget.rowCount()
                        self.packageFilesTableWidget.insertRow(rowPosition)
                    self.packageFilesTableWidget.resizeRowsToContents()
                    self.packageFilesTableWidget.setItem(0, 0, QtGui.QTableWidgetItem('M'))
                    self.packageFilesTableWidget.setItem(0, 1, QtGui.QTableWidgetItem('DRC'))
                    self.packageFilesTableWidget.setItem(1, 0, QtGui.QTableWidgetItem('M'))
                    self.packageFilesTableWidget.setItem(1, 1, QtGui.QTableWidgetItem('GEN'))
                    # self.packageFilesTableWidget.setItem(2, 0, QtGui.QTableWidgetItem('M'))
                    # self.packageFilesTableWidget.setItem(2, 1, QtGui.QTableWidgetItem('VER'))
                    self.packageFilesTableWidget.setItem(2, 0, QtGui.QTableWidgetItem('M'))
                    self.packageFilesTableWidget.setItem(2, 1, QtGui.QTableWidgetItem('PRE-OPC'))
                    self.packageFilesTableWidget.setItem(3, 0, QtGui.QTableWidgetItem('B'))
                    self.packageFilesTableWidget.setItem(3, 1, QtGui.QTableWidgetItem('OPC'))
                    self.packageFilesTableWidget.setItem(4, 0, QtGui.QTableWidgetItem('B'))
                    self.packageFilesTableWidget.setItem(4, 1, QtGui.QTableWidgetItem('DEVICE'))
                    self.packageFilesTableWidget.setItem(5, 0, QtGui.QTableWidgetItem('B'))
                    self.packageFilesTableWidget.setItem(5, 1, QtGui.QTableWidgetItem('VER'))
                    self.packageFilesTableWidget.setItem(6, 0, QtGui.QTableWidgetItem(' '))
                    self.packageFilesTableWidget.setItem(6, 1, QtGui.QTableWidgetItem('MRC_XML'))
                    self.packageFilesTableWidget.setItem(7, 0, QtGui.QTableWidgetItem(' '))
                    self.packageFilesTableWidget.setItem(7, 1, QtGui.QTableWidgetItem('PREOPC_XML'))
                    self.packageFilesTableWidget.setItem(8, 0, QtGui.QTableWidgetItem(' '))
                    self.packageFilesTableWidget.setItem(8, 1, QtGui.QTableWidgetItem('OPC_XML'))
                    self.packageFilesTableWidget.setItem(9, 0, QtGui.QTableWidgetItem(' '))
                    self.packageFilesTableWidget.setItem(9, 1, QtGui.QTableWidgetItem('VER_XML'))

                    for file in xml
                        if file.endswith('_MRC.calibre')
                            self.packageFilesTableWidget.setItem(0, 2, QtGui.QTableWidgetItem(file))
                        if file.endswith('_OPC.calibre')
                            self.packageFilesTableWidget.setItem(1, 2, QtGui.QTableWidgetItem(file))

                        '''if file.endswith('_VER.calibre')
                        self.packageFilesTableWidget.setItem(2, 2, QtGui.QTableWidgetItem(file))'''

                        if file.endswith('_PREOPC.calibre')
                            self.packageFilesTableWidget.setItem(2, 2, QtGui.QTableWidgetItem(file))

                        if file.endswith('_OPC.tflex')
                            self.packageFilesTableWidget.setItem(3, 2, QtGui.QTableWidgetItem(file))

                        if file.endswith('_device.tflex')
                            self.packageFilesTableWidget.setItem(4, 2, QtGui.QTableWidgetItem(file))

                        if file.endswith('_VER.tflex')
                            self.packageFilesTableWidget.setItem(5, 2, QtGui.QTableWidgetItem(file))

                        if file.endswith('_MRC.xml')
                            self.packageFilesTableWidget.setItem(6, 2, QtGui.QTableWidgetItem(file))

                        if file.endswith('_PREOPC.xml')
                            self.packageFilesTableWidget.setItem(7, 2, QtGui.QTableWidgetItem(file))

                        if file.endswith('_OPC.xml')
                            self.packageFilesTableWidget.setItem(8, 2, QtGui.QTableWidgetItem(file))

                        if file.endswith('_VER.xml')
                            self.packageFilesTableWidget.setItem(9, 2, QtGui.QTableWidgetItem(file))
                    for i in range(10)
                        item = self.packageFilesTableWidget.item(i, 2)

                        if not item
                            self.packageFilesTableWidget.setItem(i, 2, QtGui.QTableWidgetItem(''))
                            self.packageFilesTableWidget.item(i, 0).setBackground(QtGui.QColor(126, 126, 94))
                            self.packageFilesTableWidget.item(i, 1).setBackground(QtGui.QColor(126, 126, 94))
                            self.packageFilesTableWidget.item(i, 2).setBackground(QtGui.QColor(126, 126, 94))

                    self.setCheckButtonColor()

            def runPythonScript(self)
                resultList = getTechLayAbrFromDir(self.packageDirectoryLineEdit.text())

                self.techno, self.level = resultList[0], resultList[1]
                techno = self.techno
                level = self.level
                print('technoooooooooooooo', techno)
                print('levellllllllllllll', level)
                path = self.packageDirectoryLineEdit.text()
                text = self.newWindow.checkNoLabel_2.text()

                # os.system('workratsoftbinpython prjopcalluserssource_opcallRETToolsBoxModulesRETBKMbetaBKM_main.py BKM_launch {} {} {} NO'.format(directory, techno, level))
                os.system(
                    'workratsoftbinpython prjopcalluserssource_opcallRETToolsBoxModulesRETBKMlastBKM_main.py BKM_checktest {} {} {} NO {}reportsBKM BKM{}'.format(
                        path, self.techno, self.level, path, text))
                print('script has runned nnnnnnnnnnnnnnnnnnnnnnn')
                self.showMessage()

            def openHtmlFile(self)

                path = self.packageDirectoryLineEdit.text()
                print(path)
                text = self.newWindow.checkNoLabel_2.text()
                os.system(firefox
                {}
                reportsBKMBKM
                {}.html &.format(path, text))

                def allFiles(self)
                    p = []
                    u = []

                    j = self.newWindow.inputFileLabel_2.text()

                    path = self.packageDirectoryLineEdit.text()
                    p.append(j.split(' '))
                    print('ppppppppppppppkkkkkkkkkkkkkkkkkk', p)

                    b = []
                    for i in range(len(p[0]))
                        if p[0][i] == 'DRC' and self.packageFilesTableWidget.item(0, 2).text() != ''

                            b.append(
                                '{}packagetemplates{}'.format(path, self.packageFilesTableWidget.item(0, 2).text()))

                        if p[0][i] == 'GEN' and self.packageFilesTableWidget.item(1, 2).text() != ''

                            b.append(
                                '{}packagetemplates{}'.format(path, self.packageFilesTableWidget.item(1, 2).text()))

                        if p[0][i] == 'PRE' and self.packageFilesTableWidget.item(2, 2).text() != ''

                            b.append(
                                '{}packagetemplates{}'.format(path, self.packageFilesTableWidget.item(2, 2).text()))

                        if p[0][i] == 'OPC' and self.packageFilesTableWidget.item(3, 2).text() != ''

                            b.append(
                                '{}packagetemplates{}'.format(path, self.packageFilesTableWidget.item(3, 2).text()))

                        if p[0][i] == 'DEVICE' and self.packageFilesTableWidget.item(4, 2).text() != ''

                            b.append(
                                '{}packagetemplates{}'.format(path, self.packageFilesTableWidget.item(4, 2).text()))

                        if p[0][i] == 'VER' and self.packageFilesTableWidget.item(5, 2).text() != ''

                            b.append(
                                '{}packagetemplates{}'.format(path, self.packageFilesTableWidget.item(5, 2).text()))

                        if p[0][i] == 'MRC_XML' and self.packageFilesTableWidget.item(6, 2).text() != ''

                            b.append('{}package{}'.format(path, self.packageFilesTableWidget.item(6, 2).text()))

                        if p[0][i] == 'PREOPC_XML' and self.packageFilesTableWidget.item(7, 2).text() != ''

                            b.append('{}package{}'.format(path, self.packageFilesTableWidget.item(7, 2).text()))

                        if p[0][i] == 'OPC_XML' and self.packageFilesTableWidget.item(8, 2).text() != ''

                            b.append('{}package{}'.format(path, self.packageFilesTableWidget.item(8, 2).text()))

                        if p[0][i] == 'VER_XML' and self.packageFilesTableWidget.item(9, 2).text() != ''

                            b.append('{}package{}'.format(path, self.packageFilesTableWidget.item(9, 2).text()))

                    print('bbbbbbbbbbbbb', b)
                    openFiles =
                    openFiles = openFiles.join(b)

                    os.system(nedit
                    {} &.format(openFiles))

                    def setCheckButtonColor(self)
                        for i in range(len(self.listOfCheckNo))


                            self.listOfCheckButtonWidgetName[i][1].setStyleSheet(background - colorrgb(126, 126, 94);
                            colorwhite;
                            Text - alignleft)



                            directory = self.packageDirectoryLineEdit.text()
                            paths = directory + 'reports' + 'BKM'

                            file1 = paths + 'output.csv'
                            if os.path.exists(paths)
                                if os.path.isfile(file1)

                                    self.DF = pd.DataFrame()
                                    self.DF = pd.read_csv(file1, header=None)

                                    self.dataFrameOfCsv = []
                                    for column in self.DF[[0, 1, 2, 3, 4]]
                                        columnSeriesObj = self.DF[column]
                                        a = columnSeriesObj.values
                                        self.dataFrameOfCsv.append(a)

                                    index = 0

                                    print('kkkkkkkkkkjjjjjjjjjjj', self.dataFrameOfCsv[0])
                                    for m in range(len(self.dataFrameOfCsv[0]))
                                        for i in range(len(self.listOfCheckNo))
                                            if self.dataFrameOfCsv[0][m][3] == self.listOfCheckNo[i][1]
                                                if self.dataFrameOfCsv[1][m] == 'PASS'
                                                    self.listOfCheckButtonWidgetName[i][1].setStyleSheet(
                                                        background - colorrgb(0, 170, 0);
                                                    colorwhite;
                                                    Text - alignleft)
                                                    self.listOfCheckButtonWidgetName[i][1].setDisabled(False)
                                                    self.listOfCheckButtonWidgetName[i][1].clicked.connect(
                                                        lambda self.openGui(self.listOfCheckButtonWidgetName[i][1],
                                                                            'green'))
                                                    if self.dataFrameOfCsv[1][m] == 'FAIL'
                                                        if self.listOfCheckType[i][1] == 0
                                                            self.listOfCheckButtonWidgetName[i][1].setStyleSheet(
                                                                background - colorred;
                                                            colorwhite;
                                                            Text - alignleft)
                                                            self.listOfCheckButtonWidgetName[i][1].setDisabled(False)
                                                            self.listOfCheckButtonWidgetName[i][1].clicked.connect(
                                                                lambda self.openGui(
                                                                self.listOfCheckButtonWidgetName[i][1], 'red'))
                                                            if self.listOfCheckType[i][1] == 1
                                                                self.listOfCheckButtonWidgetName[i][1].setStyleSheet(
                                                                    background - colororange;
                                                                colorwhite;
                                                                Text - alignleft)
                                                                self.listOfCheckButtonWidgetName[i][1].setDisabled(
                                                                    False)
                                                                self.listOfCheckButtonWidgetName[i][1].clicked.connect(
                                                                    lambda self.openGui(
                                                                    self.listOfCheckButtonWidgetName[i][1], 'orange'))





                                            else
                                                for i in range(len(self.listOfCheckNo))
                                                    self.listOfCheckButtonWidgetName[i][1].setStyleSheet(
                                                        background - colorrgb(126, 126, 94);
                                                    colorwhite;
                                                    Text - alignleft)

                                                def launchBkm(self, dfFile)

                                                    directory = self.packageDirectoryLineEdit.text()
                                                    if directory == ''
                                                        self.showdialog(Message, you
                                                        did
                                                        not choose
                                                        the
                                                        package
                                                        directory)
                                                        else
                                                        resultList = getTechLayAbrFromDir(
                                                            self.packageDirectoryLineEdit.text())

                                                        self.techno, self.level = resultList[0], resultList[1]
                                                        techno = self.techno
                                                        level = self.level

                                                        if len(techno) == 0 or len(level) == 0
                                                            self.showdialog(Message,
                                                                            'please choose the correct package directory')
                                                        else
                                                            directory = self.packageDirectoryLineEdit.text()
                                                            os.system(
                                                                'workratsoftbinpython prjopcalluserssource_opcallRETToolsBoxModulesRETBKMlastBKM_main.py BKM_launch {} {} {} NO '.format(
                                                                    directory, techno, level))
                                                            print('python script has runned')

                                                            paths = directory + 'reports' + 'BKM'
                                                            file1 = paths + 'output.csv'
                                                            if os.path.exists(paths)
                                                                if os.path.isfile(file1)

                                                                    self.setCheckButtonColor()

                                                def viewBkmReport(self)
                                                    directory = self.packageDirectoryLineEdit.text()

                                                    if directory == ''
                                                        self.showdialog(Message, you
                                                        did
                                                        not choose
                                                        the
                                                        package
                                                        directory)
                                                        else

                                                        paths = directory + 'reports' + 'BKM'
                                                        if os.path.exists(paths)
                                                            path_2 = '{}{}.html'.format(paths,
                                                                                        os.path.basename(directory))

                                                            if os.path.isfile(path_2)
                                                                os.system('firefox {}{}.html &'.format(paths,
                                                                                                       os.path.basename(
                                                                                                           directory)))
                                                            else
                                                                self.showdialog(Message, '{}{}.html'.format(paths,
                                                                                                            os.path.basename(
                                                                                                                directory)) is not present,
                                                                                please
                                                                click
                                                                on
                                                                BKM
                                                                Launch
                                                                Button)

                                                                else

                                                                self.showdialog(Message,
                                                                                'please choose the correct package  directory')

                                                if __name__ == '__main__'
                                                    app = QtGui.QApplication([])
                                                    bkmGuiInfoEntry()
                                                    app.exec_()