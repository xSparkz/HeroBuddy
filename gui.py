# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Thu Apr  6 22:16:50 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(802, 668)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.TabbedLayout = QtGui.QTabWidget(self.centralwidget)
        self.TabbedLayout.setGeometry(QtCore.QRect(0, 90, 801, 491))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabbedLayout.sizePolicy().hasHeightForWidth())
        self.TabbedLayout.setSizePolicy(sizePolicy)
        self.TabbedLayout.setTabShape(QtGui.QTabWidget.Rounded)
        self.TabbedLayout.setObjectName(_fromUtf8("TabbedLayout"))
        self.tabCoreDetails = QtGui.QWidget()
        self.tabCoreDetails.setObjectName(_fromUtf8("tabCoreDetails"))
        self.framePlayerName = QtGui.QFrame(self.tabCoreDetails)
        self.framePlayerName.setGeometry(QtCore.QRect(10, 10, 421, 51))
        self.framePlayerName.setFrameShape(QtGui.QFrame.Box)
        self.framePlayerName.setFrameShadow(QtGui.QFrame.Raised)
        self.framePlayerName.setObjectName(_fromUtf8("framePlayerName"))
        self.lblPlayerName = QtGui.QLabel(self.framePlayerName)
        self.lblPlayerName.setGeometry(QtCore.QRect(10, 10, 131, 17))
        self.lblPlayerName.setScaledContents(False)
        self.lblPlayerName.setObjectName(_fromUtf8("lblPlayerName"))
        self.txtPlayerName = QtGui.QPlainTextEdit(self.framePlayerName)
        self.txtPlayerName.setGeometry(QtCore.QRect(150, 10, 181, 31))
        self.txtPlayerName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtPlayerName.setObjectName(_fromUtf8("txtPlayerName"))
        self.btnUsePlayerName = QtGui.QPushButton(self.framePlayerName)
        self.btnUsePlayerName.setGeometry(QtCore.QRect(340, 10, 71, 27))
        self.btnUsePlayerName.setObjectName(_fromUtf8("btnUsePlayerName"))
        self.frameHeroDetails = QtGui.QFrame(self.tabCoreDetails)
        self.frameHeroDetails.setGeometry(QtCore.QRect(10, 70, 421, 171))
        self.frameHeroDetails.setFrameShape(QtGui.QFrame.Box)
        self.frameHeroDetails.setFrameShadow(QtGui.QFrame.Raised)
        self.frameHeroDetails.setObjectName(_fromUtf8("frameHeroDetails"))
        self.lblHeroesName = QtGui.QLabel(self.frameHeroDetails)
        self.lblHeroesName.setGeometry(QtCore.QRect(10, 20, 91, 17))
        self.lblHeroesName.setObjectName(_fromUtf8("lblHeroesName"))
        self.txtHeroesName = QtGui.QPlainTextEdit(self.frameHeroDetails)
        self.txtHeroesName.setGeometry(QtCore.QRect(100, 10, 311, 31))
        self.txtHeroesName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtHeroesName.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.txtHeroesName.setObjectName(_fromUtf8("txtHeroesName"))
        self.checkBoxOP = QtGui.QCheckBox(self.frameHeroDetails)
        self.checkBoxOP.setGeometry(QtCore.QRect(110, 90, 88, 22))
        self.checkBoxOP.setObjectName(_fromUtf8("checkBoxOP"))
        self.lblOP = QtGui.QLabel(self.frameHeroDetails)
        self.lblOP.setGeometry(QtCore.QRect(10, 90, 81, 17))
        self.lblOP.setObjectName(_fromUtf8("lblOP"))
        self.lblSpeech = QtGui.QLabel(self.frameHeroDetails)
        self.lblSpeech.setGeometry(QtCore.QRect(10, 140, 101, 17))
        self.lblSpeech.setObjectName(_fromUtf8("lblSpeech"))
        self.txtSpeech = QtGui.QPlainTextEdit(self.frameHeroDetails)
        self.txtSpeech.setGeometry(QtCore.QRect(110, 130, 301, 31))
        self.txtSpeech.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtSpeech.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.txtSpeech.setObjectName(_fromUtf8("txtSpeech"))
        self.lblFancyName = QtGui.QLabel(self.frameHeroDetails)
        self.lblFancyName.setGeometry(QtCore.QRect(10, 50, 131, 31))
        self.lblFancyName.setWordWrap(True)
        self.lblFancyName.setObjectName(_fromUtf8("lblFancyName"))
        self.txtHeroesFancyName = QtGui.QPlainTextEdit(self.frameHeroDetails)
        self.txtHeroesFancyName.setGeometry(QtCore.QRect(140, 50, 271, 31))
        self.txtHeroesFancyName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtHeroesFancyName.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.txtHeroesFancyName.setObjectName(_fromUtf8("txtHeroesFancyName"))
        self.frame = QtGui.QFrame(self.tabCoreDetails)
        self.frame.setGeometry(QtCore.QRect(10, 260, 421, 181))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.lblTrails = QtGui.QLabel(self.frame)
        self.lblTrails.setGeometry(QtCore.QRect(10, 10, 101, 17))
        self.lblTrails.setObjectName(_fromUtf8("lblTrails"))
        self.listTrails = QtGui.QListWidget(self.frame)
        self.listTrails.setGeometry(QtCore.QRect(10, 30, 401, 141))
        self.listTrails.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listTrails.setAlternatingRowColors(True)
        self.listTrails.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listTrails.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.listTrails.setObjectName(_fromUtf8("listTrails"))
        self.framePowers = QtGui.QFrame(self.tabCoreDetails)
        self.framePowers.setGeometry(QtCore.QRect(440, 10, 351, 191))
        self.framePowers.setFrameShape(QtGui.QFrame.Panel)
        self.framePowers.setFrameShadow(QtGui.QFrame.Raised)
        self.framePowers.setObjectName(_fromUtf8("framePowers"))
        self.lblPowers = QtGui.QLabel(self.framePowers)
        self.lblPowers.setGeometry(QtCore.QRect(10, 10, 111, 17))
        self.lblPowers.setObjectName(_fromUtf8("lblPowers"))
        self.txtPowers = QtGui.QPlainTextEdit(self.framePowers)
        self.txtPowers.setGeometry(QtCore.QRect(10, 30, 331, 121))
        self.txtPowers.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.txtPowers.setBackgroundVisible(False)
        self.txtPowers.setObjectName(_fromUtf8("txtPowers"))
        self.btnLoadPowersExamples = QtGui.QPushButton(self.framePowers)
        self.btnLoadPowersExamples.setGeometry(QtCore.QRect(130, 160, 101, 27))
        self.btnLoadPowersExamples.setObjectName(_fromUtf8("btnLoadPowersExamples"))
        self.frameBuffs = QtGui.QFrame(self.tabCoreDetails)
        self.frameBuffs.setGeometry(QtCore.QRect(440, 210, 351, 231))
        self.frameBuffs.setFrameShape(QtGui.QFrame.Panel)
        self.frameBuffs.setFrameShadow(QtGui.QFrame.Raised)
        self.frameBuffs.setObjectName(_fromUtf8("frameBuffs"))
        self.lblBuffs = QtGui.QLabel(self.frameBuffs)
        self.lblBuffs.setGeometry(QtCore.QRect(10, 10, 101, 17))
        self.lblBuffs.setObjectName(_fromUtf8("lblBuffs"))
        self.txtBuffs = QtGui.QPlainTextEdit(self.frameBuffs)
        self.txtBuffs.setGeometry(QtCore.QRect(10, 30, 331, 161))
        self.txtBuffs.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.txtBuffs.setObjectName(_fromUtf8("txtBuffs"))
        self.btnLoadBuffsExample = QtGui.QPushButton(self.frameBuffs)
        self.btnLoadBuffsExample.setGeometry(QtCore.QRect(130, 200, 101, 27))
        self.btnLoadBuffsExample.setObjectName(_fromUtf8("btnLoadBuffsExample"))
        self.TabbedLayout.addTab(self.tabCoreDetails, _fromUtf8(""))
        self.tabPlayerDetails = QtGui.QWidget()
        self.tabPlayerDetails.setObjectName(_fromUtf8("tabPlayerDetails"))
        self.lblInfoPlayerName = QtGui.QLabel(self.tabPlayerDetails)
        self.lblInfoPlayerName.setGeometry(QtCore.QRect(20, 20, 101, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblInfoPlayerName.setFont(font)
        self.lblInfoPlayerName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.lblInfoPlayerName.setObjectName(_fromUtf8("lblInfoPlayerName"))
        self.lblInfoUUID = QtGui.QLabel(self.tabPlayerDetails)
        self.lblInfoUUID.setGeometry(QtCore.QRect(40, 70, 81, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblInfoUUID.setFont(font)
        self.lblInfoUUID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.lblInfoUUID.setObjectName(_fromUtf8("lblInfoUUID"))
        self.lblInfoSignature = QtGui.QLabel(self.tabPlayerDetails)
        self.lblInfoSignature.setGeometry(QtCore.QRect(20, 110, 101, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblInfoSignature.setFont(font)
        self.lblInfoSignature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.lblInfoSignature.setObjectName(_fromUtf8("lblInfoSignature"))
        self.lblInfoValue = QtGui.QLabel(self.tabPlayerDetails)
        self.lblInfoValue.setGeometry(QtCore.QRect(20, 230, 101, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblInfoValue.setFont(font)
        self.lblInfoValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.lblInfoValue.setObjectName(_fromUtf8("lblInfoValue"))
        self.txtInfoPlayerName = QtGui.QPlainTextEdit(self.tabPlayerDetails)
        self.txtInfoPlayerName.setGeometry(QtCore.QRect(140, 20, 211, 31))
        self.txtInfoPlayerName.setFrameShape(QtGui.QFrame.Box)
        self.txtInfoPlayerName.setFrameShadow(QtGui.QFrame.Sunken)
        self.txtInfoPlayerName.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtInfoPlayerName.setObjectName(_fromUtf8("txtInfoPlayerName"))
        self.txtInfoUUID = QtGui.QPlainTextEdit(self.tabPlayerDetails)
        self.txtInfoUUID.setGeometry(QtCore.QRect(140, 60, 641, 31))
        self.txtInfoUUID.setFrameShape(QtGui.QFrame.Box)
        self.txtInfoUUID.setFrameShadow(QtGui.QFrame.Sunken)
        self.txtInfoUUID.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtInfoUUID.setObjectName(_fromUtf8("txtInfoUUID"))
        self.txtInfoSignature = QtGui.QPlainTextEdit(self.tabPlayerDetails)
        self.txtInfoSignature.setGeometry(QtCore.QRect(140, 100, 641, 121))
        self.txtInfoSignature.setFrameShape(QtGui.QFrame.Box)
        self.txtInfoSignature.setFrameShadow(QtGui.QFrame.Sunken)
        self.txtInfoSignature.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtInfoSignature.setObjectName(_fromUtf8("txtInfoSignature"))
        self.txtInfoValue = QtGui.QPlainTextEdit(self.tabPlayerDetails)
        self.txtInfoValue.setGeometry(QtCore.QRect(140, 230, 641, 141))
        self.txtInfoValue.setFrameShape(QtGui.QFrame.Box)
        self.txtInfoValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.txtInfoValue.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtInfoValue.setObjectName(_fromUtf8("txtInfoValue"))
        self.TabbedLayout.addTab(self.tabPlayerDetails, _fromUtf8(""))
        self.tabColorCodes = QtGui.QWidget()
        self.tabColorCodes.setObjectName(_fromUtf8("tabColorCodes"))
        self.frameColorCodes = QtGui.QFrame(self.tabColorCodes)
        self.frameColorCodes.setGeometry(QtCore.QRect(10, 10, 461, 351))
        self.frameColorCodes.setFrameShape(QtGui.QFrame.Box)
        self.frameColorCodes.setFrameShadow(QtGui.QFrame.Sunken)
        self.frameColorCodes.setObjectName(_fromUtf8("frameColorCodes"))
        self.lblColorCodes = QtGui.QLabel(self.frameColorCodes)
        self.lblColorCodes.setGeometry(QtCore.QRect(20, 0, 431, 351))
        self.lblColorCodes.setFrameShape(QtGui.QFrame.NoFrame)
        self.lblColorCodes.setText(_fromUtf8(""))
        self.lblColorCodes.setPixmap(QtGui.QPixmap(_fromUtf8("images/colorcodes.jpg")))
        self.lblColorCodes.setObjectName(_fromUtf8("lblColorCodes"))
        self.lblColorCodes1 = QtGui.QFrame(self.tabColorCodes)
        self.lblColorCodes1.setGeometry(QtCore.QRect(480, 10, 301, 171))
        self.lblColorCodes1.setFrameShape(QtGui.QFrame.Box)
        self.lblColorCodes1.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblColorCodes1.setObjectName(_fromUtf8("lblColorCodes1"))
        self.lblBukkitCodeK = QtGui.QLabel(self.lblColorCodes1)
        self.lblBukkitCodeK.setGeometry(QtCore.QRect(100, 10, 121, 17))
        self.lblBukkitCodeK.setObjectName(_fromUtf8("lblBukkitCodeK"))
        self.lblBukkitCodeL = QtGui.QLabel(self.lblColorCodes1)
        self.lblBukkitCodeL.setGeometry(QtCore.QRect(100, 30, 111, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setBold(True)
        font.setWeight(75)
        self.lblBukkitCodeL.setFont(font)
        self.lblBukkitCodeL.setFrameShape(QtGui.QFrame.NoFrame)
        self.lblBukkitCodeL.setFrameShadow(QtGui.QFrame.Plain)
        self.lblBukkitCodeL.setTextFormat(QtCore.Qt.AutoText)
        self.lblBukkitCodeL.setObjectName(_fromUtf8("lblBukkitCodeL"))
        self.lblBukkitCodeM = QtGui.QLabel(self.lblColorCodes1)
        self.lblBukkitCodeM.setGeometry(QtCore.QRect(100, 50, 131, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setStrikeOut(True)
        self.lblBukkitCodeM.setFont(font)
        self.lblBukkitCodeM.setObjectName(_fromUtf8("lblBukkitCodeM"))
        self.lblBukkitCodeN = QtGui.QLabel(self.lblColorCodes1)
        self.lblBukkitCodeN.setGeometry(QtCore.QRect(100, 70, 121, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setUnderline(True)
        self.lblBukkitCodeN.setFont(font)
        self.lblBukkitCodeN.setObjectName(_fromUtf8("lblBukkitCodeN"))
        self.lblBukkitCodeO = QtGui.QLabel(self.lblColorCodes1)
        self.lblBukkitCodeO.setGeometry(QtCore.QRect(100, 90, 121, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setItalic(True)
        self.lblBukkitCodeO.setFont(font)
        self.lblBukkitCodeO.setObjectName(_fromUtf8("lblBukkitCodeO"))
        self.lblBukkitCodeR = QtGui.QLabel(self.lblColorCodes1)
        self.lblBukkitCodeR.setGeometry(QtCore.QRect(100, 140, 121, 17))
        self.lblBukkitCodeR.setObjectName(_fromUtf8("lblBukkitCodeR"))
        self.frameScratchPad = QtGui.QFrame(self.tabColorCodes)
        self.frameScratchPad.setGeometry(QtCore.QRect(10, 370, 781, 81))
        self.frameScratchPad.setFrameShape(QtGui.QFrame.Box)
        self.frameScratchPad.setFrameShadow(QtGui.QFrame.Sunken)
        self.frameScratchPad.setObjectName(_fromUtf8("frameScratchPad"))
        self.txtScratchPad = QtGui.QPlainTextEdit(self.frameScratchPad)
        self.txtScratchPad.setGeometry(QtCore.QRect(10, 40, 761, 31))
        self.txtScratchPad.setAutoFillBackground(False)
        self.txtScratchPad.setFrameShape(QtGui.QFrame.Box)
        self.txtScratchPad.setFrameShadow(QtGui.QFrame.Sunken)
        self.txtScratchPad.setObjectName(_fromUtf8("txtScratchPad"))
        self.lblScratchPad = QtGui.QLabel(self.frameScratchPad)
        self.lblScratchPad.setGeometry(QtCore.QRect(10, 10, 131, 17))
        self.lblScratchPad.setObjectName(_fromUtf8("lblScratchPad"))
        self.btnCloneToHeroName = QtGui.QPushButton(self.frameScratchPad)
        self.btnCloneToHeroName.setGeometry(QtCore.QRect(90, 10, 231, 27))
        self.btnCloneToHeroName.setObjectName(_fromUtf8("btnCloneToHeroName"))
        self.btnCloneToHeroesSpeech = QtGui.QPushButton(self.frameScratchPad)
        self.btnCloneToHeroesSpeech.setGeometry(QtCore.QRect(330, 10, 171, 27))
        self.btnCloneToHeroesSpeech.setObjectName(_fromUtf8("btnCloneToHeroesSpeech"))
        self.btnClearScratchPad = QtGui.QPushButton(self.frameScratchPad)
        self.btnClearScratchPad.setGeometry(QtCore.QRect(510, 10, 121, 27))
        self.btnClearScratchPad.setObjectName(_fromUtf8("btnClearScratchPad"))
        self.TabbedLayout.addTab(self.tabColorCodes, _fromUtf8(""))
        self.tabPermissions = QtGui.QWidget()
        self.tabPermissions.setObjectName(_fromUtf8("tabPermissions"))
        self.txtHeroPermissions = QtGui.QPlainTextEdit(self.tabPermissions)
        self.txtHeroPermissions.setGeometry(QtCore.QRect(10, 100, 391, 311))
        self.txtHeroPermissions.setObjectName(_fromUtf8("txtHeroPermissions"))
        self.lblHeroCustomPermissions = QtGui.QLabel(self.tabPermissions)
        self.lblHeroCustomPermissions.setGeometry(QtCore.QRect(10, 10, 191, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblHeroCustomPermissions.setFont(font)
        self.lblHeroCustomPermissions.setObjectName(_fromUtf8("lblHeroCustomPermissions"))
        self.lblAvailablePermissions = QtGui.QLabel(self.tabPermissions)
        self.lblAvailablePermissions.setGeometry(QtCore.QRect(410, 10, 161, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblAvailablePermissions.setFont(font)
        self.lblAvailablePermissions.setObjectName(_fromUtf8("lblAvailablePermissions"))
        self.lblCustomPermissionsHelp = QtGui.QLabel(self.tabPermissions)
        self.lblCustomPermissionsHelp.setGeometry(QtCore.QRect(10, 30, 381, 51))
        self.lblCustomPermissionsHelp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblCustomPermissionsHelp.setWordWrap(True)
        self.lblCustomPermissionsHelp.setObjectName(_fromUtf8("lblCustomPermissionsHelp"))
        self.lblAvailablePermissionsHelp = QtGui.QLabel(self.tabPermissions)
        self.lblAvailablePermissionsHelp.setGeometry(QtCore.QRect(410, 30, 371, 51))
        self.lblAvailablePermissionsHelp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblAvailablePermissionsHelp.setWordWrap(True)
        self.lblAvailablePermissionsHelp.setObjectName(_fromUtf8("lblAvailablePermissionsHelp"))
        self.lblPermissionsInfo = QtGui.QLabel(self.tabPermissions)
        self.lblPermissionsInfo.setGeometry(QtCore.QRect(10, 420, 771, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lblPermissionsInfo.setFont(font)
        self.lblPermissionsInfo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblPermissionsInfo.setWordWrap(True)
        self.lblPermissionsInfo.setObjectName(_fromUtf8("lblPermissionsInfo"))
        self.listPermissions = QtGui.QListWidget(self.tabPermissions)
        self.listPermissions.setGeometry(QtCore.QRect(410, 100, 371, 311))
        self.listPermissions.setAlternatingRowColors(True)
        self.listPermissions.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listPermissions.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.listPermissions.setObjectName(_fromUtf8("listPermissions"))
        self.TabbedLayout.addTab(self.tabPermissions, _fromUtf8(""))
        self.tabEnchantments = QtGui.QWidget()
        self.tabEnchantments.setObjectName(_fromUtf8("tabEnchantments"))
        self.txtEnchantments = QtGui.QPlainTextEdit(self.tabEnchantments)
        self.txtEnchantments.setGeometry(QtCore.QRect(10, 10, 781, 441))
        self.txtEnchantments.setObjectName(_fromUtf8("txtEnchantments"))
        self.TabbedLayout.addTab(self.tabEnchantments, _fromUtf8(""))
        self.tabEffects = QtGui.QWidget()
        self.tabEffects.setObjectName(_fromUtf8("tabEffects"))
        self.txtEffects = QtGui.QPlainTextEdit(self.tabEffects)
        self.txtEffects.setGeometry(QtCore.QRect(10, 10, 781, 441))
        self.txtEffects.setObjectName(_fromUtf8("txtEffects"))
        self.TabbedLayout.addTab(self.tabEffects, _fromUtf8(""))
        self.tabBlockIDs = QtGui.QWidget()
        self.tabBlockIDs.setObjectName(_fromUtf8("tabBlockIDs"))
        self.txtBlocks = QtGui.QPlainTextEdit(self.tabBlockIDs)
        self.txtBlocks.setGeometry(QtCore.QRect(10, 10, 781, 441))
        self.txtBlocks.setObjectName(_fromUtf8("txtBlocks"))
        self.TabbedLayout.addTab(self.tabBlockIDs, _fromUtf8(""))
        self.tabBuild = QtGui.QWidget()
        self.tabBuild.setObjectName(_fromUtf8("tabBuild"))
        self.picBuild = QtGui.QLabel(self.tabBuild)
        self.picBuild.setGeometry(QtCore.QRect(530, 0, 261, 291))
        self.picBuild.setText(_fromUtf8(""))
        self.picBuild.setPixmap(QtGui.QPixmap(_fromUtf8("images/build.png")))
        self.picBuild.setScaledContents(False)
        self.picBuild.setObjectName(_fromUtf8("picBuild"))
        self.btnCreate = QtGui.QPushButton(self.tabBuild)
        self.btnCreate.setGeometry(QtCore.QRect(160, 120, 261, 81))
        self.btnCreate.setObjectName(_fromUtf8("btnCreate"))
        self.progressBar = QtGui.QProgressBar(self.tabBuild)
        self.progressBar.setGeometry(QtCore.QRect(160, 220, 261, 23))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.TabbedLayout.addTab(self.tabBuild, _fromUtf8(""))
        self.picIcon = QtGui.QLabel(self.centralwidget)
        self.picIcon.setGeometry(QtCore.QRect(700, -10, 101, 131))
        self.picIcon.setText(_fromUtf8(""))
        self.picIcon.setPixmap(QtGui.QPixmap(_fromUtf8("images/icon.png")))
        self.picIcon.setObjectName(_fromUtf8("picIcon"))
        self.txtStatus = QtGui.QPlainTextEdit(self.centralwidget)
        self.txtStatus.setGeometry(QtCore.QRect(10, 590, 781, 71))
        self.txtStatus.setFrameShape(QtGui.QFrame.Box)
        self.txtStatus.setFrameShadow(QtGui.QFrame.Plain)
        self.txtStatus.setLineWidth(1)
        self.txtStatus.setMidLineWidth(0)
        self.txtStatus.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.txtStatus.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtStatus.setBackgroundVisible(False)
        self.txtStatus.setObjectName(_fromUtf8("txtStatus"))
        self.lblHeroBuddy = QtGui.QLabel(self.centralwidget)
        self.lblHeroBuddy.setGeometry(QtCore.QRect(20, 20, 661, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lblHeroBuddy.setFont(font)
        self.lblHeroBuddy.setObjectName(_fromUtf8("lblHeroBuddy"))
        self.lblMalonsServer = QtGui.QLabel(self.centralwidget)
        self.lblMalonsServer.setGeometry(QtCore.QRect(440, 60, 191, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblMalonsServer.setFont(font)
        self.lblMalonsServer.setObjectName(_fromUtf8("lblMalonsServer"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.TabbedLayout.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtPlayerName, self.btnUsePlayerName)
        MainWindow.setTabOrder(self.btnUsePlayerName, self.txtHeroesName)
        MainWindow.setTabOrder(self.txtHeroesName, self.txtHeroesFancyName)
        MainWindow.setTabOrder(self.txtHeroesFancyName, self.checkBoxOP)
        MainWindow.setTabOrder(self.checkBoxOP, self.txtSpeech)
        MainWindow.setTabOrder(self.txtSpeech, self.listTrails)
        MainWindow.setTabOrder(self.listTrails, self.txtPowers)
        MainWindow.setTabOrder(self.txtPowers, self.btnLoadPowersExamples)
        MainWindow.setTabOrder(self.btnLoadPowersExamples, self.txtBuffs)
        MainWindow.setTabOrder(self.txtBuffs, self.btnLoadBuffsExample)
        MainWindow.setTabOrder(self.btnLoadBuffsExample, self.txtInfoPlayerName)
        MainWindow.setTabOrder(self.txtInfoPlayerName, self.txtInfoUUID)
        MainWindow.setTabOrder(self.txtInfoUUID, self.txtInfoSignature)
        MainWindow.setTabOrder(self.txtInfoSignature, self.txtInfoValue)
        MainWindow.setTabOrder(self.txtInfoValue, self.txtScratchPad)
        MainWindow.setTabOrder(self.txtScratchPad, self.btnCloneToHeroName)
        MainWindow.setTabOrder(self.btnCloneToHeroName, self.btnCloneToHeroesSpeech)
        MainWindow.setTabOrder(self.btnCloneToHeroesSpeech, self.btnClearScratchPad)
        MainWindow.setTabOrder(self.btnClearScratchPad, self.txtHeroPermissions)
        MainWindow.setTabOrder(self.txtHeroPermissions, self.listPermissions)
        MainWindow.setTabOrder(self.listPermissions, self.txtEnchantments)
        MainWindow.setTabOrder(self.txtEnchantments, self.txtEffects)
        MainWindow.setTabOrder(self.txtEffects, self.txtBlocks)
        MainWindow.setTabOrder(self.txtBlocks, self.btnCreate)
        MainWindow.setTabOrder(self.btnCreate, self.TabbedLayout)
        MainWindow.setTabOrder(self.TabbedLayout, self.txtStatus)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Hero Buddy 1.0", None))
        self.lblPlayerName.setText(_translate("MainWindow", "Minecraft Player Name:", None))
        self.txtPlayerName.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter the Player Name you use in Minecraft</p></body></html>", None))
        self.btnUsePlayerName.setText(_translate("MainWindow", "use", None))
        self.lblHeroesName.setText(_translate("MainWindow", "Heroes Name:", None))
        self.txtHeroesName.setToolTip(_translate("MainWindow", "<html><head/><body><p>What is the name of your Hero going to be? Don\'t include spaces. </p></body></html>", None))
        self.checkBoxOP.setToolTip(_translate("MainWindow", "<html><head/><body><p>Set to True if your Hero requires OP. Generally if your hero is Invincible or uses features like Creative Mode.</p></body></html>", None))
        self.checkBoxOP.setText(_translate("MainWindow", "True", None))
        self.lblOP.setText(_translate("MainWindow", "Is Hero OP?", None))
        self.lblSpeech.setText(_translate("MainWindow", "Heroes Speech:", None))
        self.txtSpeech.setToolTip(_translate("MainWindow", "<html><head/><body><p>This is what your Hero says when using the command /buff. Usually your characters famous tag line.</p></body></html>", None))
        self.lblFancyName.setText(_translate("MainWindow", "Heroes Fancy Name:", None))
        self.txtHeroesFancyName.setToolTip(_translate("MainWindow", "<html><head/><body><p>How will the name of your Hero appear in-game such as chat? You can use color codes to format the name, and you can use spaces.</p></body></html>", None))
        self.lblTrails.setText(_translate("MainWindow", "Trails:", None))
        self.listTrails.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select the Trail Permissions that your Super Hero will have access too. Example: Smoke, Wings, etc.</p></body></html>", None))
        self.listTrails.setSortingEnabled(False)
        self.lblPowers.setText(_translate("MainWindow", "Powers:", None))
        self.txtPowers.setToolTip(_translate("MainWindow", "<html><head/><body><p>This is the list of powers that are displayed for your hero when the player types the command /powers</p></body></html>", None))
        self.btnLoadPowersExamples.setText(_translate("MainWindow", "Load Example", None))
        self.lblBuffs.setText(_translate("MainWindow", "Buffs:", None))
        self.txtBuffs.setToolTip(_translate("MainWindow", "<html><head/><body><p>This section gives the players special effects and/or items. See examples</p></body></html>", None))
        self.btnLoadBuffsExample.setText(_translate("MainWindow", "Load Example", None))
        self.TabbedLayout.setTabText(self.TabbedLayout.indexOf(self.tabCoreDetails), _translate("MainWindow", "Core Details", None))
        self.lblInfoPlayerName.setText(_translate("MainWindow", "Player Name:", None))
        self.lblInfoUUID.setText(_translate("MainWindow", "UUID:", None))
        self.lblInfoSignature.setText(_translate("MainWindow", "Signature:", None))
        self.lblInfoValue.setText(_translate("MainWindow", "Value:", None))
        self.TabbedLayout.setTabText(self.TabbedLayout.indexOf(self.tabPlayerDetails), _translate("MainWindow", "Your Player Info", None))
        self.lblBukkitCodeK.setText(_translate("MainWindow", "&k Obfuscated", None))
        self.lblBukkitCodeL.setText(_translate("MainWindow", "&l Bold", None))
        self.lblBukkitCodeM.setText(_translate("MainWindow", "&m Strikethrough", None))
        self.lblBukkitCodeN.setText(_translate("MainWindow", "&n Underline", None))
        self.lblBukkitCodeO.setText(_translate("MainWindow", "&o Italic", None))
        self.lblBukkitCodeR.setText(_translate("MainWindow", "&r Reset", None))
        self.lblScratchPad.setText(_translate("MainWindow", "Scratch Pad:", None))
        self.btnCloneToHeroName.setText(_translate("MainWindow", "Clone as Heroes Fancy Name", None))
        self.btnCloneToHeroesSpeech.setText(_translate("MainWindow", "Clone as Heroes Speech", None))
        self.btnClearScratchPad.setText(_translate("MainWindow", "Clear", None))
        self.TabbedLayout.setTabText(self.TabbedLayout.indexOf(self.tabColorCodes), _translate("MainWindow", "Color Codes", None))
        self.txtHeroPermissions.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter the permissions that your hero will have. Use one permission per line. To take away a permission for your hero, use a hypen before the permission name such as -permission.name</p></body></html>", None))
        self.lblHeroCustomPermissions.setText(_translate("MainWindow", "Custom Permissions:", None))
        self.lblAvailablePermissions.setText(_translate("MainWindow", "Available Permissions:", None))
        self.lblCustomPermissionsHelp.setText(_translate("MainWindow", "Write your own permissions in the box below. One for each line. Use a hyphen \'-\' to disable a permission. Used for things such as fall damage.", None))
        self.lblAvailablePermissionsHelp.setText(_translate("MainWindow", "Select which permissions you\'d like to use from the existing ones available to you. If you need to modify a permission then manually type out the permission in the left box.", None))
        self.lblPermissionsInfo.setText(_translate("MainWindow", "When you create your hero using the \'Build\' tab; both the permissions you have manually entered in the Custom Permissions box and the Permissions you have selected in the Available Permissions box will be added to your hero.", None))
        self.listPermissions.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select which permissions you\'d like your Super Hero to have. You can select multiple permissions.</p></body></html>", None))
        self.TabbedLayout.setTabText(self.TabbedLayout.indexOf(self.tabPermissions), _translate("MainWindow", "Hero Permissions", None))
        self.TabbedLayout.setTabText(self.TabbedLayout.indexOf(self.tabEnchantments), _translate("MainWindow", "Enchantments", None))
        self.TabbedLayout.setTabText(self.TabbedLayout.indexOf(self.tabEffects), _translate("MainWindow", "Effects", None))
        self.TabbedLayout.setTabText(self.TabbedLayout.indexOf(self.tabBlockIDs), _translate("MainWindow", "Block && Item ID\'s", None))
        self.btnCreate.setToolTip(_translate("MainWindow", "<html><head/><body><p>Used to create your hero and generate the neccassary files when you are finished.</p></body></html>", None))
        self.btnCreate.setText(_translate("MainWindow", "Create Hero Files", None))
        self.TabbedLayout.setTabText(self.TabbedLayout.indexOf(self.tabBuild), _translate("MainWindow", "Build", None))
        self.lblHeroBuddy.setText(_translate("MainWindow", "Hero Buddy", None))
        self.lblMalonsServer.setText(_translate("MainWindow", "Malons Server", None))

