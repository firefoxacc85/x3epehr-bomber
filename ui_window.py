# Github : https://github.com/Bllare

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGroupBox, QHBoxLayout,
    QLCDNumber, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_SmsBomberMainWindow(object):
    def setupUi(self, SmsBomberMainWindow):
        if not SmsBomberMainWindow.objectName():
            SmsBomberMainWindow.setObjectName(u"SmsBomberMainWindow")
        SmsBomberMainWindow.resize(800, 450)
        SmsBomberMainWindow.setMinimumSize(QSize(800, 450))
        SmsBomberMainWindow.setStyleSheet(u"/* =========================\n"
"   Main Window Styling\n"
"   ========================= */\n"
"QMainWindow {\n"
"    background-color: #2d3748;\n"
"}\n"
"\n"
"/* =========================\n"
"   Global Widget Styling\n"
"   ========================= */\n"
"QWidget {\n"
"    background-color: #2d3748;\n"
"    color: #f8f9fa;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"\n"
"/* =========================\n"
"   Push Buttons\n"
"   ========================= */\n"
"QPushButton {\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357abd;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2c5d9e;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #4a5568;\n"
"    color: #a0aec0;\n"
"}\n"
"\n"
"/* =========================\n"
"   Plain Text Edit\n"
"   ========================= */\n"
"QPlainTextEdit {\n"
"    background-color: #1a202c;\n"
"    color: #e2e8f0;\n"
"    border: 2px solid #4a5568;\n"
"    border-radius: 8px;\n"
"    paddi"
                        "ng: 8px;\n"
"    font-family: \"Consolas\", monospace;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #4a90e2;\n"
"}\n"
"\n"
"/* =========================\n"
"   Labels\n"
"   ========================= */\n"
"QLabel {\n"
"    color: #e2e8f0;\n"
"    background: transparent;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* =========================\n"
"   Line Edit\n"
"   ========================= */\n"
"QLineEdit {\n"
"    background-color: #2d3748;\n"
"    border: 2px solid #4a5568;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90e2;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #a0aec0;\n"
"}\n"
"\n"
"/* =========================\n"
"   Combo Box\n"
"   ========================= */\n"
"QComboBox {\n"
"    background-color: #4a5568;\n"
"    color: white;\n"
"    border: 2px solid transparent;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"    font-size: 13px;\n"
"}\n"
""
                        "\n"
"QComboBox:hover {\n"
"    background-color: #2d3748;\n"
"    border-color: #4a90e2;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/Icons/downArrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2d3748;\n"
"    color: white;\n"
"    border: 2px solid #4a5568;\n"
"    selection-background-color: #4a90e2;\n"
"}\n"
"\n"
"/* =========================\n"
"   Spin Boxes\n"
"   ========================= */\n"
"QDoubleSpinBox, QSpinBox {\n"
"    background-color: #4a5568;\n"
"    color: white;\n"
"    border: 2px solid transparent;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QDoubleSpinBox:hover, QSpinBox:hover {\n"
"    background-color: #2d3748;\n"
"    border-color: #4a90e2;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button,\n"
"QDoubleSpinBox::down-button {\n"
"    width: 18px;\n"
"}\n"
"\n"
"/* =========================\n"
"   C"
                        "heck Box\n"
"   ========================= */\n"
"QCheckBox {\n"
"    color: #e2e8f0;\n"
"    spacing: 8px;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 2px solid #4a5568;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #4a90e2;\n"
"    border-color: #4a90e2;\n"
"    image: url(:/Icons/checkmark.png);\n"
"}\n"
"\n"
"/* =========================\n"
"   List Widget\n"
"   ========================= */\n"
"QListWidget {\n"
"    background-color: #2d3748;\n"
"    border: 2px solid #4a5568;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: #4a5568;\n"
"    color: #e2e8f0;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    margin: 3px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #4a90e2;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QListWidget::item:hover:!selected {\n"
"    background-color: #5a6578;"
                        "\n"
"}\n"
"\n"
"/* =========================\n"
"   Horizontal Separator (HLine)\n"
"   ========================= */\n"
"QFrame[frameShape=\"4\"] {\n"
"    background-color: #4a5568;\n"
"}\n"
"\n"
"/* =========================\n"
"   LCD Number\n"
"   ========================= */\n"
"QLCDNumber {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* =========================\n"
"   Dynamic Status Colors\n"
"   ========================= */\n"
"QLabel[status=\"success\"] { color: #48bb78; }\n"
"QLabel[status=\"warning\"] { color: #ed8936; }\n"
"QLabel[status=\"error\"]   { color: #f56565; }\n"
"QLabel[status=\"info\"]    { color: #4299e1; }\n"
"\n"
"/* =========================\n"
"   Card Containers\n"
"   ========================= */\n"
"QWidget[card=\"true\"] {\n"
"    background-color: #2d3748;\n"
"    border: 2px solid #4a5568;\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QWidget[statsPanel=\"true\"] {\n"
"    background-color: #1a202c;\n"
"    border-radius: 10px;\n"
""
                        "    border: 2px solid #4a5568;\n"
"}\n"
"")
        self.centralWidget = QWidget(SmsBomberMainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.mainLayout = QHBoxLayout(self.centralWidget)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.logTextEdit = QPlainTextEdit(self.centralWidget)
        self.logTextEdit.setObjectName(u"logTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logTextEdit.sizePolicy().hasHeightForWidth())
        self.logTextEdit.setSizePolicy(sizePolicy)
        self.logTextEdit.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(8)
        self.logTextEdit.setFont(font)
        self.logTextEdit.setReadOnly(True)

        self.mainLayout.addWidget(self.logTextEdit)

        self.rightPanelLayout = QVBoxLayout()
        self.rightPanelLayout.setSpacing(15)
        self.rightPanelLayout.setObjectName(u"rightPanelLayout")
        self.contentLayout = QHBoxLayout()
        self.contentLayout.setSpacing(15)
        self.contentLayout.setObjectName(u"contentLayout")
        self.mainStackedWidget = QStackedWidget(self.centralWidget)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.mainStackedWidget.sizePolicy().hasHeightForWidth())
        self.mainStackedWidget.setSizePolicy(sizePolicy1)
        self.mainStackedWidget.setMinimumSize(QSize(0, 0))
        self.mainStackedWidget.setFrameShadow(QFrame.Plain)
        self.mainStackedWidget.setLineWidth(1)
        self.generalPage = QWidget()
        self.generalPage.setObjectName(u"generalPage")
        self.generalLayout = QVBoxLayout(self.generalPage)
        self.generalLayout.setSpacing(15)
        self.generalLayout.setObjectName(u"generalLayout")
        self.savedNumbersLayout = QHBoxLayout()
        self.savedNumbersLayout.setSpacing(10)
        self.savedNumbersLayout.setObjectName(u"savedNumbersLayout")
        self.savedNumbersComboBox = QComboBox(self.generalPage)
        self.savedNumbersComboBox.setObjectName(u"savedNumbersComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.savedNumbersComboBox.sizePolicy().hasHeightForWidth())
        self.savedNumbersComboBox.setSizePolicy(sizePolicy2)
        self.savedNumbersComboBox.setMinimumSize(QSize(0, 0))
        self.savedNumbersComboBox.setLayoutDirection(Qt.LeftToRight)
        self.savedNumbersComboBox.setAutoFillBackground(False)
        self.savedNumbersComboBox.setEditable(False)

        self.savedNumbersLayout.addWidget(self.savedNumbersComboBox)

        self.savedNumbersLabel = QLabel(self.generalPage)
        self.savedNumbersLabel.setObjectName(u"savedNumbersLabel")
        self.savedNumbersLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.savedNumbersLayout.addWidget(self.savedNumbersLabel)


        self.generalLayout.addLayout(self.savedNumbersLayout)

        self.generalSeparator = QFrame(self.generalPage)
        self.generalSeparator.setObjectName(u"generalSeparator")
        self.generalSeparator.setFrameShape(QFrame.Shape.HLine)
        self.generalSeparator.setFrameShadow(QFrame.Shadow.Sunken)

        self.generalLayout.addWidget(self.generalSeparator)

        self.targetNumberLayout = QHBoxLayout()
        self.targetNumberLayout.setSpacing(10)
        self.targetNumberLayout.setObjectName(u"targetNumberLayout")
        self.targetNumberLineEdit = QLineEdit(self.generalPage)
        self.targetNumberLineEdit.setObjectName(u"targetNumberLineEdit")
        sizePolicy2.setHeightForWidth(self.targetNumberLineEdit.sizePolicy().hasHeightForWidth())
        self.targetNumberLineEdit.setSizePolicy(sizePolicy2)
        self.targetNumberLineEdit.setMinimumSize(QSize(0, 0))

        self.targetNumberLayout.addWidget(self.targetNumberLineEdit)

        self.targetNumberLabel = QLabel(self.generalPage)
        self.targetNumberLabel.setObjectName(u"targetNumberLabel")
        self.targetNumberLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.targetNumberLayout.addWidget(self.targetNumberLabel)


        self.generalLayout.addLayout(self.targetNumberLayout)

        self.controlButtonsLayout = QHBoxLayout()
        self.controlButtonsLayout.setSpacing(20)
        self.controlButtonsLayout.setObjectName(u"controlButtonsLayout")
        self.stopButton = QPushButton(self.generalPage)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setMinimumSize(QSize(0, 0))
        self.stopButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #e53e3e;\n"
"    font-size: 14px;\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c53030;\n"
"}")

        self.controlButtonsLayout.addWidget(self.stopButton)

        self.startButton = QPushButton(self.generalPage)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(0, 0))
        self.startButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #38a169;\n"
