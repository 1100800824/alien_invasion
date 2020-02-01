class Settings():
    """存储游戏中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 4
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        #fleet_direction的值为1时表示右移，为-1时表示左移
        self.fleet_direction = 1