# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'eclarity'

LOGGER = getLogger(__name__)


class SmallTalkSkill(MycroftSkill):

    def __init__(self):
        super( SmallTalkSkill, self).__init__(name=" SmallTalkSkill")

    def initialize(self):
        tired_intent = IntentBuilder("TiredIntent").\
            require("TiredKeyword").build()
        self.register_intent(tired_intent, self.handle_tired_intent)

        bored_intent = IntentBuilder("BoredIntent").\
            require("BoredKeyword").build()
        self.register_intent(bored_intent,
                             self.handle_bored_intent)

        happy_intent = IntentBuilder("HappyIntent").\
            require("HappyKeyword").build()
        self.register_intent(happy_intent,
                             self.handle_happy_intent)

    def handle_tired_intent(self, message):
        self.speak_dialog("tired")

    def handle_bored_intent(self, message):
        self.speak_dialog("bored")

    def handle_happy_intent(self, message):
        self.speak_dialog("happy")

    def stop(self):
        pass


def create_skill():
    return SmallTalkSkill()