"    font-size: 14px;\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2f855a;\n"
"}")

        self.controlButtonsLayout.addWidget(self.startButton)


        self.generalLayout.addLayout(self.controlButtonsLayout)

        self.generalVerticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.generalLayout.addItem(self.generalVerticalSpacer)

        self.warningLabel = QLabel(self.generalPage)
        self.warningLabel.setObjectName(u"warningLabel")
        self.warningLabel.setMinimumSize(QSize(0, 0))
        self.warningLabel.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setItalic(False)
        font1.setUnderline(False)
        self.warningLabel.setFont(font1)
        self.warningLabel.setStyleSheet(u"")
        self.warningLabel.setFrameShape(QFrame.NoFrame)
        self.warningLabel.setTextFormat(Qt.AutoText)
        self.warningLabel.setScaledContents(False)
        self.warningLabel.setAlignment(Qt.AlignCenter)
        self.warningLabel.setWordWrap(False)
        self.warningLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.generalLayout.addWidget(self.warningLabel)

        self.mainStackedWidget.addWidget(self.generalPage)
        self.savePage = QWidget()
        self.savePage.setObjectName(u"savePage")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.savePage.sizePolicy().hasHeightForWidth())
        self.savePage.setSizePolicy(sizePolicy3)
        self.saveLayout = QVBoxLayout(self.savePage)
        self.saveLayout.setSpacing(5)
        self.saveLayout.setObjectName(u"saveLayout")
        self.saveLayout.setContentsMargins(-1, -1, 0, -1)
        self.saveSectionTitle = QLabel(self.savePage)
        self.saveSectionTitle.setObjectName(u"saveSectionTitle")
        self.saveSectionTitle.setStyleSheet(u"font-size: 16px; font-weight: bold; color: #4a90e2;")
        self.saveSectionTitle.setAlignment(Qt.AlignCenter)

        self.saveLayout.addWidget(self.saveSectionTitle)

        self.saveNameLayout = QHBoxLayout()
        self.saveNameLayout.setSpacing(10)
        self.saveNameLayout.setObjectName(u"saveNameLayout")
        self.saveNameLayout.setContentsMargins(-1, -1, -1, 5)
        self.saveNameLineEdit = QLineEdit(self.savePage)
        self.saveNameLineEdit.setObjectName(u"saveNameLineEdit")
        sizePolicy2.setHeightForWidth(self.saveNameLineEdit.sizePolicy().hasHeightForWidth())
        self.saveNameLineEdit.setSizePolicy(sizePolicy2)
        self.saveNameLineEdit.setMinimumSize(QSize(0, 0))

        self.saveNameLayout.addWidget(self.saveNameLineEdit)

        self.saveNameLabel = QLabel(self.savePage)
        self.saveNameLabel.setObjectName(u"saveNameLabel")

        self.saveNameLayout.addWidget(self.saveNameLabel)


        self.saveLayout.addLayout(self.saveNameLayout)

        self.saveNumberLayout = QHBoxLayout()
        self.saveNumberLayout.setSpacing(10)
        self.saveNumberLayout.setObjectName(u"saveNumberLayout")
        self.saveNumberLineEdit = QLineEdit(self.savePage)
        self.saveNumberLineEdit.setObjectName(u"saveNumberLineEdit")
        sizePolicy2.setHeightForWidth(self.saveNumberLineEdit.sizePolicy().hasHeightForWidth())
        self.saveNumberLineEdit.setSizePolicy(sizePolicy2)
        self.saveNumberLineEdit.setMinimumSize(QSize(0, 0))

        self.saveNumberLayout.addWidget(self.saveNumberLineEdit)

        self.saveNumberLabel = QLabel(self.savePage)
        self.saveNumberLabel.setObjectName(u"saveNumberLabel")

        self.saveNumberLayout.addWidget(self.saveNumberLabel)


        self.saveLayout.addLayout(self.saveNumberLayout)

        self.saveButton = QPushButton(self.savePage)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(0, 0))
        self.saveButton.setSizeIncrement(QSize(0, 0))
        self.saveButton.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        font2.setBold(True)
        self.saveButton.setFont(font2)
        self.saveButton.setAutoFillBackground(False)
        self.saveButton.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(74, 144, 226);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(63, 124, 194);\n"
