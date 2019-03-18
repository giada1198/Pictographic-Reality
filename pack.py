import json, os, sys
import numpy as np

# ['test', 'train', 'valid']
# test = []
# train = []
# valid = []
#
# base_path = 'raw_data'
#
# for i in os.listdir(base_path + '/ren_test'):
#     if i.endswith('.json'):
#         full_path = '%s/%s' % (base_path + '/ren_test', i)
#         with open(full_path) as f:
#             data = json.load(f)
#             nd1 = []
#             for d in data:
#                 nd2 = []
#                 nd2.append(d[0])
#                 nd2.append(d[1])
#                 nd2.append(d[3])
#                 nd1.append(nd2)
#             t = np.array(nd1, dtype='int16')
#             test.append(t)
#
# for i in os.listdir(base_path + '/ren_train'):
#     if i.endswith('.json'):
#         full_path = '%s/%s' % (base_path + '/ren_train', i)
#         with open(full_path) as f:
#             data = json.load(f)
#             nd1 = []
#             for d in data:
#                 nd2 = []
#                 nd2.append(d[0])
#                 nd2.append(d[1])
#                 nd2.append(d[3])
#                 nd1.append(nd2)
#             t = np.array(nd1, dtype='int16')
#             train.append(t)
#
# for i in os.listdir(base_path + '/ren_valid'):
#     if i.endswith('.json'):
#         full_path = '%s/%s' % (base_path + '/ren_valid', i)
#         with open(full_path) as f:
#             data = json.load(f)
#             nd1 = []
#             for d in data:
#                 nd2 = []
#                 nd2.append(d[0])
#                 nd2.append(d[1])
#                 nd2.append(d[3])
#                 nd1.append(nd2)
#             t = np.array(nd1, dtype='int16')
#             valid.append(t)
#
# np.savez_compressed('ren.npz', test=test, train=train, valid=valid)

def pack(input_path, output_path):
    output = {}
    for var in ['test', 'train', 'valid']:
        output[var] = []
        p = input_path + '/' + var
        for i in os.listdir(p):
            if i.endswith('.json'):
                full_path = '%s/%s' % (p, i)
                with open(full_path) as f:
                    data = json.load(f)
                    strokes = []
                    for d in data:
                        stroke = []
                        for s in [0,1,3]:
                            stroke.appned(d[s])
                        strokes.append(stroke)
                    t = np.array(strokes, dtype='int16')
                    output[var].append(t)
    p = output_path + '/' + 'output.npz'
    np.savez_compressed(p, test=output['test'], train=output['train'], valid=output['valid'])
    return True

if __name__ == '__main__':
    if pack(sys.argv[1], sys.argv[2]):
        print('complete!')
