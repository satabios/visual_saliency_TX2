

from makeColors import makeColors
import math
def generateChannels(imgs,params):

     [inp, in_orient, R, G, B, Y] = makeColors(imgs)

     # rg = R - G
     # by = B - Y
     # gr = G - R
     # yb = Y - B
     #
     # rg[rg < 0] = 0
     # gr[gr < 0] = 0
     # by[by < 0] = 0
     # yb[yb < 0] = 0
     #
     # subtype = []
     # img = []
     #
     #
     # for c in range(len(params['channels'])):
     #
     #
     #     if (params['channels'][c]=='I'):
     #
     #
     #         img.append({'subtype':[{'data':inp,'type':'Intensity'}]})
     #
     #
     #
     #     elif (params['channels'][c]=='C'):
     #
     #         img.append( {'subtype': [ {'data': rg, 'type': 'Red-Green Opponency'},
     #                                            {'data': gr, 'type': 'Green-Red Opponency'},
     #                                            {'data': by, 'type': 'Blue-Yellow Opponency'},
     #                                            {'data': yb, 'type': 'Yellow-Blue Opponency'}]})
     #
     #
     #         # img[c]['subtype'][0]['data'] = rg
     #         # img[c]['subtype'][0]['type'] = 'Red-Green Opponency'
     #         # img[c]['type'] = 'Color'
     #         #
     #         # img[c]['subtype'][1]['data'] = gr
     #         # img[c]['subtype'][1]['type'] = 'Green-Red Opponency'
     #         #
     #         # img[c]['subtype'][2]['data'] = by
     #         # img[c]['subtype'][2]['type'] = 'Blue-Yellow Opponency'
     #         #
     #         # img[c]['subtype'][3]['data'] = yb
     #         # img[c]['subtype'][3]['type'] = 'Yellow-Blue Opponency'
     #
     #
     #     elif (params['channels'][c] == 'O'):
     #
     #         img.append( {'subtype': [{'data': rg, 'type': 'Red-Green Opponency','ori':0},
     #                                           {'data': gr, 'type': 'Green-Red Opponency','ori':math.pi/4},
     #                                           {'data': by, 'type': 'Blue-Yellow Opponency','ori':math.pi / 2},
     #                                           {'data': yb, 'type': 'Yellow-Blue Opponency','ori':3*math.pi / 4}]})
     #
     #         # img[c]['subtype'][0]['data'] = in_orient
     #         # img[c]['subtype'][0]['ori'] = 0
     #         # img[c]['subtype'][0]['type'] = 'Orientation'
     #         # img[c]['type'] = 'Orientation'
     #         #
     #         # img[c]['subtype'][1]['data'] = in_orient
     #         # img[c]['subtype'][1]['ori'] = math.pi/4
     #         # img[c]['subtype'][1]['type'] = 'Orientation'
     #         #
     #         # img[c]['subtype'][2]['data'] = in_orient
     #         # img[c]['subtype'][2]['ori'] = math.pi / 2
     #         # img[c]['subtype'][2]['type'] = 'Orientation'
     #         #
     #         # img[c]['subtype'][3]['data'] = in_orient
     #         # img[c]['subtype'][3]['ori'] = 3*math.pi / 4
     #         # img[c]['subtype'][3]['type'] = 'Orientation'
     # # return img
     return R,G,B,inp








     








