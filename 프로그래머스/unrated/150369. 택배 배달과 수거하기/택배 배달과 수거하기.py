def solution(cap, n, deliveries, pickups):
    answer=0
    while deliveries and not deliveries[-1]: deliveries.pop()
    while pickups and not pickups[-1]: pickups.pop()
    while deliveries or pickups:
        cap_deli = cap
        if not deliveries: d=0
        else:
            d=len(deliveries)
            while cap_deli and deliveries:
                if deliveries[-1]>cap_deli:
                    deliveries[-1]-=cap_deli
                    cap_deli=0
                else:
                    cap_deli-=deliveries.pop()
            while deliveries and not deliveries[-1]: deliveries.pop()
            
        cap_pick = cap
        if not pickups: p=0
        else:
            p=len(pickups)
            while cap_pick and pickups:
                if pickups[-1]>cap_pick:
                    pickups[-1]-=cap_pick
                    cap_pick=0
                else:
                    cap_pick-=pickups.pop()
            while pickups and not pickups[-1]: pickups.pop()
        
        
        answer+=max(d,p)
        
        
    return 2*answer