"}\n"
"")

        self.saveLayout.addWidget(self.saveButton)

        self.saveSeparator = QFrame(self.savePage)
        self.saveSeparator.setObjectName(u"saveSeparator")
        self.saveSeparator.setFrameShape(QFrame.Shape.HLine)
        self.saveSeparator.setFrameShadow(QFrame.Shadow.Sunken)

        self.saveLayout.addWidget(self.saveSeparator)

        self.deleteSectionTitle = QLabel(self.savePage)
        self.deleteSectionTitle.setObjectName(u"deleteSectionTitle")
        self.deleteSectionTitle.setStyleSheet(u"font-size: 16px; font-weight: bold; color: #e53e3e;")
        self.deleteSectionTitle.setLineWidth(1)
        self.deleteSectionTitle.setAlignment(Qt.AlignCenter)

        self.saveLayout.addWidget(self.deleteSectionTitle)

        self.deleteLayout = QHBoxLayout()
        self.deleteLayout.setSpacing(10)
        self.deleteLayout.setObjectName(u"deleteLayout")
        self.deleteComboBox = QComboBox(self.savePage)
        self.deleteComboBox.setObjectName(u"deleteComboBox")
        sizePolicy2.setHeightForWidth(self.deleteComboBox.sizePolicy().hasHeightForWidth())
        self.deleteComboBox.setSizePolicy(sizePolicy2)
        self.deleteComboBox.setMinimumSize(QSize(0, 0))

        self.deleteLayout.addWidget(self.deleteComboBox)

        self.deleteLabel = QLabel(self.savePage)
        self.deleteLabel.setObjectName(u"deleteLabel")

        self.deleteLayout.addWidget(self.deleteLabel)


        self.saveLayout.addLayout(self.deleteLayout)

        self.deleteButton = QPushButton(self.savePage)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMinimumSize(QSize(0, 0))
        self.deleteButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #e53e3e;\n"
