import pygame
import random
import utils.background as background
import utils.constants as constants
import utils.shredder as shredder
import utils.bullet as bullet
import utils.enemy as enemy
import utils.beam as beam
import utils.text as text
import utils.button as button

pygame.init()

screen_width = constants.SCREEN_WIDTH
screen_height = constants.SCREEN_HEIGHT
game_name = constants.GAME_NAME
max_fps = constants.MAX_FPS

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(game_name)

clock = pygame.time.Clock()
running = True

shredder.add_shredder_if_none(screen_width, screen_height)

enemy.build_enemy()

menu_title = text.Text(game_name, 100, (218, 62, 140), 70, 50)
thank_you_text = text.Text("Thank You for Playing!", 75, (204, 0, 82), 120, 90)

start_game_button = button.Button(100, 200, "Start Game", 35)
exit_button = button.Button(100, 275, "Exit", 35)
try_again_button = button.Button(300, 325, "Try Again", 35)
exit_to_menu_button = button.Button(300, 400, "Exit to Menu", 35)

start_game = False
show_menu = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if show_menu:
        background.draw_menu_background(screen)
        text.Text.draw(menu_title, screen)
        if button.Button.draw(start_game_button, screen):
            start_game = True
            show_menu = False
        if button.Button.draw(exit_button, screen):
            running = False

    if start_game:
        
        background.draw_game_background(screen)

        current_time = pygame.time.get_ticks()
        if current_time - beam.previous_shot >= beam.beam_reload and len(
                beam.beam_group) < 8 and len(enemy.enemy_group) > 0:
            attacking_enemy = random.choice(enemy.enemy_group.sprites())
            enemy_beam = beam.Beam(attacking_enemy.rect.centerx, 
                                   attacking_enemy.rect.bottom)
            beam.beam_group.add(enemy_beam)
            beam.previous_shot = current_time
        
        shredder.shredder_group.update(screen_width)
        bullet.bullet_group.update()
        enemy.enemy_group.update()
        beam.beam_group.update(screen_height)

        bullet.bullet_group.draw(screen)
        shredder.shredder_group.draw(screen)
        enemy.enemy_group.draw(screen)
        beam.beam_group.draw(screen)
        
        if len(enemy.enemy_group) == 0:
            text.Text.draw(thank_you_text, screen)
            if button.Button.draw(exit_to_menu_button, screen):
                start_game = False
                shredder.add_shredder_if_none(screen_width, screen_height)
                enemy.enemy_group.empty()
                enemy.build_enemy()
                beam.beam_group.empty()
                bullet.bullet_group.empty()
                show_menu = True

        if len(shredder.shredder_group) == 0:
            beam.beam_group.empty()
            bullet.bullet_group.empty()
            if button.Button.draw(try_again_button, screen):
                shredder.add_shredder_if_none(screen_width, screen_height)
                enemy.enemy_group.empty()
                enemy.build_enemy()
                start_game = True
            if button.Button.draw(exit_to_menu_button, screen):
                start_game = False
                shredder.add_shredder_if_none(screen_width, screen_height)
                enemy.enemy_group.empty()
                enemy.build_enemy()
                show_menu = True

    pygame.display.flip()
    
    clock.tick(max_fps)

pygame.quit()

