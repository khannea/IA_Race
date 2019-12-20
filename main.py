import pygame
import math
import tensorflow
import random
import tensorflow as tf
import keras as keras
from keras.models     import Sequential
from keras.layers     import Dense
from keras.optimizers import Adam
from keras import backend as Backend
from keras.models import load_model
import numpy as np
import time 
#VARIABLE
etape_ia = 9

game_speed = 20

ia_game = 30
random_game = 15

lives = 100

fps_graph = 120
fps_calc = 60
apm_ia = 2

move_random = 3

#ETAPES
rot_etape = np.full(10,0)
x_etape1 = 270
y_etape1 = 150
rot_etape[1] = -30

x_etape2 = 410
y_etape2 = 200
rot_etape[2] = -1

x_etape3 = 550
y_etape3 = 200
rot_etape[3] = -1

x_etape4 = 582
y_etape4 = 345
rot_etape[4] = 70

x_etape5 = 550
y_etape5 = 365
rot_etape[5] = 30

x_etape6 = 400
y_etape6 = 470
rot_etape[6] = 1

x_etape7 = 200
y_etape7 = 442
rot_etape[7] = -25

x_etape8 = 30
y_etape8 = 380
rot_etape[8] = 90

rot_etape[0] = 51
rot_etape[9] = 51
 
max_lap = 0
max_etape = 0

def blit():
    window_surface.blit(circuit, (0, 100))
    window_surface.blit(start, (80, 145))
    window_surface.blit(etape1, (x_etape1, y_etape1))
    window_surface.blit(etape2, (x_etape2, y_etape2))
    window_surface.blit(etape3, (x_etape3, y_etape3))
    window_surface.blit(etape4, (x_etape4, y_etape4))
    window_surface.blit(etape5, (x_etape5, y_etape5))
    window_surface.blit(etape6, (x_etape6, y_etape6))
    window_surface.blit(etape7, (x_etape7, y_etape7))
    window_surface.blit(etape8, (x_etape8, y_etape8))
    window_surface.blit(public, (0, 0))
    window_surface.blit(voitureUsed, rect)
    if(len(inside_text) > 0):
        window_surface.blit(text, (0, 0))
    pygame.display.flip()

def f_etape8(old_front_x, old_front_y, front_x, front_y, tours, rotation):
    if old_front_y > old_front_x/math.tan(math.radians(rot_etape[8])) + y_etape8 - x_etape8/math.tan(math.radians(rot_etape[8])) and front_y <= front_x/math.tan(math.radians(rot_etape[8])) + y_etape8 - x_etape8/math.tan(math.radians(rot_etape[8])):
        return (tours+1)
    return tours

def f_etape7(old_front_x, old_front_y, front_x, front_y, tours, rotation):
    if old_front_y > old_front_x/math.tan(math.radians(rot_etape[7])) + y_etape7 - x_etape7/math.tan(math.radians(rot_etape[7])) and front_y <= front_x/math.tan(math.radians(rot_etape[7])) + y_etape7 - x_etape7/math.tan(math.radians(rot_etape[7])):
        return (tours+1)
    return tours

def f_etape6(old_front_x, old_front_y, front_x, front_y, tours, rotation):
    if old_front_y < old_front_x/math.tan(math.radians(rot_etape[6])) + y_etape6 - x_etape6/math.tan(math.radians(rot_etape[6])) and front_y >= front_x/math.tan(math.radians(rot_etape[6])) + y_etape6 - x_etape6/math.tan(math.radians(rot_etape[6])):
        return (tours+1)
    return tours

def f_etape5(old_front_x, old_front_y, front_x, front_y, tours, rotation):
    if old_front_y < old_front_x/math.tan(math.radians(rot_etape[5])) + y_etape5 - x_etape5/math.tan(math.radians(rot_etape[5])) and front_y >= front_x/math.tan(math.radians(rot_etape[5])) + y_etape5 - x_etape5/math.tan(math.radians(rot_etape[5])):
        return (tours+1)
    return tours

def f_etape4(old_front_x, old_front_y, front_x, front_y, tours, rotation):
    if old_front_y < old_front_x/math.tan(math.radians(rot_etape[4])) + y_etape4 - x_etape4/math.tan(math.radians(rot_etape[4])) and front_y >= front_x/math.tan(math.radians(rot_etape[4])) + y_etape4 - x_etape4/math.tan(math.radians(rot_etape[4])):
        return (tours+1)
    return tours

