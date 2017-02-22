# def estimate_house_sales_price(num_of_bedrooms, sqft, neighborhood):
#     price = 0
#
#     # In my area，the average house cost $200 per sqft
#     price_per_sqft = 200
#
#     if neighborhood == 'hipsterton':
#         # but some areas cost a bit more
#         price_per_sqft = 400
#
#     elif neighborhood == 'skid row':
#         # and some areas cost less
#         price_per_sqft = 100
#
#     # start with a base price estimate base on how big the place is
#     price = price_per_sqft * sqft
#
#     # now adjust our estimate based on the number of bedrooms
#     if num_of_bedrooms == 0:
#         # Studio apartments are cheap
#         price = price - 20000
#     else:
#         # places width more bedrooms are usually
#         # more valuable
#         price = price + (num_of_bedrooms * 1000)
#     return price

# 上面的程序，当价格变化的时候很难维护，不如让计算机来帮我们做，至于程序内做了什么，我们完全不用关心，so

# def estimate_house_sales_price(num_of_bedrooms,sqft,neighborhood):
# price = <computer, plz do something for me>
# return price

# 考虑这个问题的角度，是将房价看作一碗美味的汤。如果你能算出每种成分对价格的影响，也许就能得到各种成分混合起来的最终价格的具体比例
# ，可以将第一段的程序简化成如下的样子
# def estimate_house_sales_price(num_of_bedrooms, sqft, neighborhood):
#     price = 0
#     # a little pitch of this
#     price += num_of_bedrooms * .8412352764234787
#     # and a big pitch of that
#     price += sqft * 1234.3265
#     # maybe a handful of this
#     price += neighborhood * 2.322346
#     # and finally , just a little extra salt for good measure
#     price += 201.234725634
#     return price

# .8412352764234787 1234.3265等这些数字成为
