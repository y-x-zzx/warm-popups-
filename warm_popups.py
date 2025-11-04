import pygame
import random
import time

pygame.init()
# 获取屏幕信息并设置为全屏
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("暖心弹窗")
clock = pygame.time.Clock()

# 字体设置
try:
    font = pygame.font.SysFont(['SimHei', "Microsoft YaHei", "黑体"], 24)
    title_font = pygame.font.SysFont(['SimHei', "Microsoft YaHei", "黑体"], 28)
except:
    font = pygame.font.Font(None, 24)
    title_font = pygame.font.Font(None, 28)


def randomColor():
    """生成随机RGB颜色"""
    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))


def randomCode():
    """随机选择暖心短语（排除第一个特殊消息）"""
    return random.choice([
        "多喝水哦~",
        "保持微笑",
        "每天都要元气满满",
        "记得好好休息",
        "保持好心情",
        "好好爱自己",
        "梦想成真",
        "别太累啦",
        "要相信自己",
        "你很棒的",
        "记得好好护肤",
        "早点休息",
        "别熬夜",
        "今天过得开心吗",
        "天冷了，多穿衣服",
        "你是最棒的",
        "保持积极心态",
        "一切都会好的",
        "相信自己",
        "加油！",
        "坚持就是胜利",
        "明天会更好",
        "保持耐心",
        "你很特别",
        "世界因你而美丽"
    ])


def getPopupColor(index):
    """为弹窗生成不同的颜色"""
    colors = [
        (240, 248, 255),  # 爱丽丝蓝
        (255, 240, 245),  # 薰衣草红
        (240, 255, 240),  # 蜜瓜绿
        (255, 250, 240),  # 杏仁白
        (240, 255, 255),  # 薄荷蓝
        (255, 245, 238),  # 贝壳粉
        (245, 245, 220),  # 米色
        (240, 248, 255),  # 幽灵白
        (255, 239, 213),  # 木瓜橙
        (224, 255, 255),  # 浅蓝
        (255, 228, 225),  # 雾玫瑰
        (245, 255, 250),  # 薄荷奶油
        (255, 250, 250),  # 雪白
        (248, 248, 255),  # 幽灵白
        (245, 245, 245),  # 白烟
        (255, 255, 240),  # 象牙白
        (240, 255, 240),  # 蜜瓜绿
        (255, 240, 245),  # 薰衣草红
        (240, 248, 255),  # 爱丽丝蓝
        (230, 230, 250),  # 薰衣草紫
    ]
    return colors[index % len(colors)]


def getBorderColor(index):
    """为弹窗边框生成不同的颜色"""
    colors = [
        (70, 130, 180),  # 钢蓝色
        (199, 21, 133),  # 中紫红色
        (60, 179, 113),  # 中海绿色
        (210, 105, 30),  # 巧克力色
        (0, 139, 139),  # 深青色
        (219, 112, 147),  # 浅紫红色
        (139, 69, 19),  # 鞍棕色
        (72, 61, 139),  # 暗板岩蓝
        (255, 140, 0),  # 深橙色
        (30, 144, 255),  # 道奇蓝
        (220, 20, 60),  # 猩红色
        (0, 206, 209),  # 暗绿松石色
        (138, 43, 226),  # 紫罗兰色
        (75, 0, 130),  # 靛蓝色
        (0, 100, 0),  # 深绿色
        (139, 0, 0),  # 深红色
        (0, 0, 139),  # 深蓝色
        (85, 107, 47),  # 暗橄榄绿
        (139, 0, 139),  # 深洋红色
        (47, 79, 79),  # 暗石板灰
    ]
    return colors[index % len(colors)]


