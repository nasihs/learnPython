"""
实现动画效果
"""
import pygame


def main():
    # 初始化pygame
    pygame.init()
    # 初始化用于显示的窗口
    screen = pygame.display.set_mode((800, 600))
    # 设置窗口标题
    pygame.display.set_caption('第一个游戏')
    # 定义变量表示小球位置坐标
    x, y = 50, 50
    running = True
    # 开启一个时间循环处理发生的事件
    while running:
        # 从消息队列中获取时间并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
        pygame.display.flip()
        # 每隔50毫秒就改变小球位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()
