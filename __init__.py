from opsdroid.matchers import match_regex, match_rasanlu
import logging
import random


def setup(opsdroid):
    logging.debug("Loaded hello module")


@match_regex(r'hi|hello|hey|hallo')
@match_rasanlu('smalltalk.hello')
async def hello(opsdroid, config, message):
    text = random.choice(["Hi {}", "Hello {}", "Hey {}"]).format(message.user)
    await message.respond(text)


@match_regex(r'bye( bye)?|see y(a|ou)|au revoir|gtg|I(\')?m off')
@match_rasanlu('smalltalk.goodbye')
async def goodbye(opsdroid, config, message):
    text = random.choice(["Bye {}", "See you {}", "Au revoir {}"]).format(message.user)
    await message.respond(text)


@match_rasanlu('smalltalk.how-are-you')
async def how_are_you(opsdroid, config, message):
    text = random.choice(["Good thanks", "Ok thanks", "Fine thanks"]).format(message.user)
    await message.respond(text)


@match_rasanlu('smalltalk.name')
async def how_are_you(opsdroid, config, message):
    text = random.choice(["I'm opsdroid", "My name is opsdroid", "It's opsdroid"]).format(message.user)
    await message.respond(text)

