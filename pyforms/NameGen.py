
import pyforms
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlText
from pyforms.Controls import ControlPlayer
import matplotlib


class SimpleExample1(pyforms.BaseWidget):

    def __init__(self):
        super(SimpleExample1, self).__init__('Simple Example 1')
        self._formset = [('_firstname','_middlename','_lastname'),'_fullname',('','_button','')]

        self._firstname = ControlText('First name')
        self._middlename = ControlText('Middle name')
        self._lastname = ControlText('Lastname name')
        self._fullname = ControlText('Full name')
        self._button = ControlButton('Press this button')
        self._button.value = self.__buttonAction
        self.player = ControlPlayer('Choose a file')

        self._fullname.addPopupSubMenuOption('Path',
                                             {
                                                 'Delete': self.__dummyEvent,
                                                 'Edit': self.__dummyEvent,
                                                 'Interpolate': self.__dummyEvent
                                             })

        self.mainmenu=[
            {'File': [
                {'Open': self.__dummyEvent},
                '-',
                {'Save': self.__dummyEvent},
                {'Save As': self.__dummyEvent}
                ]
            },
            {'Edit': [
                {'Copy': self.__dummyEvent}
            ]
            }
        ]

    def __buttonAction(self):
        self._fullname.value = self._firstname.value + " " + self._middlename.value + \
                               " " + self._lastname.value

    def __dummyEvent(self):
        print "Menu option selected"

if __name__ == "__main__":
    pyforms.startApp(SimpleExample1)

