def rebalance(stock, target, safety, route_cost):
    """stock/target/safety: {wh: qty}; route_cost: {(from,to): cost per unit}. Returns transfers [(from,to,qty)]."""
    surplus = {w: stock[w] - max(target[w], safety[w]) for w in stock if stock[w] > max(target[w], safety[w])}
    deficit = {w: target[w] - stock[w] for w in stock if stock[w] < target[w]}
    moves = []
    for to in sorted(deficit, key=lambda w: -deficit[w]):
        need = deficit[to]
        for frm in sorted(surplus, key=lambda f: route_cost.get((f, to), float("inf"))):
            if need == 0: break
            if (frm, to) not in route_cost or surplus[frm] == 0: continue
            qty = min(need, surplus[frm])
            moves.append((frm, to, qty)); surplus[frm] -= qty; need -= qty
    return moves