"    padding: 10px 30px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c53030;\n"
"}")

        self.saveLayout.addWidget(self.deleteButton)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.saveLayout.addItem(self.verticalSpacer)

        self.mainStackedWidget.addWidget(self.savePage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.settingsPage.setMinimumSize(QSize(0, 0))
        self.settingsLayout = QVBoxLayout(self.settingsPage)
        self.settingsLayout.setSpacing(0)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.settingsLayout.setContentsMargins(-1, 0, -1, 0)
        self.settingsTitle = QLabel(self.settingsPage)
        self.settingsTitle.setObjectName(u"settingsTitle")
        self.settingsTitle.setStyleSheet(u"font-size: 18px; font-weight: bold; color: #4a90e2; padding-bottom: 10px;")
        self.settingsTitle.setAlignment(Qt.AlignCenter)

        self.settingsLayout.addWidget(self.settingsTitle)

        self.smsGroupBox = QGroupBox(self.settingsPage)
        self.smsGroupBox.setObjectName(u"smsGroupBox")
        self.smsGroupBox.setMinimumSize(QSize(0, 0))
        self.smsSettingsLayout = QVBoxLayout(self.smsGroupBox)
        self.smsSettingsLayout.setSpacing(10)
        self.smsSettingsLayout.setObjectName(u"smsSettingsLayout")
        self.smsDelayLayout = QHBoxLayout()
        self.smsDelayLayout.setObjectName(u"smsDelayLayout")
        self.smsDelaySpinBox = QDoubleSpinBox(self.smsGroupBox)
        self.smsDelaySpinBox.setObjectName(u"smsDelaySpinBox")
        self.smsDelaySpinBox.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setKerning(True)
        self.smsDelaySpinBox.setFont(font3)
        self.smsDelaySpinBox.setWrapping(False)
        self.smsDelaySpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.smsDelaySpinBox.setAccelerated(False)
        self.smsDelaySpinBox.setProperty(u"showGroupSeparator", False)
        self.smsDelaySpinBox.setDecimals(2)
        self.smsDelaySpinBox.setMinimum(0.100000000000000)
        self.smsDelaySpinBox.setMaximum(99999999.000000000000000)
        self.smsDelaySpinBox.setValue(1.500000000000000)

        self.smsDelayLayout.addWidget(self.smsDelaySpinBox)

        self.smsDelayLabel = QLabel(self.smsGroupBox)
        self.smsDelayLabel.setObjectName(u"smsDelayLabel")

        self.smsDelayLayout.addWidget(self.smsDelayLabel)


        self.smsSettingsLayout.addLayout(self.smsDelayLayout)


        self.settingsLayout.addWidget(self.smsGroupBox)

        self.generalSettingsGroupBox = QGroupBox(self.settingsPage)
        self.generalSettingsGroupBox.setObjectName(u"generalSettingsGroupBox")
        self.generalSettingsGroupBox.setFlat(False)
        self.generalSettingsLayout = QVBoxLayout(self.generalSettingsGroupBox)
        self.generalSettingsLayout.setSpacing(3)
        self.generalSettingsLayout.setObjectName(u"generalSettingsLayout")
        self.generalSettingsLayout.setContentsMargins(-1, 0, -1, -1)
        self.loopDelayLayout = QHBoxLayout()
        self.loopDelayLayout.setObjectName(u"loopDelayLayout")
        self.loopDelaySpinBox = QDoubleSpinBox(self.generalSettingsGroupBox)
        self.loopDelaySpinBox.setObjectName(u"loopDelaySpinBox")
        self.loopDelaySpinBox.setMinimumSize(QSize(0, 0))
        self.loopDelaySpinBox.setMinimum(1.000000000000000)
        self.loopDelaySpinBox.setMaximum(99999999.000000000000000)
        self.loopDelaySpinBox.setValue(60.000000000000000)

        self.loopDelayLayout.addWidget(self.loopDelaySpinBox)

        self.loopDelayLabel = QLabel(self.generalSettingsGroupBox)
        self.loopDelayLabel.setObjectName(u"loopDelayLabel")

        self.loopDelayLayout.addWidget(self.loopDelayLabel)


        self.generalSettingsLayout.addLayout(self.loopDelayLayout)

        self.featuresLayout = QHBoxLayout()
        self.featuresLayout.setObjectName(u"featuresLayout")
        self.callCheckBox = QCheckBox(self.generalSettingsGroupBox)
        self.callCheckBox.setObjectName(u"callCheckBox")
        self.callCheckBox.setEnabled(False)
        self.callCheckBox.setLayoutDirection(Qt.RightToLeft)

        self.featuresLayout.addWidget(self.callCheckBox)

        self.smsCheckBox = QCheckBox(self.generalSettingsGroupBox)
        self.smsCheckBox.setObjectName(u"smsCheckBox")
        self.smsCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.smsCheckBox.setAutoFillBackground(False)
        self.smsCheckBox.setChecked(True)

        self.featuresLayout.addWidget(self.smsCheckBox)


        self.generalSettingsLayout.addLayout(self.featuresLayout)


        self.settingsLayout.addWidget(self.generalSettingsGroupBox)

        self.saveSettingsButton = QPushButton(self.settingsPage)
        self.saveSettingsButton.setObjectName(u"saveSettingsButton")
        self.saveSettingsButton.setMinimumSize(QSize(0, 0))
        self.saveSettingsButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #38a169;\n"
"    font-size: 14px;\n"
"    padding: 12px 40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2f855a;\n"
"}")

        self.settingsLayout.addWidget(self.saveSettingsButton)

        self.settingsVerticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.settingsLayout.addItem(self.settingsVerticalSpacer)

        self.mainStackedWidget.addWidget(self.settingsPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.aboutLayout = QVBoxLayout(self.aboutPage)
        self.aboutLayout.setSpacing(10)
        self.aboutLayout.setObjectName(u"aboutLayout")
        self.appIconLabel = QLabel(self.aboutPage)
        self.appIconLabel.setObjectName(u"appIconLabel")
        sizePolicy3.setHeightForWidth(self.appIconLabel.sizePolicy().hasHeightForWidth())
        self.appIconLabel.setSizePolicy(sizePolicy3)
        self.appIconLabel.setSizeIncrement(QSize(0, 0))
        self.appIconLabel.setBaseSize(QSize(0, 0))
        self.appIconLabel.setAcceptDrops(False)
        self.appIconLabel.setStyleSheet(u"QLabel{image:url(:/Icons/Icon.png);}\n"
"")
        self.appIconLabel.setTextFormat(Qt.AutoText)
        self.appIconLabel.setScaledContents(False)
        self.appIconLabel.setAlignment(Qt.AlignCenter)
        self.appIconLabel.setWordWrap(False)
        self.appIconLabel.setMargin(0)
        self.appIconLabel.setOpenExternalLinks(False)
        self.appIconLabel.setTextInteractionFlags(Qt.NoTextInteraction)

        self.aboutLayout.addWidget(self.appIconLabel)

        self.appNameLabel = QLabel(self.aboutPage)
        self.appNameLabel.setObjectName(u"appNameLabel")
        sizePolicy3.setHeightForWidth(self.appNameLabel.sizePolicy().hasHeightForWidth())
        self.appNameLabel.setSizePolicy(sizePolicy3)
        self.appNameLabel.setStyleSheet(u"font-size: 24px; font-weight: bold; color: #4a90e2;")
        self.appNameLabel.setAlignment(Qt.AlignCenter)

        self.aboutLayout.addWidget(self.appNameLabel)

        self.versionLabel = QLabel(self.aboutPage)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setStyleSheet(u"font-size: 14px; color: #a0aec0;")
        self.versionLabel.setAlignment(Qt.AlignCenter)

        self.aboutLayout.addWidget(self.versionLabel)

        self.aboutSeparator = QFrame(self.aboutPage)
        self.aboutSeparator.setObjectName(u"aboutSeparator")
        self.aboutSeparator.setFrameShape(QFrame.Shape.HLine)
        self.aboutSeparator.setFrameShadow(QFrame.Shadow.Sunken)

        self.aboutLayout.addWidget(self.aboutSeparator)

        self.githubLabel = QLabel(self.aboutPage)
        self.githubLabel.setObjectName(u"githubLabel")
        self.githubLabel.setStyleSheet(u"font-size: 14px;")
        self.githubLabel.setAlignment(Qt.AlignCenter)

        self.aboutLayout.addWidget(self.githubLabel)

        self.discordLabel = QLabel(self.aboutPage)
        self.discordLabel.setObjectName(u"discordLabel")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        self.discordLabel.setFont(font4)
        self.discordLabel.setStyleSheet(u"font-size: 14px; color: #4299e1;")
        self.discordLabel.setAlignment(Qt.AlignCenter)

        self.aboutLayout.addWidget(self.discordLabel)

        self.aboutVerticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.aboutLayout.addItem(self.aboutVerticalSpacer)

        self.aboutLayout.setStretch(0, 5)
        self.aboutLayout.setStretch(1, 3)
        self.aboutLayout.setStretch(6, 6)
        self.mainStackedWidget.addWidget(self.aboutPage)

        self.contentLayout.addWidget(self.mainStackedWidget)

        self.navigationListWidget = QListWidget(self.centralWidget)
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        __qlistwidgetitem = QListWidgetItem(self.navigationListWidget)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem.setFont(font5);
        __qlistwidgetitem1 = QListWidgetItem(self.navigationListWidget)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1.setFont(font5);
        __qlistwidgetitem2 = QListWidgetItem(self.navigationListWidget)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2.setFont(font5);
        __qlistwidgetitem3 = QListWidgetItem(self.navigationListWidget)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3.setFont(font5);
        self.navigationListWidget.setObjectName(u"navigationListWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.navigationListWidget.sizePolicy().hasHeightForWidth())
        self.navigationListWidget.setSizePolicy(sizePolicy4)
        self.navigationListWidget.setMinimumSize(QSize(0, 0))
        self.navigationListWidget.setMaximumSize(QSize(200, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(9)
        self.navigationListWidget.setFont(font6)
        self.navigationListWidget.setFocusPolicy(Qt.NoFocus)
        self.navigationListWidget.setStyleSheet(u"QListWidget {\n"
"    border: none;\n"
"    background-color: #1a202c;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    border-radius: 8px;\n"
"    margin: 5px;\n"
"    padding: 12px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #4a90e2;\n"
"}")
        self.navigationListWidget.setAutoScroll(True)
        self.navigationListWidget.setProperty(u"showDropIndicator", True)
        self.navigationListWidget.setSortingEnabled(False)

        self.contentLayout.addWidget(self.navigationListWidget)


        self.rightPanelLayout.addLayout(self.contentLayout)

        self.statsFrame = QFrame(self.centralWidget)
        self.statsFrame.setObjectName(u"statsFrame")
        self.statsFrame.setStyleSheet(u"QFrame {\n"
"    background-color: #1a202c;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #4a5568;\n"
"}")
        self.statsFrame.setFrameShape(QFrame.StyledPanel)
        self.statsFrame.setFrameShadow(QFrame.Raised)
        self.statsLayout = QHBoxLayout(self.statsFrame)
        self.statsLayout.setSpacing(20)
        self.statsLayout.setObjectName(u"statsLayout")
        self.statsLayout.setContentsMargins(15, 10, 15, 10)
        self.totalFrame = QFrame(self.statsFrame)
        self.totalFrame.setObjectName(u"totalFrame")
        self.totalLayout = QVBoxLayout(self.totalFrame)
        self.totalLayout.setSpacing(5)
        self.totalLayout.setObjectName(u"totalLayout")
        self.totalLayout.setContentsMargins(5, 5, 5, 5)
        self.totalLabel = QLabel(self.totalFrame)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setAlignment(Qt.AlignCenter)

        self.totalLayout.addWidget(self.totalLabel)

        self.totalLcdNumber = QLCDNumber(self.totalFrame)
        self.totalLcdNumber.setObjectName(u"totalLcdNumber")
        self.totalLcdNumber.setStyleSheet(u"color: #4a90e2;")
        self.totalLcdNumber.setDigitCount(8)
        self.totalLcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.totalLayout.addWidget(self.totalLcdNumber)


        self.statsLayout.addWidget(self.totalFrame)

        self.errorFrame = QFrame(self.statsFrame)
        self.errorFrame.setObjectName(u"errorFrame")
        self.errorLayout = QVBoxLayout(self.errorFrame)
        self.errorLayout.setSpacing(5)
        self.errorLayout.setObjectName(u"errorLayout")
        self.errorLayout.setContentsMargins(5, 5, 5, 5)
        self.errorLabel = QLabel(self.errorFrame)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.errorLayout.addWidget(self.errorLabel)

        self.errorLcdNumber = QLCDNumber(self.errorFrame)
        self.errorLcdNumber.setObjectName(u"errorLcdNumber")
        self.errorLcdNumber.setStyleSheet(u"color: rgb(170, 85, 0);")
        self.errorLcdNumber.setDigitCount(8)
        self.errorLcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.errorLayout.addWidget(self.errorLcdNumber)


        self.statsLayout.addWidget(self.errorFrame)

        self.failedFrame = QFrame(self.statsFrame)
        self.failedFrame.setObjectName(u"failedFrame")
        self.failedLayout = QVBoxLayout(self.failedFrame)
        self.failedLayout.setSpacing(5)
        self.failedLayout.setObjectName(u"failedLayout")
        self.failedLayout.setContentsMargins(5, 5, 5, 5)
        self.failedLabel = QLabel(self.failedFrame)
        self.failedLabel.setObjectName(u"failedLabel")
        self.failedLabel.setAlignment(Qt.AlignCenter)

        self.failedLayout.addWidget(self.failedLabel)

        self.failedLcdNumber = QLCDNumber(self.failedFrame)
        self.failedLcdNumber.setObjectName(u"failedLcdNumber")
        self.failedLcdNumber.setStyleSheet(u"color: #f56565;")
        self.failedLcdNumber.setDigitCount(8)
        self.failedLcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.failedLayout.addWidget(self.failedLcdNumber)


        self.statsLayout.addWidget(self.failedFrame)

        self.unknownFrame = QFrame(self.statsFrame)
        self.unknownFrame.setObjectName(u"unknownFrame")
        self.unknownLayout = QVBoxLayout(self.unknownFrame)
        self.unknownLayout.setSpacing(5)
        self.unknownLayout.setObjectName(u"unknownLayout")
        self.unknownLayout.setContentsMargins(5, 5, 5, 5)
        self.unknownLabel = QLabel(self.unknownFrame)
        self.unknownLabel.setObjectName(u"unknownLabel")
        self.unknownLabel.setAlignment(Qt.AlignCenter)

        self.unknownLayout.addWidget(self.unknownLabel)

        self.unknownLcdNumber = QLCDNumber(self.unknownFrame)
        self.unknownLcdNumber.setObjectName(u"unknownLcdNumber")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(9)
        font7.setKerning(True)
        self.unknownLcdNumber.setFont(font7)
        self.unknownLcdNumber.setTabletTracking(False)
        self.unknownLcdNumber.setStyleSheet(u"color: #ed8936;")
        self.unknownLcdNumber.setDigitCount(8)
        self.unknownLcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.unknownLcdNumber.setProperty(u"intValue", 0)

        self.unknownLayout.addWidget(self.unknownLcdNumber)


        self.statsLayout.addWidget(self.unknownFrame)

        self.sentFrame = QFrame(self.statsFrame)
        self.sentFrame.setObjectName(u"sentFrame")
        self.sentFrame.setFont(font6)
        self.sentLayout = QVBoxLayout(self.sentFrame)
        self.sentLayout.setSpacing(5)
        self.sentLayout.setObjectName(u"sentLayout")
        self.sentLayout.setContentsMargins(5, 5, 5, 5)
        self.sentLabel = QLabel(self.sentFrame)
        self.sentLabel.setObjectName(u"sentLabel")
        self.sentLabel.setMinimumSize(QSize(0, 0))
        self.sentLabel.setFont(font4)
        self.sentLabel.setMouseTracking(True)
        self.sentLabel.setFrameShadow(QFrame.Plain)
        self.sentLabel.setTextFormat(Qt.AutoText)
        self.sentLabel.setScaledContents(False)
        self.sentLabel.setAlignment(Qt.AlignCenter)
        self.sentLabel.setWordWrap(False)
        self.sentLabel.setOpenExternalLinks(False)

        self.sentLayout.addWidget(self.sentLabel)

        self.sentLcdNumber = QLCDNumber(self.sentFrame)
        self.sentLcdNumber.setObjectName(u"sentLcdNumber")
        self.sentLcdNumber.setMouseTracking(False)
        self.sentLcdNumber.setStyleSheet(u"color: #48bb78;")
        self.sentLcdNumber.setDigitCount(8)
        self.sentLcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.sentLayout.addWidget(self.sentLcdNumber)


        self.statsLayout.addWidget(self.sentFrame)


        self.rightPanelLayout.addWidget(self.statsFrame)

        self.rightPanelLayout.setStretch(0, 5)
        self.rightPanelLayout.setStretch(1, 1)

        self.mainLayout.addLayout(self.rightPanelLayout)

        SmsBomberMainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(SmsBomberMainWindow)

        self.mainStackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SmsBomberMainWindow)
    # setupUi

    def retranslateUi(self, SmsBomberMainWindow):
        SmsBomberMainWindow.setWindowTitle(QCoreApplication.translate("SmsBomberMainWindow", "Blare Bomber", None))
        self.logTextEdit.setPlainText("")
        self.logTextEdit.setPlaceholderText(QCoreApplication.translate("SmsBomberMainWindow", "Application logs will appear here...", None))
        self.savedNumbersComboBox.setCurrentText("")
        self.savedNumbersLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0634\u0645\u0627\u0631\u0647 \u0647\u0627\u06cc \u0630\u062e\u06cc\u0631\u0647 \u0634\u062f\u0647:", None))
        self.targetNumberLineEdit.setPlaceholderText(QCoreApplication.translate("SmsBomberMainWindow", "09XXXXXXXXX", None))
        self.targetNumberLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0634\u0645\u0627\u0631\u0647 \u0645\u0648\u0631\u062f \u0646\u0638\u0631:", None))
        self.stopButton.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u067e\u0627\u06cc\u0627\u0646", None))
        self.startButton.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0634\u0631\u0648\u0639", None))
        self.warningLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ff0000;\">\u26a0\ufe0f \u0627\u0639\u062f\u0627\u062f \u0646\u0645\u0627\u06cc\u0634 \u062f\u0627\u062f\u0647 \u0634\u062f\u0647 \u0632\u06cc\u0631 </span><span style=\" font-size:9pt; text-decoration: underline; color:#ff0000;\">\u062a\u0642\u0631\u06cc\u0628\u06cc</span><span style=\" font-size:9pt; color:#ff0000;\"> \u0647\u0633\u062a\u0646\u062f</span></p></body></html>", None))
        self.saveSectionTitle.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0630\u062e\u06cc\u0631\u0647 \u0634\u0645\u0627\u0631\u0647 \u062c\u062f\u06cc\u062f", None))
        self.saveNameLineEdit.setPlaceholderText(QCoreApplication.translate("SmsBomberMainWindow", "\u0646\u0627\u0645", None))
        self.saveNameLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0646\u0627\u0645 \u0641\u0631\u062f:", None))
        self.saveNumberLineEdit.setPlaceholderText(QCoreApplication.translate("SmsBomberMainWindow", "09XXXXXXXXX", None))
        self.saveNumberLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0634\u0645\u0627\u0631\u0647 \u0641\u0631\u062f:", None))
        self.saveButton.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0627\u0636\u0627\u0641\u0647 \u06a9\u0631\u062f\u0646", None))
        self.deleteSectionTitle.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u062d\u0630\u0641 \u0634\u0645\u0627\u0631\u0647 \u0630\u062e\u06cc\u0631\u0647 \u0634\u062f\u0647", None))
        self.deleteLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0627\u0646\u062a\u062e\u0627\u0628 \u0634\u0645\u0627\u0631\u0647:", None))
        self.deleteButton.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u062d\u0630\u0641", None))
        self.settingsTitle.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u062a\u0646\u0638\u06cc\u0645\u0627\u062a", None))
        self.smsGroupBox.setTitle(QCoreApplication.translate("SmsBomberMainWindow", "\u062a\u0646\u0638\u06cc\u0645\u0627\u062a SMS", None))
        self.smsDelaySpinBox.setSuffix(QCoreApplication.translate("SmsBomberMainWindow", " \u062b\u0627\u0646\u06cc\u0647", None))
        self.smsDelayLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u062a\u0627\u062e\u06cc\u0631 \u0628\u06cc\u0646 SMS (\u062b\u0627\u0646\u06cc\u0647):", None))
        self.generalSettingsGroupBox.setTitle(QCoreApplication.translate("SmsBomberMainWindow", "\u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u06a9\u0644\u06cc", None))
        self.loopDelaySpinBox.setSuffix(QCoreApplication.translate("SmsBomberMainWindow", " \u062b\u0627\u0646\u06cc\u0647", None))
        self.loopDelayLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u062a\u0627\u062e\u06cc\u0631 \u0628\u06cc\u0646 \u0686\u0631\u062e\u0647 (\u062b\u0627\u0646\u06cc\u0647):", None))
        self.callCheckBox.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0641\u0639\u0627\u0644\u200c\u0633\u0627\u0632\u06cc \u062a\u0645\u0627\u0633", None))
        self.smsCheckBox.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0641\u0639\u0627\u0644\u200c\u0633\u0627\u0632\u06cc SMS", None))
        self.saveSettingsButton.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0630\u062e\u06cc\u0631\u0647 \u062a\u0646\u0638\u06cc\u0645\u0627\u062a", None))
        self.appIconLabel.setText("")
        self.appNameLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "Blare Bomber", None))
        self.versionLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0646\u0633\u062e\u0647 1.0.0 (Beta)", None))
        self.githubLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "GitHub: Bllare", None))
        self.discordLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "<html><head/><body><p><a href=\"https://bit.ly/Blare\"><span style=\" text-decoration: underline; color:#0078d7;\">bit.ly/Blare</span></a></p></body></html>", None))

        __sortingEnabled = self.navigationListWidget.isSortingEnabled()
        self.navigationListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.navigationListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("SmsBomberMainWindow", "\U0001f4a3 \U00000628\U00000645\U00000628\U00000631", None));
        ___qlistwidgetitem1 = self.navigationListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("SmsBomberMainWindow", "\U0001f4be \U00000630\U0000062e\U000006cc\U00000631\U00000647", None));
        ___qlistwidgetitem2 = self.navigationListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u2699\ufe0f \u062a\u0646\u0638\u06cc\u0645\u0627\u062a", None));
        ___qlistwidgetitem3 = self.navigationListWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u2139\ufe0f \u062f\u0631\u0628\u0627\u0631\u0647", None));
        self.navigationListWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(accessibility)
        self.navigationListWidget.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.totalLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u06a9\u0644", None))
        self.errorLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u062e\u0637\u0627", None))
        self.failedLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0646\u0627\u0645\u0648\u0641\u0642", None))
        self.unknownLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0646\u0627\u0645\u0639\u0644\u0648\u0645", None))
        self.sentLabel.setText(QCoreApplication.translate("SmsBomberMainWindow", "\u0641\u0631\u0633\u062a\u0627\u062f\u0647 \u0634\u062f", None))
    # retranslateUi

