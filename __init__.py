import random

from opsdroid.matchers import match_regex
from opsdroid.skill import Skill


class HelloByeSkill(Skill):

    @match_regex(r'hi|hello|hey|hallo', case_sensitive=False)
    async def hello(self, message):
        text = random.choice(
            ["Hi {}", "Hello {}", "Hey {}"]).format(message.user)
        await message.respond(text)

    @match_regex(r'bye( bye)?|see y(a|ou)|au revoir|gtg|I(\')?m off', case_sensitive=False)
    async def goodbye(self, message):
        text = random.choice(
            ["Bye {}", "See you {}", "Au revoir {}"]).format(message.user)
        await message.respond(text)
