price=[7,6,4,3,1]
price_1=sorted(price)

small=min(price_1)
large=max(price_1)

while price.index(small)>price.index(large):
    small=min(price_1)
    large=max(price_1)
    if price.index(small)>price.index(large):
        
        price_1.remove(large)
    else:
        break
print(large-small)
