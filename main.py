from imports import *
from Background import *
from Bird import *
from Pipe import *
from Text import *

class Game:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(pygame.image.load(utils.resourcePath('Graphics/bird_yellow.png')))

        # Loading sounds
        self.sounds = {}
        self.sounds['score'] = pygame.mixer.Sound(utils.resourcePath('Sounds/sfx_point.wav'))
        self.sounds['wing'] = pygame.mixer.Sound(utils.resourcePath('Sounds/sfx_wing.wav'))
        self.sounds['hit'] = pygame.mixer.Sound(utils.resourcePath('Sounds/sfx_hit.wav'))
        self.sounds['die'] = pygame.mixer.Sound(utils.resourcePath('Sounds/sfx_die.wav'))
        self.sounds['swoosh'] = pygame.mixer.Sound(utils.resourcePath('Sounds/sfx_swooshing.wav'))
        for sound in self.sounds.values():
            sound.set_volume(Settings.SOUND_VOLUME)

        self.clock = pygame.time.Clock()
        self.resetValues()

    def resetValues(self):
        self.score = 0
        with open(Settings.HIGHSCORE_FILE, 'r') as f:
            try:
                self.highscore = int(f.read())
            except Exception:
                self.highscore = 0
        
        self.sky = Background(0, 0, utils.resourcePath('Graphics/sky.png'), self.screen)
        self.ground = Background(0, Settings.GROUND_LEVEL, utils.resourcePath('Graphics/ground.png'), self.screen)

        bird_image = [utils.resourcePath('Graphics/bird_yellow.png'), utils.resourcePath('Graphics/bird_red.png'), utils.resourcePath('Graphics/bird_green.png'), utils.resourcePath('Graphics/bird_blue.png')]
        self.bird = Bird(Settings.BIRD_POS_X, Settings.BIRD_POS_Y, Settings.BIRD_SIZE, random.choice(bird_image), -5, 0, self.screen)
        pipe_height = [random.randint(Settings.PIPE_MIN_HEIGHT, Settings.PIPE_MAX_HEIGHT) for _ in range(Settings.PIPE_NMB)]
        self.pipes = [Pipe(Settings.SCREEN_WIDTH + i * (Settings.PIPE_WIDTH + Settings.PIPE_DISTANCE) + Settings.PIPE_INITIAL_OFFSET, Settings.SCREEN_HEIGHT - pipe_height[i], Settings.PIPE_WIDTH, pipe_height[i], utils.resourcePath('Graphics/pipe.png'), utils.resourcePath('Graphics/pipe_upside_down.png'), self.screen) for i in range(Settings.PIPE_NMB)]
        
        self.intro_text = Text(Settings.SCREEN_WIDTH / 2, Settings.SCREEN_HEIGHT / 2 - 45, 'FLAPPY BIRD\nCLICK LMB TO START\n\nHIGHSCORE: ' + str(self.highscore), Settings.INTRO_TEXT_SIZE, self.screen)
        self.score_text = Text(Settings.SCREEN_WIDTH / 2, 40, str(self.score), Settings.SCORE_TEXT_SIZE, self.screen)
        self.highscore_text = Text(Settings.SCREEN_WIDTH / 2, 100, 'NEW HIGHSCORE!', Settings.HIGHSCORE_TEXT_SIZE, self.screen)
        self.game_over_text = Text(Settings.SCREEN_WIDTH / 2, Settings.SCREEN_HEIGHT / 2 - 45, 'GAME OVER!\nCLICK LMB TO RESTART', Settings.GAME_OVER_TEXT_SIZE, self.screen)

        self.game_over = False
        self.pipe_hit = False
        self.new_highscore = False
        self.show_intro = True
        self.bird_intro_v = Physics.BIRD_INTRO_V
        self.pipe_add_velocity_counter = 0
        self.rot = 0

        pygame.mixer.Sound.play(self.sounds['swoosh'])

    def run(self):
        running = True
        fps_counter = Settings.FRAMERATE
        
        while running:
            delta_time = self.clock.tick(Settings.FRAMERATE) * 0.01

            # Fps counter
            # fps_counter -= 1
            # if fps_counter == 0:
            #     fps_counter = Settings.FRAMERATE
            #     print(round(self.clock.get_fps()))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.show_intro:
                            self.show_intro = False
                        if not self.show_intro:
                            if self.game_over:
                                self.resetValues()
                            elif not self.pipe_hit:
                                pygame.mixer.Sound.play(self.sounds['wing'])
                                self.bird.setVelocityY(Physics.UP_V)
                                self.rot = int(5 / delta_time)
            
            self.screen.fill(Color.WHITE)

            if not self.game_over:
                if not self.show_intro:
                    if not self.pipe_hit:
                        # Collisions
                        for pipe in self.pipes:
                            for rect in pipe.getRects():
                                if self.bird.checkCollision(rect):
                                    pygame.mixer.Sound.play(self.sounds['hit'])
                                    self.pipe_hit = True
                                    break
                    if not self.pipe_hit:    
                        # Score
                        for pipe in self.pipes:
                            if pipe.isScored():
                                pygame.mixer.Sound.play(self.sounds['score'])
                                self.score += 1         
                                self.score_text.text = str(self.score)        
                                # Speed up pipes and bg
                                if self.score != 0 and (self.score - self.pipe_add_velocity_counter * Settings.PIPE_ADD_VELOCITY_INTERVAL) % Settings.PIPE_ADD_VELOCITY_INTERVAL == 0:
                                    self.pipe_add_velocity_counter += 1
                                    for p in self.pipes:
                                        p.addVelocityX(Physics.PIPE_ADDED_V)
                                    self.sky.addVelocityX(Physics.PIPE_ADDED_V)
                                    self.ground.addVelocityX(Physics.PIPE_ADDED_V)
                                break       
                                
                        # Moving pipes and bg
                        for pipe in self.pipes:
                            pipe.moveX(delta_time * 100)        
                        self.sky.moveX(delta_time * 100)
                        self.ground.moveX(delta_time * 100)
                
                    # Moving bird
                    self.bird.addVelocityY(Physics.GRAVITY_V * delta_time)
                    if self.rot * Physics.BIRD_ROTATION_ANGLE_STEP * delta_time > Physics.BIRD_ROTATION_DOWN_MAX:
                        self.bird.rotate(self.rot * Physics.BIRD_ROTATION_ANGLE_STEP * delta_time)
                        self.rot -= 1
                    if self.bird.moveY(delta_time * 100):
                        pygame.mixer.Sound.play(self.sounds['die'])
                        self.game_over = True
                        if self.score > self.highscore:
                            with open(Settings.HIGHSCORE_FILE, 'w') as f:
                                f.write(str(self.score))
                            self.new_highscore = True
                else:
                    # Moving bg
                    self.sky.moveX(delta_time * 100)
                    self.ground.moveX(delta_time * 100)
                    # Moving bird up and down
                    if self.bird.getY() < 0 or self.bird.getY() > Settings.GROUND_LEVEL:
                        self.bird.setY(Settings.BIRD_POS_Y)
                    if abs(self.bird.getY() - Settings.BIRD_POS_Y) > Settings.BIRD_INTRO_OFFSET:
                        if self.bird.getY() - Settings.BIRD_POS_Y > 0:
                            self.bird_intro_v = -Physics.BIRD_INTRO_V
                        else:
                            self.bird_intro_v = Physics.BIRD_INTRO_V
                    self.bird.setVelocityY(self.bird_intro_v * delta_time)
                    self.bird.moveY(delta_time * 100)

            # Drawing
            self.sky.draw()
            for pipe in self.pipes:
                pipe.draw()
            self.ground.draw()
            self.bird.draw()
            if self.game_over:
                self.game_over_text.draw()
            if self.new_highscore:
                self.highscore_text.draw()
            if not self.show_intro:
                self.score_text.draw()
            else:
                self.intro_text.draw()
            
            pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    game = Game(Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT, Settings.SCREEN_TITLE)
    game.run()