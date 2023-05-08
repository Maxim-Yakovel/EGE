def game(heap, move, to):
    if heap >= 78:
        return move % 2 == to % 2
    if move == to:
        return 0
    h = [game(heap + 1, move + 1, to), game(heap + 4, move + 1, to), game(heap * 4, move + 1, to)]
    return any(h) if (move + 1) % 2 == to % 2 else all(h)
print(f'19: {[s for s in range(1, 78) if game(s, 0, 2)]}')
print(f'20: {[s for s in range(1, 78) if game(s, 0, 3) and not game(s, 0, 1)]}')
print(f'21: {[s for s in range(1, 78) if game(s, 0, 4) and not game(s, 0, 2)]}')
