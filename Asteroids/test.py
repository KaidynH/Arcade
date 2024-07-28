from tinydb import TinyDB, Query
import tinydb, pygame
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Asteroids')

highscores_database = TinyDB('db.json')

highscores_database.truncate()
highscores_database.insert({'rank':0, 'score':10000000, 'initials':'JJJ'})
highscores_database.insert({'rank':1, 'score':10020, 'initials':'FRD'})
highscores_database.insert({'rank':2, 'score':9270, 'initials':'BOB'})
highscores_database.insert({'rank':3, 'score':840, 'initials':'TIM'})
highscores_database.insert({'rank':4, 'score':790, 'initials':'JIM'})
highscores_database.insert({'rank':5, 'score':550, 'initials':'JOE'})
highscores_database.insert({'rank':6, 'score':520, 'initials':'ABC'})
highscores_database.insert({'rank':7, 'score':500, 'initials':'DEF'})
highscores_database.insert({'rank':8, 'score':350, 'initials':'GHI'})
highscores_database.insert({'rank':9, 'score':270, 'initials':'JKL'})
highscores_database.insert({'rank':10, 'score':120, 'initials':'LMN'})
highscores_database.insert({'rank':11, 'score':0, 'initials':''})

# font = pygame.font.Font('freesansbold.ttf', 15)

# print(highscores_database.all())



# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# current_letter = ''
# initials = ''
# alpha_index = -1

# while len(initials) < 3:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 if alpha_index == 25:
#                     alpha_index = 0
#                 else:
#                     alpha_index += 1
#                 current_letter = alphabet[alpha_index]
#                 print(current_letter)
#                 print(initials)
#             if event.key == pygame.K_DOWN:
#                 if alpha_index == -26:
#                     alpha_index = 25
#                 else:
#                     alpha_index -= 1
#                 current_letter = alphabet[alpha_index]
#                 print(current_letter)
#                 print(initials)
#             if event.key == pygame.K_SPACE:
#                 initials += current_letter
#                 print(current_letter)
#                 print(initials)

# highscore = 0

# Score = Query()

# if len(initials) == 3:
#     for score in highscores_database.all():
#         if highscore > score.get('score'):
#             need_changed = []

#             highscores_database.update({'rank':-1}, doc_ids=[score.get('rank')+1])
#             highscores_database.all()

#             for s in highscores_database.all():
#                 if s.get('rank') > score.get('rank'):
#                     need_changed.append(s.doc_id)

#             need_changed.reverse()

#             for id in need_changed:
#                 highscores_database.update({'score':highscores_database.get(doc_id=id-1).get('score')}, doc_ids=[id])


#             highscores_database.update({'score':highscore}, Score.rank == -1)
#             highscores_database.update({'rank':score.get('rank')}, Score.rank == -1)
#             break


print(highscores_database.all())