def f_etape3(old_front_x, old_front_y, front_x, front_y, tours, rotation):
    if front_y <= 350 and old_front_y < old_front_x/math.tan(math.radians(rot_etape[3])) + y_etape3 - (x_etape3+etape3.get_width())/math.tan(math.radians(rot_etape[3])) and front_y >= front_x/math.tan(math.radians(rot_etape[3])) + y_etape3 - (x_etape3+etape3.get_width())/math.tan(math.radians(rot_etape[3])):
        return (tours+1)
    return tours

def f_etape2(old_front_x, old_front_y, front_x, front_y, tours, rotation):
    if front_y <= 350 and old_front_y < old_front_x/math.tan(math.radians(rot_etape[2])) + y_etape2 - (x_etape2+etape2.get_width())/math.tan(math.radians(rot_etape[2])) and front_y >= front_x/math.tan(math.radians(rot_etape[2])) + y_etape2 - (x_etape2+etape2.get_width())/math.tan(math.radians(rot_etape[2])):
        return (tours+1)
    return tours

def f_etape1(old_front_x, old_front_y, front_x, front_y, tours, rotation):
    if front_y <= 350 and old_front_y < old_front_x/math.tan(math.radians(rot_etape[1])) + y_etape1 - (x_etape1+etape1.get_width())/math.tan(math.radians(rot_etape[1])) and front_y >= front_x/math.tan(math.radians(rot_etape[1])) + y_etape1 - (x_etape1+etape1.get_width())/math.tan(math.radians(rot_etape[1])):
        return (tours+1)
    return tours

def ligne_arrivee(old_front_x, old_front_y, front_x, front_y, tours, rotation):
    if x <= 300 and front_y >= 145 and old_front_y > old_front_x/math.tan(math.radians(rot_etape[0])) + 145 - 80/math.tan(math.radians(rot_etape[0])) and front_y <= front_x/math.tan(math.radians(rot_etape[0])) + 145 - 80/math.tan(math.radians(rot_etape[0])):
        return (tours+1)

    return tours

def f_action(action,rotation_diff):
    if action == [1,0,0]:
        rotation_diff += 15
    elif action == [0,1,0]:
        rotation_diff -= 15
    return rotation_diff


def test_crash():
    global tours,total_etape,front_x,front_y,mode,echec,exist_model,exist_saved,game,reussite,echec,echec_index,training_data,weight_tmp,weight,i,lives,round_ia,t_ia,t_calc
    if tours < total_etape and (front_x <= 0 or front_x >= circuit.get_width() or front_y-100 <= 0 or front_y-100 >= circuit.get_height() or circuit.get_at((front_x, front_y-100))) != (255, 255, 255, 255):
        echec += 1
        echec_index += tours
        if mode != "libre" and mode != "random" and mode != "ia_randomLL":
            lives -= 1
        else:
            lives -= 0.5
        if lives <= 0:
            if exist_saved == 1 and mode != "randomLL":
                round_ia -= 1
                trained_model.set_weights(model_copy.get_weights())
                exist_saved = 0
                exist_model = 0
            else:
                if total_etape != 1:
                    if mode == "full_mutate":
                        mode = "mutate_"+str(round(echec_index/echec))
                    elif mode == "full_ia":
                        mode = "mutate_"+str(round(echec_index/echec))
                    elif mode.find("mutate_") >= 0:
                        if total_etape != etape_ia:
                            mode = "ia_randomLL"
                        else:
                            mode = "full_ia"
                        # mode = "mutate_"+str(round(echec_index/echec) - 1)
                    elif mode == "ia_randomLL":
                        total_etape -= 1
                        mode = "full_mutate"
                    # if mode == "full_ia":
                    #     mode = "full_mutate"
                    # elif mode == "full_mutate":
                    #     mode = "ia_mutateLL"
                    # elif mode == "ia_mutateLL":
                    #     mode = "ia_randomLL"
                    # else: 
                    #     mode = "ia_mutateLL"  
                    #     total_etape -= 1
                else:
                    Backend.clear_session()
                    mode = "random"
                    exist_model = 0
                round_ia = 0

            init_ia_training()
            init_round()
        init_course()
    t_ia += 1
    t_calc = time_start + (pygame.time.get_ticks() - time_start)*game_speed


# INITIALISATION FENETRE
resolution = (800, 630)
blue_color = (89, 152, 255)
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 18)