class PopupWindow:
    def __init__(self, message, is_first=False, color_index=0):
        self.message = message
        self.is_first = is_first
        self.color_index = color_index
        self.width = 350  # 稍微缩小弹窗以适应更多数量
        self.height = 180
        self.x = random.randint(50, WIDTH - self.width - 50)
        self.y = random.randint(50, HEIGHT - self.height - 50)
        self.lifetime = 3.0  # 弹窗显示时间（秒）
        self.created_time = time.time()

        # 使用不同的颜色
        self.bg_color = getPopupColor(color_index)
        self.border_color = getBorderColor(color_index)
        self.text_color = (25, 25, 112)  # 深蓝色文字
        self.close_color = (220, 20, 60)  # 红色关闭按钮

        # 关闭按钮区域
        self.close_rect = pygame.Rect(self.x + self.width - 35, self.y + 8, 25, 25)

        # 渲染文字
        self.title_surface = title_font.render("暖心提醒", True, self.text_color)
        self.message_surface = font.render(self.message, True, self.text_color)

        self.active = True

    def update(self):
        """更新弹窗状态，检查是否超时"""
        if not self.is_first:  # 只有非第一个弹窗会自动消失
            if time.time() - self.created_time > self.lifetime:
                self.active = False
                return False
        return True

    def draw(self, surface):
        if not self.active:
            return

        # 绘制窗口背景
        pygame.draw.rect(surface, self.bg_color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, self.border_color, (self.x, self.y, self.width, self.height), 3)

        # 绘制标题栏
        pygame.draw.rect(surface, self.border_color, (self.x, self.y, self.width, 35))
        pygame.draw.rect(surface, self.bg_color, (self.x + 2, self.y + 2, self.width - 4, 31))

        # 绘制标题
        surface.blit(self.title_surface, (self.x + 15, self.y + 5))

        # 绘制关闭按钮（只在第一个弹窗显示）
        if self.is_first:
            pygame.draw.rect(surface, self.close_color, self.close_rect)
            pygame.draw.rect(surface, (255, 255, 255), self.close_rect, 2)
            # 绘制X符号
            close_x1 = (self.close_rect.left + 6, self.close_rect.top + 6)
            close_x2 = (self.close_rect.right - 6, self.close_rect.bottom - 6)
            close_x3 = (self.close_rect.right - 6, self.close_rect.top + 6)
            close_x4 = (self.close_rect.left + 6, self.close_rect.bottom - 6)
            pygame.draw.line(surface, (255, 255, 255), close_x1, close_x2, 2)
            pygame.draw.line(surface, (255, 255, 255), close_x3, close_x4, 2)

        # 绘制消息内容
        surface.blit(self.message_surface, (self.x + self.width // 2 - self.message_surface.get_width() // 2,
                                            self.y + self.height // 2))

    def handle_event(self, event):
        if not self.active:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_first and self.close_rect.collidepoint(event.pos):
                self.active = False
                return True
        return False


# 弹窗管理
popups = []
first_popup_shown = False
first_popup_closed = False
last_popup_time = 0
popup_interval = 0.1  # 弹窗出现间隔（秒），非常快
max_popups = 100  # 最大同时显示弹窗数量
color_counter = 0  # 颜色计数器
total_popups_created = 0  # 总弹窗计数

running = True
while running:
    current_time = time.time()

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # 按ESC退出全屏
                running = False

        # 处理弹窗点击事件（只处理第一个弹窗）
        for popup in popups[:]:
            if popup.handle_event(event):
                if popup.is_first:
                    first_popup_closed = True
                popups.remove(popup)

    # 清屏
    screen.fill((0, 0, 0))

    # 显示第一个特殊弹窗
    if not first_popup_shown:
        first_popup = PopupWindow("我想你了", is_first=True, color_index=0)
        popups.append(first_popup)
        first_popup_shown = True
        total_popups_created += 1

    # 第一个弹窗关闭后，持续快速生成100个其他弹窗
    if first_popup_closed and len(popups) < max_popups:
        if current_time - last_popup_time > popup_interval:
            new_popup = PopupWindow(randomCode(), color_index=color_counter + 1)
            popups.append(new_popup)
            color_counter = (color_counter + 1) % 20  # 循环使用颜色
            last_popup_time = current_time
            total_popups_created += 1

    # 更新所有弹窗状态（自动移除超时的弹窗）
    popups = [popup for popup in popups if popup.update()]

    # 绘制所有弹窗
    for popup in popups:
        popup.draw(screen)

    # 绘制提示信息
    if not first_popup_closed and first_popup_shown:
        hint_text = font.render("点击右上角X关闭第一个弹窗开始循环", True, (255, 255, 255))
        screen.blit(hint_text, (WIDTH // 2 - hint_text.get_width() // 2, HEIGHT - 40))
        esc_text = font.render("按ESC键退出全屏", True, (255, 255, 255))
        screen.blit(esc_text, (WIDTH // 2 - esc_text.get_width() // 2, HEIGHT - 70))
    elif first_popup_closed:
        # 显示统计信息
        info_text = font.render(f"当前弹窗: {len(popups)}/{max_popups} | 总弹窗数: {total_popups_created}", True,
                                (255, 255, 255))
        screen.blit(info_text, (WIDTH // 2 - info_text.get_width() // 2, HEIGHT - 40))
        esc_text = font.render("按ESC键退出全屏", True, (255, 255, 255))
        screen.blit(esc_text, (WIDTH // 2 - esc_text.get_width() // 2, HEIGHT - 70))

    # 更新显示
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
