# Part of Shii (
#
# Description: Shii is a discord bot that can be taught to respond to certain keywords.
from logging import Logger
import json

study_return = None
no_study_return = None

def study_return_text(text):
    '''Sets the text returned when training is complete.'''
    ''':study_return_text ex): study_return_text("네! 알았어요!")'''
    '''학습 성공시 리턴되는 텍스트를 정의 합니다.'''
    global study_return
    study_return = text


def no_study_return_text(text):
  '''Sets the text returned when training is not complete.'''
  ''':no_study_return_text ex): no_study_return_text("으에?")"'''
  global no_study_return
  no_study_return = text


def load_bot_info():
    try:
        with open('bot_info.json', 'r', encoding='utf-8') as f:
            bot_info = json.load(f)
    except FileNotFoundError:
        bot_info = {}

    return bot_info


def save_bot_info(bot_info):
    with open('bot_info.json', 'w', encoding='utf-8') as f:
        json.dump(bot_info, f, ensure_ascii=False, indent=4)


def study(keyword: str, description: str, author_nickname: str):
    '''Teaches the bot to respond to a keyword.'''
    ''':return ex): study_return'''
    bot_info = load_bot_info()
    user_id = author_nickname
    if '@' in description:
        return "@을 추가하지 말아주세요..."
    if 'https://' in description or 'https://' in keyword:
        return "링크를 포함시키지 말아주세요..."
    if keyword not in bot_info:
        bot_info[keyword] = {
            'description': description,
            'author_nickname': user_id
        }
        save_bot_info(bot_info)
        if study_return == None:
          return f"'{keyword}'를 학습하였습니다."
        else:
          return study_return
    else:
        return f"`{keyword}`는 이미 알고 있어요!"


def study_say(keyword: str):
    '''Returns the description of the keyword.'''
    ''':return ex): 안녕하세요'''
    bot_info = load_bot_info()
    info = bot_info.get(keyword)
    word = {
        'shii': f"`pip install -U shii`\n`bot.load_extension('shii')` or `await bot.load_extension('shii')`",
    }
    if keyword in word.keys():
        return f'{word[keyword]}'
    else:
        if info:
            author_nickname = info['author_nickname']
            description = info['description']
            return f"{description}\n`{author_nickname} 님이 알려주셨어요!`"
        else:
          if no_study_return == None:
            return f"{keyword}는 아직 모르겠어요.."
          else:
            return no_study_return


def del_study(keyword: str):
  '''Deletes the keyword and its description.'''
  info = load_bot_info()
  if keyword in info:
    del info[keyword]
    save_bot_info(info)
    return f"`{keyword}`를 삭제하였습니다."
  else:
    return "이미 삭제되었거나 존재하지 않는 키워드입니다."