window_surface = pygame.display.set_mode(resolution, pygame.DOUBLEBUF) # | pygame.HWSURFACE)

circuit = pygame.image.load("circuit.png").convert()
voiture = pygame.image.load("voitureUsed.png").convert_alpha()
start = pygame.transform.rotate(pygame.image.load("start.png").convert_alpha(), rot_etape[0])
etape1 = pygame.transform.rotate(pygame.image.load("start.png").convert_alpha(), rot_etape[1])
etape2 = pygame.transform.rotate(pygame.image.load("start.png").convert_alpha(), rot_etape[2])
etape3 = pygame.transform.rotate(pygame.image.load("start.png").convert_alpha(), rot_etape[3])
etape4 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("start.png").convert_alpha(), (11,190)), rot_etape[4])
etape5 = pygame.transform.rotate(pygame.image.load("start.png").convert_alpha(), rot_etape[5])
etape6 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("start.png").convert_alpha(), (11,210)), rot_etape[6])
etape7 = pygame.transform.rotate(pygame.image.load("start.png").convert_alpha(), rot_etape[7])
etape8 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("start.png").convert_alpha(), (11,170)), rot_etape[8])

public = pygame.image.load("public.png").convert_alpha()


# MUSIQUE
pygame.mixer.init()
pygame.mixer.music.load("zelda.wav")
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play()
acceleration = pygame.mixer.Sound("acceleration.wav")
acceleration.set_volume(0)
crash = pygame.mixer.Sound("crash.wav")
crash.set_volume(0)

training_data = []
last_lap = 0
mode = "libre"
inside_text = ""
round_ia = 0
reussite = 0
echec = 0
echec_index = 0
game = 0
exist_model = 0
exist_saved = 0
total_etape = 1
weight = np.array([0])
i = 1
t0 = pygame.time.get_ticks()
tmax = 0
precision = 0

# DONNEES DE DEPART
def init_course():
    global random_activation,weight_tmp,total_game,x,y,fronty_x,front_y,old_front_x,old_front_y,vitesse,rotation,rotation_diff,tours,statut,action,score,game_memory,previous_observation,t1,time_start,time_end,t_graph,t_calc,t_ia,voitureUsed,init_w,init_h,rect_x,rect_y

    rotation = -35
    rotation_diff = -35
    x = 80
    y = 180

    random_activation = 0
    voitureUsed = pygame.transform.rotate(voiture, rotation)
    init_w = voitureUsed.get_width()
    init_h = voitureUsed.get_height()
    rect_x = (init_w - voitureUsed.get_width())/2
    rect_y = (init_h - voitureUsed.get_height())/2

    front_x = round(x + init_w/2 - 80/100*voitureUsed.get_width()/2 * math.sin(math.radians(rotation)) )
    front_y = round(100 + y + init_h/2 - 100 - 80/100*voitureUsed.get_height()/2 * math.cos(math.radians(rotation)))
    old_front_x = front_x
    old_front_y = front_y

    vitesse = 200

    tours = -1

    statut = "depart"
    action = [0,0,1]

    weight_tmp = np.array([0])
    game_memory = []
    observation = []
    previous_observation = []

    time_start = pygame.time.get_ticks()
    time_end = 0

    t_graph = time_start
    t_calc = time_start
    t1 = time_start
    t_ia = 0

    if mode == "random":
        total_game = random_game
    else:
        total_game = ia_game #Non optimisé, creer fonction init_round ou init_session

    inside_text = 'MaxTps: %.2fs | Obj:%d | V:%.2f | TpsMax:%.2fs | Vies:%d | MaxTours:%d | Mode:%s '%(max_lap,total_game-game,game_speed,tmax,lives,max_etape,mode)

def init_round():
    global lives, i
    init_course()
    lives = 100
    i = 1

def init_ia_training():
    global weight, training_data, precision, echec, echec_index, reussite, round_ia, game
    training_data = []
    weight_tmp = np.array([0])
    weight = np.array([0])
    precision = 0  
    echec = 0
    echec_index = 0
    reussite = 0   
    round_ia += 1
    game = 0   
    lives = 100

init_course()
rect = pygame.draw.rect(window_surface, (255, 0, 0), [(x, y), voitureUsed.get_size()], 1)

window_surface.fill(blue_color)
blit()
launched = True
pygame.key.set_repeat(100,100)

