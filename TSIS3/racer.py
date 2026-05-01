import pygame, random
LANES = [80, 180, 280]

class RacerGame:
    def __init__(self, settings):
        self.player_lane = 1
        self.y = 500
        self.speed = 5
        self.enemy_speed = 5

        self.coins = []
        self.obstacles = []
        self.traffic = []
        self.powerups = []

        self.score = 0
        self.distance = 0
        self.coin_score = 0

        self.active_power = None
        self.power_timer = 0
        self.shield = False

        self.game_over = False

    def spawn_coin(self):
        lane = random.randint(0,2)
        return [lane, -20]

    def spawn_obstacle(self):
        lane = random.randint(0,2)
        return [lane, -50]

    def spawn_traffic(self):
        lane = random.randint(0,2)
        return [lane, -100]

    def spawn_powerup(self):
        lane = random.randint(0,2)
        t = random.choice(["nitro","shield","repair"])
        return [lane, -30, t]

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.player_lane = max(0, self.player_lane-1)
        if keys[pygame.K_RIGHT]: self.player_lane = min(2, self.player_lane+1)

        if random.randint(1,40)==1: self.coins.append(self.spawn_coin())
        if random.randint(1,80)==1: self.obstacles.append(self.spawn_obstacle())
        if random.randint(1,100)==1: self.traffic.append(self.spawn_traffic())
        if random.randint(1,200)==1: self.powerups.append(self.spawn_powerup())

        for c in self.coins: c[1]+=self.speed
        for o in self.obstacles: o[1]+=self.speed
        for t in self.traffic: t[1]+=self.speed+2
        for p in self.powerups: p[1]+=self.speed

        player_rect = pygame.Rect(LANES[self.player_lane], self.y, 40,60)

        for c in self.coins[:]:
            rect = pygame.Rect(LANES[c[0]], c[1], 20,20)
            if player_rect.colliderect(rect):
                self.coin_score+=1
                self.coins.remove(c)

        for o in self.obstacles:
            rect = pygame.Rect(LANES[o[0]], o[1], 40,40)
            if player_rect.colliderect(rect):
                if self.shield:
                    self.shield=False
                else:
                    self.game_over=True

        for t in self.traffic:
            rect = pygame.Rect(LANES[t[0]], t[1], 40,60)
            if player_rect.colliderect(rect):
                if self.shield:
                    self.shield=False
                else:
                    self.game_over=True

        for p in self.powerups[:]:
            rect = pygame.Rect(LANES[p[0]], p[1], 30,30)
            if player_rect.colliderect(rect):
                self.active_power = p[2]
                if p[2]=="nitro": self.power_timer=180; self.speed+=3
                if p[2]=="shield": self.shield=True
                if p[2]=="repair": self.game_over=False
                self.powerups.remove(p)

        if self.active_power=="nitro":
            self.power_timer-=1
            if self.power_timer<=0:
                self.speed-=3
                self.active_power=None

        self.distance+=self.speed
        self.score=self.coin_score*10+self.distance

    def draw(self, screen):
        player_rect = pygame.Rect(LANES[self.player_lane], self.y, 40,60)
        pygame.draw.rect(screen,(255,0,0),player_rect)

        for c in self.coins:
            pygame.draw.circle(screen,(255,215,0),(LANES[c[0]]+10,int(c[1])),10)

        for o in self.obstacles:
            pygame.draw.rect(screen,(0,0,0),(LANES[o[0]],o[1],40,40))

        for t in self.traffic:
            pygame.draw.rect(screen,(0,0,255),(LANES[t[0]],t[1],40,60))

        for p in self.powerups:
            pygame.draw.rect(screen,(0,255,0),(LANES[p[0]],p[1],30,30))