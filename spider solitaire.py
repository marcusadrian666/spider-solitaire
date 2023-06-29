import random

# 初始化牌堆
def init_deck():
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['♠', '♥', '♦', '♣']
    deck = [rank + suit for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# 发牌
def deal_cards(deck, num_players):
    hands = [[] for _ in range(num_players)]
    for _ in range(6):
        for i in range(num_players):
            hands[i].append(deck.pop(0))
    return hands

# 打印玩家手牌
def print_hands(hands):
    for i, hand in enumerate(hands):
        print(f'玩家 {i + 1} 的手牌：{", ".join(hand)}')

# 游戏主循环
def play_spider_solitaire():
    num_players = 4  # 玩家数量
    deck = init_deck()
    hands = deal_cards(deck, num_players)
    print_hands(hands)

# 运行游戏
play_spider_solitaire()