while launched:
    # TOUCHES
    
    
    t1 = time_start + (pygame.time.get_ticks() - time_start)*game_speed     


    #COURSE
    if tours != total_etape:
        # IA
        if t1 - t_calc >= 1000/fps_calc:
            if t_ia >= apm_ia:
                if mode != "libre":

                    observation = np.array([rotation, round(front_x/3), round(front_y/3)])
                    previous_observation = observation

                    if mode == "random":
                        nombre_random = random.randrange(0,3)
                    elif mode == "full_mutate":        
                        if len(previous_observation) == 0:
                            nombre_random = 1
                        else:
                            if  random.randrange(0,move_random) == 0:
                                nombre_random = random.randrange(0,3)
                            else:
                                nombre_random = np.argmax(trained_model.predict(previous_observation.reshape(-1, len(previous_observation)))[0])
                    elif mode == "ia_randomLL":        
                        if len(previous_observation) == 0:
                            nombre_random = 1
                        else:
                            if total_etape - tours == 1:
                                nombre_random = random.randrange(0,3) 
                            else:
                                nombre_random = np.argmax(trained_model.predict(previous_observation.reshape(-1, len(previous_observation)))[0])
                    elif mode == "ia_random2LL":        
                        if len(previous_observation) == 0:
                            nombre_random = 1
                        elif total_etape - tours == 1:                  
                            nombre_random = random.randrange(0,3)                             
                        elif total_etape - tours == 2:
                            if  random.randrange(0,move_random) == 0:
                                nombre_random = random.randrange(0,3)
                            else:
                                nombre_random = np.argmax(trained_model.predict(previous_observation.reshape(-1, len(previous_observation)))[0])
                        else:
                            nombre_random = np.argmax(trained_model.predict(previous_observation.reshape(-1, len(previous_observation)))[0])
                    elif mode == "ia_mutateLL":        
                        if len(previous_observation) == 0:
                            nombre_random = 1
                        else:
                            if total_etape - tours == 1:
                                if  random.randrange(0,move_random) == 0:
                                    nombre_random = random.randrange(0,3) 
                                else:
                                    nombre_random = np.argmax(trained_model.predict(observation.reshape(-1, len(observation)))[0])
                            else:
                                nombre_random = np.argmax(trained_model.predict(observation.reshape(-1, len(observation)))[0])
                    elif mode == "full_ia":
                        if len(previous_observation) == 0:
                            nombre_random = random.randrange(0,3)        
                        else:
                            nombre_random = np.argmax(trained_model.predict(observation.reshape(-1, len(observation)))[0])
                    elif mode.find("mutate_") >= 0:
                        etape_mutation = int(mode.replace("mutate_",""))
                        if len(previous_observation) == 0:
                            nombre_random = random.randrange(0,3)
                        else:
                            if tours == etape_mutation:
                                if  random.randrange(0,move_random) == 0:
                                    nombre_random = random.randrange(0,3) 
                                else:
                                    nombre_random = np.argmax(trained_model.predict(observation.reshape(-1, len(observation)))[0])
                            else:
                                nombre_random = np.argmax(trained_model.predict(observation.reshape(-1, len(observation)))[0])
                        
                    if nombre_random == 0:
                        action = [1,0,0]
                    elif nombre_random == 1:
                        action = [0,1,0]
                    else:
                        action = [0,0,1]

                    rotation_diff = f_action(action, rotation_diff)

            
                    if len(observation) > 0:
                        game_memory.append([observation, action])
                        if weight_tmp[0] == 0:
                            weight_tmp = np.array([i])
                        else:
                            weight_tmp = np.append(weight_tmp,[i])


                    previous_observation = observation
                    t_ia=0
        
                for event in pygame.event.get():
                    # PENDANT LE JEU
                    # if pygame.mixer.get_busy == 0 and vitesse > 0:
                    #     acceleration.play()
                    if event.type == pygame.KEYDOWN:
                        tkey = pygame.key.get_pressed()
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                        if tkey[pygame.K_PAGEUP]:  
                            apm_ia += 5
                            init_course()
                        if tkey[pygame.K_DOWN]:  
                            apm_ia -= 5
                            init_course()
                        if tkey[pygame.K_KP0]:  
                            mode = "libre"
                            total_etape = etape_ia
                        elif tkey[pygame.K_KP1]:
                            mode = "random"
                            total_etape = 1
                            init_course()
                            total_etape = 1
                        elif tkey[pygame.K_KP2]:
                            mode = "full_ia"
                            init_course()
                        elif tkey[pygame.K_KP3]:
                            mode = "full_mutate"
                            init_course()
                        elif tkey[pygame.K_KP4]:
                            if exist_model == 1:
                                mode = "ia_randomLL"
                                init_course()
                        elif tkey[pygame.K_DELETE]:
                            if exist_model == 1:
                                Backend.clear_session()
                                mode = "random"
                                round_ia = 0
                                total_etape = 1
                            training_data = []
                            game = 0
                            init_course()
                        if tkey[pygame.K_KP_PLUS]:
                            game_speed += 0.5
                            init_course()
                        if tkey[pygame.K_KP_MINUS]:
                            if game_speed > 0.5:
                                game_speed -= 0.5
                            init_course()
                        if event.key == pygame.K_RETURN:
                            init_course()
                        if mode == "libre":
                            if tkey[pygame.K_LEFT]:
                                rotation_diff += 15
                            if tkey[pygame.K_RIGHT]:
                                rotation_diff -= 15
                            if tkey[pygame.K_UP]:
                                if (vitesse <= 3):
                                    vitesse += 0.5
                                # if pygame.mixer.get_busy() == 0:          
                                #     acceleration.play()
                            if tkey[pygame.K_DOWN]:
                                if vitesse > 0:
                                    vitesse -= 1
                                if vitesse < 0:
                                    vitesse = 0   
                    if event.type == pygame.QUIT:
                        launched = False

            # CALCUL
            rotation = rotation_diff
            x = x - math.sin(math.radians(rotation))*vitesse*(t1 - t_calc)/1000
            y = y - math.cos(math.radians(rotation))*vitesse*(t1 - t_calc)/1000
            rect_x = (init_w - voitureUsed.get_width())/2
            rect_y = (init_h - voitureUsed.get_height())/2

            front_x = round(x + init_w/2 - 80/100*voitureUsed.get_width()/2 * math.sin(math.radians(rotation)) )
            front_y = round(100 + y + init_h/2 - 100 - 80/100*voitureUsed.get_height()/2 * math.cos(math.radians(rotation)))
            
            if total_etape >= 1 and tours < 1:
                tours = f_etape1(old_front_x, old_front_y, front_x, front_y, tours, rotation)
            elif total_etape >= 2 and tours == 1:
                tours = f_etape2(old_front_x, old_front_y, front_x, front_y, tours, rotation)
            elif total_etape >= 3 and tours == 2:
                tours = f_etape3(old_front_x, old_front_y, front_x, front_y, tours, rotation)
            elif total_etape >= 4 and tours == 3:
                tours = f_etape4(old_front_x, old_front_y, front_x, front_y, tours, rotation)
            elif total_etape >= 5 and tours == 4:
                tours = f_etape5(old_front_x, old_front_y, front_x, front_y, tours, rotation)
            elif total_etape >= 6 and tours == 5:
                tours = f_etape6(old_front_x, old_front_y, front_x, front_y, tours, rotation)
            elif total_etape >= 7 and tours == 6:
                tours = f_etape7(old_front_x, old_front_y, front_x, front_y, tours, rotation)
            elif total_etape >= 8 and tours == 7:
                tours = f_etape8(old_front_x, old_front_y, front_x, front_y, tours, rotation)
            if tours == -1 or tours == 8:
                tours = ligne_arrivee(old_front_x, old_front_y, front_x, front_y, tours, rotation)
            
            old_front_x = front_x
            old_front_y = front_y

            # CRASH
            test_crash()

        # GRAPHIQUE
        if t1 - t_graph >= 1000/fps_graph/game_speed:          
            window_surface.fill(blue_color)
            voitureUsed = pygame.transform.rotate(voiture, rotation)
            
            rect = pygame.draw.rect(window_surface, (255, 0, 0), [(x + rect_x, y + rect_y), voitureUsed.get_size()], 1)
            inside_text = 'MaxTps: %.2fs | Obj:%d | V:%.2f | TpsMax:%dmin | Vies:%d | MaxTours:%d | Mode:%s '%(max_lap,total_game-game,game_speed,tmax,lives,max_etape,mode)
            text = font.render(inside_text, True, (255,255,255), (0,0,0)) 
            blit()

            t_graph = time_start + (pygame.time.get_ticks() - time_start)*game_speed


    #FIN COURSE
    if tours == total_etape:
        game += 1
        reussite += 1

        if time_end == 0:
            last_lap = (t1 - time_start)/1000

            if max_etape < total_etape:
                tmax = (pygame.time.get_ticks() - t0) / 1000 / 60
                max_etape = total_etape
                max_lap = last_lap
            elif total_etape == max_etape:
                if max_lap == 0:
                    max_lap = last_lap
                else:
                    max_lap = min(max_lap,last_lap)

            time_end = 1
        # Entrainement IA
        if mode != "libre":
            i += 1
            k = 0
            l = 0
            while k < len(weight_tmp):
                weight_tmp[k] = 10*abs(math.cos(math.radians(rot_etape[total_etape]-rotation-90)))#round((1+abs(math.cos(math.radians(rot_etape[total_etape]-rotation-90))))*(tours+1)/last_lap)
                k += 1
            if weight[0] == 0:
                weight = weight_tmp
            else:
                weight = np.append(weight,weight_tmp)

            for data in game_memory:
                training_data.append([data[0], data[1]])

            game_memory = []
            previous_observation = []
            observation = []

            if game == total_game or ((mode == "ia_randomLL" or mode == "ia_random2LL") and game == random_game) or lives == 0:
                precision = round(reussite/(echec+reussite)*100)

                def build_model(input_size, output_size):
                    model = Sequential()

                    model.add(Dense(64, input_dim=input_size, activation='relu'))
                    
                    model.add(Dense(64, activation='relu'))
                    model.add(Dense(64, activation='relu'))
                    model.add(Dense(64, activation='relu'))
                    model.add(Dense(64, activation='relu'))

                    model.add(Dense(64, activation='relu'))    

                    model.add(Dense(output_size, activation='linear'))
                    
                    model.compile(loss='mse', optimizer=Adam()) 

                    # model.add(Dense(256, activation='sigmoid'))
                    # model.add(Dense(512, activation='sigmoid'))
                    # model.add(Dense(256, activation='sigmoid'))
                    # model.add(Dense(output_size, activation='linear'))
                    # model.compile(loss='mse', optimizer=Adam()) 

                    return model

                def train_model(training_data):
                    global exist_model, model

                    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]))
                    y = np.array([i[1] for i in training_data]).reshape(-1, len(training_data[0][1]))

                    if exist_model == 0 :
                        model = build_model(input_size=len(X[0]), output_size=len(y[0]))
                        exist_model = 1
                            
                    
                    model.fit(X, y, epochs=100, sample_weight=weight)
                    return model

                if exist_model == 1:
                    model_copy= keras.models.clone_model(trained_model)
                    model_copy.build((None, 3)) # replace 10 with number of variables in input layer
                    model_copy.compile(loss='mse', optimizer=Adam())
                    model_copy.set_weights(trained_model.get_weights())
                    exist_saved = 1

                trained_model = train_model(training_data)

                if mode == "random" or mode == "ia_randomLL":
                    mode = "full_ia"
                elif mode == "full_ia":
                    if precision > 90:
                        if total_etape != etape_ia:
                            total_etape += 1
                            mode = "ia_randomLL"
                    else:
                        if  total_etape != etape_ia or precision < 10:
                            mode = "mutate_"+str(round(echec_index/echec))
                elif mode.find("mutate_") >= 0:
                    mode = "full_ia"
                elif mode == "ia_mutateLL":
                    mode = "full_ia"
                elif mode == "full_mutate":
                    mode = "full_ia"
                
                # if mode == "random":
                #     mode = "ia_mutateLL"
                # elif mode == "full_mutate" and total_etape != etape_ia:
                #     mode = "ia_mutateLL"
                # elif mode == "ia_randomLL":
                #     mode = "ia_mutateLL"
                # elif (mode == "ia_mutateLL") and precision > 40:
                #         mode = "full_ia"
                #         lives /= 2
                # elif mode == "full_ia":
                #     if precision > 90:
                #         if total_etape != etape_ia:
                #             total_etape += 1
                #             mode = "ia_randomLL"
                #     elif precision <50:
                #         mode = "ia_mutateLL"
                # elif mode == "ia_random2LL":
                #     mode = "ia_mutateLL"

                print("Précision:",precision,"%")
                init_ia_training()
        init_round()
    
    if pygame.time.get_ticks()-t0>15*60*1000:
        my_output1 = str("max etape:%d, tmax:%dmin, max_lap:%.2fs, Précision:%d"%(max_etape,tmax,max_lap,precision))
        print(my_output1)
        break

